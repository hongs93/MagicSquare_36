# PRD — Magic Square 4x4 TDD Practice

## 1. Executive Summary
본 PRD는 4x4 Magic Square 문제를 "정답 산출"이 아니라 "불변식 기반 계약 충족"으로 정의하고, Dual-Track TDD(Track A: Boundary/UI Contract, Track B: Domain/Logic Invariant)를 통해 구현 전 검증 기준을 고정하는 문서다. 본 문서는 입력/출력 계약, 계층 경계(ECB/Clean Architecture), RED-GREEN-REFACTOR 흐름, Concept-to-Code Traceability를 명시하며, 모든 요구사항을 테스트 가능한 문장으로 규정한다.

---

## 2. Background
Report/1 기반으로 본 프로젝트의 핵심 배경은 다음과 같다.

- 학습자는 문제를 구현부터 시작해 검증 기준을 사후에 맞추는 경향이 있다.
- "마방진을 만든다"는 표현은 범위가 넓고 판정 기준이 불명확하다.
- 테스트 가능한 규칙(불변식, 입력/출력 계약, 실패 정책)이 사전에 고정되지 않으면 회귀 검증이 불가능해진다.
- 본 프로젝트는 알고리즘 완성도가 아니라 규칙 명세 → 검증 → 구현 → 리팩토링 훈련을 목표로 한다.

---

## 3. Problem Statement
본 문제는 "4x4 마방진을 만든다"가 아니라, 아래 조건을 항상 검증 가능하게 충족하는 것이다.

1. 입력 계약을 만족하는 4x4 행렬을 받는다.
2. 두 개의 빈칸(`0`)과 두 개의 누락 숫자(1~16, 0 제외)를 규칙대로 식별한다.
3. 고정된 두 시도 순서(small-first, reverse)로 배치를 판정한다.
4. 성공 시 고정 출력 형식(`int[6]`, 1-index)을 반환한다.
5. 실패 시 고정 실패 정책을 반환한다.
6. 동일 입력은 동일 결과를 반환한다(결정성).

입력/출력 계약은 기능 설명보다 우선하며, 계약 위반은 Boundary에서 차단한다.

---

## 4. Why Now / Why Chain
왜 지금 이 프로젝트를 수행해야 하는지의 근거는 다음과 같다.

- 학습자는 구현을 먼저 작성하고, 테스트 기준을 나중에 맞춘다.
- 입력/출력 계약이 없으면 테스트 케이스가 요구사항을 대표하지 못한다.
- Boundary와 Domain 책임이 섞이면 오류 원인 분리가 불가능해진다.
- 리팩토링 후 계약 보존 여부를 검증할 수 없다.
- Dual-Track TDD를 적용하면 UI/Boundary 계약과 Domain 불변식의 회귀를 분리해 통제할 수 있다.

---

## 5. Target Users
- TDD 학습자
- 코드 리뷰어
- Clean Architecture/ECB 계층 분리를 훈련하는 개발자

사용 환경:
- 콘솔 실행 또는 테스트 실행 중심
- UI/DB/Web 의존성은 범위 밖

---

## 6. Vision & Epic Goal
**Epic Goal:** 불변식 기반 사고 훈련 시스템 구축

Vision:
- Concept를 Rule로 분해하고, Rule을 Use Case와 Contract로 고정한다.
- Contract를 Test로 검증하고, Component 책임으로 추적한다.
- 구현보다 검증 기준을 우선 고정하는 개발 습관을 형성한다.

---

## 7. Persona
1. TDD를 학습 중인 개발자
2. Clean Architecture 계층 분리를 이해하려는 학습자
3. 알고리즘 정답보다 설계/계약/테스트/리팩토링 흐름을 훈련하려는 사용자

---

## 8. User Journey Summary

