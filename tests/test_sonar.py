"""Run the installed skill's Sonar snapshot tests in repository CI."""

import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "skills/drupal-development/scripts/test_sonar_rules.py"
spec = importlib.util.spec_from_file_location("skill_sonar_tests", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


def load_tests(loader, tests, pattern):
    return loader.loadTestsFromModule(module)
