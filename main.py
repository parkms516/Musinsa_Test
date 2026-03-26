from utils.driver import get_driver
from tests.searchs.search import *
from tests.filters.filter import *
from tests.sortings.sorting import *
from tests.products.product import *
from tests.carts.cart import *

ALL_TESTS = [
    TC_SEARCH_01, TC_SEARCH_02, TC_SEARCH_03,
    TC_FILTER_01, TC_FILTER_02, TC_FILTER_03,
    TC_SORTING_01, TC_SORTING_02,
    TC_PRODUCT_01, TC_PRODUCT_02,
    TC_CART_01, TC_CART_02
]


def main():
    driver = None

    while True:
        print("\n[테스트 목록]")
        print("0 | 전체 테스트")

        for i, test in enumerate(ALL_TESTS, 1):
            print(f"{i} | {test.__name__}")

        choice = input("\n번호 입력 (예: 1 3 5, 종료 = n) : ").strip()

        if choice.lower() == 'n':
            break

        nums = []
        for c in choice.split():
            if not c.isdigit():
                print("숫자 또는 n을 입력하세요")
                nums = []
                break
            nums.append(int(c))

        if not nums:
            continue

        if 0 in nums:
            selected_tests = ALL_TESTS
            print("\n[전체 테스트 시작]")
        else:
            selected_tests = []

            for n in nums:
                if 1 <= n <= len(ALL_TESTS):
                    test = ALL_TESTS[n - 1]
                    if test not in selected_tests:
                        selected_tests.append(test)
                else:
                    print(f"{n}번은 없는 번호입니다")
                    selected_tests = []
                    break

            if not selected_tests:
                continue

            print(f"\n[{', '.join(t.__name__ for t in selected_tests)}] 시작")

        print("-" * 50)

        if driver is None:
            driver = get_driver()

        for test in selected_tests:
            print(f"[실행] {test.__name__}")
            test(driver)

        print("-" * 50)

        again = input("다시 실행하시겠습니까? (y/n) : ").strip().lower()
        if again == 'n':
            break

    if driver:
        print("브라우저 종료")
        driver.quit()


if __name__ == "__main__":
    main()