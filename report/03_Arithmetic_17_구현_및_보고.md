# Arithmetic_17 — 레이어 구조 구현·이행 보고

**작성일:** 2026-04-27

---

## 1. 작업 개요

| 항목 | 내용 |
|------|------|
| 목적 | `Arithmetic_1004` 일회용 폴더를 **제거**하고, 설계안에 맞춘 **`src` / `tests` 레이어 구조**로 **Python** 프로젝트를 정리 |
| 언어·런타임 | Python 3.10+ |
| 루트 | `Arithmetic_17/` (본 저장소/작업 루트) |
| 산출 | `src` 밑 `App`·`Cli`·`Domain`·`Services`·`Common`, `tests` 밑 도메인/서비스/CLI 단위 테스트, `run_tests.py`·`pyproject.toml`·`README.md` |

---

## 2. 이전·삭제

| 사항 | 처리 |
|------|------|
| `Arithmetic_1004/` | 단일 모듈(`arithmetic.py`)·`test_arithmetic.py` 중심 구조였음. **삭제**하고, 역할은 `src` 아래 레이어로 **이전** |
| 사칙연산 로직 | `Services/ArithmeticCalculator` (메서드 `add`·`subtract`·`multiply`·`divide`, `evaluate` 가 선택적 편의 API) |
| 0으로 나누기 | `Common/DivideByZeroException` + `Common/validation_messages` (메시지 상수) |

---

## 3. 실제 디렉터리 구조 (요약)

```
Arithmetic_17/
├── src/
│   ├── App/
│   │   ├── __init__.py
│   │   └── __main__.py              # 진입점: Cli.console_runner.main
│   ├── Cli/
│   │   ├── __init__.py
│   │   ├── console_runner.py      # REPL(한 줄씩 식 → 결과, 빈 줄로 종료)
│   │   └── expression_parser.py     # 문자열 → BinaryExpression (최소 이항식)
│   ├── Domain/
│   │   ├── __init__.py
│   │   ├── operation.py             # Operation(열거형)
│   │   ├── binary_expression.py     # left, op, right
│   │   └── calculation_result.py   # value 래핑(확장용)
│   ├── Services/
│   │   ├── __init__.py
│   │   └── arithmetic_calculator.py # 사칙연산·이항식 평가
│   └── Common/
│       ├── __init__.py
│       ├── divide_by_zero_exception.py
│       └── validation_messages.py
├── tests/
│   ├── Domain.Tests/                # C# 스타일 네이밍 유지
│   ├── Services.Tests/
│   └── Cli.Tests/
├── run_tests.py                    # `src`를 path에 넣고 test_*.py를 파일 단위로 로드
├── pyproject.toml
├── README.md
└── report/
    └── 03_Arithmetic_17_구현_및_보고.md
```

`PYTHONPATH`에 `src`를 두면 `import Common`, `import Services` 등 **최상위 패키지명**으로 import한다. (`src`는 패키지 루트로 취급)

---

## 4. 레이어·책임 (구현 기준)

| 위치 | 역할 |
|------|------|
| `App` | `python -m App` 시 `__main__`이 `Cli` 쪽 `main` 호출(부팅만) |
| `Cli` | 입력/출력 흐름, `parse_expression`으로 문자열 → `BinaryExpression`, `ArithmeticCalculator`로 계산·출력 |
| `Domain` | `Operation`·`BinaryExpression`·`CalculationResult` — **형태와 의미**만, IO 없음 |
| `Services` | `ArithmeticCalculator` — 실제 수치 연산, `BinaryExpression` → `CalculationResult`의 `evaluate` |
| `Common` | `DivideByZeroException`(0으로 나누기), `validation_messages` |

---

## 5. 예외·검안

| 상황 | 동작 |
|------|------|
| 제수가 0 | `DivideByZeroException` 발생(기본 메시지는 `validation_messages.DIVISOR_MUST_NOT_BE_ZERO`) |
| 파싱 실패(형식 없음) | `ValueError`, 메시지에 `INVALID_EXPRESSION` 사용 |
| `ArithmeticError` | 도메인 예외가 `ArithmeticError`를 상속해, 필요 시 상위에서 묶어 처리 가능 |

---

## 6. 단위 테스트

| 경로 | 검증 내용 |
|------|------------|
| `tests/Domain.Tests/test_domain.py` | `Operation` 열거에 네 가지 연산이 존재 |
| `tests/Services.Tests/test_arithmetic_calculator.py` | 사칙, 0으로 나누기, `BinaryExpression` `evaluate` |
| `tests/Cli.Tests/test_expression_parser.py` | 파싱, 잘못된 입력, `1 / 0` 파싱 후 `evaluate`에서 예외 |

- **10개** 테스트, 루트에서 `py run_tests.py` 로 실행.
- `tests/Domain.Tests` 처럼 **폴더 이름에 점(`.`)**이 있어, 표준 `unittest discover`만 쓰면 import 이름이 꼬일 수 있으므로 **`run_tests.py`는 `test_*.py` 파일 경로로 직접 모듈 로드**하도록 구현됨.

---

## 7. 실행 방법 (참고)

| 목적 | 명령(예) |
|------|----------|
| 전체 테스트 | `py run_tests.py` (작업 루트: `Arithmetic_17`) |
| 콘솔 REPL | `PYTHONPATH`에 `.../Arithmetic_17/src`를 넣은 뒤 `py -m App` (상세: `README.md`) |

---

## 8. 정리

- **설계 보고(02)에서 제안한** `App / Cli / Domain / Services / Common` + `tests` 삼분 **구조**를 **Python**으로 **반영**함.
- 초기 `Arithmetic_1004` **단일 폴더 구현**은 **삭제**하고, 동일한 기능·테스트는 **Services·Common·Domain·Cli**에 **나누어** 두었음.
- **보고·제출**용으로 본 문서를 `report/`에 두었음.

---

*본 문서는 2026-04-27 시점 `Arithmetic_17` 작업 내용에 기반한다.*
