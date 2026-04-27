"""실행 루프·프롬프트(최소)"""

from __future__ import annotations

from Common.divide_by_zero_exception import DivideByZeroException
from Services.arithmetic_calculator import ArithmeticCalculator
from Cli.expression_parser import parse_expression


def run_repl() -> None:
    """한 줄씩 `식`을 입력 → 결과 출력(종료: 빈 줄)."""
    calc = ArithmeticCalculator()
    print("이항식 (예: 1 + 2) 입력. 끝내려면 빈 줄. ")
    while True:
        line = input("> ").strip()
        if not line:
            break
        try:
            ex = parse_expression(line)
            r = calc.evaluate(ex)
            print(r.value)
        except (ValueError, DivideByZeroException) as e:
            print("오류:", e)


def main() -> None:
    run_repl()
