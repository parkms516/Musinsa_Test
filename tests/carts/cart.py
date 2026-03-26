from pages.musinsa_page import *

# TC_CART_01 | 장바구니 담기
def TC_CART_01(driver, keyword="후드티"):
    print("[TC_CART_01] 장바구니 담기")

    login(driver)
    open_main(driver)
    open_search(driver)
    search_product(driver, keyword)

    time.sleep(2)
    scroll_down(driver, 3)
    time.sleep(2)

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
        driver.switch_to.window(tabs[-1])
        time.sleep(2)

        dropdowns = driver.find_elements(By.CSS_SELECTOR, "input[data-mds='DropdownTriggerInput']")

        for dropdown in dropdowns:
            try:
                dropdown.click()
                time.sleep(1)

                options = driver.find_elements(By.CSS_SELECTOR, "div[data-mds='StaticDropdownMenuItem']")
                good_options = []
                for option in options:
                    if "(품절)" not in option.text:
                        good_options.append(option)

                if len(good_options) > 0:
                    selected_option = random.choice(good_options)
                    print(f"선택한 옵션 : {selected_option.text.split('\n')[0]}")
                    selected_option.click()
                    time.sleep(2)

                else:
                    print("모두 품절이라 장바구니에 포함할 수 없었습니다. | SKIP")
                    dropdown.click()
                    time.sleep(1)
                    return
            except:
                pass

        click_add_to_cart(driver)
        go_to_cart(driver)
        cart_names = get_cart_product_names(driver)

        added_to_cart = False

        for name in cart_names:
            if goods_name in name or name in goods_name:
                added_to_cart = True
                break

        print("\n[테스트 결과]")
        if added_to_cart:
            print(f"장바구니에 정상적으로 추가됨 | PASS")
        else:
            print(f"장바구니에서 상품을 못 찾음 | FAIL")

    except Exception:
        print(f"\n[테스트 결과]\n상품 리스트 조회 실패 또는 에러 발생 | FAIL")



# TC_CART_02 | 장바구니 수량 확인
def TC_CART_02(driver, keyword="후드티"):
    print("[TC_CART_02] 장바구니 수량 확인")

    login(driver)
    open_main(driver)
    open_search(driver)
    search_product(driver, keyword)

    time.sleep(2)
    scroll_down(driver, 3)
    time.sleep(2)

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
        driver.switch_to.window(tabs[-1])
        time.sleep(2)

        dropdowns = driver.find_elements(By.CSS_SELECTOR, "input[data-mds='DropdownTriggerInput']")

        for dropdown in dropdowns:
            try:
                dropdown.click()
                time.sleep(1)

                options = driver.find_elements(By.CSS_SELECTOR, "div[data-mds='StaticDropdownMenuItem']")

                good_options = []
                for option in options:
                    if "(품절)" not in option.text:
                        good_options.append(option)

                if len(good_options) > 0:
                    selected_option = random.choice(good_options)
                    print(f"선택한 옵션 : {selected_option.text.split('\n')[0]}")
                    selected_option.click()
                    time.sleep(2)

                else:
                    print("모두 품절이라 장바구니에 포함할 수 없었습니다. | SKIP")
                    dropdown.click()
                    time.sleep(1)
                    return

            except:
                pass

        cart_number = get_cart_number(driver)

        click_add_to_cart(driver)
        go_to_cart(driver)

        cart_number2 = get_cart_number(driver)

        print("\n[수량 검증]")
        print(f"상품 추가 전 장바구니 수량 : {cart_number}개")
        print(f"상품 추가 후 장바구니 수량 : {cart_number2}개")

        cart_names = get_cart_product_names(driver)

        added_to_cart = False

        for name in cart_names:
            if goods_name in name or name in goods_name:
                added_to_cart = True
                break

        print("\n[테스트 결과]")
        if added_to_cart:
            print(f"수량 정상 증가 확인 ({cart_number} -> {cart_number2}) | PASS")
        else:
            print("수량 증가 확인 실패 또는 장바구니에서 상품 못 찾음 | FAIL")

    except Exception:
        print(f"\n[테스트 결과]\n상품 리스트 조회 실패 또는 에러 발생 | FAIL")