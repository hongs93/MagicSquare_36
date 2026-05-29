# MagicSquare_XX — 테스트 계획서 (AC-FR01-01)

| 항목 | 내용 |
|------|------|
| 문서 ID | TP-AC-FR01-01 |
| 버전 | 1.0 |
| 작성일 | 2026-05-29 |
| 작성 역할 | 시니어 QA 리드 |
| 대상 AC | **AC-FR01-01** (부가: **AC-FR01-05**) |
| 대상 FR | **FR-01** Input Verification (PRD §10) |
| 관련 BR | **BR-01** — 입력은 4행 4열 정수 행렬이어야 한다 (PRD §11) |
| 관련 Test Case | **TS-E-01** (PRD §16.2) |
| 대상 컴포넌트 | `BoundaryValidator` (Boundary 계층) |
| 기술 스택 | Python 3.11+, pytest, pydantic, unittest.mock |
| 참조 문서 | `docs/PRD_MagicSquare.md`, `Report/02. MagicSquare_TDD-Design-Report.md` |

---

## 1. 문서 목적

본 계획서는 FR-01 Acceptance Criteria 중 **AC-FR01-01(크기 4×4 검증)** 을 중심으로, pytest 기반 단위 테스트의 **범위·우선순위·경계값·격리 전략·커버리지 측정 방법**을 정의한다.

AC-FR01-01은 FR-01 검증 파이프라인의 **최선행 게이트**(Report 02 Wave 0, D1)이며, 실패 시 **AC-FR01-05**(Domain resolver 미호출)와 함께 검증한다.

---

## 2. 테스트 목표

| ID | 목표 | 검증 AC |
|----|------|---------|
| OBJ-01 | 4×4가 아닌 입력에 대해 `E001_INVALID_SIZE` 실패 응답을 반환한다 | AC-FR01-01 |
| OBJ-02 | 실패 응답은 `{ errorCode, message }` pydantic 계약을 만족한다 | AC-FR01-01, PRD §13 |
| OBJ-03 | 크기 검증 실패 시 Domain resolver 진입점이 **0회** 호출된다 | AC-FR01-05 |
| OBJ-04 | 예외를 던지지 않고(result object 반환) 결정성을 유지한다 | PRD §13, NFR-03 |
| OBJ-05 | 입력 행렬(존재하는 경우)이 처리 후 변경되지 않는다 | NFR-04 |

---

## 3. pytest 단위 테스트 범위 및 우선순위

### 3.1 테스트 계층 범위

| 우선순위 | 계층 | 테스트 대상 | 본 문서 범위 | 비고 |
|----------|------|-------------|--------------|------|
| **P0** | Boundary (단위) | `BoundaryValidator.validate_size()` 또는 동등 public API | **포함** | AC-FR01-01 직접 검증 |
| **P0** | Control (단위/통합) | `Solver` / resolver orchestration + mock Domain | **포함** | AC-FR01-05 격리 검증 |
| P1 | Boundary (단위) | FR-01 나머지 AC (blank count, range, duplicate) | 제외 | 후속 TP 문서 |
| P2 | Domain (단위) | `BlankFinder`, `MissingNumberFinder`, `MagicSquareValidator` | 제외 | Track B |
| P3 | Integration | Boundary → Control → Domain 정상 경로 | 제외 | FR-01 통과 후 |

### 3.2 RED → GREEN 진행 우선순위 (Wave 0)

Report 02 §8 Wave 0 및 PRD Dual-Track §15.1에 따라 아래 순서로 RED 테스트를 추가한다.

