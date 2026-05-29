# MagicSquare_XX

4×4 Magic Square를 다루는 소프트웨어 프로젝트입니다.  
현재 단계는 **구현 이전의 문제 정의(Problem Definition)** 이며, QA·TDD 관점에서 **검증 가능한 규칙과 판정 기준**을 고정하는 것이 1차 목표입니다.

---

## 프로젝트가 풀려는 문제

### 표면 요구 (피해야 할 정의)

> 「4×4 마방진을 만드는 프로그램을 만든다.」

「만든다」·「완성」·「마방진」만으로는 생성/검증/입력 책임, 다중 정답, 성공 기준이 분명하지 않습니다.

### 진짜 문제 (현재 합의)

> **4×4 격자에 1~16이 각각 한 번씩 배치된 경우, 합의된 선(행·열·정의된 대각선)마다 합이 34인지를 결정론적으로 판정하고, 그 기준을 반복 실행·자동 검증·회귀에 사용할 수 있게 고정하는 것.**

| 구분 | 표면 | 진짜 |
|------|------|------|
| 대상 | 마방진 한 장 | 4×4 배치에 대한 **규칙 판정** |
| 성공 | 숫자가 채워짐 | 유·무효에 **일관된 판정** |
| 산출물 | 실행 파일 | **고정된 판정 기준 + 검증 가능한 요구** |

생성·UI·학습 게임 등은 **판정 문제** 위에 올리는 2차 범위로 둡니다.

---

## 왜 이 프로젝트인가

- **4×4**: 규칙이 명확하고(마법 상수 34), 규모가 작아 QA·TDD 연습에 적합합니다.
- **프로그램**: 같은 규칙을 **반복** 적용하고, **자동 검증**·**오류 방지**·**규칙 기반 사고**를 훈련하기 위함입니다.
- **TDD**: 판정 기준·불변식·입출력 계약을 구현보다 먼저 **통제**하기 위한 설계 방식 후보입니다.

---

## 핵심 Invariant (요약)

### 도메인

| ID | 내용 |
|----|------|
| D1 | 항상 **4×4** 격자 |
| D2 | 값은 **1~16 순열** (중복·누락 없음) |
| D3 | 검사 대상 각 선의 합 = **34** |
| D4 | 검사 **선 집합**은 요구에 명시·고정 |

D2가 깨지면 D3만으로 「유효」라고 하지 않습니다.

### 판정·품질

| ID | 내용 |
|----|------|
| P1 | 「만족」= D1~D4 **모두** 충족 |
| P2 | 동일 입력 → 동일 판정(및 실패 분류) |
| P3 | 순열·범위 위반은 합이 맞아도 **불만족** |
| Q1~Q3 | 기준 변경 시 검증 선행, 회귀 추적, I/O 계약 일치 |

---

## 훈련 목표 (사고 능력)

구현 기술보다 다음을 연습하는 프로젝트로 봅니다.

- **요구 분해** — 순열 / 선 합 / 검사 범위 / 입출력 경계
- **오라클 설계** — 유·무효 대표 예시, 다중 정답 이해
- **불변식 사고** — 부분 만족 vs 전역 유효
- **계약·경계** — 완성 격자만 vs 부분 입력, 실패 이유 명시
- **검증·회귀** — 반복 가능한 기대, 요구 변경 영향 예측
- **범위 통제** — 검증기 우선, 데모 완료 ≠ 규칙 증명

---

## 현재 상태

| 항목 | 상태 |
|------|------|
| 문제 정의 (STEP 1~5) | ✅ 완료 |
| TDD 설계 (Report 02) | ✅ 완료 |
| Must / Should / Won’t | ✅ Report 02 |
| 유·무효 대표 예시 표 | ✅ Report 02 |
| 입출력 계약 초안 | ✅ Report 02 |
| 구현 기반 (Report 03) | ✅ 완료 |
| `.cursorrules` · ECB 골격 · User entity | ✅ 완료 |
| Grid 검증기 (Report 02 Wave) | ❌ 미착수 |

---

## 저장소 구조

```
MagicSquare_XX/
├── README.md                 ← 이 파일 (프로젝트 개요)
├── .cursorrules              ← Cursor AI 규칙 (YAML)
├── pyproject.toml
├── src/magicsquare/          ← ECB (entity·control·boundary)
├── tests/
├── Report/                   ← 문제 정의·TDD 설계·구현 기반 보고서
│   ├── README.md
│   ├── 01. MagicSquare_Problem-Definition-Report.md
│   ├── 02. MagicSquare_TDD-Design-Report.md
│   ├── 03. MagicSquare_Implementation-Setup-Report.md
│   ├── 04. MagicSquare_Cursor-Rules-Modularization-Report.md
│   └── 06. MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md
├── docs/
│   └── test_plan.md
├── defect_list.md
└── Prompting/                ← 워크숍 프롬프트·대화 기록
    ├── 01. cursor_4x4_magic_square_problem_definit-Prompt.md
    ├── 02. cursor_4x4_magic_square_tdd_design-Prompt.md
    ├── 03. cursor_magicsquare_cursorrules_ecb_user-Prompt.md
    ├── 04. cursor_magicsquare_cursor-rules_modularization-Prompt.md
    └── 06. cursor_magicsquare_ac-fr01-01-red-test-Prompt.md
```

---

## 문서

