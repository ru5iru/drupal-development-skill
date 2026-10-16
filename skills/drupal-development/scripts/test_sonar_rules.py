"""Check loss detection and exact retrieval of the supplied Sonar snapshot."""

import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SKILL = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("sonar_rules", SKILL / "scripts/sonar_rules.py")
SONAR = importlib.util.module_from_spec(spec)
spec.loader.exec_module(SONAR)


class SonarSnapshotTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "drupal-development"
        (self.root / "scripts").mkdir(parents=True)
        (self.root / "references").mkdir()
        shutil.copytree(SKILL / "references/sonar", self.root / "references/sonar")
        shutil.copyfile(SKILL / "references/sonar-guidance.md", self.root / "references/sonar-guidance.md")
        shutil.copyfile(SKILL / "scripts/sonar_rules.py", self.root / "scripts/sonar_rules.py")

    def cli(self, *args):
        return subprocess.run([sys.executable, str(self.root / "scripts/sonar_rules.py"), *args],
                              capture_output=True, text=True, encoding="utf-8")

    def edit_export(self, name, change):
        path = self.root / "references/sonar/exports" / name
        doc = json.loads(path.read_text(encoding="utf-8"))
        change(doc)
        path.write_text(json.dumps(doc, ensure_ascii=False), encoding="utf-8")

    def assert_rejected(self, fragment):
        errors = SONAR.verify(self.root)
        self.assertTrue(errors)
        self.assertIn(fragment, "\n".join(errors))

    def test_complete_snapshot_and_unknown_provenance(self):
        self.assertEqual(SONAR.verify(self.root), [])
        manifest = SONAR.read_json(self.root / "references/sonar/manifest.json")
        self.assertEqual((manifest["rule_count"], manifest["section_count"],
                          manifest["context_section_count"]), (566, 1343, 43))
        self.assertIsNone(manifest["provenance"]["active_rule_parameters"])

    def test_missing_export_is_rejected(self):
        (self.root / "references/sonar/exports/html.json").unlink()
        self.assert_rejected("Missing or symlinked Sonar export: html.json")

    def test_altered_description_is_detected(self):
        self.edit_export("php.json", lambda d: d["rules"][0]["descriptionSections"][0].update(content="Changed rule text"))
        self.assert_rejected("Sonar manifest/source mismatch: files")

    def test_omitted_rule_is_detected(self):
        self.edit_export("js.json", lambda d: d["rules"].pop())
        self.assert_rejected("Incomplete Sonar export totals: js.json")

    def test_duplicate_rule_id_is_rejected(self):
        self.edit_export("css.json", lambda d: d["rules"][1].update(key=d["rules"][0]["key"]))
        self.assert_rejected("Duplicate or wrong-language rule key")

    def test_wrong_language_key_is_rejected(self):
        self.edit_export("html.json", lambda d: d["rules"][0].update(key="javascript:S1135"))
        self.assert_rejected("Duplicate or wrong-language rule key")

    def test_lost_context_is_detected(self):
        def remove_context(doc):
            for rule in doc["rules"]:
                for section in rule["descriptionSections"]:
                    if "context" in section:
                        del section["context"]
                        return
        self.edit_export("php.json", remove_context)
        self.assert_rejected("Sonar manifest/source mismatch: context_section_count")

    def test_lost_repeated_section_is_detected(self):
        def drop_variant(doc):
            rule = next(r for r in doc["rules"] if r["key"] == "php:S5808")
            rule["descriptionSections"] = [s for s in rule["descriptionSections"]
                                           if s.get("context", {}).get("key") != "laravel"]
        self.edit_export("php.json", drop_variant)
        self.assert_rejected("Sonar manifest/source mismatch: section_count")

    def test_empty_root_cause_is_rejected(self):
        self.edit_export("php.json", lambda d: d["rules"][0]["descriptionSections"][0].update(content=""))
        self.assert_rejected("Empty description section")

    def test_incomplete_index_is_detected(self):
        path = self.root / "references/sonar/index.md"
        path.write_text("# Incomplete index\n", encoding="utf-8")
        self.assert_rejected("Sonar index is incomplete or stale")

    def test_unlisted_export_is_detected(self):
        (self.root / "references/sonar/exports/extra.json").write_text("{}", encoding="utf-8")
        self.assert_rejected("Sonar export directory has missing or unlisted entries")

    def test_hotspots_with_empty_impacts_are_preserved(self):
        docs = SONAR.snapshot(self.root)
        hotspots = [r for d in docs.values() for r in d["rules"] if r["type"] == "SECURITY_HOTSPOT"]
        self.assertEqual(len(hotspots), 76)
        self.assertTrue(all(r["impacts"] == [] for r in hotspots))
        self.assertEqual(SONAR.verify(self.root), [])

    def test_full_json_retrieval_preserves_framework_variants(self):
        result = self.cli("show", "php:S5808", "--format", "json")
        self.assertEqual(result.returncode, 0, result.stderr)
        retrieved = json.loads(result.stdout)
        source = SONAR.snapshot(self.root)["php.json"]["rules"]
        expected = next(r for r in source if r["key"] == "php:S5808")
        self.assertEqual(retrieved, [expected])
        self.assertEqual([s["context"]["key"] for s in retrieved[0]["descriptionSections"] if "context" in s],
                         ["symfony", "laravel"])

    def test_text_retrieval_exposes_drupal_fallbacks_and_links(self):
        result = self.cli("show", "php:S100", "php:S1781")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Drupal framework is detected", result.stdout)
        self.assertIn("TRUE", result.stdout)
        self.assertIn("do_something", result.stdout)
        self.assertIn("https://", result.stdout)

    def test_language_aliases_and_search_use_full_keys(self):
        result = self.cli("list", "--language", "html")
        self.assertEqual(result.returncode, 0, result.stderr)
        rows = result.stdout.splitlines()
        self.assertEqual(len(rows), 49)
        self.assertTrue(all(row.startswith("Web:") for row in rows))
        result = self.cli("list", "--language", "php", "--search", "Drupal")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("php:S100 |", result.stdout)
        self.assertIn("php:S1781 |", result.stdout)

    def test_unknown_rule_fails_without_substituting_another_language(self):
        result = self.cli("show", "html:S5254")
        self.assertEqual(result.returncode, 2)
        self.assertIn("Unknown full Sonar rule key", result.stderr)

    def test_duplicate_json_object_key_is_rejected(self):
        path = self.root / "references/sonar/exports/php.json"
        path.write_text('{"total":178,"total":179}', encoding="utf-8")
        self.assert_rejected("Duplicate JSON object key: total")

    def test_verify_cli_runs_without_archives_or_server(self):
        result = self.cli("verify")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("566 Sonar rules", result.stdout)


if __name__ == "__main__":
    unittest.main()