| 순서 | RED Test ID | 테스트 이름 (예) | Given | Then |
|------|-------------|------------------|-------|------|
| 1 | `RED-BND-VAL-001a` | `test_should_return_invalid_size_when_grid_is_none` | `grid = None` | `E001_INVALID_SIZE` |
| 2 | `RED-BND-VAL-001b` | `test_should_return_invalid_size_when_grid_is_empty_list` | `grid = []` | `E001_INVALID_SIZE` |
| 3 | `RED-BND-VAL-001c` | `test_should_return_invalid_size_when_rows_exist_but_columns_empty` | `grid = [[]] * 4` | `E001_INVALID_SIZE` |
| 4 | `RED-BND-VAL-001d` | `test_should_return_invalid_size_when_grid_is_3x4` | 3×4 행렬 | `E001_INVALID_SIZE` |
| 5 | `RED-BND-VAL-001e` | `test_should_return_invalid_size_when_grid_is_4x3` | 4×3 행렬 | `E001_INVALID_SIZE` |
| 6 | `RED-BND-VAL-001f` | `test_should_return_invalid_size_when_grid_is_5x5` | 5×5 행렬 | `E001_INVALID_SIZE` |
| 7 | `RED-BND-VAL-001g` | `test_should_not_call_domain_resolver_when_size_invalid` | 임의 size-invalid grid | Domain 0회 호출 |

### 3.3 권장 테스트 파일 배치

```text
tests/
  unit/
    boundary/
      test_boundary_validator_size.py      # P0: AC-FR01-01 순수 Boundary
    control/
      test_solver_size_validation_gate.py  # P0: AC-FR01-05 orchestration + mock
  conftest.py                              # 공통 fixture, pydantic response helper
```

### 3.4 AAA 패턴 및 네이밍 규칙

- **패턴:** Arrange → Act → Assert (프로젝트 `.cursor/rules/magicsquare-tdd-testing.mdc` 준수)
- **함수명:** `test_<기대>_when_<조건>` (Report 02 §7.3)
- **클래스 그룹:** `TestBoundaryValidatorSize` / `TestSolverDomainIsolation`
- **fixture 스코프:** 기본 `function`; 행렬 fixture는 `@pytest.fixture`로 분리

---

## 4. 경계값 케이스 목록 (AC-FR01-01)

> **범위 외 명시:** `grid = 4×4` **정상 입력**(빈칸 2개·값 범위·중복 규칙 충족)은 AC-FR01-01 범위에 **포함하지 않는다**. 해당 케이스는 FR-01 후속 AC 및 Track B(Domain) 테스트에서 다룬다.

### 4.1 포함 케이스 (TS-E-01)

| Case ID | 입력 (`grid`) | 행×열 | 실패 유형 | 기대 `errorCode` | 기대 `message` (PRD §13) | 비고 |
|---------|---------------|-------|-----------|------------------|--------------------------|------|
| BV-01 | `None` | — | null 참조 | `E001_INVALID_SIZE` | `Input matrix must be 4x4.` | Report 02 §5.4, §8 Wave 0 |
| BV-02 | `[]` | 0×— | 빈 리스트 | `E001_INVALID_SIZE` | 동일 | 행 수 0 |
| BV-03 | `[[]] * 4` | 4×0 | 열 없음 | `E001_INVALID_SIZE` | 동일 | 각 행 길이 0 |
| BV-04 | 3×4 정수 행렬 | 3×4 | 행 부족 | `E001_INVALID_SIZE` | 동일 | RD-03, I-01 |
| BV-05 | 4×3 정수 행렬 | 4×3 | 열 부족 | `E001_INVALID_SIZE` | 동일 | PRD §12.1 |
| BV-06 | 5×5 정수 행렬 | 5×5 | 행·열 초과 | `E001_INVALID_SIZE` | 동일 | PRD §12.1 |

### 4.2 BV-04~06 대표 fixture (Arrange용)

```python
# BV-04: 3×4
grid_3x4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# BV-05: 4×3
grid_4x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

# BV-06: 5×5 (값은 임의; 크기만 검증 대상)
grid_5x5 = [[i * 5 + j + 1 for j in range(5)] for i in range(5)]
```

### 4.3 명시적 제외 (Out of Scope for AC-FR01-01)

