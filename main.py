from utils.driver import get_driver
from tests.searchs.search import *
from tests.filters.filter import *
from tests.sortings.sorting import TC_SORTING_01, TC_SORTING_02
from tests.products.product import *
from tests.carts.cart import *

print("\n[자동화 테스트 시작]")
driver = get_driver()

# 1. 검색 테스트
#TC_SEARCH_01(driver)
#TC_SEARCH_02(driver)
#TC_SEARCH_03(driver)

# 2. 필터 테스트
#TC_FILTER_01(driver)
#TC_FILTER_02(driver)
#TC_FILTER_03(driver)

# 3. 정렬 테스트
#TC_SORTING_01(driver)
#TC_SORTING_02(driver)

# 4. 상품 상세페이지 테스트
#TC_PRODUCT_01(driver)
#TC_PRODUCT_02(driver)

# 5. 장바구니 테스트
TC_CART_01(driver)
#TC_CART_02(driver)


# 테스트 종료 문구 및 브라우저 닫기
print("\n[테스트 종료] 모든 테스트가 완료되었습니다.")
driver.quit()