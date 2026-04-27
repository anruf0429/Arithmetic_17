"""`src` 를 `PYTHONPATH`에 넣은 뒤 `test_*.py`를 파일 기준으로 로드 (점(.)이 폴더명에 있어도 동작)"""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(_ROOT / "src"))


def _load_test_module(file_path: Path) -> object:
    unique = f"_{file_path.parent.name.replace('.', '_')}_{file_path.stem}"
    spec = importlib.util.spec_from_file_location(unique, file_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load: {file_path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _suite() -> unittest.TestSuite:
    tests_dir = _ROOT / "tests"
    loader = unittest.TestLoader()
    all_tests = unittest.TestSuite()
    for f in sorted(tests_dir.rglob("test_*.py")):
        if "__pycache__" in f.parts or "site-packages" in f.parts:
            continue
        mod = _load_test_module(f)
        all_tests.addTests(loader.loadTestsFromModule(mod))
    return all_tests


if __name__ == "__main__":
    result = unittest.TextTestRunner(verbosity=2).run(_suite())
    raise SystemExit(0 if result.wasSuccessful() else 1)