| Case ID | 입력 | 제외 사유 |
|---------|------|-----------|
| **EX-01** | 4×4 정상 계약 충족 행렬 | AC-FR01-01 통과 케이스; FR-02~05 / Track B 대상 |
| EX-02 | 4×4이나 `0` 개수 ≠ 2 | AC-FR01-02 (TS-E-02) |
| EX-03 | 4×4이나 값 범위 위반 | AC-FR01-03 (TS-E-03) |
| EX-04 | 4×4이나 non-zero 중복 | AC-FR01-04 (TS-E-04) |

---

## 5. 예외 / 특이 케이스 목록

AC-FR01-01은 **예외 throw 금지** 정책(PRD §13) 하에 동작한다. 아래는 크기 검증 경로에서 추가로 점검할 특이 케이스이다.

| Case ID | 입력 / 조건 | 기대 동작 | 테스트 의도 |
|---------|-------------|-----------|-------------|
| SP-01 | `grid = None` | `E001_INVALID_SIZE` 반환, **예외 없음** | null-safe early return |
| SP-02 | `grid = [[]] * 4` (동일 inner list 참조) | `E001_INVALID_SIZE` | Python list 곱셈 함정; 열 길이 0 일관 판정 |
| SP-03 | jagged array `[ [1,2,3,4], [5,6,7], [8,9,10,11], [12,13,14,15] ]` | `E001_INVALID_SIZE` | 행마다 열 길이 불일치 |
| SP-04 | `grid = [[1]*4]*4` (행 참조 공유) | 크기 4×4로 **통과 가능**; 값 검증은 후속 AC | 참조 공유 side effect; NFR-04 별도 점검 |
| SP-05 | non-integer cell (예: `"1"`, `None` 셀) | 구현 전 **Decision Needed**; 최소 기대: 예외 throw 금지 | pydantic/타입 계약 확장 시 재정의 |
| SP-06 | 동일 invalid grid 2회 연속 호출 | 동일 `{errorCode, message}` (NFR-03) | 결정성 |
| SP-07 | size-invalid 입력 후 원본 grid 객체 변경 없음 | mutable grid 입력 시 in-place 변경 금지 (NFR-04) | BV-04~06에 적용 |

> **SP-05 메모:** AC-FR01-01 1차 Wave에서는 **구조(행·열 수) 검증**에 집중한다. 셀 타입 검증은 FR-01 후속 또는 pydantic 입력 모델 도입 시 별도 AC로 승격한다.

---

## 6. Domain resolver 진입점 호출 횟수 검증 전략 (mock / spy)

### 6.1 검증 대상 (AC-FR01-05)

PRD §13, §15.1, GS-03에 따라 size-invalid 입력 시 아래 진입점이 **호출되지 않음**을 검증한다.

| Layer | 진입점 (Component) | mock 대상 |
|-------|-------------------|-----------|
| Domain | `BlankFinder.find_blanks` | FR-02 |
| Domain | `MissingNumberFinder.find_missing_numbers` | FR-03 |
| Domain | `MagicSquareValidator.is_magic` | FR-04 |
| Control | `Solver.resolve` (또는 orchestration facade) | FR-05 |

### 6.2 전략 A — Boundary 단위 테스트 (순수 검증)

**범위:** `BoundaryValidator`만 단독 테스트.

- Domain/Control 의존성 **주입하지 않음**
- `validate(grid)` → `ValidationResult` / `FailureResponse` 반환 assert
- **호출 횟수 검증 불필요** (컴포넌트 내부에 Domain 참조가 없어야 함 — NFR-06)

```python
# Arrange
grid = None

# Act
result = boundary_validator.validate(grid)

# Assert
assert result.error_code == "E001_INVALID_SIZE"
assert result.message == "Input matrix must be 4x4."
```

### 6.3 전략 B — Control orchestration 테스트 (mock / spy, AC-FR01-05)

**범위:** Boundary 검증 실패 시 Control이 Domain을 호출하지 않는지 검증.