| Stage | 핵심 행동 | Pain Point | Learning Outcome |
|---|---|---|---|
| 1. Problem Recognition | 문제를 "정답 찾기"가 아닌 "계약 충족"으로 재정의 | 목표가 기능 구현으로만 보임 | 문제를 검증 가능한 문장으로 정의 |
| 2. Contract Definition | 입력/출력/실패 정책 고정 | 입력 형태와 실패 기준이 문서마다 다름 | 테스트 가능한 계약 작성 |
| 3. Domain Separation | Boundary와 Domain 규칙 분리 | 검증 로직과 포맷/예외 처리가 혼합됨 | 계층 책임 분리 |
| 4. Dual-Track TDD Progress | Track A/Track B 병행 Red→Green→Refactor | 한 트랙 완료 후 다른 트랙 임시 처리 | 병렬 진척 규칙 준수 |
| 5. Regression Protection | 핵심 시나리오 회귀 고정 | 리팩토링 후 계약 파손 발견 지연 | 회귀 기준과 추적성 유지 |

---

## 9. Scope

### 9.1 In-Scope
- 빈칸 좌표 탐색
- 누락 숫자 탐색
- 마방진 판정
- 두 조합 시도 후 결과 반환
- Boundary 입력 검증
- 출력 계약 검증
- RED-GREEN-REFACTOR 기반 테스트 가능 요구 정의

### 9.2 Out-of-Scope
- UI 화면 개발
- DB 저장/검색
- Web/API 서버 개발
- N×N 일반화
- 완전한 마방진 생성 알고리즘
- 사용자 인증/권한
- 네트워크 오류 처리
- QR 스캔
- 외부 서비스 연동

---

## 10. Functional Requirements

### FR-01 Input Verification
- **Description:** 입력 행렬이 고정 입력 계약을 충족하는지 검증한다.
- **Layer:** Boundary
- **Input:** `int[][] grid`
- **Processing Rules:**
  - 행 수 4, 열 수 4를 만족해야 한다.
  - 값은 `0` 또는 `1..16`만 허용한다.
  - `0` 개수는 정확히 2개여야 한다.
  - `0` 제외 값은 중복될 수 없다.
- **Output:** 검증 통과 시 Domain 호출 허용, 실패 시 오류 반환
- **Acceptance Criteria:**
  - AC-FR01-01: 크기가 4x4가 아니면 `E001_INVALID_SIZE` 반환
  - AC-FR01-02: `0` 개수가 2개가 아니면 `E002_INVALID_BLANK_COUNT` 반환
  - AC-FR01-03: 값 범위 위반 시 `E003_INVALID_RANGE` 반환
  - AC-FR01-04: `0` 제외 중복 시 `E004_DUPLICATE_NONZERO` 반환
  - AC-FR01-05: 검증 실패 시 Domain resolver를 호출하지 않는다
- **Error / Exception Policy:** 오류 코드 기반 실패 응답 반환, 예외 전파 금지
- **Related Business Rules:** BR-01, BR-02, BR-03, BR-04
- **Related Test Direction:** Boundary 실패 케이스 단위 검증
- **Component Candidate:** BoundaryValidator

### FR-02 Blank Coordinate Discovery
- **Description:** row-major 기준 첫 번째/두 번째 빈칸 좌표를 식별한다.
- **Layer:** Domain
- **Input:** 계약 검증 완료된 4x4 행렬
- **Processing Rules:**
  - `0` 위치를 row-major 순서로 탐색한다.
  - 첫 번째 발견 위치를 blank1, 두 번째를 blank2로 정의한다.
- **Output:** `(blank1, blank2)` 0-index 내부 좌표
- **Acceptance Criteria:**
  - AC-FR02-01: 빈칸 2개를 정확히 반환한다
  - AC-FR02-02: blank1은 blank2보다 row-major 순서상 앞선다
- **Error / Exception Policy:** 본 단계에서 입력 오류 처리 금지(전제: FR-01 통과)
- **Related Business Rules:** BR-05
- **Related Test Direction:** row-major 순서 판정 테스트
- **Component Candidate:** BlankFinder

### FR-03 Missing Number Discovery
- **Description:** `1..16` 중 누락된 두 숫자를 찾는다.
- **Layer:** Domain
- **Input:** 계약 검증 완료된 4x4 행렬
- **Processing Rules:**
  - `0` 제외 값 집합을 구성한다.
  - `1..16`에서 미포함 값을 누락 숫자로 산출한다.
  - 누락 숫자 2개를 오름차순으로 정렬한다.
