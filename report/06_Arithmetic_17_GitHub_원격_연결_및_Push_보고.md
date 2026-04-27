# Arithmetic_17 — GitHub 원격 연결 및 Push 작업 보고

**작성일:** 2026-04-27

---

## 1. 보고 목적·범위

| 항목 | 내용 |
|------|------|
| 목적 | GitHub에 생성한 원격 저장소와 로컬 프로젝트를 연결하고, **`main`** 브랜치로 **첫 push**까지 이르는 절차를 문서화한다. |
| 범위 | 원격 URL(`Arithmetic_17`), **Author / Reviewer(김원택)**, 커밋 메시지 **본문(description)**에 Author·Reviewer 포함, 실행 명령어 단계 전부 |

과제 일반 요구(브랜치·Description 필드 등)는 **`01_Arithmetic_Git_Push_과제_보고서.md`** 와 함께 참고한다.

---

## 2. 원격 저장소 정보

| 항목 | 값 |
|------|-----|
| Repository | [anruf0429/Arithmetic_17](https://github.com/anruf0429/Arithmetic_17) |
| Clone/Push URL (HTTPS) | `https://github.com/anruf0429/Arithmetic_17.git` |
| 작업 브랜치 | **`main`** |
| 커밋 Author (로컬 설정 예) | **김원택** (`git config user.name`) |
| Reviewer (과제·메시지에 명시) | **김원택** |
| 커밋 메시지 본문 | **Author**, **Reviewer** 줄을 **description(본문)**에 포함 |

> **참고:** GitHub 저장소 페이지의 **Description**(About) 필드에도 과제 요구 시 **Author·Reviewer**를 적는다. **README**만으로 대체 불가할 수 있으므로 **`01`** 의 체크리스트를 따른다.

---

## 3. 수행 명령 (단계별)

프로젝트 루트(예: `C:\DEV\Arithmetic_17`)에서 실행한다.

**1) 저장소 초기화, `main` 브랜치**

```text
git init -b main
```

이미 `git init`만 한 경우:

```text
git branch -M main
```

**2) 원격 추가**

```text
git remote add origin https://github.com/anruf0429/Arithmetic_17.git
```

이미 `origin`이 있으면:

```text
git remote set-url origin https://github.com/anruf0429/Arithmetic_17.git
```

**3) 이 저장소 범위 Author 설정 (필요 시)**

```text
git config user.name "김원택"
git config user.email "본인이_사용하는_이메일@example.com"
```

**4) 첫 커밋 — 본문에 Author / Reviewer 포함**

```text
git add .
git commit -m "Initial commit" -m "Author: 김원택" -m "Reviewer: 김원택"
```

여러 `-m`은 각각 커밋 메시지의 한 단락(제목·본문)이 된다. 제목 문안은 **`05_Arithmetic_17_첫_커밋_메시지_작성_보고.md`** 의 Conventional 예시로 바꿔도 된다.

**5) 원격으로 push**

```text
git push -u origin main
```

원격에 이미 커밋이 있어 거절되면, 저장소 정책과 충돌하지 않을 때만 예를 들어 아래를 검토한다.

```text
git pull origin main --rebase
git push -u origin main
```

---

## 4. 실행 전 확인 사항

| 항목 | 내용 |
|------|------|
| Git 설치 | 새 터미널에서 `git --version`으로 확인 |
| 인증 | HTTPS push 시 **토큰·자격 증명**, SSH 사용 시 **키 등록** |
| `.gitignore` | 불필요한 파일이 커밋에 들어가지 않았는지 `git status`로 확인 |

---

## 5. 관련 문서

| 파일 | 관계 |
|------|------|
| `01_Arithmetic_Git_Push_과제_보고서.md` | 과제 공통 요구(`main`, 원격 Description 등) |
| `05_Arithmetic_17_첫_커밋_메시지_작성_보고.md` | 첫 커밋 메시지 형식·예시 |
| `04_Arithmetic_17_현재_작업_종합_보고.md` | 프로젝트·테스트·Git 절차 종합 |

---

## 6. 정리

- 원격 저장소 **`https://github.com/anruf0429/Arithmetic_17.git`** 를 **`origin`** 으로 두고, **`main`** 에 커밋 후 **`git push -u origin main`** 으로 반영한다.
- 커밋 **Author**는 로컬 `user.name`·`user.email`로, **Reviewer** 및 **Author** 문자열은 커밋 메시지 **본문**에 명시하였다.
- GitHub 웹 UI의 **Repository Description**에는 과제 지시에 따라 **Author·Reviewer**를 별도로 기입한다.

---

*본 문서는 2026-04-27에 GitHub 저장소 생성·로컬 연결·push 조건을 정리한 작업 내역을 보고 목적으로 기록한다.*