| 기법 | 용도 | 권장 |
|------|------|------|
| `unittest.mock.patch` | Domain 클래스/함수 전체 대체 | **1차 권장** |
| `unittest.mock.MagicMock` + `assert_not_called()` | 호출 여부 단언 | **1차 권장** |
| `wraps=` (spy) | 실제 구현 호출 추적 | 2차; 통합 테스트 |
| `pytest-mock` (`mocker.patch`) | pytest fixture 스타일 patch | 팀 선호 시 |

**패턴 예시 (의사 코드):**

```python
from unittest.mock import patch, MagicMock

@patch("magicsquare.control.solver.BlankFinder")
@patch("magicsquare.control.solver.MissingNumberFinder")
@patch("magicsquare.control.solver.MagicSquareValidator")
def test_should_not_invoke_domain_when_grid_is_none(
    mock_validator_cls,
    mock_missing_cls,
    mock_blank_cls,
    solver,
):
    # Arrange
    grid = None
    mock_blank_cls.return_value = MagicMock()
    mock_missing_cls.return_value = MagicMock()
    mock_validator_cls.return_value = MagicMock()

    # Act
    result = solver.handle(grid)

    # Assert — AC-FR01-01
    assert result.error_code == "E001_INVALID_SIZE"

    # Assert — AC-FR01-05 (호출 횟수 0)
    mock_blank_cls.return_value.find_blanks.assert_not_called()
    mock_missing_cls.return_value.find_missing_numbers.assert_not_called()
    mock_validator_cls.return_value.is_magic.assert_not_called()
```

### 6.4 mock 주입 위치 원칙

| 원칙 | 설명 |
|------|------|
| **patch where used** | `Solver`가 import하는 모듈 경로에 patch (`magicsquare.control.solver.X`) |
| **생성자 DI 우선 (REFACTOR)** | Green 이후 `Solver(blank_finder=..., ...)` 형태로 mock 주입 가능 |
| **call_count 명시** | `assert_called_once()` 대신 **`assert_not_called()`** 또는 `call_count == 0` 사용 |
| **부분 mock 금지** | size-invalid 7케이스(BV-01~06 + jagged) 각각에서 0회 호출 확인 (parametrize) |

### 6.5 BV-01~06 parametrize 격리 테스트

```python
@pytest.mark.parametrize(
    "grid,case_id",
    [
        (None, "BV-01"),
        ([], "BV-02"),
        ([[]] * 4, "BV-03"),
        (grid_3x4, "BV-04"),
        (grid_4x3, "BV-05"),
        (grid_5x5, "BV-06"),
    ],
)
def test_should_not_call_domain_resolver_for_invalid_size(grid, case_id, solver, domain_mocks):
    result = solver.handle(grid)
    assert result.error_code == "E001_INVALID_SIZE"
    for mock in domain_mocks:
        mock.assert_not_called()
```

---

## 7. pydantic 응답 계약 검증

PRD §13 실패 payload `{ errorCode, message }`를 pydantic 모델로 고정하여 Boundary 테스트에서 스키마 위반을 조기 탐지한다.

```python
from pydantic import BaseModel

class FailureResponse(BaseModel):
    error_code: str = Field(alias="errorCode")
    message: str

# Assert 시
parsed = FailureResponse.model_validate(result.to_dict())
assert parsed.error_code == "E001_INVALID_SIZE"
assert parsed.message == "Input matrix must be 4x4."
```

| 검증 항목 | 기대 |
|-----------|------|
| 필수 필드 | `errorCode`, `message` |
| 누락 필드 | pydantic `ValidationError` (테스트 fixture에서 계약 깨짐 탐지) |
| 추가 필드 | `model_config = ConfigDict(extra="forbid")` 권장 |

---

## 8. 커버리지 목표

PRD §14 NFR-01, NFR-02 및 §20 Engineering Principles 기준.