- **Output:** `(mSmall, mLarge)` with `mSmall < mLarge`
- **Acceptance Criteria:**
  - AC-FR03-01: 누락 숫자는 정확히 2개다
  - AC-FR03-02: 반환 순서는 오름차순이다
- **Error / Exception Policy:** 본 단계에서 입력 오류 처리 금지
- **Related Business Rules:** BR-06, BR-07
- **Related Test Direction:** 누락 숫자 계산/정렬 검증
- **Component Candidate:** MissingNumberFinder

### FR-04 Magic Square Validation
- **Description:** 완성 행렬이 4x4 마방진 조건(상수 34)을 충족하는지 판정한다.
- **Layer:** Domain
- **Input:** 빈칸에 후보 숫자가 채워진 완성 4x4 행렬
- **Processing Rules:**
  - 모든 행 합 = 34
  - 모든 열 합 = 34
  - 주대각선 합 = 34
  - 부대각선 합 = 34
- **Output:** `isMagic: boolean`
- **Acceptance Criteria:**
  - AC-FR04-01: 행/열/대각선 중 하나라도 불일치하면 false
  - AC-FR04-02: 모든 조건이 일치하면 true
- **Error / Exception Policy:** 판정 결과만 반환, 예외 발생 금지
- **Related Business Rules:** BR-08, BR-09
- **Related Test Direction:** 합 규칙 위반 위치별 판정 테스트
- **Component Candidate:** MagicSquareValidator

### FR-05 Two-Combination Solver and Result Formatting
- **Description:** small-first, reverse 순서로 시도하고 성공 조합을 고정 포맷으로 반환한다.
- **Layer:** Control/Application + Boundary Output
- **Input:** FR-01 통과 입력, FR-02/03/04 결과
- **Processing Rules:**
  - Attempt 1: `mSmall -> blank1`, `mLarge -> blank2`
  - Attempt 2: Attempt 1 실패 시 `mLarge -> blank1`, `mSmall -> blank2`
  - 성공 시 해당 조합을 즉시 반환한다.
  - 두 시도 모두 실패 시 실패 정책을 반환한다.
  - 출력 좌표는 1-index로 변환한다.
- **Output:** 성공 시 `int[6] = [r1, c1, n1, r2, c2, n2]`
- **Acceptance Criteria:**
  - AC-FR05-01: Attempt 1 성공 시 Attempt 2를 수행하지 않는다
  - AC-FR05-02: Attempt 1 실패/Attempt 2 성공 시 reverse 조합을 반환한다
  - AC-FR05-03: 성공 반환은 길이 6 정수 배열이다
  - AC-FR05-04: 좌표는 1-index다
  - AC-FR05-05: 두 시도 실패 시 `E005_UNSOLVABLE_TWO_COMBINATIONS` 반환
- **Error / Exception Policy:** 실패 응답 객체 반환(예외 던지기 금지)
- **Related Business Rules:** BR-10, BR-11, BR-12, BR-13
- **Related Test Direction:** small-first 성공/실패-역전/양쪽 실패 시나리오 테스트
- **Component Candidate:** Solver, ResultFormatter

---

## 11. Business Rules / Domain Rules

| Rule ID | Rule (항상 참) |
|---|---|
| BR-01 | 입력은 4행 4열 정수 행렬이어야 한다. |
| BR-02 | 빈칸 값 `0`은 정확히 2개여야 한다. |
| BR-03 | 각 셀 값은 `0` 또는 `1..16`이어야 한다. |
| BR-04 | `0`을 제외한 숫자는 중복될 수 없다. |
| BR-05 | 첫 번째 빈칸은 row-major 스캔 순서의 첫 `0`으로 정의한다. |
| BR-06 | 누락 숫자는 `1..16`에서 입력에 없는 값 2개다. |
| BR-07 | 누락 숫자 반환 순서는 오름차순이다. |
| BR-08 | 4x4 마방진 상수는 34다. |
| BR-09 | 완성 행렬은 모든 행/열/주대각/부대각 합이 34여야 마방진이다. |
| BR-10 | Attempt 1은 `small->blank1`, `large->blank2` 순서다. |
| BR-11 | Attempt 2는 Attempt 1 실패 시에만 수행한다. |
| BR-12 | 성공 출력 좌표는 1-index다. |
| BR-13 | 성공 출력 형식은 길이 6의 `int[6]`이다. |

