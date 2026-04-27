from __future__ import annotations

import unittest

from Common.divide_by_zero_exception import DivideByZeroException
from Services.arithmetic_calculator import ArithmeticCalculator
from Domain.operation import Operation
from Cli.expression_parser import parse_expression
from Common.validation_messages import INVALID_EXPRESSION


class TestExpressionParser(unittest.TestCase):
    def test_parse_add(self) -> None:
        b = parse_expression("2 + 3")
        self.assertEqual(b.op, Operation.ADD)
        self.assertEqual(b.left, 2.0)
        self.assertEqual(b.right, 3.0)
        c = ArithmeticCalculator()
        self.assertEqual(c.evaluate(b).value, 5.0)

    def test_parse_invalid(self) -> None:
        with self.assertRaises(ValueError) as ctx:
            parse_expression("nope")
        self.assertIn(INVALID_EXPRESSION, str(ctx.exception))

    def test_parse_divide_by_zero_calculation(self) -> None:
        b = parse_expression("1 / 0")
        c = ArithmeticCalculator()
        with self.assertRaises(DivideByZeroException) as ctx:
            c.evaluate(b)
        self.assertIn("divisor", str(ctx.exception).lower())


if __name__ == "__main__":
    unittest.main()