| 문서 | 설명 |
|------|------|
| [Report/01. MagicSquare_Problem-Definition-Report.md](./Report/01.%20MagicSquare_Problem-Definition-Report.md) | STEP 1~5 통합 보고서 (관찰, Why #1~#3, 진짜 문제 정의, Invariant) |
| [Report/02. MagicSquare_TDD-Design-Report.md](./Report/02.%20MagicSquare_TDD-Design-Report.md) | TDD 설계 (범위, I/O, 오라클, Wave, 회귀) |
| [Report/03. MagicSquare_Implementation-Setup-Report.md](./Report/03.%20MagicSquare_Implementation-Setup-Report.md) | 구현 기반 (`.cursorrules`, ECB, User entity) |
| [Report/04. MagicSquare_Cursor-Rules-Modularization-Report.md](./Report/04.%20MagicSquare_Cursor-Rules-Modularization-Report.md) | `.cursor/rules/*.mdc` 규칙 모듈화 및 적용 보고 |
| [Report/06. MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md](./Report/06.%20MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md) | AC-FR-01-01 RED 테스트·결함·실행 결과 보고 |
| [docs/test_plan.md](./docs/test_plan.md) | AC-FR-01-01 상세 테스트 계획서 |
| [defect_list.md](./defect_list.md) | RED 단계 결함 목록 (DEF-001~004) |
| [Report/README.md](./Report/README.md) | Report 폴더 안내 |
| [Prompting/01. cursor_4x4_magic_square_problem_definit-Prompt.md](./Prompting/01.%20cursor_4x4_magic_square_problem_definit-Prompt.md) | 문제 정의 단계 프롬프트·대화 기록 |
| [Prompting/02. cursor_4x4_magic_square_tdd_design-Prompt.md](./Prompting/02.%20cursor_4x4_magic_square_tdd_design-Prompt.md) | TDD 설계 프롬프트·대화 기록 |
| [Prompting/03. cursor_magicsquare_cursorrules_ecb_user-Prompt.md](./Prompting/03.%20cursor_magicsquare_cursorrules_ecb_user-Prompt.md) | Cursor 규칙·ECB User 프롬프트·대화 기록 |
| [Prompting/04. cursor_magicsquare_cursor-rules_modularization-Prompt.md](./Prompting/04.%20cursor_magicsquare_cursor-rules_modularization-Prompt.md) | Cursor rules 분할 생성·작성 대화 기록 |
| [Prompting/06. cursor_magicsquare_ac-fr01-01-red-test-Prompt.md](./Prompting/06.%20cursor_magicsquare_ac-fr01-01-red-test-Prompt.md) | AC-FR-01-01 RED 테스트·결함 대화 기록 |

보고서에는 **구현 설계, 코드, 알고리즘**을 포함하지 않습니다.

---

## 문제 정의 단계 요약

```mermaid
flowchart LR
  S1[STEP 1 관찰] --> S2[STEP 2 Why 완성]
  S2 --> S3[STEP 3 Why 프로그램]
  S3 --> S4[STEP 4 Why TDD]
  S4 --> S5[STEP 5 진짜 문제]
```

1. **관찰** — 미정의 과제, QA·학습 맥락  
2. **Why #1** — 완성 = 증거(oracle), 정의·책임 모호성 분석  
3. **Why #2** — 반복 가능성, 검증 자동화, 오류 방지, 규칙 사고  
4. **Why #3** — TDD로 판정·불변식·I/O 통제  
5. **진짜 문제** — 규칙 판정 고정이 1차 목표  

---

## 다음 단계 (권장)

1. Report 02 **Wave 0**부터 `Grid` 검증기 TDD (entity → control → acceptance 테스트)  
2. **failureType** Should → Must 승격 여부 결정  
3. I-01 fixture로 SIZE Red → Green 진행  

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 test_plan.md 기반으로 생성되었습니다.
> 각 항목은 RED(실패 테스트 작성) 완료 시 체크합니다.

### Track A — UI / Boundary 테스트

- [ ] TC-A-01: grid=None 입력 → 실패 결과 반환 (Happy Path of Failure)
- [ ] TC-A-02: code가 정확히 "INVALID_SIZE" 문자열인지 검증
- [ ] TC-A-03: message가 "Grid must be 4x4." 와 문자 단위 동일한지 검증
- [ ] TC-A-04: grid=None 시 Domain 진입점 0회 호출 (mock/spy 검증)
- [ ] TC-A-05: grid=[] 빈 리스트 → 실패 결과 반환
- [ ] TC-A-06: grid=3×4 크기 불일치 → 실패 결과 반환
- [ ] TC-A-07: 반환 객체 타입이 지정 실패 결과 구조체인지 검증

### Track B — Domain / Logic 테스트

- [ ] TC-B-01: resolve()가 None grid를 직접 받지 않음을 격리 검증
- [ ] TC-B-02: Boundary가 None 분기를 처리 후 resolve() 미호출 확인
- [ ] TC-B-03: resolve() mock이 호출됐을 경우 테스트 실패 처리
- [ ] TC-B-04: AC-FR-01-02~05 범위의 케이스는 이 커밋에 포함하지 않음 확인

### 커버리지 목표

- [ ] Domain Logic: 95%+ (pip install pytest-cov)
- [ ] Boundary Layer: 85%+
- [ ] 전체 TOTAL: 90%+

### 결함 목록 연결

- [x] [defect_list.md](./defect_list.md) 생성 및 발견 결함 기록
- [ ] 모든 결함 수정 후 회귀 테스트 통과 확인

---

## 대상 독자

- QA · 요구·테스트 설계 담당  
- TDD로 도메인 규칙을 먼저 고정하려는 개발자  
- 4×4 마방진을 **작은 규칙 엔진** 연습 문제로 쓰는 학습자  

---

## 변경 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-28 | 프로젝트 README 초안 (STEP 1~5 기반) |