---

## 12. Input / Output Contract

### 12.1 Input Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Error Code / Failure Policy |
|---|---|---|---|---|---|
| grid | `int[][]` | 4x4 고정 | 4행 x 4열 | 3x4, 4x5 | E001_INVALID_SIZE |
| cell value | int | `0` 또는 `1..16` | `0`, `1`, `16` | `-1`, `17` | E003_INVALID_RANGE |
| blank count | int | `0` 개수 = 2 | `0` 두 개 포함 | `0` 한 개/세 개 | E002_INVALID_BLANK_COUNT |
| non-zero uniqueness | set rule | `0` 제외 중복 금지 | 1~16 중 중복 없음 | `5`가 두 번 등장 | E004_DUPLICATE_NONZERO |
| blank ordering | scan rule | row-major 첫 `0`이 blank1 | `(r1,c1)`이 먼저 발견 | 순서 미고정 | Decision Needed-DN03 |

### 12.2 Output Contract

| Field / Item | Type | Rule | Valid Example | Invalid Example | Related Error Code / Failure Policy |
|---|---|---|---|---|---|
| success payload | `int[6]` | `[r1,c1,n1,r2,c2,n2]` | `[1,1,1,4,4,16]` | 길이 5/7 | E006_INVALID_OUTPUT_CONTRACT (internal) |
| r1,c1,r2,c2 | int | 1-index 좌표 | 1~4 | 0, 5 | E006_INVALID_OUTPUT_CONTRACT (internal) |
| n1,n2 | int | 누락 숫자 2개 | 1~16, 서로 다름 | 범위 밖/동일 값 | E006_INVALID_OUTPUT_CONTRACT (internal) |
| failure payload | object | `{errorCode,message}` | `E001...` 등 | 코드 없음 | FR-01/05 실패 정책 |

---

## 13. Error / Failure Policy

**정책 고정:** 본 PRD는 실패 시 예외를 던지지 않고, 표준 실패 응답(`errorCode`, `message`)을 반환한다.

| Failure Case | Error Code | Message | Layer | Domain resolver 호출 여부 | Related Acceptance Criteria |
|---|---|---|---|---|---|
| 4x4가 아닌 입력 | E001_INVALID_SIZE | Input matrix must be 4x4. | Boundary | No | AC-FR01-01, AC-FR01-05 |
| 빈칸 개수 != 2 | E002_INVALID_BLANK_COUNT | Exactly two blanks (0) are required. | Boundary | No | AC-FR01-02, AC-FR01-05 |
| 값 범위 위반 | E003_INVALID_RANGE | Values must be 0 or 1..16. | Boundary | No | AC-FR01-03, AC-FR01-05 |
| 0 제외 중복 값 | E004_DUPLICATE_NONZERO | Non-zero values must be unique. | Boundary | No | AC-FR01-04, AC-FR01-05 |
| 두 조합 모두 실패 | E005_UNSOLVABLE_TWO_COMBINATIONS | No valid magic square from two fixed attempts. | Control/Domain result | Yes | AC-FR05-05 |

---

## 14. Non-Functional Requirements

| NFR ID | Requirement |
|---|---|
| NFR-01 | Domain Logic 테스트 커버리지는 95% 이상이어야 한다. |
| NFR-02 | Boundary Validation 테스트 커버리지는 85% 이상이어야 한다. |
| NFR-03 | 동일 입력은 동일 출력(성공/실패 코드 포함)을 반환해야 한다. |
| NFR-04 | 입력 행렬은 처리 후 변경되지 않아야 한다(No side effects). |
| NFR-05 | 4x4 단일 실행은 50ms 이내여야 한다(로컬 표준 실행 환경 기준). |
| NFR-06 | Boundary와 Domain 책임은 분리되어야 한다. |
| NFR-07 | 설명 없는 매직 넘버 사용을 금지한다(34 포함 상수 명명 필수). |
| NFR-08 | 하드코딩과 테스트 약화를 통해 Green을 달성하는 방식을 금지한다. |

