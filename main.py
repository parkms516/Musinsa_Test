from utils.driver import get_driver
from tests.searchs.search import *
from tests.filters.filter import *
from tests.sortings.sorting import TC_SORTING_01, TC_SORTING_02
from tests.products.product import *
from tests.carts.cart import *

# ==========================================
# 1. 테스트 그룹 정의
# ==========================================
TEST_SUITES = {
    "search": [
        ("TC_SEARCH_01", TC_SEARCH_01),
        ("TC_SEARCH_02", TC_SEARCH_02),
        ("TC_SEARCH_03", TC_SEARCH_03)
    ],
    "filter": [
        ("TC_FILTER_01", TC_FILTER_01),
        ("TC_FILTER_02", TC_FILTER_02),
        ("TC_FILTER_03", TC_FILTER_03)
    ],
    "sorting": [
        ("TC_SORTING_01", TC_SORTING_01),
        ("TC_SORTING_02", TC_SORTING_02)
    ],
    "product": [
        ("TC_PRODUCT_01", TC_PRODUCT_01),
        ("TC_PRODUCT_02", TC_PRODUCT_02)
    ],
    "cart": [
        ("TC_CART_01", TC_CART_01),
        ("TC_CART_02", TC_CART_02)
    ]
}

# all = 전체 테스트
TEST_SUITES["all"] = sum(TEST_SUITES.values(), [])


def main():
    # ==========================================
    # 2. 메뉴 출력
    # ==========================================
    print("\n" + "="*50)
    print("🛒 무신사 자동화 테스트 프로그램 🛒")
    print("="*50)

    all_tests = TEST_SUITES["all"]

    # 번호 목록 출력
    for i, (tc_name, _) in enumerate(all_tests, start=1):
        print(f"{i}. {tc_name}")

    print("-" * 50)
    print("👉 번호 선택 (예: 1 2 3)")
    print("👉 또는 그룹 입력 (search / filter / sorting / product / cart / all)")
    print("-" * 50)

    target = input("입력: ").strip().lower()

    # ==========================================
    # 3. 입력 처리
    # ==========================================
    selected_tests = []

    # 숫자 입력 (예: "1 2 3")
    if target and target[0].isdigit():
        numbers = target.split()

        for num in numbers:
            if num.isdigit():
                idx = int(num) - 1
                if 0 <= idx < len(all_tests):
                    selected_tests.append(all_tests[idx])

    # 그룹 입력
    elif target in TEST_SUITES:
        selected_tests = TEST_SUITES[target]

    # 잘못된 입력
    if not selected_tests:
        print(f"\n❌ 잘못된 입력입니다. 프로그램 종료")
        return

    # ==========================================
    # 4. 테스트 실행
    # ==========================================
    print("\n" + "="*50)
    print("🚀 테스트 실행 시작")
    print("="*50 + "\n")

    driver = get_driver()
    pass_count = 0
    fail_count = 0

    try:
        for tc_name, tc_func in selected_tests:
            print(f"▶ 실행 중 : {tc_name}")

            try:
                driver.get("https://www.musinsa.com/app/")
                tc_func(driver)

                print(f"✅ PASS: {tc_name}")
                pass_count += 1

            except Exception as e:
                print(f"❌ FAIL: {tc_name} - {e}")
                fail_count += 1

            print("-" * 50)

    finally:
        driver.quit()

    # ==========================================
    # 5. 결과 출력
    # ==========================================
    print("\n" + "="*50)
    print("📊 테스트 결과 요약")
    print(f"✅ PASS : {pass_count} 건")
    print(f"❌ FAIL : {fail_count} 건")
    print("="*50 + "\n")


# ==========================================
# 6. 실행 진입점
# ==========================================
if __name__ == "__main__":
    main()