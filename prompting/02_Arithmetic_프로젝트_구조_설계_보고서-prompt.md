# Arithmetic project folder structure design
_Exported on 4/27/2026 at 14:44:31 GMT+9 from Cursor (3.0.16)_

---

**User**

Arithmetic 프로젝트의 기본 폴더 구조를 설계해 주세요.

조건:
- 순수 콘솔 기반
- UI, DB 없음
- 사칙연산 기능 포함
- 단일 책임 원칙 고려
- 추후 확장 가능하도록 구조 설계

출력:
- 폴더 구조
- 각 파일 역할 설명
- 클래스 책임 정의


---

**Cursor**

프로젝트 워크스페이스에 기존 코드가 있는지 간단히 확인합니다.



워크스페이스에는 과제 보고서용 문서만 있고 실행 코드는 없습니다. 조건에 맞춘 **일반적인 패키지/폴더 설계**를 제안합니다. 언어는 Java·C#·Python 등 어디에도 옮기기 쉽도록 **역할 중심**으로 잡았습니다.

---

## 폴더 구조 (예시)

```
Arithmetic/
├── src/
│   ├── App/
│   │   └── Program.cs                    # 또는 Main.java, __main__.py 진입점
│   ├── Cli/
│   │   ├── ConsoleRunner.cs             # 실행 루프, 프롬프트
│   │   └── ExpressionParser.cs          # 문자열 → 내부 표현
│   ├── Domain/
│   │   ├── Operation.cs                 # 연산 종류 (덧셈 등)
│   │   ├── BinaryExpression.cs          # 피연산자 + 연산자 묶음 (선택)
│   │   └── CalculationResult.cs         # 결과 값·단위·메타 (선택)
│   ├── Services/
│   │   └── ArithmeticCalculator.cs      # 실제 계산 수행
│   └── Common/
│       ├── DivideByZeroException.cs     # 도메인 예외 예시
│       └── ValidationMessages.cs        # 에러 메시지 상수 (선택)
├── tests/
│   ├── Domain.Tests/
│   ├── Services.Tests/
│   └── Cli.Tests/
├── Arithmetic.sln                       # 또는 pom.xml, pyproject.toml 등
└── README.md
```

**네이밍**: 실제 프로젝트에서는 `Arithmetic` 하나의 루트 네임스페이스 아래에 `Arithmetic.Cli`, `Arithmetic.Domain`처럼 묶어도 됩니다.

---

## 각 파일(또는 모듈) 역할

| 위치 | 역할 |
|------|------|
| **`App/Program`** | 프로세스 시작만 담당. DI/설정이 있으면 여기서 조립하고 `ConsoleRunner`에 위임. |
| **`Cli/ConsoleRunner`** | 콘솔 읽기/쓰기, 명령 한 번 처리 흐름(입력 받기 → 파싱 → 계산 → 출력). **비즈니스 규칙은 넣지 않음.** |
| **`Cli/ExpressionParser`** | 사용자 문자열을 도메인 객체(연산 종류, 피연산자)로 변환. 파싱 규칙 변경 시 여기만 수정. |
| **`Domain/Operation`** | 지원하는 연산 집합(열거형 또는 전략 키). 새 연산 추가 시 확장 지점. |
| **`Domain/BinaryExpression`** | (선택) 좌·우 피연산자와 연산 하나를 표현하는 불변 값 객체. 테스트와 재사용에 유리. |
| **`Domain/CalculationResult`** | (선택) 결과 래핑, 나중에 “단계별 로그”, “분수 모드” 등 확장 시 사용. |
| **`Services/ArithmeticCalculator`** | **유효한 입력**에 대해 사칙연산만 수행. 0으로 나누기 같은 규칙은 여기서 결정하거나 예외로 표현. |
| **`Common/*`** | 도메인 외 공용 예외·문자열·작은 헬퍼. 과도하게 비대해지지 않게 유지. |
| **`tests/*`** | 단위 테스트: Calculator·Parser·(있다면) Domain 순으로. |

---

## 클래스 책임 정의 (단일 책임 기준)

1. **`Program` / `Main`**  
   - 애플리케이션 부팅, 의존성 생성·연결, 종료 코드만 책임.

2. **`ConsoleRunner`**  
   - “언제 입력을 받고, 어떤 순서로 서비스를 호출할지”만 책임. 계산 공식·파싱 규칙은 책임지지 않음.

3. **`ExpressionParser`**  
   - 입력 문자열 해석 책임만. 잘못된 형식은 여기서 판별하거나 구조화된 오류 정보 반환.

4. **`Operation` (또는 `IOperation` + 구현체들)**  
   - “어떤 연산이 존재하는지”와 연산별 식별만. 실제 숫자 계산은 Calculator에 두어도 되고, **전략 패턴**으로 나누면 연산 추가 시 `Operation.Add` 클래스만 추가하는 식으로 확장 가능.

5. **`ArithmeticCalculator`**  
   - 숫자와 연산에 따른 결과 산출만 책임. 콘솔·문자열 형식과 무관.

6. **`BinaryExpression`** (선택)  
   - 한 번의 계산에 필요한 데이터 구조 고정. Parser 출력과 Calculator 입력의 계약 역할.

7. **예외 클래스 (`DivideByZeroException` 등)**  
   - 실패 유형을 호출자(`ConsoleRunner`)가 사용자 메시지로 바꿀 수 있게 하는 신호.

---

## 확장을 열어두는 포인트

- **새 연산**(나머지, 거듭제곱): `Operation` + Calculator 내부 또는 전략 구현 추가. Parser에 토큰·문법만 반영.
- **입력 형식 변경**(후위 표기, 공백 규칙): `ExpressionParser`만 교체·확장.
- **출력 형식**(로그 레벨, 파일 로깅): `ConsoleRunner` 옆에 `IOutputSink` 같은 인터페이스를 두고 구현체 분리.

이 구조면 **콘솔 전용**, **DB/UI 없음**, **사칙연산**, **SRP**, **확장** 조건을 한 번에 만족하기 쉽습니다. 사용 언어(C#, Java, Python 등)를 정하면 그 언어 관례에 맞춰 파일 확장자와 빌드 파일명만 바꿔 적용하면 됩니다.

---

**User**

report  폴더를 만들어서 지금 작업한 내용을 보고서로 내보내줘

---

**Cursor**

기존 보고서 형식과 `report` 폴더 상태를 확인합니다.



`report` 폴더가 이미 있습니다. 이전 대화에서 정리한 **Arithmetic 프로젝트 폴더 구조 설계**를 동일한 보고서 스타일로 문서화합니다.



작업 반영했습니다.

**`report` 폴더**는 이미 있어서, 그 안에 이번에 정리한 설계를 **새 보고서 파일**로 넣었습니다.

| 파일 | 설명 |
|------|------|
| `report\02_Arithmetic_프로젝트_구조_설계_보고서.md` | 설계 목적·범위, 폴더 트리, 파일·폴더 역할 표, 클래스 책임 표, 확장 시 수정 포인트, 요약 |

기존 `01_Arithmetic_Git_Push_과제_보고서.md`와 맞추려고 **표·섹션 번호·작성일(2026-04-27)** 형식을 비슷하게 맞춰 두었습니다. 필요하면 과제 형식에 맞게 제목이나 번호만 바꾸면 됩니다.

