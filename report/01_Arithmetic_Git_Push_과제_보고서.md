# Arithmetic Git Push 과제 — 정리 보고서

**작성일:** 2026-04-27

---

## 1. 과제 개요

| 항목 | 내용 |
|------|------|
| 목표 | Arithmetic 관련 작업을 Git에 반영한 뒤 **원격 저장소에 push** |
| Repository 이름 | `Arithmetic_XX` (예: `Arithmetic_01`, 본인 번호에 맞게 사용) |
| Description | **Author**와 **Reviewer** 이름 **필수 포함** |
| 작업 분기 | **`main` 브랜치**에서 **commit** 후 **push** |

---

## 2. 수행 절차

1. 로컬에서 작업이 과제 기준에 맞는지 확인한다.
2. 저장소가 없으면 원격에 `Arithmetic_XX` 이름으로 **repository**를 만든다 (플랫폼은 강의/과제 지시에 따른다).
3. 필요 시 `git init` 후 `git remote add origin <URL>`로 **remote**를 연결한다.
4. **`main`에서 작업**한다 — 기본 분기가 `main`이 아니면 `main`으로 맞춘 뒤 진행한다.
5. 변경을 스테이징(`git add`)한 뒤 **`main`에서 commit**한다.
6. 원격에 **push**한다 (일반적으로 `main` → `origin/main`, 최초에는 `git push -u origin main` 등).
7. 저장소 **Description** 필드에 **Author, Reviewer 이름**을 **명시**한다 (강의에서 형식·예시가 있으면 그에 맞춘다).

---

## 3. 명명 규칙

| 구분 | 규칙 |
|------|------|
| **Repository 이름** | `Arithmetic_XX` — `XX`는 **지정된 번호** (본인 과제 번호 사용) |
| **브랜치** | **작업·최종 반영**은 **`main`** (별도 정책이 없는 한 `main`이 기준) |
| **Description** | **Author 이름**, **Reviewer 이름** **모두** 포함 |

---

## 4. 필수 제출 요소

- **원격 Repository** 이름: **`Arithmetic_XX`**
- **커밋·푸시**: **`main` 브랜치**에 commit이 있고, **push**가 완료될 것
- **Description**: **Author**와 **Reviewer** 이름 **포함** (누락 시 감점·미제출로 처리될 수 있음)
- 강의/시스템이 별도로 정한 경우: **URL 제출**, 스크린샷, 제출 링크 등 (해당 **안내문이 최종 기준**)

---

## 5. 실수하기 쉬운 부분

- **`main`이 아닌 브랜치**에만 commit하고, **`main`은 비어** 있거나 **`master`에만** push하는 경우
- Repository 이름 **오타** 또는 **번호 착오** (예: `Arithmatic`, `Arithmetic_01` vs `Arithmetic_17` 혼동)
- **README**에만 Author/Reviewer를 적고, **웹에서 보이는 repository Description**에 **누락**하는 경우
- **최초 push** 시: remote 미설정, `upstream` 없이 `git push`만 시도해 **오류**가 나는 경우
- **인증**: HTTPS/SSH, **2FA**·**personal access token** 등 미설정으로 **push 실패**하는 경우
- **.gitignore** 누락으로 불필요한 **대용량/비밀** 파일이 커밋에 포함되는 경우 (과제에서 제한하는 경우)

---

## 6. 체크리스트 (자가 점검)

- [ ] Repository 이름: `Arithmetic_XX` (본인 번호)
- [ ] `main` 브랜치에 반영·push 완료
- [ ] Description에 **Author** 명시
- [ ] Description에 **Reviewer** 명시
- [ ] 강의에 따른 **제출 방식** (URL/과제 시스템) 완료

---

*본 문서는 과제 안내를 구조화하여 정리한 내부용 보고서이며, 최종 기준은 강의/PL의 공식 지시에 따릅니다.*
