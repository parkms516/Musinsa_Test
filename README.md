# 🛒 무신사(MUSINSA) 웹 E2E 테스트 자동화 프레임워크 (QA)

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=flat-square&logo=selenium&logoColor=white)
![Test](https://img.shields.io/badge/Test-E2E%20Automation-FF5722?style=flat-square)

이커머스 플랫폼 무신사(MUSINSA)의 핵심 구매 과정에서 발생할 수 있는 기능 오류를 사전에 방지하기 위해 웹 E2E UI 테스트 자동화 프레임워크를 설계 및 구현한 프로젝트이다.

<br>

## 1. 프로젝트 개요
* **진행 기간** : 2026.02 ~ 2026.03
* **테스트 대상** : 무신사 웹 페이지 (PC)
* **사용 기술** : Python, Selenium WebDriver
* **테스트 유형** : E2E 테스트, 기능/예외 테스트, 데이터 검증 테스트

<br>

## 🎯 목표 및 테스트 전략 (Test Strategy)
본 프로젝트는 단순한 기능 동작 확인이 아닌, 실제 사용자 행동 흐름 기반의 **E2E 테스트 중심 전략**을 채택하여 서비스 품질 관리(QA) 관점의 자동화를 지향했습니다.

1. **사용자 구매 흐름 중심 설계** : `Search` → `Filter` → `Detail` → `Cart` 로 이어지는 핵심 비즈니스 로직 최우선 검증
2. **데이터 정합성 검증** : 단순 UI 표시 여부를 넘어, 실제 할인율 계산 등 내부 데이터의 정확성 검증 수행
3. **Edge Case 커버** : 정상 작동(Happy Path)뿐만 아니라 빈칸 검색, 존재하지 않는 검색어 등 예외 시나리오 포함
4. **회귀 테스트 자동화** : 반복적인 수동 테스트 리소스를 줄이고, 동적 웹 환경에서도 안정적으로 실행되는 구조 구현

<br>

## 📁 프로젝트 구조
```text
📦 MUSINSA_QA_AUTOMATION
 ┣ 📂 pages/                 # 웹 요소(Element) 식별 및 핵심 동작 정의
 ┃ ┗ 📜 musinsa_page.py      
 ┣ 📂 utils/                 # 드라이버 초기화 및 환경 설정
 ┃ ┗ 📜 driver.py            
 ┗ 📜 main.py                # 테스트 시나리오 실행 및 결과 출력
````

<br>

## 📋 테스트 케이스 (Test Coverage)

총 12개의 주요 테스트 시나리오를 설계하고 자동화했다.

| 구분 | TC ID | 테스트 명 | 예상 결과 |
| :--- | :--- | :--- | :--- |
| **기능** | `TC_SEARCH_01` | 정상 검색 | 검색어와 관련된 상품 목록이 1개 이상 노출되어야 함 |
| **예외** | `TC_SEARCH_02` | 존재하지 않는 검색 | 상품 0개 노출 및 '검색결과가 없습니다' 안내 노출 |
| **예외** | `TC_SEARCH_03` | 빈칸 검색 | 검색 차단 및 경고 알림창(Alert) 노출 |
| **기능** | `TC_FILTER_01` | 남성 필터 적용 | 성별 라벨이 '남성' 또는 '공용'인 상품만 노출 |
| **검증** | `TC_FILTER_02` | 여성 상품 배제 | 남성 필터 적용 시 '여성' 라벨 상품이 존재하지 않아야 함 |
| **기능** | `TC_FILTER_03` | 복수 필터 적용 | 성별(남성)+색상(레드) 두 가지 조건을 모두 충족하는 상품만 노출 |
| **기능** | `TC_SORTING_01` | 낮은 가격순 정렬 | 상품 가격이 이전 상품보다 크거나 같은 오름차순으로 노출 |
| **기능** | `TC_SORTING_02` | 할인율순 정렬 | 상품 할인율이 이전 상품보다 작거나 같은 내림차순으로 노출 |
| **UI/UX** | `TC_PRODUCT_01` | 상세 페이지 이동 | 클릭한 상품 상세 페이지가 새 탭(창)에서 정상 로딩됨 |
| **검증** | `TC_PRODUCT_02` | 할인 금액 계산식 | 원가와 할인율로 계산된 금액이 화면의 판매가와 일치해야 함 |
| **기능** | `TC_CART_01` | 장바구니 상품 추가 | 로그인 후 장바구니 목록에 선택한 상품/옵션이 정상 노출됨 |
| **UI/UX** | `TC_CART_02` | 장바구니 뱃지 갱신 | 상품을 담은 직후 상단 장바구니 뱃지 수량이 +1 증가함 |

<br>

## 💡 핵심 구현 포인트

### 1\. Explicit Wait 기반 대기 안정성 확보

  * 무조건적인 `time.sleep()` 대기를 배제하고, `WebDriverWait`과 `Expected Conditions`를 활용하여 DOM 렌더링 시점에 맞춘 동적 대기를 구현함으로써 불필요한 대기 시간을 제거하고 테스트 속도 및 안정성을 대폭 개선했습니다.

### 2\. E2E 흐름 유지를 위한 로그인 선행 처리

  * 장바구니 테스트 수행 시 비회원 접근이 차단되는 문제를 해결하기 위해, 테스트 사전 조건으로 유효한 계정을 통한 **로그인 자동화**를 구현하여 전체 구매 흐름이 단절되지 않도록 구성했습니다.

### 3\. 데이터 정합성 검증 (할인율 계산식 구현)

  * 웹에 노출된 텍스트('원가', '할인율')를 파싱 및 전처리한 뒤, 스크립트 내부에서 수학적 수식을 통해 계산된 최종 금액과 실제 UI 화면에 렌더링된 '판매가'가 정확히 일치하는지 비교하는 고도화된 검증을 수행했습니다.

<br>

## 📊 실행 결과 예시

실제 스크립트 실행을 통해 다음과 같은 E2E 자동 검증이 수행됩니다.

```text
[TC_SEARCH_01] PASS
[TC_FILTER_03] PASS
[TC_SORTING_02] PASS
[TC_PRODUCT_02] PASS
[TC_CART_01] PASS

==============================
총 결과:
PASS: 10
FAIL: 2
==============================
```

<br>

## ⚠️ 한계점 및 개선 방향 (Next Step)

**한계점 (Limitations)**

  * UI 기반(Selenium) 테스트의 특성상 렌더링 대기로 인해 전체 실행 속도가 상대적으로 느림
  * 테스트 데이터가 스크립트 내에 고정(Hard-coding)되어 있어 다양한 엣지 케이스 커버에 한계 존재

**개선 및 확장 계획 (Action Item)**

  * `pytest` 프레임워크 도입 및 테스트 데이터 파라미터화(Data-Driven Testing) 적용
  * GitHub Actions를 활용한 CI/CD 자동화 파이프라인 연동
  * 속도 최적화를 위한 Headless 모드 및 병렬 실행 적용
  * API 테스트 연동(Postman / REST Assured) 및 성능 테스트(k6, JMeter) 확장
  * Allure Report를 연동한 테스트 실행 결과 리포트 시각화

<br>

## 🚀 실행 방법 (Getting Started)

### ✔ Prerequisites

  * Python 3.x
  * Chrome Browser

### ✔ Installation

```bash
pip install selenium webdriver-manager
```

### ✔ Run

```bash
python main.py
```

<br>

## 🙋‍♂️ 프로젝트 의의

이 프로젝트는 단순한 스크립트 작성이나 자동화 툴 사용을 넘어, **테스트 설계 능력 - 프레임워크 구현 능력 - 문제 해결 및 지속적 개선 역량**을 종합적으로 보여주기 위해 기획되었습니다.

> 💬 *"좋은 테스트는 단순히 버그를 찾는 것을 넘어서, 서비스의 신뢰도를 만든다."*

```
```

