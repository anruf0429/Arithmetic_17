from __future__ import annotations

import unittest

from Domain.operation import Operation


class TestOperation(unittest.TestCase):
    def test_all_members(self) -> None:
        self.assertIn(Operation.ADD, Operation)
        self.assertIn(Operation.SUBTRACT, Operation)
        self.assertIn(Operation.MULTIPLY, Operation)
        self.assertIn(Operation.DIVIDE, Operation)


if __name__ == "__main__":
    unittest.main()
