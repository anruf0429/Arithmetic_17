# Arithmetic_17

`src`와 `tests`의 분리, 도메인·서비스·CLI·App 레이어 구조.

## 구조(요지)

- `src/App/`: `__main__.py` (진입점; `App` 모듈 실행)
- `src/Cli/`: `console_runner` (REPL), `expression_parser` (문자열 → `BinaryExpression`)
- `src/Domain/`: `Operation`, `BinaryExpression`, `CalculationResult`
- `src/Services/`: `ArithmeticCalculator` (사칙연산)
- `src/Common/`: `DivideByZeroException`, `validation_messages`
- `tests/Domain.Tests/`, `tests/Services.Tests/`, `tests/Cli.Tests/`: 단위 테스트
- `pyproject.toml`

## 실행

- 프로젝트 루트에서 `src` 를 경로에 둡니다. 예 (PowerShell):

  ```text
  $env:PYTHONPATH = "$PWD\src"
  py -m App
  ```

- 루트에 있는 `run_tests.py`로 테스트(내부에서 `src` 를 임시로 `sys.path`에 추가):

  ```text
  py run_tests.py
  ```

0으로 나누는 경우는 `DivideByZeroException`( `ArithmeticError` )으로 처리됩니다.
