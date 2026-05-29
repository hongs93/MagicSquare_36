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
| AC-FR-01-01 RED (Report 06, ECB 30건) | ✅ 완료 |
| AC-FR-01-01 GREEN (Wave 0, ECB) | ✅ 완료 (C0~C6, 30 passed) |
| Dual-Track RED Skeleton (Report 09, 23건) | ✅ 완료 |
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
| [Report/07. MagicSquare_DualTrack-FR01-FR05-RED-Design-Report.md](./Report/07.%20MagicSquare_DualTrack-FR01-FR05-RED-Design-Report.md) | Dual-Track FR-01~05 RED 설계표 |
| [Report/09.MagicSquare_DualTrack_RED_TestPlan_Design_Report.md](./Report/09.MagicSquare_DualTrack_RED_TestPlan_Design_Report.md) | Dual-Track RED Skeleton 테스트·실행 보고 |
| [Report/10. MagicSquare_AC-FR01-01-GREEN-Wave0-Kickoff-Report.md](./Report/10.%20MagicSquare_AC-FR01-01-GREEN-Wave0-Kickoff-Report.md) | AC-FR-01-01 GREEN Wave 0 착수·C0~C6·최소 구현 보고 |
| [docs/test_plan.md](./docs/test_plan.md) | AC-FR-01-01 상세 테스트 계획서 |
| [docs/architecture_stacks.md](./docs/architecture_stacks.md) | ECB vs Dual-Track 이중 스택·호출 경로·마이그레이션 |
| [docs/error_contracts.md](./docs/error_contracts.md) | ECB vs Dual-Track 오류 코드·메시지 SSOT (C-03) |
| [defect_list.md](./defect_list.md) | RED 단계 결함 목록 (DEF-001~004) |
| [Report/README.md](./Report/README.md) | Report 폴더 안내 |
| [Prompting/01. cursor_4x4_magic_square_problem_definit-Prompt.md](./Prompting/01.%20cursor_4x4_magic_square_problem_definit-Prompt.md) | 문제 정의 단계 프롬프트·대화 기록 |
| [Prompting/02. cursor_4x4_magic_square_tdd_design-Prompt.md](./Prompting/02.%20cursor_4x4_magic_square_tdd_design-Prompt.md) | TDD 설계 프롬프트·대화 기록 |
| [Prompting/03. cursor_magicsquare_cursorrules_ecb_user-Prompt.md](./Prompting/03.%20cursor_magicsquare_cursorrules_ecb_user-Prompt.md) | Cursor 규칙·ECB User 프롬프트·대화 기록 |
| [Prompting/04. cursor_magicsquare_cursor-rules_modularization-Prompt.md](./Prompting/04.%20cursor_magicsquare_cursor-rules_modularization-Prompt.md) | Cursor rules 분할 생성·작성 대화 기록 |
| [Prompting/06. cursor_magicsquare_ac-fr01-01-red-test-Prompt.md](./Prompting/06.%20cursor_magicsquare_ac-fr01-01-red-test-Prompt.md) | AC-FR-01-01 RED 테스트·결함 대화 기록 |
| [Prompting/09. cursor_magicsquare_ac-fr01-01-green-wave0-Prompt.md](./Prompting/09.%20cursor_magicsquare_ac-fr01-01-green-wave0-Prompt.md) | AC-FR-01-01 GREEN Wave 0 대화 기록 |

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

