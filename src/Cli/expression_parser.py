"""
문자열 → 내부 표현 `BinaryExpression`.

단순 `"12 + 3"` / `"1.5*2"` 형식만 다루는 최소 구현(범위는 제한).
"""

from __future__ import annotations

import re

from Common.validation_messages import INVALID_EXPRESSION
from Domain.binary_expression import BinaryExpression
from Domain.operation import Operation

_PATTERN = re.compile(
    r"^\s*("
    r"[-+]?[0-9]+(?:\.[0-9]*)?|[-+]?\.[0-9]+"
    r")"
    r"\s*([+*/-])\s*"
    r"("
    r"[-+]?[0-9]+(?:\.[0-9]*)?|[-+]?\.[0-9]+"
    r")\s*$"
)

_OP_MAP: dict[str, Operation] = {
    "+": Operation.ADD,
    "-": Operation.SUBTRACT,
    "*": Operation.MULTIPLY,
    "/": Operation.DIVIDE,
}


def parse_expression(s: str) -> BinaryExpression:
    m = _PATTERN.match(s)
    if not m:
        raise ValueError(INVALID_EXPRESSION)
    a = float(m.group(1))
    sym = m.group(2)
    b = float(m.group(3))
    if sym not in _OP_MAP:
        raise ValueError(INVALID_EXPRESSION)
    return BinaryExpression(left=a, op=_OP_MAP[sym], right=b)
