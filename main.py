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
        for i in range(len(ALL_TESTS)):
            print(f"{i + 1} | {ALL_TESTS[i].__name__}")

        choice = input("\n실행할 번호 입력 (종료 = n) : ").strip()

        if choice.lower() == 'n':
            break

        if choice.isdigit():
            num = int(choice)
            selected_tests = []

            if num == 0:
                selected_tests = ALL_TESTS
                print("\n[전체 테스트] 시작")
                print("-" * 50)

            elif 1 <= num <= len(ALL_TESTS):
                selected_tests = [ALL_TESTS[num - 1]]
                print(f"\n[{ALL_TESTS[num - 1].__name__}] 시작")
                print("-" * 50)

            else:
                print("[없는 번호] 다시 확인해주세요.")
                continue

            # --- 실제 실행 로직 ---
            if driver is None:
                driver = get_driver()

            for test_case in selected_tests:
                try:
                    driver.get("https://www.musinsa.com")
                    test_case(driver)

                except Exception as e:
                    print(f"오류 발생 : {e}")

        else:
            print("숫자 또는 'n'만 입력 가능합니다.")

        print("-" * 50)
        again = input("다른 테스트를 더 진행할까요? (y/n) : ").strip().lower()
        if again == 'n':
            break

    if driver:
        print("프로그램을 종료하고 브라우저를 닫습니다.")
        driver.quit()


if __name__ == "__main__":
    main()