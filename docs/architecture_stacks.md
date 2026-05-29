# MagicSquare_XX — Dual-Stack Architecture

| 항목 | 내용 |
|------|------|
| 문서 버전 | 1.0 |
| 작성일 | 2026-05-29 |
| 범위 | ECB Training Stack vs Dual-Track Production Stack |
| SSOT | Report/03, Report/07, Report/12 |

---

## 1. 개요

본 저장소는 **두 개의 독립 ECB 스택**을 병행 운영한다. Wave 0(GREEN)은 ECB 훈련 트랙으로 완료되었으며, Dual-Track은 FR-01~05 프로덕션 경로이다. REFACTOR 1번 그룹(A-01~A-06)은 **스택 통합 없이** 역할·호출 경로·마이그레이션 방향을 고정한다.

---

## 2. 스택 비교

| 구분 | ECB Training (Wave 0) | Dual-Track Production |
|------|----------------------|------------------------|
| **목적** | AC-FR-01-01 size 검증 TDD 훈련 | FR-01~05 입력·출력·solve 계약 |
| **Boundary** | `src/magicsquare/boundary/` | `src/boundary/` |
| **Control** | `src/magicsquare/control/solver.py` | `src/control/solve_partial_magic_square.py` |
| **Entity** | `src/magicsquare/entity/` (얇은 래퍼) | `src/entity/` (도메인 SSOT) |
| **Failure envelope** | `FailureResult` (dataclass) | `FailureResponse` (pydantic) |
| **INVALID_SIZE 코드** | `"INVALID_SIZE"` | `"E001_INVALID_SIZE"` |
| **테스트** | `tests/unit/boundary/`, `tests/unit/control/` | `tests/dualtrack/boundary/`, `tests/dualtrack/entity/` |

---

## 3. 호출 경로

### 3.1 ECB Training Stack

```text
Solver.handle(grid)
  └─ BoundaryValidator.validate_size(grid)  → FailureResult | None
       └─ (size OK) Solver.resolve(grid)      → NotImplementedError (FR-02+)
```

- **AC-FR-01-01:** size-invalid → `INVALID_SIZE` + `"Grid must be 4x4."`
- **AC-FR-01-05:** size-invalid 시 `resolve()` 0회 (Control 격리)

### 3.2 Dual-Track Production Stack

```text
UIBoundary.solve(matrix)
  └─ InputValidator.validate(matrix)           → FailureResponse | None
       └─ (valid) SolvePartialMagicSquare.execute(matrix) → list[int] payload
            └─ entity.services (find_blank_coords, is_magic_square, …)
```

- **FR-01:** null / size / blank / range / duplicate 검증 (Boundary)
- **FR-05:** 성공 payload `int[6]`, 1-index 좌표

### 3.3 Control 레이어 대응 (A-02)

| 클래스 | 패키지 | 역할 | FR / AC |
|--------|--------|------|---------|
| `Solver` | `magicsquare.control` | ECB size 게이트 + (미래) domain resolve | AC-FR-01-01, AC-FR-01-05 |
| `SolvePartialMagicSquare` | `control` | Dual-Track 2-combination solver | FR-05 |

두 Control 클래스는 **병합하지 않는다**. ECB `Solver`는 Wave 0 훈련용; Dual-Track `SolvePartialMagicSquare`는 Golden Master·UIBoundary 경유 프로덕션 경로이다.

---

## 4. Entity SSOT (A-03)

| 패키지 | 역할 |
|--------|------|
| `entity.constants` | `GRID_SIZE`, `MAGIC_CONSTANT`, `BLANK_VALUE` 등 **단일 정의** |
| `magicsquare.entity.constants` | `entity.constants.GRID_SIZE` **re-export** (ECB import 경로 유지) |
| `magicsquare.entity.user` | ECB 학습용 User 값 객체 — **solve 경로 미연결** (A-06) |

---

## 5. User entity (A-06)

`magicsquare.entity.user.User`는 Report/03 ECB 스캐폴딩으로 도입되었다.

- **용도:** 도메인 엔티티·불변식 TDD 연습 (식별자·표시 이름 검증)
- **테스트:** `tests/unit/entity/test_user.py` 전용
- **solve 경로:** `Solver`, `UIBoundary`, `InputValidator`와 **연결되지 않음**
- **향후:** UI 사용자 컨텍스트가 필요할 때 Boundary/Control에서 주입 검토; 현재는 범위 밖

---

## 6. Import 규칙

| import | 사용처 |
|--------|--------|
| `from magicsquare.boundary.*` | ECB unit tests, Wave 0 |
| `from magicsquare.control.solver import Solver` | ECB Control 격리 tests |
| `from boundary.*` | Dual-Track tests, UIBoundary, Golden Master |
| `from entity.*` | Dual-Track Domain/Control |
| `from magicsquare.entity.constants import GRID_SIZE` | ECB Boundary (re-export 경유) |

**주의:** `tests/dualtrack/boundary/` 디렉터리에 `__init__.py`를 두지 않는다. `boundary` 이름이 `src/boundary`를 가리지 않도록 한다 (`tests/conftest.py`가 `src/`를 path 우선).

---

## 7. 마이그레이션 경로 (A-01)

단기(현재): 두 스택 **병행 유지**, ECB 30건 + GM-5 회귀 게이트.

중기(Wave D GREEN 후):

1. REFACTOR 그룹 3~5 — 오라클·envelope SSOT 통합 (`C-*`, `T-*`)
2. REFACTOR 그룹 4 — size 검증 공통화 (`R-02`)
3. Dual-Track GREEN 완료 후 envelope 단일화 검토

장기: 단일 Boundary + 단일 Control facade; **Wave D·FR-02+ GREEN 선행 필수**.

---

## 8. 변경 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | REFACTOR 1번 그룹 — Dual-Stack 아키텍처 문서 초판 |