| NFR | 계층 | 목표 | 본 TP 기여 |
|-----|------|------|------------|
| NFR-01 | Domain (`src/magicsquare/entity/`, `control/` 내 Domain 로직) | **≥ 95%** | 간접 — AC-FR01-05 mock 테스트로 Domain 오호출 방지 |
| NFR-02 | Boundary (`src/magicsquare/boundary/`) | **≥ 85%** | **직접** — BV-01~06 size 검증 분기 커버 |
| — | Control orchestration gate | ≥ 85% (Boundary 동등 적용) | AC-FR01-05 parametrize |

### 8.1 AC-FR01-01 관련 최소 커버 분기

- `grid is None` 분기
- `len(grid) != 4` 분기
- `any(len(row) != 4 for row in grid)` 분기
- early return 후 Domain 미진입 (Control 테스트)

---

## 9. pytest-cov 측정 전략

### 9.1 설치

```bash
pip install pytest-cov
```

또는 `pyproject.toml` dev 의존성에 추가:

```toml
[project.optional-dependencies]
dev = ["pytest>=8.0", "pytest-cov>=5.0", "pydantic>=2.0"]
```

### 9.2 실행 명령 (전체)

```bash
pytest --cov=src --cov-report=term-missing
```

### 9.3 AC-FR01-01 범위 한정 측정

```bash
# Boundary size 검증만
pytest tests/unit/boundary/test_boundary_validator_size.py \
  --cov=src/magicsquare/boundary \
  --cov-report=term-missing \
  --cov-fail-under=85

# Control Domain 격리 gate
pytest tests/unit/control/test_solver_size_validation_gate.py \
  --cov=src/magicsquare/control \
  --cov-report=term-missing
```

### 9.4 계층별 fail-under (CI 권장)

```bash
# Domain
pytest tests/unit/entity tests/unit/control \
  --cov=src/magicsquare/entity \
  --cov=src/magicsquare/control \
  --cov-report=term-missing \
  --cov-fail-under=95

# Boundary
pytest tests/unit/boundary \
  --cov=src/magicsquare/boundary \
  --cov-report=term-missing \
  --cov-fail-under=85
```

### 9.5 커버리지 해석 가이드

| `--cov-report` | 용도 |
|----------------|------|
| `term-missing` | 로컬 RED/GREEN — **미커버 라인 번호** 확인 |
| `html` | PR 리뷰 — `htmlcov/index.html` |
| `--cov-branch` | size 검증 분기(행 vs 열) 누락 탐지 (2차 도입) |

> **주의:** mock-heavy Control 테스트는 Domain **실행** 커버리지를 올리지 않는다. NFR-01(95%) 달성은 Track B Domain 단위 테스트와 병행해야 한다.

---

## 10. Traceability Matrix (본 TP 범위)

| Business Rule | FR | AC | Test Case | Boundary Case | RED Test ID | Component |
|---------------|-----|-----|-----------|---------------|-------------|-----------|
| BR-01 | FR-01 | AC-FR01-01 | TS-E-01 | BV-01~06 | RED-BND-VAL-001a~f | BoundaryValidator |
| — | FR-01 | AC-FR01-05 | TS-E-01 + GS-03 | BV-01~06, SP-03 | RED-BND-VAL-001g | Solver (+ mocks) |

---

## 11. 완료 기준 (Exit Criteria)

- [ ] BV-01~06 전 케이스 pytest GREEN
- [ ] AC-FR01-05: size-invalid 입력 7종(None, [], [[]]*4, 3×4, 4×3, 5×5, jagged)에서 Domain mock **call_count == 0**
- [ ] pydantic `FailureResponse` 계약 검증 통과
- [ ] 예외 throw 없음 (SP-01, SP-06)
- [ ] Boundary `--cov-fail-under=85` 통과
- [ ] 4×4 정상 입력(EX-01)이 **본 테스트 파일에 없음** 확인

---

## 12. 변경 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | AC-FR01-01 기반 초판 — 경계값·mock 전략·pytest-cov |

---

*본 문서는 테스트 **계획**이며, production 구현 코드를 포함하지 않는다.*
