# Report



4×4 Magic Square 프로젝트의 **문제 정의·TDD 설계·구현 기반** 단계 산출물입니다.



## 문서



| 파일 | 설명 |

|------|------|

| [01. MagicSquare_Problem-Definition-Report.md](./01.%20MagicSquare_Problem-Definition-Report.md) | STEP 1~5 통합 보고서 (관찰, Why #1~#3, 진짜 문제 정의) |

| [02. MagicSquare_TDD-Design-Report.md](./02.%20MagicSquare_TDD-Design-Report.md) | TDD 설계 (Must/Should/Won't, I/O 계약, 오라클, Wave, 회귀) |

| [03. MagicSquare_Implementation-Setup-Report.md](./03.%20MagicSquare_Implementation-Setup-Report.md) | 구현 기반 (`.cursorrules`, ECB 골격, User entity, pytest) |

| [04. MagicSquare_Cursor-Rules-Modularization-Report.md](./04.%20MagicSquare_Cursor-Rules-Modularization-Report.md) | `.cursor/rules/*.mdc` 5개 규칙 파일 도입 및 구조화 보고 |

| [05. MagicSquare_User-Journey-Story-Scenario-Report.md](./05.%20MagicSquare_User-Journey-Story-Scenario-Report.md) | Level 1~4 요구 구조화(Epic, Journey, Stories, Technical Scenario) 보고 |
| [06. MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md](./06.%20MagicSquare_AC-FR01-01-RED-Test-Plan-Report.md) | AC-FR-01-01 테스트 계획·RED 30건·결함·실행 결과 보고 |
| [07. MagicSquare_DualTrack-FR01-FR05-RED-Design-Report.md](./07.%20MagicSquare_DualTrack-FR01-FR05-RED-Design-Report.md) | FR-01~FR-05 Dual-Track RED 설계표 (Track A Boundary / Track B Logic) |
| [09. MagicSquare_DualTrack_RED_TestPlan_Design_Report.md](./09.%20MagicSquare_DualTrack_RED_TestPlan_Design_Report.md) | Dual-Track RED Skeleton 23건·pytest RED 결과·G0~G3 placeholder |
| [10. MagicSquare_AC-FR01-01-GREEN-Wave0-Kickoff-Report.md](./10.%20MagicSquare_AC-FR01-01-GREEN-Wave0-Kickoff-Report.md) | AC-FR-01-01 GREEN Wave 0 착수·C0~C6 커밋 묶음·최소 구현 |



## 작성 범위



| 문서 | 포함 | 미포함 |

|------|------|--------|

| 01 문제 정의 | 문제 인식 · Why · Invariant · 훈련 목표 | 구현·코드·알고리즘 |

| 02 TDD 설계 | 테스트 전략 · 오라클 · Red 순서 · 계약 | 구현·테스트 코드·알고리즘 |

| 03 구현 기반 | Cursor 규칙 · 패키지 구조 · User entity · 단위 테스트 | Grid 검증기 · Wave 0~5 구현 |

| 04 규칙 모듈화 | `.cursor/rules` 구조 · 5개 `.mdc` 규칙 분리 | Grid 검증기 기능 구현 |

| 05 요구 구조화 | Epic · User Journey · User Stories · Implementation Scenario | 실제 구현 코드 · 테스트 코드 · Task 실행 |
| 06 AC-FR-01-01 RED | 테스트 계획 · RED 테스트 30건 · defect_list · pytest RED 결과 | GREEN 구현 · 30 passed |
| 07 Dual-Track RED | FR-01~FR-05 RED 설계표 · G0~G3 · U-/D- Test ID | 테스트 코드 · GREEN 구현 |
| 09 RED Skeleton | 23건 스켈레톤 · tests/boundary · tests/entity · pytest collection ERROR | GREEN 구현 · assert 교체 |
| 10 GREEN Wave 0 | C0~C6 커밋 묶음 · FailureResult · grid=None GREEN · README 체크리스트 | C1~C6 완료 · 30 passed · REFACTOR |



## 다음 단계 (예정)



- README § GREEN **C1~C6** 순차 커밋 (`stabilize/green`)
- Dual-Track Wave D1 (`src/boundary/`) — ECB 30건 회귀 유지
- failureType Should → Must 승격 여부 결정



## 관련



- 프로젝트 개요: [../README.md](../README.md)

- 프롬프트 기록: [../Prompting/](../Prompting/)


