"""계산 결과 값(·추가 메타 확장용) (선택)"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CalculationResult:
    value: float
