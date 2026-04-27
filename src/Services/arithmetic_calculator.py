"""
실제 사칙연산 수행.

`BinaryExpression`을 받는 편의 메서드는 선택적으로 제공합니다.
"""

from __future__ import annotations

from Common.divide_by_zero_exception import DivideByZeroException
from Common.validation_messages import DIVISOR_MUST_NOT_BE_ZERO
from Domain.binary_expression import BinaryExpression
from Domain.calculation_result import CalculationResult
from Domain.operation import Operation


class ArithmeticCalculator:
    """add / subtract / multiply / divide (0으로 나누기는 도메인 예외)"""

    def add(self, a: float, b: float) -> float:
        return a + b

    def subtract(self, a: float, b: float) -> float:
        return a - b

    def multiply(self, a: float, b: float) -> float:
        return a * b

    def divide(self, a: float, b: float) -> float:
        if b == 0:
            raise DivideByZeroException(DIVISOR_MUST_NOT_BE_ZERO)
        return a / b

    def evaluate(self, expression: BinaryExpression) -> CalculationResult:
        """이항식 → `CalculationResult` (선택)"""
        op = expression.op
        a, b = expression.left, expression.right
        if op is Operation.ADD:
            v = self.add(a, b)
        elif op is Operation.SUBTRACT:
            v = self.subtract(a, b)
        elif op is Operation.MULTIPLY:
            v = self.multiply(a, b)
        else:
            v = self.divide(a, b)
        return CalculationResult(v)
