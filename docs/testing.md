# MagicSquare_XX — Testing Guide

| 항목 | 내용 |
|------|------|
| 문서 버전 | 1.0 |
| 작성일 | 2026-05-29 |

---

## 1. 회귀 게이트 (REFACTOR)

```powershell
# ECB Wave 0 (30건) — assert 변경 금지 (Q-04)
python -m pytest tests/unit/boundary/ tests/unit/control/ -v

# Golden Master GM-2 (5건) — 파일 경로 지정 권장 (Q-02)
python -m pytest tests/unit/test_golden_master_magic_square.py -m golden_master -v

# Dual-Track RED skeleton (23건, pytest.fail 의도적 실패)
python -m pytest tests/dualtrack/boundary/ tests/dualtrack/entity/ -v

# 전체 수집 (67 tests, shadowing 해소 후)
python -m pytest tests/ --collect-only -q
```

---

## 2. Q-02 Golden Master 단독 실행

`pytest -m golden_master`만 실행하면 dualtrack 수집이 포함될 수 있다. **GM 전용**은 테스트 파일 경로를 지정한다.

```powershell
python -m pytest tests/unit/test_golden_master_magic_square.py -m golden_master -v
```

---

## 3. Q-03 Dual-Track RED skeleton

`tests/dualtrack/` 23건은 Wave D GREEN 전 **의도적 RED** (`pytest.fail`). REFACTOR 중 GM-2·ECB 30건 green 유지.

---

## 4. Q-01 커버리지 (2026-05-29)

```powershell
python -m pytest tests/unit/boundary/ tests/unit/control/ tests/unit/test_golden_master_magic_square.py tests/unit/entity/ --cov=src --cov-report=term-missing
```

| 구분 | 결과 |
|------|------|
| TOTAL | **93%** |
| Boundary ECB | 85~100% |
| Domain `magic_square_validator` | 76% (Wave D6 선행) |

---

## 5. 변경 이력

| 버전 | 일자 | 내용 |
|------|------|------|
| 1.0 | 2026-05-29 | REFACTOR 6번 그룹 — testing guide |
