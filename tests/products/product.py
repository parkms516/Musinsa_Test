from pages.musinsa_page import *

# TC_PRODUCT_01 | 상품 상세페이지 이동
def TC_PRODUCT_01(driver):
    print("\n[TC_PRODUCT_01] 상품 상세페이지 이동")

    open_main(driver)
    open_search(driver)
    search_product(driver, "맨투맨")

    scroll_down(driver, 3)
    time.sleep(2)

    try:
        items = get_product_items(driver)
        print(f" - 조회된 총 상품 수 : {len(items)}개")

        random_index = random.randint(0, len(items) - 1)
        selected_item = items[random_index]

        goods_name = selected_item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
        print(f"선택한 상품 : {goods_name} ({random_index}번째)")

        product_link = selected_item.find_element(By.XPATH, './/a[contains(@class, "gtm-select-item")]')
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_link)
        time.sleep(2)
        product_link.send_keys(Keys.ENTER)

    except Exception:
        print(f"\n[테스트 결과]\n상품 요소를 찾을 수 없음 | FAIL")
        return

    time.sleep(3)

    tabs = driver.window_handles

    print("\n[테스트 결과]")
    if len(tabs) > 1:
        driver.switch_to.window(tabs[-1])
        print("상품 상세페이지로 이동 완료 | PASS")
    else:
        print("상품 상세페이지로 이동 실패 | FAIL")

# TC_PRODUCT_02 | 할인율 계산
def TC_PRODUCT_02(driver):
    print("\n[TC_PRODUCT_02] 할인율 계산")

    open_main(driver)
    open_search(driver)
    search_product(driver, "맨투맨")

    scroll_down(driver, 3)
    time.sleep(2)

    pass_count = 0
    fail_count = 0

    for i in range(1, 6):
        print(f"\n[{i}/5] 번째 상품 검증")

        try:
            items = get_product_items(driver)
            selected_item = random.choice(items)

            goods_name = selected_item.find_element(By.CSS_SELECTOR, "a.gtm-select-item span").text
            print(f"선택한 상품 : {goods_name}")

            product_link = selected_item.find_element(By.XPATH, './/a[contains(@class, "gtm-select-item")]')
            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", product_link)
            time.sleep(2)
            product_link.send_keys(Keys.ENTER)

            time.sleep(3)

            tabs = driver.window_handles
            driver.switch_to.window(driver.window_handles[-1])
            time.sleep(2)

            name = get_product_name(driver)
            sale_price = int(get_sale_price(driver).replace("원", "").replace(",", ""))

            try:
                sale_rate = int(get_product_salerate(driver).replace("%", ""))
            except:
                sale_rate = 0

            try:
                original_price = int(get_original_price(driver).replace("원", "").replace(",", ""))
            except:
                original_price = sale_price

            calc_price = int(original_price * (100 - sale_rate) / 100)

            print("\n[가격 정보]")
            print(f"상품명 : {name}")
            print(f"원가 : {original_price}원")
            print(f"할인율 : {sale_rate}%")
            print(f"표시 가격 : {sale_price}원")
            print(f"계산 가격 : {calc_price}원")

            print("\n[테스트 결과]")
            if sale_price == calc_price:
                print("할인율 계산 가격 일치 | PASS")
                pass_count += 1
            else:
                diff = sale_price - calc_price
                print(f"할인율 계산 가격 불일치 (차이: {diff}원) | FAIL")
                fail_count += 1

        except Exception:
            print(f"\n[테스트 결과]\n요소 추출 또는 계산 중 오류 발생 | FAIL")
            fail_count += 1

        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(1)

    print("\n[최종 테스트 결과]")
    print(f"PASS : {pass_count}건")
    print(f"FAIL : {fail_count}건")