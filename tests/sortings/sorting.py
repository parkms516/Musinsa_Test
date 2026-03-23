from pages.musinsa_page import *

# TC_SORTING_01 | 낮은 가격순 정렬
def TC_SORTING_01(driver):
    print("\n[TC_SORTING_01] 낮은 가격순 정렬")

    open_main(driver)
    open_search(driver)
    search_product(driver, "맨투맨")

    click_sort_button(driver)
    sort_low_price(driver)

    scroll_down(driver, 3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(2)
    print("상품 로딩 및 정렬 완료")

    try:
        items = get_product_items(driver)

        prices = []
        names = []

        print("\n[추출된 상품 가격 정보 (상위 15개)]")

        for i, item in enumerate(items[:15], 1):
            try:
                name = item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
                price_text = item.find_element(By.XPATH, './/span[contains(text(),"원")]').text

                price = int(price_text.replace("원", "").replace(",", ""))

                names.append(name)
                prices.append(price)

                print(f"{i:02d} | {name} | {price}원")

            except Exception:
                print(f"{i:02d} | 상품 정보 추출 실패 | FAIL")

        pass_count = 0
        fail_count = 0

        print("\n[가격 비교]")

        for i in range(1, len(prices)):
            current_price = prices[i - 1]
            next_price = prices[i]

            if current_price <= next_price:
                print(f"{i:02d} | {current_price}원 <= {next_price}원 | PASS")
                pass_count += 1
            else:
                print(f"{i:02d} | {current_price}원 > {next_price}원 | FAIL")
                fail_count += 1

        print("\n[최종 테스트 결과]")
        print(f"PASS : {pass_count}건")
        print(f"FAIL : {fail_count}건")

    except Exception:
        print(f"\n[최종 테스트 결과]\n상품 리스트 조회 실패 | FAIL")



# TC_SORTING_02 | 낮은 할인율순 정렬
def TC_SORTING_02(driver):
    print("\n[TC_SORTING_02] 할인율순 정렬")

    open_main(driver)
    open_search(driver)
    search_product(driver, "맨투맨")

    click_sort_button(driver)
    sort_sale_price(driver)

    scroll_down(driver, 3)
    driver.execute_script("window.scrollTo(0,0)")
    time.sleep(2)
    print("상품 로딩 및 정렬 완료")

    try:
        items = get_product_items(driver)

        sales = []
        names = []

        print("\n[추출된 상품 할인율 정보 (상위 15개)]")

        for i, item in enumerate(items[:15], 1):
            try:
                name = item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
                sale_text = item.find_element(By.XPATH, './/span[contains(., "%")]').text

                if sale_text == "":
                    print(f"{i:02d} | {name} | 할인율 없음 | FAIL")
                    continue

                sale = int(sale_text.replace("%", "").strip())

                names.append(name)
                sales.append(sale)

                print(f"{i:02d} | {name} | {sale}%")

            except Exception:
                print(f"{i:02d} | 상품 정보 추출 실패 | FAIL")

        pass_count = 0
        fail_count = 0

        print("\n[할인율 비교]")

        for i in range(1, len(sales)):
            current_sale = sales[i - 1]
            next_sale = sales[i]

            if current_sale >= next_sale:
                print(f"{i:02d} | {current_sale}% >= {next_sale}% | PASS")
                pass_count += 1
            else:
                print(f"{i:02d} | {current_sale}% < {next_sale}% | FAIL")
                fail_count += 1

        print("\n[최종 테스트 결과]")
        print(f"PASS : {pass_count}건")
        print(f"FAIL : {fail_count}건")

    except Exception:
        print(f"\n[최종 테스트 결과]\n상품 리스트 조회 실패 | FAIL")