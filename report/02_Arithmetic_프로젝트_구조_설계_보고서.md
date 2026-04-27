# Arithmetic 프로젝트 기본 폴더 구조 설계 — 보고서

**작성일:** 2026-04-27

---

## 1. 설계 목적·범위

| 항목 | 내용 |
|------|------|
| 실행 환경 | **순수 콘솔** 기반 |
| 제외 범위 | **UI 프레임워크**, **DB** 없음 |
| 핵심 기능 | **사칙연산**(덧셈, 뺄셈, 곱셈, 나눗셈) |
| 설계 원칙 | **단일 책임 원칙(SRP)** 반영 |
| 향후 대응 | 연산 추가, 입력 형식 변경, 출력 대상 분리 등 **확장**을 고려한 레이어링 |

본 문서는 소스 코드가 아니라 **프로젝트 디렉터리 구조와 각 구성 요소의 책임**을 정의한 설계 산출물이다.

---

## 2. 제안 폴더 구조

```
Arithmetic/
├── src/
│   ├── App/
│   │   └── Program.cs                    # 언어별: Main.java, __main__.py 등 진입점에 대응
│   ├── Cli/
│   │   ├── ConsoleRunner.cs             # 콘솔 실행 루프·프롬프트
│   │   └── ExpressionParser.cs          # 문자열 입력 → 도메인 표현으로 변환
│   ├── Domain/
│   │   ├── Operation.cs                 # 연산 종류 정의
│   │   ├── BinaryExpression.cs          # (선택) 피연산자·연산 한 묶음 표현
│   │   └── CalculationResult.cs         # (선택) 결과 래핑·확장용
│   ├── Services/
│   │   └── ArithmeticCalculator.cs      # 실제 산술 계산
│   └── Common/
│       ├── DivideByZeroException.cs     # 도메인 예외 예시
│       └── ValidationMessages.cs        # (선택) 오류 메시지 상수
├── tests/
│   ├── Domain.Tests/
│   ├── Services.Tests/
│   └── Cli.Tests/
├── Arithmetic.sln                       # 또는 pom.xml, pyproject.toml 등 빌드·의존성 정의
└── README.md
```

**참고:** 실제 구현 시 루트 네임스페이스·패키지 하나 아래에 `Arithmetic.App`, `Arithmetic.Cli` 형태로 묶어도 된다. 확장자와 빌드 파일명은 사용 언어에 맞게 조정한다.

---

## 3. 폴더·파일별 역할

| 위치 | 역할 요약 |
|------|-----------|
| **`App/Program`** | 프로세스 시작. 필요 시 의존성 조립 후 `ConsoleRunner`에 위임만 담당. |
| **`Cli/ConsoleRunner`** | 콘솔 입출력, 한 번의 처리 흐름(입력 → 파싱 → 계산 → 출력). **비즈니스 규칙은 두지 않음.** |
| **`Cli/ExpressionParser`** | 사용자 문자열을 도메인이 이해할 형태로 파싱. 파싱 규칙 변경 시 수정 범위를 이곳으로 한정. |
| **`Domain/Operation`** | 지원 연산 집합(열거형 또는 전략 키). 새 연산 추가 시 확장 지점. |
| **`Domain/BinaryExpression`** | (선택) 좌·우 피연산자와 연산을 담는 불변 값 객체. 테스트·재사용에 유리. |
| **`Domain/CalculationResult`** | (선택) 결과 타입 고정 및 추후 로그·표현 방식 확장 시 사용. |
| **`Services/ArithmeticCalculator`** | 유효한 입력에 대한 **숫자 계산만** 수행. 0으로 나누기 등 규칙은 여기서 처리하거나 예외로 표현. |
| **`Common/*`** | 도메인 외 공용 예외·문자열 등. 과도한 비대화를 피한다. |
| **`tests/*`** | 단위 테스트: Calculator, Parser, Domain 순으로 검증하는 것을 권장. |

---

## 4. 클래스(또는 모듈) 책임 정의

다음은 **단일 책임** 기준으로 역할을 나눈 정의이다.

| 구성 요소 | 책임 |
|-----------|------|
| **`Program` / `Main`** | 애플리케이션 부팅, 의존성 생성·연결, 종료 코드. |
| **`ConsoleRunner`** | “언제 입력을 받고 어떤 순서로 서비스를 호출할지”만 책임. 계산 공식·파싱 세부는 책임지지 않음. |
| **`ExpressionParser`** | 입력 문자열 해석만 담당. 잘못된 형식 판별 또는 구조화된 오류 정보 반환. |
| **`Operation`** (또는 `IOperation` + 구현체) | 존재하는 연산과 식별. 계산 로직은 Calculator에 두거나, 전략 패턴으로 연산별 클래스 분리 시 **연산 추가만 국소 수정** 가능. |
| **`ArithmeticCalculator`** | 숫자와 연산에 따른 결과 산출. 콘솔·문자열 형식과 무관. |
| **`BinaryExpression`** (선택) | 한 번의 계산에 필요한 데이터 구조. Parser 출력과 Calculator 입력 간 **계약** 역할. |
| **도메인 예외** (`DivideByZeroException` 등) | 실패 유형을 신호로 전달. `ConsoleRunner`가 사용자 메시지로 변환. |

---

## 5. 확장 시 수정 포인트

| 확장 요구 | 주로 수정하는 영역 |
|-----------|---------------------|
| 새 연산(나머지, 거듭제곱 등) | `Operation`, `ArithmeticCalculator`(또는 연산 전략 구현), Parser에 토큰·문법 반영 |
| 입력 형식 변경(후위 표기, 공백 규칙) | `ExpressionParser` |
| 출력 대상 분리(파일, 로깅 등) | `ConsoleRunner`와 출력을 인터페이스(`IOutputSink` 등)로 분리한 구현체 추가 |

---

## 6. 요약

- **콘솔 전용**, **DB/UI 없음**, **사칙연산** 요구를 **Cli / Domain / Services / Common**으로 분리하면 SRP와 테스트 용이성을 동시에 확보할 수 있다.
- **확장**은 Parser(입력)·Calculator·Operation(연산 집합) 세 축으로 나누어 변경 범위를 예측 가능하게 유지한다.

---

*본 문서는 2026-04-27 세션에서 수행한 폴더 구조 설계 내용을 보고서 형식으로 정리한 것이다.*
