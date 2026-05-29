# MagicSquare_XX — Error Contract (Dual-Stack)

| 항목 | 내용 |
|------|------|
| 문서 버전 | 1.0 |
| 작성일 | 2026-05-29 |
| SSOT 코드 | [`src/entity/oracles.py`](../src/entity/oracles.py) |

---

## 1. 의도적 이중 계약 (C-03)

ECB Training(Wave 0)과 Dual-Track Production은 **동일 size 규칙**, **다른 envelope·코드 prefix**를 사용한다.

| 입력 | ECB (`BoundaryValidator`) | Dual-Track (`InputValidator`) |
|------|---------------------------|-------------------------------|
| `grid is None` | `INVALID_SIZE` / `Grid must be 4x4.` | `E003_NULL_INPUT` / `Input matrix must not be null.` |
| size 위반 | `INVALID_SIZE` / `Grid must be 4x4.` | `E001_INVALID_SIZE` / `Input matrix must be 4x4.` |

**T-02 결정:** PRD §8.1 ECB 오라클은 Report/06 30건 assert로 **동결**. Dual-Track null 분기는 FR-01 UIBoundary 계약. Wave D GREEN 후 envelope 통합(T-01) 검토.

---

## 2. SSOT 참조 (C-02)

| 상수 | 정의 위치 | 소비 |
|------|-----------|------|
| `AC_FR_01_01_INVALID_SIZE_*` | `entity.oracles` | `magicsquare.boundary.responses`, `tests/constants.py` |
| `DT_INVALID_SIZE_*`, `DT_NULL_INPUT_*` | `entity.oracles` | `boundary.schemas` (re-export) |

---

## 3. 변경 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | REFACTOR 3번 그룹 — oracles SSOT, C-03 문서화 |
