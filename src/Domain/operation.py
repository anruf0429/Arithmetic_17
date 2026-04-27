"""연산 종류(덧셈 등)"""

from __future__ import annotations

from enum import Enum, auto


class Operation(Enum):
    ADD = auto()
    SUBTRACT = auto()
    MULTIPLY = auto()
    DIVIDE = auto()
