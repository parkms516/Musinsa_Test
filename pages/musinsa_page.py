from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# 계정 정보 입력
USER_ID = "your_id_here"
USER_PW = "your_password_here"


# 명시적 대기 (최대 10초)
def get_wait(driver):
    return WebDriverWait(driver, 10)


# 무신사 메인 페이지 접속
def open_main(driver):
    driver.get("https://www.musinsa.com")


# 로그인
def login(driver):
    driver.get("https://www.musinsa.com/main/musinsa/recommend?gf=F")
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "_gnb__login--button_5pcry_214").click()
    time.sleep(2)

    id_input = driver.find_element(By.CSS_SELECTOR, "input[placeholder='통합계정 또는 이메일']")
    id_input.send_keys(USER_ID)

    pw_input = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
    pw_input.send_keys(USER_PW)

    driver.find_element(By.CSS_SELECTOR, "button[data-button-id='login_login']").click()
    time.sleep(3)


# 상단 검색창 버튼 클릭
def open_search(driver):
    get_wait(driver).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-button-name="검색창"]'))).click()


# 검색어 입력 후 Enter 키 실행
def search_product(driver, keyword):
    search_input = get_wait(driver).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-button-name="검색홈_검색창선택"]'))
    )
    search_input.send_keys(keyword)
    search_input.send_keys(Keys.ENTER)


# 필터 : 성별 '남성' 선택
def click_gender_filter_male(driver):
    get_wait(driver).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[title="남성"]'))).click()
    time.sleep(2)


# 페이지 하단으로 스크롤
def scroll_down(driver, count=3):
    for _ in range(count):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)


# 상품 리스트
def get_product_items(driver):
    return get_wait(driver).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.sc-fOOuSg"))
    )


# 컬러 필터 열기
def click_color_filter(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-filter-type="컬러"]'))
    ).click()
    time.sleep(2)


# 필터 : 색상 '레드' 선택
def click_red_color(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="레드"]/ancestor::button'))
    ).click()
    time.sleep(2)


# '레드' 필터 적용
def click_red_color_apply(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-section-name="apply_filter"]'))
    ).click()
    time.sleep(2)


# 정렬 버튼
def click_sort_button(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.DropDown__Button-sc-tsoic9-1.hDLGPf'))
    ).click()
    time.sleep(2)


# 낮은 가격순
def sort_low_price(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="낮은 가격순"]'))
    ).click()
    time.sleep(2)


# 할인율순
def sort_sale_price(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, '//span[text()="할인율순"]'))
    ).click()
    time.sleep(2)


# 상품명
def get_product_name(driver):
    return get_wait(driver).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(@class,"GoodsName")]'))
    ).text


# 정가
def get_original_price(driver):
    return get_wait(driver).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(@class,"line-through")]'))
    ).text


# 할인율
def get_product_salerate(driver):
    return get_wait(driver).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(@class,"DiscountRate")]'))
    ).text


# 할인가
def get_sale_price(driver):
    return get_wait(driver).until(
        EC.presence_of_element_located((By.XPATH, '//span[contains(@class,"CalculatedPrice")]'))
    ).text


# 장바구니 담기
def click_add_to_cart(driver):
    button = get_wait(driver).until(
        EC.presence_of_element_located((By.XPATH, '//button[@data-button-name="장바구니담기"]'))
    )
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
    button.click()
    time.sleep(1)


# 장바구니 이동
def go_to_cart(driver):
    get_wait(driver).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@data-button-name="장바구니 바로가기"]'))
    ).click()
    time.sleep(2)


# 장바구니 상품명 리스트
def get_cart_product_names(driver):
    time.sleep(2)
    elements = driver.find_elements(By.CSS_SELECTOR, "div.cart-goods__name a")

    names_list = []
    for element in elements:
        text = element.text
        if text != "":
            names_list.append(text)

    return names_list


# 장바구니 수량
def get_cart_number(driver):
    return get_wait(driver).until(
        EC.presence_of_element_located((By.XPATH, '//span[@class="_gnb__menu-cart_5pcry_170"]'))
    ).text