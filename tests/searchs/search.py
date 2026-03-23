from pages.musinsa_page import *

# TC_SEARCH_01 | 정상 검색
def TC_SEARCH_01(driver):
    print("\n[TC_SEARCH_01] 정상 검색")

    open_main(driver)
    open_search(driver)
    search_product(driver, "후드티")

    print("검색 완료 및 상품 로딩")

    try:
        items = get_product_items(driver)

        print("\n[테스트 결과]")
        if len(items) > 0:
            print(f"'후드티' 관련 상품 정상 노출 확인 (총 {len(items)}개) | PASS")
        else:
            print("상품 목록이 비어 있음 | FAIL")

    except Exception:
        print(f"\n[테스트 결과]\n상품 요소를 찾을 수 없음 | FAIL")


# TC_SEARCH_02 | 존재하지 않는 검색
def TC_SEARCH_02(driver):
    print("\n[TC_SEARCH_02] 존재하지 않는 검색")

    open_main(driver)
    open_search(driver)

    keyword = "test_" + str(random.randint(100000, 999999))
    print(f"입력한 검색어 : {keyword}")

    search_product(driver, keyword)
    print("검색 완료 및 상품 로딩")

    print("\n[테스트 결과]")
    try:
        get_wait(driver).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'없습니다')]")))
        print("검색 결과 없음 안내 문구 정상 표시됨 | PASS")

    except Exception:
        items = driver.find_elements(By.CSS_SELECTOR, "div.sc-fOOuSg")

        if len(items) == 0:
            print("검색 결과 없음 문구는 없으나 노출된 상품이 0개임 | PASS")
        else:
            print(f"존재하지 않는 검색어임에도 상품 노출 | FAIL")


# TC_SEARCH_03 | 빈칸 검색
def TC_SEARCH_03(driver):
    print("\n[TC_SEARCH_03] 빈칸 검색")

    open_main(driver)
    open_search(driver)
    search_product(driver, " ")

    print("빈칸 입력 및 검색 시도")

    print("\n[테스트 결과]")
    try:
        alert = get_wait(driver).until(EC.alert_is_present())
        print(f"알림창 문구 : '{alert.text}'")
        alert.accept()
        print("빈칸 검색 차단 및 알림창 정상 노출 | PASS")

    except Exception:
        print(f"알림창 없이 검색이 진행됨 | FAIL")