---

## 15. Dual-Track TDD Strategy

### 15.1 Track A — Boundary / UI Contract TDD
- 입력 검증 테스트
- 출력 형식 테스트
- 실패 응답 테스트
- 입력 검증 실패 시 Domain resolver 미호출 테스트

### 15.2 Track B — Domain / Logic TDD
- 빈칸 탐색 테스트
- 누락 숫자 탐색 테스트
- 마방진 검증 테스트
- small-first 성공 테스트
- small-first 실패 후 reverse 성공 테스트
- 두 조합 모두 실패 테스트

### 15.3 Parallel Progression Rules
1. UI(Track A) RED와 Logic(Track B) RED를 분리한다.
2. Track A GREEN과 Track B GREEN은 각각 최소 변경으로 달성한다.
3. 구조 개선은 REFACTOR 단계에서만 수행한다.
4. Domain 전체 구현 후 Boundary를 나중에 붙이는 직렬 방식은 금지한다.
5. 테스트 삭제/약화/skip/xfail로 통과를 만드는 행위를 금지한다.

---

## 16. Test Plan / QA

### 16.1 Normal Scenarios
- TS-N-01: small-first 성공
- TS-N-02: small-first 실패 후 reverse 성공

### 16.2 Exception Scenarios
- TS-E-01: 4x4가 아닌 입력
- TS-E-02: 빈칸 개수 오류
- TS-E-03: 값 범위 오류
- TS-E-04: 중복 숫자 오류
- TS-E-05: 두 조합 모두 실패

### 16.3 Boundary Scenarios
- TS-B-01: 최소값 1 처리
- TS-B-02: 최대값 16 처리
- TS-B-03: `0`은 빈칸으로만 처리
- TS-B-04: 출력 좌표 1-index 검증
- TS-B-05: 성공 반환 배열 길이 6 검증

### 16.4 Representative Test Data

- **RD-01 small-first 성공 행렬**
  - 기반: 표준 4x4 마방진에서 `(1,1)=0`, `(4,4)=0` (1-index 표기)
  - 누락 숫자: 1, 16
  - 기대: Attempt 1 성공

- **RD-02 reverse 성공 행렬**
  - 기반: 표준 4x4 마방진에서 첫 빈칸 자리에 큰 수, 둘째 빈칸 자리에 작은 수가 원래 값인 조합
  - 예: 누락 숫자 2, 15이며 첫 빈칸 원래값이 15
  - 기대: Attempt 1 실패, Attempt 2 성공

- **RD-03 invalid size 행렬**
  - 3x4 또는 4x5
  - 기대: E001

- **RD-04 invalid blank count 행렬**
  - `0` 개수 1 또는 3
  - 기대: E002

- **RD-05 duplicate value 행렬**
  - `0` 제외 값 중복 존재
  - 기대: E004

- **RD-06 invalid range 행렬**
  - `-1` 또는 `17` 포함
  - 기대: E003

---

## 17. Architecture Overview, High-Level

- **Boundary Layer**
  - 입력 검증
  - 오류 응답 표준화
  - 성공 출력 포맷 검증/변환

- **Domain Layer**
  - 빈칸 탐색
  - 누락 숫자 탐색
  - 마방진 판정
  - 시도 순서 기반 조합 판정

- **Control / Application Layer**
  - Boundary와 Domain 호출 흐름 오케스트레이션
  - Attempt 1/2 실행 순서 보장
  - 최종 성공/실패 응답 조립

의존 방향:
- Boundary → Control → Domain
- Domain은 Boundary를 참조하지 않는다.
- Domain은 UI/DB/Web/파일시스템에 의존하지 않는다.

---

## 18. Component Candidates

