# Arithmetic_17 — 첫 커밋 메시지 작성 보고

**작성일:** 2026-04-27

---

## 1. 보고 목적·범위

| 항목 | 내용 |
|------|------|
| 목적 | Git **첫 커밋** 시 사용할 메시지를 **Conventional Commits** 규칙에 맞게 준비하고, **한 줄 요약 + 본문** 형태로 변경 범위를 명확히 기록한다. |
| 범위 | 요구 조건 정리, 현재 코드베이스 기준 반영 내용 요약, 제안 메시지 **예시 3건** 전문 |

---

## 2. 요구 조건

| 조건 | 설명 |
|------|------|
| 형식 | **Conventional Commit** (`<type>(optional-scope): 요약`) |
| 명확성 | 변경 내용을 제목·본문에서 바로 파악 가능할 것 |
| 구조 | **한 줄 요약** 후 빈 줄, 그다음 **상세 설명**(본문) |
| 산출 | 동일 조건을 만족하는 **예시 3개** |

---

## 3. 커밋에 담기는 작업 범위 (현재 저장소 기준)

첫 커밋에는 아래가 함께 포함되는 것으로 가정하였다.

| 구분 | 내용 |
|------|------|
| 구현 | Python 3.10+, `src/` — `App`, `Cli`(REPL·표현식 파서), `Domain`, `Services`(사칙연산), `Common`(0으로 나누기 예외 등) |
| 테스트 | `tests/Domain.Tests`, `Services.Tests`, `Cli.Tests`, 루트 `run_tests.py` |
| 설정·안내 | `pyproject.toml`, `README.md` |
| 문서 | `report/`, `prompting/` 과제·설계·구현 보고 및 프롬프트 |

원격 저장소 생성·push·Description(Author/Reviewer)은 **`01_Arithmetic_Git_Push_과제_보고서.md`** 절차를 따른다.

---

## 4. 산출물: 첫 커밋 메시지 예시 3건

### 예시 1 — 기능 중심 (`feat`)

```
feat(calculator): Arithmetic_17 레이어형 사칙연산 프로젝트 초기 반영

- App(`py -m App`), Cli(REPL·표현식 파서), Domain(Operation·BinaryExpression 등),
  Services(ArithmeticCalculator), Common(0으로 나누기 예외 등) 구조 추가
- Domain/Services/Cli 단위 테스트 및 루트 run_tests.py 경로 로딩 방식 적용
- pyproject.toml, README, 과제·설계·구현 보고서(prompting/report) 포함
```

### 예시 2 — 저장소 스캐폴드 중심 (`chore`)

```
chore: Arithmetic_17 저장소 초기 커밋 — 레이어 설계·테스트·문서 포함

- Python 패키지 레이아웃(src/*)과 setuptools 메타(pyproject.toml) 추가
- 사칙연산 도메인·계산 서비스·CLI 파서/실행기 구현 및 unittest 10건 구성
- Git 관리·프로젝트 구조·구현 내역을 정리한 report/ 및 prompting/ 마크다운 추가
```

### 예시 3 — 구현과 문서를 균형 있게 (`feat`)

```
feat: 레이어 분리 사칙연산기와 제출용 보고서 일괄 추가

구현: BinaryExpression 평가, 문자열 파싱, 콘솔 REPL, DivideByZeroException 처리
품질: Domain.Tests / Services.Tests / Cli.Tests 및 run_tests.py 실행 경로
문서: report/, prompting/ 보고서·프롬프트, README에 실행·테스트 방법 명시
```

---

## 5. 형식 참고

- 첫 줄은 `<type>(optional-scope): 요약` 형태로 두고, **약 50자 전후**로 짧게 유지하는 것이 일반적이다.
- 빈 줄 다음 본문에는 **bullet** 또는 짧은 문단으로 디렉터리·역할을 나누어 적으면 리뷰·과제 채점 시 읽기 좋다.
- `feat`는 사용자 가치가 있는 기능 추가, `chore`는 초기 묶음·도구·메타 작업에 자주 쓴다. 팀·과제 규칙에 맞춰 **type 하나로 통일**해도 된다.

---

## 6. 관련 문서

| 파일 | 관계 |
|------|------|
| `01_Arithmetic_Git_Push_과제_보고서.md` | 원격 저장소·`main`·push·Description 요구 |
| `04_Arithmetic_17_현재_작업_종합_보고.md` | 프로젝트 현황·Git 절차 요약 |

---

*본 문서는 2026-04-27 시점 Arithmetic_17 작업 내역(첫 커밋 메시지 작성)을 보고서로 남긴 것이다.*
