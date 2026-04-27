# GitHub repository connection and push commands
_Exported on 4/27/2026 at 15:12:15 GMT+9 from Cursor (3.0.16)_

---

**User**

GitHub에 https://github.com/anruf0429/Arithmetic_17.git  이라는 Repository를 생성했습니다.

로컬 프로젝트를 다음 조건으로 연결하고 push하는 명령어를 알려주세요.

* main 브랜치 사용
* Author: 김원택
* Reviewer: 김원택
* description에 Author/Reviewer 포함

명령어만 단계별로 작성해 주세요.

---

**Cursor**

아래는 **명령어만** 단계별로 정리한 예시입니다. 터미널에서 프로젝트 루트(예: `c:\DEV\Arithmetic_17`)로 이동한 뒤 순서대로 실행하면 됩니다.

---

**1. 저장소 초기화, `main` 브랜치**

```bash
git init -b main
```

(이미 `git init`만 했다면)

```bash
git branch -M main
```

---

**2. 원격 추가**

```bash
git remote add origin https://github.com/anruf0429/Arithmetic_17.git
```

(이미 `origin`이 있으면)

```bash
git remote set-url origin https://github.com/anruf0429/Arithmetic_17.git
```

---

**3. Author(커밋 작성자) — 이 저장소에만 적용**

```bash
git config user.name "김원택"
git config user.email "본인이_쓰는_이메일@example.com"
```

---

**4. 첫 커밋 — 본문(description)에 Author / Reviewer 포함**

```bash
git add .
git commit -m "Initial commit" -m "Author: 김원택" -m "Reviewer: 김원택"
```

(한 번에 여러 `-m`이면 각각이 커밋 메시지의 한 단락이 됩니다.)

---

**5. GitHub로 push**

```bash
git push -u origin main
```

---

**참고:** 원격에 이미 커밋이 있어 거절되면, 과제 요구와 충돌하지 않을 때만 아래를 검토하세요.

```bash
git pull origin main --rebase
git push -u origin main
```

---

**User**

report  폴더에 지금 작업한 내용을 보고서로 내보내줘

---

**Cursor**

기존 보고서 형식과 프로젝트 상태를 확인한 뒤 보고서를 작성합니다.



대화에서 다룬 GitHub 저장소 연결·push 절차를 기존 보고서 형식에 맞춰 `report`에 새 보고서로 추가합니다.



`report` 폴더에 아래 파일을 추가했습니다.

**파일:** `report/06_Arithmetic_17_GitHub_원격_연결_및_Push_보고.md`

**포함 내용 요약**

| 섹션 | 내용 |
|------|------|
| 목적·범위 | GitHub `Arithmetic_17` 연결·`main` push 절차 문서화 |
| 원격 정보 | `https://github.com/anruf0429/Arithmetic_17.git`, Author/Reviewer **김원택**, 커밋 본문에 Author·Reviewer 포함 |
| 명령 단계 | `git init -b main` → `remote` → `user.name`/`email` → `commit`(`-m` 여러 줄) → `push -u origin main`, 필요 시 `pull --rebase` |
| 참고 | 저장소 **About Description**은 `01` 보고서·체크리스트와 함께 처리 |
| 관련 문서 | `01`, `04`, `05` 링크 |

종합 목록(`04`)에는 아직 반영하지 않았습니다. `04` 표에 `06` 한 줄을 넣어 두길 원하면 알려 주세요.

