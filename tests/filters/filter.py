from pages.musinsa_page import *

# TC_FILTER_01 | 남성 필터 적용
def TC_FILTER_01(driver, keyword="맨투맨"):
    print("[TC_FILTER_01] 남성 필터 적용")

    open_main(driver)
    open_search(driver)
    search_product(driver, keyword)
    print(f"'{keyword}' 검색 완료 및 상품 로딩")

    click_gender_filter_male(driver)
    scroll_down(driver, count=3)
    print("상품 로딩 및 필터 적용 완료")

    try:
        items = get_product_items(driver)
        test_items = random.sample(items, min(len(items), 30))

        pass_count = 0
        fail_count = 0

        print(f"\n[필터 적용 결과 검증 (랜덤 최대 {len(test_items)}개)]")

        for i, item in enumerate(test_items, 1):
            try:
                goods_name = item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
                gender = item.find_element(By.XPATH, './/span[text()="남성" or text()="공용"]').text

                if gender in ["남성", "공용"]:
                    print(f"{i:02d} | {goods_name} | {gender} | PASS")
                    pass_count += 1
                else:
                    print(f"{i:02d} | {goods_name} | {gender} | FAIL")
                    fail_count += 1

            except Exception:
                print(f"{i:02d} | 상품 정보 추출 실패 | FAIL")
                fail_count += 1

        print("\n[테스트 결과]")
        print(f"PASS : {pass_count}건")
        print(f"FAIL : {fail_count}건")

    except Exception:
        print(f"\n[테스트 결과]\n상품 리스트 조회 실패 | FAIL")



# TC_FILTER_02 | 여성 상품 배제
def TC_FILTER_02(driver, keyword="맨투맨"):
    print("[TC_FILTER_02] 여성 상품 배제")

    open_main(driver)
    open_search(driver)
    search_product(driver, keyword)

    click_gender_filter_male(driver)
    scroll_down(driver, count=3)
    print(f"'{keyword}' 검색 완료 및 상품 로딩")

    try:
        items = get_product_items(driver)
        test_items = random.sample(items, min(len(items), 30))

        pass_count = 0
        fail_count = 0

        print(f"\n[여성 상품 배제 (랜덤 최대 {len(test_items)}개)]")

        for i, item in enumerate(test_items, 1):
            try:
                goods_name = item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
                gender = item.find_element(By.XPATH, './/span[text()="남성" or text()="공용" or text()="여성"]').text

                if gender == "여성":
                    print(f"{i:02d} | {goods_name} | {gender} | FAIL")
                    fail_count += 1
                else:
                    print(f"{i:02d} | {goods_name} | {gender} | PASS")
                    pass_count += 1

            except Exception:
                print(f"{i:02d} | 상품 정보 추출 실패 | FAIL")
                fail_count += 1

        print("\n[테스트 결과]")
        print(f"PASS : {pass_count}건")
        print(f"FAIL : {fail_count}건")

    except Exception:
        print(f"\n[테스트 결과]\n상품 리스트 조회 실패 | FAIL")



# TC_FILTER_03 | 복수 필터 적용
def TC_FILTER_03(driver, keyword="맨투맨"):
    print("[TC_FILTER_03] 복수 필터 적용")

    open_main(driver)
    open_search(driver)
    search_product(driver, keyword)
    print(f"'{keyword}' 검색 완료 및 상품 로딩")

    click_gender_filter_male(driver)
    click_color_filter(driver)
    click_red_color(driver)
    click_red_color_apply(driver)

    scroll_down(driver, count=3)
    print("상품 로딩 및 복수 필터 적용 완료")

    try:
        items = get_product_items(driver)
        test_items = random.sample(items, min(len(items), 30))

        pass_count = 0
        fail_count = 0

        print(f"\n[복수 필터 적용 결과 검증 (랜덤 최대 {len(test_items)}개)]")

        for i, item in enumerate(test_items, 1):
            try:
                goods_name = item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
                gender = item.find_element(By.XPATH, './/span[text()="남성" or text()="공용"]').text
                red = item.find_element(By.CSS_SELECTOR, 'a[data-item-applied-filter-group-1*="컬러:레드"]')

                if gender in ["남성", "공용"] and red:
                    print(f"{i:02d} | {goods_name} | {gender} | RED | PASS")
                    pass_count += 1
                else:
                    print(f"{i:02d} | {goods_name} | {gender} | 조건 불일치 | FAIL")
                    fail_count += 1

            except Exception:
                print(f"{i:02d} | 상품 정보 추출 실패 (또는 필터 조건 불일치) | FAIL")
                fail_count += 1

        print("\n[최종 테스트 결과]")
        print(f"PASS : {pass_count}건")
        print(f"FAIL : {fail_count}건")

    except Exception:
        print(f"\n[테스트 결과]\n상품 리스트 조회 실패 | FAIL")