| Component | Responsibility | Layer | Input | Output | Related FR | Related Test |
|---|---|---|---|---|---|---|
| BoundaryValidator | 입력 계약 검증 및 오류 코드 반환 | Boundary | `int[][]` | pass/fail | FR-01 | TS-E-01~04 |
| BlankFinder | row-major 빈칸 2개 탐색 | Domain | validated grid | blank1, blank2 | FR-02 | TS-B-03, TS-N-01/02 |
| MissingNumberFinder | 누락 숫자 2개 계산/정렬 | Domain | validated grid | `mSmall,mLarge` | FR-03 | TS-N-01/02 |
| MagicSquareValidator | 행/열/대각선 합(34) 판정 | Domain | completed grid | bool | FR-04 | TS-N-01/02, TS-E-05 |
| Solver | Attempt 1/2 실행 및 성공/실패 결정 | Control | domain outputs | success/failure | FR-05 | TS-N-01/02, TS-E-05 |
| ResultFormatter | 성공 `int[6]` 1-index 포맷 보장 | Boundary/Control | blanks+numbers | `int[6]` | FR-05 | TS-B-04, TS-B-05 |

---

## 19. Risks & Ambiguities

| Risk | Impact | Decision / Mitigation |
|---|---|---|
| 1-index/0-index 혼동 | 잘못된 좌표 반환 | 내부 좌표 0-index, 외부 반환 1-index를 계약으로 분리 |
| row-major 첫 빈칸 정의 누락 | Attempt 순서 불결정 | BR-05로 강제, AC-FR02-02로 검증 |
| small-first/reverse 데이터 혼동 | 시나리오 오탐 | RD-01/02를 분리 유지 |
| 입력 행렬 변경 여부 불명확 | 부작용 회귀 발생 | NFR-04로 불변 처리 강제 |
| 두 조합 실패 정책 누락 | 예외/응답 불일치 | E005 실패 응답 정책 고정 |
| 상수 34 하드코딩 | 유지보수 저하 | 명명 상수 사용 원칙 강제 |
| Boundary/Domain 책임 혼합 | 테스트 격리 실패 | 계층별 FR/컴포넌트 책임 고정 |

---

## 20. Engineering Principles

Report/3 및 Cursor Rules 요약 반영:

1. PEP8 준수
2. 모든 함수 파라미터/반환 타입 힌트 필수
3. 테스트 프레임워크는 pytest 사용
4. 테스트는 AAA 패턴 사용
5. 커버리지 목표: Domain 95%+, Boundary 85%+
6. ECB 계층 분리 및 의존 방향 준수
7. RED-GREEN-REFACTOR 단계 준수
8. `print()` 디버깅 금지
9. bare `except:` 금지
10. 테스트 약화(삭제/완화/무분별 skip) 금지
11. 설명 없는 magic number 사용 금지

---

## 21. Traceability Matrix

| Concept / Invariant | Business Rule | Feature ID | Acceptance Criteria | Test Case Candidate | Component |
|---|---|---|---|---|---|
| 4x4 입력 | BR-01 | FR-01 | AC-FR01-01 | TS-E-01 | BoundaryValidator |
| 빈칸 2개 | BR-02 | FR-01 | AC-FR01-02 | TS-E-02 | BoundaryValidator |
| 값 범위 0 또는 1~16 | BR-03 | FR-01 | AC-FR01-03 | TS-E-03 | BoundaryValidator |
| 중복 금지(0 제외) | BR-04 | FR-01 | AC-FR01-04 | TS-E-04 | BoundaryValidator |
| row-major 첫 빈칸 | BR-05 | FR-02 | AC-FR02-02 | TS-B-03 | BlankFinder |
| 누락 숫자 2개 | BR-06 | FR-03 | AC-FR03-01 | TS-N-01/02 | MissingNumberFinder |
| 누락 숫자 오름차순 | BR-07 | FR-03 | AC-FR03-02 | TS-N-01/02 | MissingNumberFinder |
| 마방진 상수 34 | BR-08 | FR-04 | AC-FR04-02 | TS-N-01/02 | MagicSquareValidator |
| 행/열/대각선 합 | BR-09 | FR-04 | AC-FR04-01/02 | TS-E-05, TS-N-01/02 | MagicSquareValidator |
| small-first 시도 | BR-10 | FR-05 | AC-FR05-01 | TS-N-01 | Solver |
| reverse 시도 | BR-11 | FR-05 | AC-FR05-02 | TS-N-02 | Solver |
| int[6] 반환 | BR-13 | FR-05 | AC-FR05-03 | TS-B-05 | ResultFormatter |
| 1-index 좌표 | BR-12 | FR-05 | AC-FR05-04 | TS-B-04 | ResultFormatter |

