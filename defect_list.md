# MagicSquare_XX — 결함 목록 (Defect List)

| 항목 | 내용 |
|------|------|
| 문서 버전 | 1.0 |
| 작성일 | 2026-05-29 |
| 작성 역할 | QA 리드 |
| 관련 AC | AC-FR-01-01, AC-FR-01-05 |
| 관련 테스트 | `tests/unit/boundary/test_boundary_validator_size.py`, `tests/unit/control/test_solver_size_validation_gate.py` |
| 재현 환경 | Python 3.13.13, pytest 9.0.3, `.venv` (Windows) |

---

## 요약

| 구분 | 수량 |
|------|------|
| Critical | 3 |
| High | 0 |
| Medium | 1 |
| **합계 (Open)** | **0** |
| 수집된 테스트 | 30 / 30 |
| 마지막 실행 명령 | `python -m pytest tests/unit/boundary/ tests/unit/control/ -v --cov=src --cov-report=term-missing` |

RED 단계 테스트는 작성 완료되었으며, **GREEN Wave 0 (C0~C6)** 완료로 ECB 30건 전부 통과한다.

---

## GREEN Wave 0 완료 (2026-05-29)

```text
python -m pytest tests/unit/boundary/ tests/unit/control/ -v
→ 30 passed
```

DEF-001~003 **Closed**. DEF-004 Partial Close (boundary+control 88%).

---

## 결함 목록

| ID | Severity | AC ID | 재현 절차 | 기대값 | 실제값 | 근본 원인 | 수정 요약 |
|----|----------|-------|-----------|--------|--------|-----------|-----------|
| DEF-001 | Critical | AC-FR-01-01 | 1. `.venv` 활성화<br>2. `python -m pytest tests/unit/boundary/test_boundary_validator_size.py -v`<br>3. 수집 단계에서 `FailureResult` import 확인 | `from magicsquare.boundary.responses import FailureResult` 성공 | ~~`ModuleNotFoundError`~~ | `src/magicsquare/boundary/responses.py` 미구현 | **Closed** — `FailureResult` 구현 (Wave 0 C0) |
| DEF-002 | Critical | AC-FR-01-01 | 1. DEF-001 해결 후 동일 명령 실행<br>2. `BoundaryValidator` import 및 size-invalid 호출 | `validator.validate(...)` → `INVALID_SIZE`, 예외 없음 | ~~`ModuleNotFoundError` / `NotImplementedError`~~ | `validator.py` 미구현 | **Closed** — None·[]·4×0·3×4 분기 (Wave 0 C1~C5) |
| DEF-003 | Critical | AC-FR-01-01, AC-FR-01-05 | 1. `python -m pytest tests/unit/control/test_solver_size_validation_gate.py -v`<br>2. `Solver` import 확인 | `handle(None)` 시 `resolve()` 0회 | ~~`ModuleNotFoundError`~~ | `solver.py` 미구현 | **Closed** — `Solver.handle` + Boundary 게이트 (Wave 0 C6) |
| DEF-004 | Medium | AC-FR-01-01 | 1. `python -m pytest tests/unit/boundary/ tests/unit/control/ --cov=src --cov-report=term-missing`<br>2. 출력 맨 아래 coverage 표 확인 | `term-missing` 커버리지 표 출력 (Boundary ≥85% 목표 측정 가능) | ~~`collected 0 items`~~ | DEF-001~003으로 수집 중단 | **Closed** — TOTAL **93%** (2026-05-29 REFACTOR Q-01); Domain validator 76%는 Wave D6 |

---

## AC-FR-01-01 관점 — 차단된 검증 (Blocked)

아래는 구현 결함 해결 전 **자동 검증 불가** 항목이다. (테스트 코드는 존재함)

| 테스트 영역 | 대표 케이스 | 기대 동작 | 차단 결함 |
|-------------|-------------|-----------|-----------|
| 정상 실패 반환 | `grid=None` | `INVALID_SIZE` + `Grid must be 4x4.` | DEF-001, DEF-002 |
| 경계값 | `grid=[]`, `[[]]*4`, 3×4 | 동일 실패 응답 | DEF-002 |
| 메시지 동일성 | PRD §8.1 문구 문자 단위 일치 | `message == "Grid must be 4x4."` | DEF-002 |
| 실패 구조체 | `isinstance(result, FailureResult)` | pydantic/타입 계약 | DEF-001, DEF-002 |
| Domain 격리 | `grid=None` 시 `resolve()` 0회 | `assert_not_called()` | DEF-003 |
| 범위 제한 | size 오류 시 `INVALID_BLANK_COUNT` 등 미반환 | `code == INVALID_SIZE` only | DEF-002 |

---

## 재현 로그 (발췌)

```text
tests\unit\boundary\test_boundary_validator_size.py:7: in <module>
    from magicsquare.boundary.responses import FailureResult
E   ModuleNotFoundError: No module named 'magicsquare.boundary.responses'

tests\unit\control\test_solver_size_validation_gate.py:7: in <module>
    from magicsquare.control.solver import Solver
E   ModuleNotFoundError: No module named 'magicsquare.control.solver'

collected 0 items / 2 errors
Interrupted: 2 errors during collection
```

---

## 수정 우선순위 (권장)

1. **DEF-001** — `FailureResult` (모든 Boundary/Control 실패 응답의 공통 타입)
2. **DEF-002** — `BoundaryValidator` (AC-FR-01-01 핵심)
3. **DEF-003** — `Solver` (AC-FR-01-05 격리)
4. **DEF-004** — 회귀 실행으로 커버리지 재측정

GREEN 완료 후:

```powershell
python -m pytest tests/unit/boundary/ tests/unit/control/ -v --cov=src --cov-report=term-missing
```

Exit criteria: **30 passed**, DEF-001~003 **Closed**, README 결함 체크리스트 2번 항목 체크.

---

## 변경 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | RED 수집 실패 기준 초기 결함 4건 등록 |
| 1.1 | 2026-05-29 | GREEN Wave 0 완료 — DEF-001~003 Closed, 30 passed |
