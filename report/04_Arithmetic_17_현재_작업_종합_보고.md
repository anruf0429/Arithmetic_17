# Arithmetic_17 — 현재 작업 종합 보고

**작성일:** 2026-04-27

---

## 1. 보고 목적·범위

| 항목 | 내용 |
|------|------|
| 목적 | 본 프로젝트(`Arithmetic_17`)의 **구현 상태**, **테스트 결과**, **문서 산출물**, **Git 관리 계획**을 한곳에 정리하여 제출·검토에 활용한다. |
| 범위 | 레이어 구조 구현 이후 시점의 코드베이스, `report/` 폴더 보고서 목록, Windows 환경에서의 Git 초기화·첫 커밋 절차 요약 |

---

## 2. 프로젝트 현황 요약

| 항목 | 내용 |
|------|------|
| 루트 | `Arithmetic_17/` |
| 언어 | Python 3.10+ |
| 구조 | `src/`: `App`, `Cli`, `Domain`, `Services`, `Common` — 설계 보고(`02`)와 동일한 레이어 분리 |
| 진입점 | `PYTHONPATH`에 `src` 추가 후 `py -m App` → REPL (`console_runner`) |
| 연산 | `ArithmeticCalculator` — `add` / `subtract` / `multiply` / `divide`, `BinaryExpression` 평가 |
| 예외 | 0으로 나누기 → `DivideByZeroException` (`Common`), 파싱 오류 → `ValueError` 등 |

### 2.1 단위 테스트

| 실행 | 결과 (2026-04-27 확인) |
|------|-------------------------|
| 프로젝트 루트에서 `py run_tests.py` | **10개** 테스트 **전부 통과** (`Domain.Tests`, `Services.Tests`, `Cli.Tests`) |

`tests` 폴더명에 점(`.`)이 포함되어 있어, 표준 `unittest discover` 대신 루트의 `run_tests.py`로 `test_*.py`를 직접 로드하는 방식을 사용한다.

---

## 3. `report/` 문서 체계

| 파일 | 요지 |
|------|------|
| `01_Arithmetic_Git_Push_과제_보고서.md` | Git push 과제 개요, `main` 브랜치·원격 저장소·Description(Author/Reviewer) 요구 정리 |
| `02_Arithmetic_프로젝트_구조_설계_보고서.md` | App / Cli / Domain / Services / Common 레이어 설계 |
| `03_Arithmetic_17_구현_및_보고.md` | `Arithmetic_1004` 제거 후 `src`·`tests` 구조로의 이행, 레이어 책임·예외·테스트 상세 |
| `04_Arithmetic_17_현재_작업_종합_보고.md` | **본 문서** — 현재 작업·검증·Git 절차를 한 페이지로 요약 |
| `05_Arithmetic_17_첫_커밋_메시지_작성_보고.md` | Conventional Commit 형식의 **첫 커밋 메시지** 조건·예시 3건 전문 |

상세 구현·디렉터리 트리는 **`03`** 을 기준으로 한다. 첫 커밋 메시지 문안은 **`05`** 를 참고한다.

---

## 4. Git 저장소 관리 절차 (Windows 요약)

프로젝트를 Git으로 관리할 때의 기본 순서이다. Git for Windows 설치 후 **새 터미널**에서 `git --version`으로 동작을 확인한다.

| 단계 | 내용 |
|------|------|
| 1. 초기화 | `cd C:\DEV\Arithmetic_17` 후 `git init -b main` — 기본 브랜치를 `main`으로 둠 (Git 2.28+) |
| 2. `main` 확인 | `git branch` → `* main` 표시 확인. 예전 방식으로 `master`만 있으면 `git branch -M main` |
| 3. 사용자 정보 (최초 1회) | `git config --global user.name`, `user.email` |
| 4. 첫 커밋 | `.gitignore` 등 준비 후 `git add .`, `git status`로 확인, `git commit -m "…"` |
| 5. 원격 (과제 시) | `01` 보고서 절차에 따라 remote 추가·`git push -u origin main` 등 |

### 4.1 첫 커밋 메시지 예시

| 유형 | 예시 |
|------|------|
| 초기 반영 | `chore: Arithmetic_17 초기 커밋` |
| 한글만 | `첫 커밋: 프로젝트 구조 및 보고서 추가` |
| Conventional | `feat: 사칙연산 레이어 구현 및 단위 테스트` |

---

## 5. 실행·검증 (참고)

| 목적 | 명령 |
|------|------|
| 전체 테스트 | 프로젝트 루트에서 `py run_tests.py` |
| 콘솔 REPL | PowerShell: `$env:PYTHONPATH = "$PWD\src"; py -m App` |

---

## 6. 정리

- **구현**은 `03` 에 기술된 대로 레이어 구조로 정리되었고, **단위 테스트 10건**이 통과한다.
- **보고·제출**용으로 `01`~`03`과 함께 본 **`04`** 를 두어, 과제 진행 상황과 Git 절차를 한 파일에서 파악할 수 있게 했다.
- 원격 저장소 생성·push·Description 작성은 **`01_Arithmetic_Git_Push_과제_보고서.md`** 를 따른다.

---

*본 문서는 2026-04-27 시점 `Arithmetic_17` 저장소 상태 및 작업 내역에 기반한다.*
