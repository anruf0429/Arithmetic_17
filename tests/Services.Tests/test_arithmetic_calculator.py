from __future__ import annotations

import unittest

from Common.divide_by_zero_exception import DivideByZeroException
from Services.arithmetic_calculator import ArithmeticCalculator
from Domain.binary_expression import BinaryExpression
from Domain.operation import Operation


class TestArithmeticCalculator(unittest.TestCase):
    def setUp(self) -> None:
        self.c = ArithmeticCalculator()

    def test_add(self) -> None:
        self.assertEqual(self.c.add(2, 3), 5)
        self.assertEqual(self.c.add(0.1, 0.2), 0.30000000000000004)
        self.assertAlmostEqual(self.c.add(0.1, 0.2), 0.3, places=7)

    def test_subtract(self) -> None:
        self.assertEqual(self.c.subtract(5, 3), 2)
        self.assertEqual(self.c.subtract(1.5, 0.5), 1.0)

    def test_multiply(self) -> None:
        self.assertEqual(self.c.multiply(3, 4), 12)
        self.assertEqual(self.c.multiply(0, 99), 0)

    def test_divide(self) -> None:
        self.assertEqual(self.c.divide(10, 2), 5.0)
        self.assertEqual(self.c.divide(0, 5), 0.0)

    def test_divide_by_zero(self) -> None:
        with self.assertRaises(DivideByZeroException) as ctx:
            self.c.divide(1, 0)
        self.assertIn("divisor", str(ctx.exception).lower())

    def test_evaluate(self) -> None:
        be = BinaryExpression(2.0, Operation.ADD, 3.0)
        r = self.c.evaluate(be)
        self.assertEqual(r.value, 5.0)


if __name__ == "__main__":
    unittest.main()
