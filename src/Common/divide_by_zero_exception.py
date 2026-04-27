"""
도메인: 0으로 나누기.

표준 `ZeroDivisionError` 대신, 서비스/도메인 경계에서 의도를 드러내기 위해
별도 예외로 둡니다. 호출부에서 `ArithmeticError`로 같이 잡을 수도 있습니다.
"""

from __future__ import annotations

from .validation_messages import DIVISOR_MUST_NOT_BE_ZERO


class DivideByZeroException(ArithmeticError):
    """제수(나누는 수)가 0인 경우"""

    def __init__(self, message: str | None = None) -> None:
        super().__init__(message or DIVISOR_MUST_NOT_BE_ZERO)