---

## 22. Open Questions / Decision Needed

| ID | Decision Needed | 이유(문서 충돌/미확정) |
|---|---|---|
| DN-01 | 본 PRD의 "두 빈칸 완성 Solver" 범위를 공식 1차 범위로 승인할지 결정 필요 | 기존 Report/2 일부 내용은 "완성 격자 판정기 only" 중심으로 정리되어 있음 |
| DN-02 | 실패 응답 메시지 표준 언어(영문/국문)와 포맷 규칙 확정 필요 | 운영/리뷰 환경에 따라 메시지 표준이 달라질 수 있음 |
| DN-03 | row-major 정의를 계약 본문에서 좌표 예시까지 포함할지 확정 필요 | 팀 내 오해 방지를 위해 예시 고정 필요 |
| DN-04 | E006(출력 계약 위반) 노출 범위 확정 필요 | 내부 방어 코드로만 둘지 외부 오류 코드로 공개할지 결정 필요 |

---

## 23. Appendix

### 23.1 참고 문서 목록
- `Report/1.ProblemDefinition_Report.md`
- `Report/4.UserJourney_Epic_to_TechnicalScenario_Report.md`
- `Report/2.CleanArchitecture_DualTrack_TDD_Design_Report.md`
- `Report/3.DevelopmentEnvironment_CursorRules_ECB_UserEntity_Report.md`
- `.cursorrules`
- `.cursor/rules/*.mdc`

### 23.2 Cursor Rules 요약
- 프로젝트 범위 고정, 계층 경계 준수, 타입힌트/문서화 강제
- TDD phase별 금지 행위 명시
- pytest/AAA/coverage 정책 고정
- 금지 패턴(`print`, bare except, magic number, 테스트 약화) 고정

### 23.3 대표 Gherkin Scenario 요약

- **GS-01 small-first 성공**
  - Given 유효 입력 계약을 만족하는 4x4 행렬과 빈칸 2개
  - When small-first 조합을 시도하면
  - Then 마방진 판정을 통과하고 `int[6]`을 1-index로 반환한다

- **GS-02 reverse 성공**
  - Given 유효 입력 계약을 만족하고 small-first가 실패하는 행렬
  - When reverse 조합을 시도하면
  - Then 마방진 판정을 통과하고 reverse 순서 결과를 반환한다

- **GS-03 입력 계약 실패**
  - Given 4x4/빈칸2개/범위/중복 규칙 중 하나를 위반한 입력
  - When 요청을 처리하면
  - Then 해당 오류 코드를 반환하고 Domain resolver를 호출하지 않는다

- **GS-04 양쪽 조합 실패**
  - Given 입력 계약은 유효하지만 두 조합 모두 마방진이 아닌 행렬
  - When 요청을 처리하면
  - Then `E005_UNSOLVABLE_TWO_COMBINATIONS`를 반환한다

### 23.4 향후 RED Test ID 후보
- `RED-BND-VAL-001` invalid size
- `RED-BND-VAL-002` invalid blank count
- `RED-BND-VAL-003` invalid range
- `RED-BND-VAL-004` duplicate non-zero
- `RED-DOM-BLANK-001` row-major first blank
- `RED-DOM-MISS-001` two missing numbers ascending
- `RED-DOM-MAGIC-001` magic constant 34 validation
- `RED-CTRL-SOL-001` small-first success
- `RED-CTRL-SOL-002` reverse success
- `RED-CTRL-SOL-003` unsolvable two combinations

---

본 문서는 파일 생성 없이 Markdown 본문으로만 작성되었으며, 이후 `docs/PRD_MagicSquare.md`로 저장 가능하다.
