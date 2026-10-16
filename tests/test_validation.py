"""Exercise corruption and omission detection without changing the real bundle."""

import contextlib
import importlib.util
import io
import re
import shutil
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_repository", ROOT / "scripts/check_repository.py")
CHECKER = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CHECKER)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repository"
        shutil.copytree(ROOT, self.repo, ignore=shutil.ignore_patterns(
            ".git", ".venv", "__pycache__", "dist", "build"
        ))
        self.skill = self.repo / "skills/drupal-development"
        self.verifier = CHECKER.bundle_module(self.skill)

    def bundle_output(self, archive=None):
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            status = self.verifier.verify(self.skill, archive)
        return status, output.getvalue()

    def assert_bundle_rejects(self, message, archive=None):
        status, output = self.bundle_output(archive)
        self.assertEqual(status, 1, output)
        self.assertIn(message, output)

    def repository_errors(self):
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            return CHECKER.check_repository(self.repo)

    def test_complete_repository_passes_without_source_archive(self):
        self.assertEqual(self.repository_errors(), [])

    def test_bundled_source_archive_is_rejected(self):
        (self.repo / "coding_standards-main.zip").write_bytes(b"not for distribution")
        self.assertIn(
            "Do not include coding_standards-main.zip; refer to the upstream repository",
            self.repository_errors(),
        )

    def test_installed_skill_verifies_without_source_zip_or_repository(self):
        installed = Path(self.temp.name) / "installed/drupal-development"
        shutil.copytree(self.skill, installed)
        shutil.rmtree(self.repo)
        verifier = CHECKER.bundle_module(installed)
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(verifier.verify(installed), 0)
        self.assertTrue((installed / "LICENSE").is_file())
        self.assertTrue((installed / "THIRD_PARTY_NOTICES.md").is_file())
        self.assertTrue((installed / "LICENSES/GPL-2.0-or-later.txt").is_file())

    def test_missing_original_dotfile_is_detected(self):
        (self.skill / "references/standards/.gitlab-ci.yml").unlink()
        self.assert_bundle_rejects("Missing source file: .gitlab-ci.yml")

    def test_changed_original_bytes_are_detected(self):
        path = self.skill / "references/standards/docs/php/coding.md"
        path.write_bytes(path.read_bytes() + b"\nUnexpected change.\n")
        self.assert_bundle_rejects("Source bytes/hash mismatch: docs/php/coding.md")

    def test_unlisted_source_file_is_detected(self):
        (self.skill / "references/standards/unlisted.md").write_text("extra", encoding="utf-8")
        self.assert_bundle_rejects("Unlisted source file: unlisted.md")

    def test_incomplete_source_map_is_detected(self):
        path = self.skill / "references/source-map.md"
        path.write_text(path.read_text(encoding="utf-8").split("## Original files")[0], encoding="utf-8")
        self.assert_bundle_rejects("Source map is incomplete")

    def test_missing_direct_route_is_detected(self):
        path = self.skill / "SKILL.md"
        text = path.read_text(encoding="utf-8")
        path.write_text(text.replace(
            "[E_ALL compliance](references/standards/docs/php/e_all.md)", "E_ALL compliance"
        ), encoding="utf-8")
        self.assert_bundle_rejects("Source is not directly routed from SKILL.md: docs/php/e_all.md")

    def test_wrong_source_archive_is_detected(self):
        archive = self.repo / "wrong.zip"
        with ZipFile(archive, "w") as zipped:
            zipped.writestr("coding_standards-main/README.md", "wrong archive")
        self.assert_bundle_rejects("Archive SHA-256 differs", archive)

    def test_broken_authored_reference_is_detected(self):
        path = self.skill / "references/compatibility.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[Missing](absent.md)\n", encoding="utf-8")
        self.assert_bundle_rejects("Broken/escaping authored link: compatibility.md: absent.md")

    def test_missing_repository_file_is_detected(self):
        (self.repo / ".github/workflows/ci.yml").unlink()
        self.assertIn("Missing required file: .github/workflows/ci.yml", self.repository_errors())

    def test_invalid_skill_name_is_detected(self):
        path = self.skill / "SKILL.md"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "name: drupal-development", "name: different-name", 1
        ), encoding="utf-8")
        self.assertIn("Skill name must match directory: drupal-development", self.repository_errors())

    def test_missing_icon_is_detected(self):
        (self.skill / "assets/icon.svg").unlink()
        self.assertIn("Missing or escaping agent icon: icon_small", self.repository_errors())

    def test_broken_readme_link_is_detected(self):
        path = self.repo / "README.md"
        path.write_text(path.read_text(encoding="utf-8") + "\n[Missing](missing.md)\n", encoding="utf-8")
        self.assertIn("Broken or escaping local link in README.md: missing.md", self.repository_errors())

    def test_unpinned_action_is_detected(self):
        path = self.repo / ".github/workflows/ci.yml"
        workflow = path.read_text(encoding="utf-8")
        for action in ("actions/checkout", "actions/setup-python"):
            with self.subTest(action=action):
                # Match the current pin so Dependabot can update it freely.
                # Always start from the original workflow to isolate each action.
                pattern = rf"(?m)(\buses:\s*{re.escape(action)}@)[0-9a-f]{{40}}(?=\s|$)"
                changed, count = re.subn(pattern, r"\g<1>v6", workflow, count=1)
                self.assertEqual(count, 1, f"Expected to replace the current SHA pin for {action}")
                path.write_text(changed, encoding="utf-8")
                self.assertIn(
                    f"Pin each CI action to a full commit hash: {action}@v6",
                    self.repository_errors(),
                )

    def test_elevated_ci_permission_is_detected(self):
        path = self.repo / ".github/workflows/ci.yml"
        path.write_text(path.read_text(encoding="utf-8").replace(
            "contents: read", "contents: write"
        ), encoding="utf-8")
        self.assertIn("CI must use read-only contents permission", self.repository_errors())

    def test_changed_installable_license_is_detected(self):
        (self.skill / "LICENSE").write_text("different terms\n", encoding="utf-8")
        self.assertIn("Installed skill must carry the same MIT license as the repository",
                      self.repository_errors())

    def test_duplicate_metadata_keys_are_rejected(self):
        path = self.skill / "agents/openai.yaml"
        path.write_text(path.read_text(encoding="utf-8") + "\ninterface: {}\n", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Duplicate YAML key: interface"):
            self.repository_errors()


if __name__ == "__main__":
    unittest.main()
