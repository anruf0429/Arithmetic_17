"""피연산자 + 연산자를 묶은 이항 표현 (선택)"""

from __future__ import annotations

from dataclasses import dataclass

from .operation import Operation


@dataclass(frozen=True)
class BinaryExpression:
    left: float
    op: Operation
    right: float