1. **GREEN Wave 0** — 아래 [ECB GREEN 커밋 묶음](#ecb-green-커밋-묶음-wave-0) C1~C6 순서로 최소 구현·커밋  
2. **Dual-Track Wave D1~** — ECB 30건 회귀 유지 후 `src/boundary/` 진행  
3. Report 02 **failureType** Should → Must 승격 여부 결정  

---

## RED 단계 To-Do 리스트

> 이 체크리스트는 [docs/test_plan.md](./docs/test_plan.md) · [Report/06](./Report/06.%20MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md) 기반입니다.  
> ECB Full RED 30건은 `tests/unit/boundary/` + `tests/unit/control/`에 **작성 완료** — assert 수정·삭제 금지.

### Golden Master 회귀 안전장치

> Refactoring 시작 전 구축. GREEN 완료 후 즉시 적용.

**기준 파일 생성**

- GM-01: `tests/golden_master_expected.txt` 생성
- GM-02: 정상/역순/오류 시나리오 추가
- GM-03: `git add tests/golden_master_expected.txt`

**테스트 코드**

- GM-04: `test_golden_master_magic_square` 작성
- GM-05: approve 패턴 적용
- GM-06: Golden Master 테스트 PASS 확인

**회귀 보호**

- GM-07: row-major 규칙 보호
- GM-08: 1-index 출력 보호
- GM-09: reverse 조합 fallback 보호
- GM-10: Error Contract 보호

### Track A — ECB Boundary / Control (Report/06, 30건)

- [x] TC-A-01~07: `test_boundary_validator_size.py` (25건) — `grid=None` / `[]` / `[[]]*4` / 3×4 등
- [x] TC-A-04: `test_solver_size_validation_gate.py` (5건) — `resolve()` 0회 mock/spy
- [x] 오라클 상수: `tests/constants.py` (`INVALID_SIZE`, `Grid must be 4x4.`)

### Track B — Dual-Track Skeleton (Report/09, 23건)

- [x] `tests/dualtrack/boundary/test_u_in.py` · `test_u_out.py` · `test_u_flow.py` (11건, `pytest.fail` 스켈레ton)
- [x] `tests/dualtrack/entity/test_d_*.py` (12건, 스켈레ton)

### 커버리지 목표 (GREEN 이후 측정)

- [ ] Domain Logic: 95%+ (`pytest-cov`) — 현재 `magic_square_validator` 76% (Wave D6 선행)
- [x] Boundary Layer: 85%+ — ECB boundary+control 85~100%, Dual-Track boundary 85%+
- [x] 전체 TOTAL: 90%+ — **93%** (2026-05-29, `tests/unit/` + GM 회귀 기준)

### 결함 목록 연결

- [x] [defect_list.md](./defect_list.md) 생성 및 발견 결함 기록 (DEF-001~004)
- [x] DEF-001~003 Close 및 회귀 30 passed (DEF-004 커버리지 재측정)

---

## GREEN 단계 To-Do 리스트

> **SSOT:** [Report/06](./Report/06.%20MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md) (ECB 30건), [Report/09](./Report/09.MagicSquare_DualTrack_RED_TestPlan_Design_Report.md) (Dual-Track)  
> **원칙:** RED 확인 → **GREEN 최소 구현만** → REFACTOR 분리. Report/06 assert **수정·삭제 금지**.  
> **오라클:** `tests/constants.py` — `EXPECTED_INVALID_SIZE_CODE` / `EXPECTED_INVALID_SIZE_MESSAGE`  
> **권장 순서:** 입력 복잡도 `None` → `[]` → `[[]]*4` → `3×4` → Control 격리 (C6). Dual-Track은 ECB 30건 후.

### ECB GREEN 커밋 묶음 (Wave 0)

RED 30건을 **6개 커밋**으로 나눠 GREEN합니다. 각 커밋은 해당 `-k` 필터만 통과시킨 뒤, C5·C6에서 Boundary/Control 전체 회귀를 확인합니다.

| 커밋 | BV | 구현 요약 | 테스트 수 | pytest 필터 | 상태 |
|------|-----|-----------|-----------|-------------|------|
| **C0** | — | `FailureResult` (`responses.py`) | 수집만 | `--collect-only` | [x] |
| **C1** | BV-01 | `grid is None` → `INVALID_SIZE` | 13 | `-k none_grid` | [x] |
| **C2** | BV-02 | `grid=[]` (행 0) | 3 | `-k empty_list` | [x] |
| **C3** | BV-03 | `grid=[[]]*4` (4×0) | 2 | `-k four_empty_rows` | [x] |
| **C4** | BV-04 | `grid_3x4` (행≠4 또는 열≠4) | 6 | `-k 3x4` | [x] |
| **C5** | 통합 | None·[]·4×0·3×4 fixture 루프 | 1 | 아래 단일 테스트 | [x] |
| **C6** | 격리 | `Solver.handle` + `resolve()` mock 0회 | 5 | `tests/unit/control/` | [x] |

**구현 경로:** `src/magicsquare/boundary/responses.py`, `validator.py`, `src/magicsquare/control/solver.py`  
**미포함 (현재 RED 30건에 없음):** 4×3, 5×5, jagged — RED 추가 시 C4 다음 Wave.

#### C0 — 수집 가능 (인프라)

- [x] `magicsquare.boundary.responses.FailureResult` (`code`, `message`, `is_failure`)
- [x] `magicsquare.boundary.validator.BoundaryValidator` 스켈레ton

```powershell
python -m pytest tests/unit/boundary/test_boundary_validator_size.py --collect-only -q
```

**커밋 메시지 예:** `green(ac-fr-01-01): add FailureResult for pytest collection`

#### C1 — BV-01 `grid=None` (13건)

| # | 클래스::테스트 |
|---|----------------|
| 1 | `TestNormalFailureReturn::test_none_grid_returns_failure_invalid_size_code` |
| 2 | `::test_none_grid_returns_failure_invalid_size_message` |
| 3 | `::test_none_grid_returns_result_without_exception` |
| 4 | `::test_none_grid_failure_has_code_attribute` |
| 5 | `::test_none_grid_failure_has_message_attribute` |
| 6 | `TestMessageIdentity::test_none_grid_message_matches_prd_exactly_char_by_char` |
| 7 | `::test_invalid_size_message_character_count` |
| 8 | `::test_invalid_size_message_starts_with_grid` |
| 9 | `::test_invalid_size_message_ends_with_period` |
| 10 | `::test_invalid_size_message_no_extra_whitespace` |
| 11 | `TestFailureResponseType::test_none_grid_returns_failure_result_type` |
| 12 | `::test_failure_result_matches_pydantic_schema` |
| 13 | `TestAcFr0101ScopeRestriction::test_none_grid_failure_code_not_in_out_of_scope_set` |

```powershell
python -m pytest tests/unit/boundary/test_boundary_validator_size.py -k "none_grid" -v
```

**커밋 메시지 예:** `green(ac-fr-01-01): INVALID_SIZE for grid=None`

#### C2 — BV-02 `grid=[]` (3건)

| # | 클래스::테스트 |
|---|----------------|
| 14 | `TestBoundaryValues::test_empty_list_returns_invalid_size_failure` |
| 15 | `::test_empty_list_failure_code_is_invalid_size` |
| 16 | `TestFailureResponseType::test_empty_list_returns_failure_result_type` |

```powershell
python -m pytest tests/unit/boundary/test_boundary_validator_size.py -k "empty_list" -v
```

**커밋 메시지 예:** `green(ac-fr-01-01): INVALID_SIZE for empty grid`

#### C3 — BV-03 `grid=[[]]*4` (2건)

| # | 클래스::테스트 |
|---|----------------|
| 17 | `TestBoundaryValues::test_four_empty_rows_returns_invalid_size_failure` |
| 18 | `TestFailureResponseType::test_four_empty_rows_returns_failure_result_type` |

```powershell
python -m pytest tests/unit/boundary/test_boundary_validator_size.py -k "four_empty_rows" -v
```

**커밋 메시지 예:** `green(ac-fr-01-01): INVALID_SIZE for four empty rows`

#### C4 — BV-04 `grid_3x4` (6건)

| # | 클래스::테스트 |
|---|----------------|
| 19 | `TestBoundaryValues::test_3x4_matrix_returns_invalid_size_failure` |
| 20 | `::test_3x4_matrix_failure_message_is_exact` |
| 21 | `TestFailureResponseType::test_3x4_matrix_returns_failure_result_type` |
| 22 | `TestAcFr0101ScopeRestriction::test_3x4_failure_code_is_not_invalid_blank_count` |
| 23 | `::test_3x4_failure_code_is_not_invalid_range` |
| 24 | `::test_3x4_failure_code_is_not_duplicate_nonzero` |

```powershell
python -m pytest tests/unit/boundary/test_boundary_validator_size.py -k "3x4" -v
```

**커밋 메시지 예:** `green(ac-fr-01-01): INVALID_SIZE for non-4x4 dimensions`

#### C5 — BV 통합 루프 (1건)

| # | 클래스::테스트 |
|---|----------------|
| 25 | `TestAcFr0101ScopeRestriction::test_size_only_fixtures_never_use_valid_4x4_contract` |

```powershell
python -m pytest tests/unit/boundary/test_boundary_validator_size.py::TestAcFr0101ScopeRestriction::test_size_only_fixtures_never_use_valid_4x4_contract -v
python -m pytest tests/unit/boundary/test_boundary_validator_size.py -v
```

**커밋 메시지 예:** `green(ac-fr-01-01): boundary size-invalid fixture loop`

#### C6 — AC-FR-01-05 Control 격리 (5건)

| # | 테스트 (`test_solver_size_validation_gate.py`) |
|---|------------------------------------------------|
| 26 | `test_none_grid_resolve_called_zero_times` |
| 27 | `test_none_grid_handle_returns_failure_without_resolve` |
| 28 | `test_empty_list_resolve_called_zero_times` |
| 29 | `test_four_empty_rows_resolve_called_zero_times` |
| 30 | `test_3x4_matrix_resolve_called_zero_times` |

```powershell
python -m pytest tests/unit/control/test_solver_size_validation_gate.py -v
python -m pytest tests/unit/boundary/ tests/unit/control/ -v
```

**커밋 메시지 예:** `green(ac-fr-01-05): Solver skips resolve on size-invalid grid`

#### ECB 30건 전체 오름차순 (참조)

```text
[BoundaryValidator — tests/unit/boundary/test_boundary_validator_size.py]
  1–13   None          (C1)
 14–16   []            (C2)
 17–18   [[]]*4        (C3)
 19–24   3×4           (C4)
 25      4종 fixture   (C5)

[Solver + mock — tests/unit/control/test_solver_size_validation_gate.py]
 26–27   None          (C6)
 28      []
 29      [[]]*4
 30      3×4
```

### 선행 게이트 체크리스트 — ECB Track

- [x] **C0** `FailureResult` — pytest 수집 가능
- [x] **C1** `grid=None` (13건)
- [x] **C2** `grid=[]` (+3건)
- [x] **C3** `grid=[[]]*4` (+2건)
- [x] **C4** `grid_3x4` (+6건)
- [x] **C5** fixture 루프 (+1건)
- [x] **C6** Control 격리 (5건)
- [x] **회귀** `tests/unit/boundary/` + `tests/unit/control/` → **30 passed**

```powershell
# ECB 전체 회귀 (선행 게이트 완료 시)
python -m pytest tests/unit/boundary/ tests/unit/control/ -v
```

### Import / pytest 주의 (Dual-Track)

Dual-Track 테스트는 `tests/dualtrack/boundary/` · `tests/dualtrack/entity/`에 두며 **`__init__.py` 없음** — `src/boundary` import shadowing 방지 (REFACTOR A-05).

| 구분 | 테스트 경로 | 구현 경로 | import 예 |
|------|-------------|-----------|-----------|
| ECB | `tests/unit/boundary/` | `src/magicsquare/boundary/` | `magicsquare.boundary.*` |
| Dual-Track | `tests/dualtrack/boundary/` | `src/boundary/` | `boundary.input_validator` |

- [x] `pyproject.toml` `pythonpath = ["src", "."]` 확인
- [x] Dual-Track pytest는 **ECB와 분리** 실행 (`tests/dualtrack/boundary/` vs `tests/unit/boundary/`)
- [ ] collection 시 `ModuleNotFoundError: boundary.*` → 해당 Wave 구현 스켈레ton 추가
- [x] `tests/dualtrack/boundary/` 디렉터리가 `boundary` **패키지로 shadowing**되지 않는지 import smoke 확인

```powershell
# Dual-Track import smoke
python -c "from boundary.input_validator import InputValidator; print(InputValidator)"

# Dual-Track 테스트만 (ECB와 분리)
python -m pytest tests/dualtrack/boundary/ -v
```

---

### Wave D1 — U-IN-01 계열 (`InputValidator` null / size)

**구현:** `src/boundary/input_validator.py`, `src/boundary/schemas.py`  
**GREEN 시점:** `grid is None` → `FailureResponse(type="ERROR", code="INVALID_SIZE", message="Grid must be 4x4.")`

> `tests/dualtrack/boundary/test_ac_fr_01_01_*.py`가 없으면 **RED(assert Full) 먼저** 작성 후 GREEN.

- [ ] **D1-RED** `tests/dualtrack/boundary/test_ac_fr_01_01_input_validation.py` + `ac_fr_01_01_constants.py` (없을 경우)
- [ ] **D1-GREEN** `InputValidator.validate(None)` — INVALID_SIZE 분기
- [ ] **D1-GREEN** `FailureResponse` 스키마 (`type`, `code`, `message`)
- [ ] **D1-VERIFY** `TestNormalFailureReturn::test_none_grid_returns_failure_with_invalid_size_code` passed
- [ ] **D1-COMMIT** `green(dual-track): InputValidator null → INVALID_SIZE`

---

### Wave D2 — U-IN-02 (`InputValidator` size 분기)

**구현:** `InputValidator.validate()` — `[]`, `[[]]*4`, 3×4, 4×3, 5×5 등 size 위반  
**테스트:** ECB와 동일 시나리오는 `tests/unit/boundary/`(Report/06); Dual-Track 전용 assert는 RED 추가 후 GREEN

- [ ] **D2-GREEN** `grid=[]` → INVALID_SIZE
- [ ] **D2-GREEN** `grid=[[]]*4` (4×0) → INVALID_SIZE
- [ ] **D2-GREEN** 3×4 행렬 → INVALID_SIZE
- [ ] **D2-GREEN** (선택) 4×3, 5×5 — RED 추가 시에만
- [ ] **D2-VERIFY** ECB C2~C5 회귀 + Dual-Track size assert (있을 경우)
- [ ] **D2-COMMIT** `green(dual-track): InputValidator size validation`

> U-IN-02a~d는 Report/09 기준 Report/06 ECB RED에 포함. Dual-Track `test_u_in.py`에는 **U-IN-04~08만** 존재.

---

### Wave D3 — U-IN-03~08 (`test_u_in.py`, AC-FR-01-02~04)

**구현:** 빈칸 개수 → E002, 값 범위 → E004, non-zero 중복 → E005 (Report/07 워크숍 계약)  
**전제:** 스켈레ton `pytest.fail` → assert로 **교체**(RED Full) 후 GREEN

- [ ] **D3-RED** `test_u_in_03` (빈칸 0개, G0) — assert 추가 (현재 스켈레ton 미포함)
- [ ] **D3-RED→GREEN** `test_u_in_04_blank_count_three_returns_e002`
- [ ] **D3-RED→GREEN** `test_u_in_05_negative_value_returns_e004`
- [ ] **D3-RED→GREEN** `test_u_in_06_value_seventeen_returns_e004`
- [ ] **D3-RED→GREEN** `test_u_in_07_nonzero_duplicate_returns_e005`
- [ ] **D3-RED→GREEN** `test_u_in_08_blank_count_one_returns_e002`
- [ ] **D3-VERIFY** `python -m pytest tests/dualtrack/boundary/test_u_in.py -v` → 전부 passed
- [ ] **D3-COMMIT** `green(dual-track): InputValidator blank/range/duplicate`

---

### Wave D4 — U-FLOW-02 (`test_u_flow.py`, execute 격리)

**구현:** `src/boundary/ui_boundary.py` — invalid 입력 시 `execute` **0회**  
**AC:** AC-FR-01-05 (Domain resolver 미호출)

- [ ] **D4-RED→GREEN** `test_u_flow_02_null_matrix_execute_not_called`
- [ ] **D4-RED→GREEN** `test_u_flow_02_invalid_size_execute_not_called`
- [ ] **D4-RED→GREEN** `test_u_flow_02_blank_count_invalid_execute_not_called`
- [ ] **D4-VERIFY** `python -m pytest tests/dualtrack/boundary/test_u_flow.py -v` → 3 passed
- [ ] **D4-COMMIT** `green(dual-track): UIBoundary invalid → execute×0`

---

### Wave D5 — U-OUT (`test_u_out.py`, FR-05 출력 계약)

**구현:** `UIBoundary.solve()` — 성공 payload `int[6]`, 1-index 좌표  
**전제:** Control/Entity mock 또는 stub (U-OUT은 execute 결과 포맷 검증)

- [ ] **D5-RED→GREEN** `test_u_out_01_success_payload_length_six`
- [ ] **D5-RED→GREEN** `test_u_out_02_one_indexed_coordinates`
- [ ] **D5-RED→GREEN** `test_u_out_03_exact_success_tuple_g1` → `[2,2,7,3,3,10]`
- [ ] **D5-VERIFY** `python -m pytest tests/dualtrack/boundary/test_u_out.py -v` → 3 passed
- [ ] **D5-COMMIT** `green(dual-track): UIBoundary success payload contract`

---

### Wave D6 — Track B Logic (`tests/dualtrack/entity/`, 별도 Wave)

Report/09 RED Skeleton 15건. ECB·Dual-Track Track A GREEN 후 진행 권장.

- [ ] **D6** D-LOC-01 `find_blank_coords` (G1)
- [ ] **D6** D-MIS-01 `find_not_exist_nums` (G1)
- [ ] **D6** D-VAL-01~06 `is_magic_square` (G0, I-04~I-08)
- [ ] **D6** D-SOL-01~04 `solution` (G1~G3; G2/G3 fixture TBD)
- [ ] **D6-VERIFY** `python -m pytest tests/dualtrack/entity/ -v`

---

### Dual-Track Track A 전체 완료 체크

- [ ] `python -m pytest tests/dualtrack/boundary/ -v` → 11 passed (U-IN-04~08 + U-OUT + U-FLOW)
- [ ] ECB 30건 회귀 유지 (`tests/unit/boundary/` + `tests/unit/control/`)
- [ ] [defect_list.md](./defect_list.md) DEF-001~003 Close 및 커버리지 재측정 (DEF-004)

---

## REFACTOR 단계 To-Do 리스트

> **SSOT:** [Report/12](./Report/12.%20MagicSquare_AC-FR01-01-GREEN-Wave0-Complete-Report.md) (Wave 0 완료), [Report/13](./Report/13.%20MagicSquare_Golden-Master-GM2-Complete-Report.md) (GM-2 회귀 게이트)  
> **원칙:** GREEN Wave 0 완료 후 **동작 보존** 리팩터링만. Report/06 assert **수정·삭제 금지**.  
> **회귀 게이트:** ECB 30건 + Golden Master 5 TC green 유지 후 각 항목 체크.

```powershell
python -m pytest tests/unit/boundary/ tests/unit/control/ -v
python -m pytest tests/unit/test_golden_master_magic_square.py -m golden_master -v
```

**권장 Wave 순서:** R-01 → I-01 → C-01~C-04 → T-01~T-03 → R-02~R-03 → Q-01 (Dual-Track D1 전후 타입·상수 통합 결정)

### 1. 구조·아키텍처 (Architecture)

- [x] **A-01** Dual-Track / ECB 이중 Boundary — `src/magicsquare/boundary/` vs `src/boundary/` 병행 → 단일 스택 통합 또는 마이그레이션 경로 문서화
- [x] **A-02** Control 레이어 이중화 — `magicsquare.control.Solver` vs `control.SolvePartialMagicSquare` 역할·호출 경로 정리
- [x] **A-03** Entity 패키지 이중화 — `src/magicsquare/entity/` vs `src/entity/` → SSOT re-export 또는 흡수
- [x] **A-04** `NotImplementedError` 제어 흐름 — `BoundaryValidator` → `Solver.handle` 예외 분기 → FR-02+ 시 명시적 결과 타입 검토
- [x] **A-05** `tests/dualtrack/boundary/` import shadowing — 테스트 패키지와 `src/boundary/` 이름 충돌 해소
- [x] **A-06** `User` entity 고립 — `magicsquare.entity.user` 사용 경로 연결 또는 범위 밖 문서화

### 2. 문서·규칙 (Documentation / Config)

- [x] **D-01** `.cursorrules` vs `.mdc` 중복 — Report/04 중복 조항 제거, SSOT를 `.cursor/rules/*.mdc`로 고정
- [x] **D-02** README 커버리지 체크리스트 — Domain 95%+, TOTAL 90% 측정 결과 반영
- [x] **D-03** `pyproject.toml` 의존성 — ECB failure envelope pydantic 통일 시 runtime `dependencies` 승격 검토

### 3. 상수·SSOT (Constants)

- [x] **C-01** `GRID_SIZE` 이중 정의 — `magicsquare/entity/constants.py` · `entity/constants.py` → 단일 SSOT 참조
- [x] **C-02** INVALID_SIZE 오라클 3중 정의 — `responses.py` · `tests/constants.py` · `schemas.py` → 단일 출처, 테스트는 import만
- [x] **C-03** ECB vs Dual-Track 오라클 불일치 — `"INVALID_SIZE"` vs `"E001_INVALID_SIZE"`, 메시지 문구 → PRD §8.1 기준 SSOT 확정
- [x] **C-04** `magicsquare/entity/constants` 불완전 — ECB도 `entity/constants.py` 참조로 통일

### 4. 코드 중복 (Duplication)

- [ ] **R-01** `_invalid_size_failure()` 미추출 — `validator.py` 동일 `FailureResult` 생성 2회 → private 헬퍼 추출
- [ ] **R-02** 4×4 차원 검증 로직 중복 — `BoundaryValidator` ↔ `InputValidator` → 공통 `is_valid_grid_size()` 추출
- [ ] **R-03** size-invalid early return 패턴 — ECB `FailureResult` vs Dual-Track `FailureResponse` → 공통 size 검사 후 envelope 매핑
- [ ] **R-04** `BoundaryValidator()` 반복 생성 — 테스트·`Solver`에서 매번 `new` → DI 또는 fixture 공유

### 5. 타입·계약 (Type / Contract)

- [ ] **T-01** `FailureResult` vs `FailureResponse` — ECB `@dataclass` vs Dual-Track pydantic → 단일 failure envelope 통합
- [ ] **T-02** null 입력 계약 분기 — ECB `None` → `INVALID_SIZE` vs Dual-Track `None` → `E003_NULL_INPUT` → PRD 기준 통일 또는 문서화
- [ ] **T-03** pydantic 스키마 이중 정의 — 테스트 `FailureResponseSchema` vs 프로덕션 `FailureResponse` → 프로덕션 타입으로 대체
- [ ] **T-04** `Solver.handle` 반환 타입 — `FailureResult`만 선언 → FR-05 성공 경로 시 union 타입
- [ ] **T-05** `FailureResult.is_failure` — Dual-Track `FailureResponse`와 필드·의미 동기화

### 6. 테스트·품질 (Test / Quality)

- [ ] **Q-01** DEF-004 TOTAL 커버리지 — boundary+control 88%, TOTAL 90% 미달 → Wave D 이후 재측정
- [ ] **Q-02** Golden Master vs 전체 pytest — `-m golden_master` 단독 시 Dual-Track skeleton import 오류 → GM 전용 수집 범위 분리
- [ ] **Q-03** Dual-Track RED skeleton — `tests/dualtrack/boundary/` · `tests/dualtrack/entity/` `pytest.fail` → GREEN 시 assert 교체, REFACTOR 전 GM-2 회귀 유지
- [ ] **Q-04** ECB 30건 assert 불변 — REFACTOR는 구현만 변경, 테스트 약화 없이 green 유지

### 7. 의존성 주입 (Dependency Injection)

- [ ] **I-01** `Solver` validator 하드코딩 — `Solver(validator: BoundaryValidator | None = None)` 생성자 DI
- [ ] **I-02** `Solver.resolve` mock/spy — DI 후 `resolve` stub 주입으로 C6 격리 테스트 단순화
- [ ] **I-03** `UIBoundary` DI 대칭 — ECB `Solver`에 `UIBoundary`와 동일 injectable 패턴 적용

### 8. 명명·가독성 (Naming / Readability)

- [ ] **N-01** `NotImplementedError` 메시지 — `"size validation not implemented"` → FR-02+ 미구현 의미로 정확화
- [ ] **N-02** `validate()` vs `handle()` — 레이어별 docstring에 Boundary/Control 책임 경계 명시
- [ ] **N-03** Dual-Track 오류 코드 prefix — `E001_` … vs ECB plain `INVALID_SIZE` → naming convention 또는 `StrEnum` 도입

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
| 1.1 | 2026-05-29 | RED 완료·GREEN Wave 0 커밋 묶음(C0~C6) 상세, Dual-Track Wave D1~D6 정리 |
| 1.2 | 2026-05-29 | GREEN Wave 0 완료 — C1~C6·ECB 30 passed·DEF-001~003 Close |
| 1.3 | 2026-05-29 | REFACTOR 단계 To-Do 8그룹(A~N) 체크리스트 추가 |
| 1.4 | 2026-05-29 | REFACTOR 1번 그룹(A-01~A-06) — architecture doc, validate_size, dualtrack tests |
| 1.5 | 2026-05-29 | REFACTOR 2번 그룹(D-01~D-03) — rules SSOT, pydantic runtime, coverage |
