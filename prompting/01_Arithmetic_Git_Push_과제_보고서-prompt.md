# Assignment structure for Git push
_Exported on 4/27/2026 at 14:38:30 GMT+9 from Cursor (3.0.16)_

---

**User**

다음 과제 내용을 구조적으로 정리해 주세요.

과제:
- Arithmetic Git Push하기
- Repository 이름: Arithmetic_XX (예: Arithmetic_01)
- Author, Reviewer 이름을 description에 포함
- main 브랜치에서 commit 후 push

정리 항목:
1. 수행 절차
2. 명명 규칙
3. 필수 제출 요소
4. 실수하기 쉬운 부분


---

**Cursor**

# Arithmetic Git Push 과제 — 구조적 정리

## 과제 요약
- **목표**: Arithmetic 관련 작업을 Git에 반영한 뒤 **원격 저장소에 push**한다.  
- **저장소 이름**: `Arithmetic_XX` 형식 (예: `Arithmetic_01` — 본인 번호에 맞게 사용).  
- **설명(description)**: **Author**와 **Reviewer** 이름을 반드시 포함.  
- **분기/작업 흐름**: **`main` 브랜치**에서 **commit** 후 **push**한다.

---

## 1. 수행 절차

1. **로컬에서 작업 완료** (코드/파일이 과제 기준에 맞는지 확인)  
2. **저장소가 없으면** 원격에 `Arithmetic_XX` 이름으로 **repository 생성** (플랫폼은 과제/강의 지시에 따름).  
3. **remote 연결** (필요 시 `git init`, `git remote add origin <URL>`).  
4. **`main`으로 작업**  
   - 기본 분기가 `main`이 아니면: `main`을 만들어 체크아웃하거나, 기본 분기를 `main`으로 맞춤.  
5. **변경 스테이징** → **`main`에서 commit** (메시지는 과제 요구에 맞게)  
6. **원격에 push** (보통 `main` → `origin/main`).  
7. **Description 설정**: 저장소 **설명(description) 필드**에 **Author, Reviewer 이름**을 **명시** (쉼표·줄바꿈 등 형식은 과제 예시가 있으면 그에 맞춤).

---

## 2. 명명 규칙

| 구분 | 규칙 |
|------|------|
| **Repository 이름** | `Arithmetic_XX` — `XX`는 **지정된 번호** (예: `Arithmetic_17`). |
| **브랜치** | **작업·최종 반영**은 **`main`**. (별도 브랜치 정책이 없으면 `main`이 기준.) |
| **Description** | **Author 이름**, **Reviewer 이름** **모두** 포함. (과제에 “누가 작성·누가 검토”를 구분하라는 문구가 있으면 그 형식을 따를 것.) |

---

## 3. 필수 제출 요소

- **Push된 원격 Repository**: 이름이 **`Arithmetic_XX`**.  
- **커밋·푸시**: **`main` 브랜치**에 **commit**이 있고, **원격에 push** 완료.  
- **Description**: **Author**와 **Reviewer** 이름 **포함** (누락 시 감점/미제출로 볼 수 있음).  
- (과제/시스템이 요구하는 경우) **URL 제출** 또는 **제출용 스크린샷/링크** — 강의 안내만이 최종 기준.

---

## 4. 실수하기 쉬운 부분

- **`main`이 아닌 브랜치**에서만 commit하고 `main`은 비어 있거나, **`master`에만** 올리는 경우.  
- **Repository 이름**이 `Arithmetic_XX`가 아닌 **오타·다른 번호** (예: `Arithmatic`, `_01` vs `_17`).  
- **Description**에 **Author/Reviewer**를 **README**에만 적고, **웹에 보이는 저장소 description**에는 **안 넣는** 경우.  
- **처음 push**일 때: remote 미설정, `upstream` 없이 `git push`만 해서 **거절/오류**.  
- **권한/URL**: HTTPS vs SSH, **2FA**·**토큰** 미설정으로 **인증 실패**.  
- **.gitignore** 누락으로 **불필요한 대용량 파일**까지 commit하는 경우(과제에서 막는 경우).  

---

**한 줄로 요약**: `Arithmetic_XX` **저장소**를 **만들거나 연결**한 뒤, **`main`에서 commit → push**하고, **description에 Author와 Reviewer**를 **반드시** 적는다.

---

**User**

report  폴더를 만들어서 지금 작업한 내용을 보고서로 내보내줘

---

**Cursor**

`report` 폴더를 만들고 이전에 정리한 과제 요약을 보고서 문서로 저장합니다.



작업 반영했습니다.

## 생성한 것

- **폴더:** `c:\DEV\Arithmetic_17\report\`
- **보고서 파일:** `report\Arithmetic_Git_Push_과제_보고서.md`

포함한 내용은 다음과 같습니다.

1. 과제 개요(표)  
2. 수행 절차(7단계)  
3. 명명 규칙  
4. 필수 제출 요소  
5. 실수하기 쉬운 부분  
6. 자가 점검용 **체크리스트**

PDF나 Word로도 필요하면 원하는 형식을 알려주시면 됩니다.

