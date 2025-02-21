from selenium import webdriver  # Selenium WebDriver를 사용하여 웹페이지 조작
from selenium.webdriver.common.by import By  # 요소를 찾기 위한 By 모듈
from selenium.webdriver.common.keys import Keys  # 키보드 입력을 위한 Keys 모듈
from selenium.webdriver.chrome.options import Options  # Chrome 옵션 설정을 위한 모듈
import time  # 페이지 로딩을 기다리기 위한 time 모듈
from bs4 import BeautifulSoup  # HTML 파싱을 위한 BeautifulSoup
import pymysql  # MySQL 데이터베이스와 연결하기 위한 pymysql 라이브러리

# ========================================
# **1. Selenium을 사용하여 웹페이지 크롤링**
# ========================================

# User-Agent 설정 (크롤링 감지를 피하고 브라우저처럼 동작하도록 설정)
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"

# Chrome 옵션 설정
options_ = Options()
# User-Agent={} 형식이 아니라, --user-agent=...로 정확히 설정해야함.
options_.add_argument(f"--user-agent={user_agent}")  # User-Agent 설정
# options_.add_experimental_option("detach", True)  # 브라우저 자동 종료 방지.  # 기본 적용된거 같은데.
options_.add_experimental_option("excludeSwitches", ["enable-logging", "enable-automation"])  # 불필요한 로그 제거 및 "자동화 메시지" 숨기기

# enable-logging
# ChromeDriver가 실행될 때 터미널 또는 콘솔에 불필요한 디버그 로그 메시지를 출력하는 것을 방지합니다.
# 특히 DevTools 관련 불필요한 메시지가 출력되는 것을 막습니다.

# enable-automation
# Chrome을 자동화 모드(Selenium을 통한 실행)로 실행할 때 **"Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다."**라는 메시지를 제거합니다.

# Chrome WebDriver 실행
driver = webdriver.Chrome(options=options_)
# 적용된 옵션 확인
# print(driver.capabilities)

# url 설정
url = "https://kream.co.kr"

# 웹페이지 접속
driver.get(url)

# ========================================
# **2. 검색어 입력 및 결과 페이지 크롤링**
# ========================================

# 검색 버튼 클릭
driver.find_element(By.CSS_SELECTOR, ".btn_search.header-search-button.search-button-margin").click()

# 검색어 입력 후 엔터
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys("슈프림")
driver.find_element(By.CSS_SELECTOR, ".input_search.show_placeholder_on_focus").send_keys(Keys.ENTER)

# 페이지를 여러 번 스크롤 다운하여 더 많은 상품을 로드
for i in range(10):
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
    time.sleep(0.7)

# HTML 소스 가져오기
html = driver.page_source  # 페이지 정보를 가져옴.
soup = BeautifulSoup(html, "html.parser")   # HTML로 파싱 # 가져온 text정보를 html태그로 인식

# Chrome WebDriver 종료
driver.quit()

# ========================================
# **3. 웹페이지에서 상품 정보 추출**
# ========================================

# select 해당하는 모든 정보를 가져옵니다.
# select_one 해당하는 것중에서 가장 위에 있는 하나만 가져옵니다. 

products = soup.select(".product_card") #list 형태. # CSS 선택자를 사용하여 모든 상품 정보 가져오기
product_list = []  # 크롤링한 데이터를 저장할 리스트

# 가져온 상품 정보를 하나씩 처리
for rank, i in enumerate(products, 1):
    name_ko = i.select_one(".translated_name").text  # 상품 한글명

    # 제품명에 후드가 들어간것만 출력
    if "후드" in name_ko:
        brand = i.select_one(".product_info_brand, .brand").text  # 브랜드명 
        name_en = i.select_one(".product_info_product_name").text  # 상품 영문명 가져오기
        amount = i.select_one(".amount").text  # 가격 가져오기
        link = i.select_one("a")["href"]  # 상세 페이지 링크 가져오기

        # 리스트에 저장 (카테고리, 브랜드, 한글 상품명, 가격)
        product_list.append(["상의", brand, name_ko, amount])

        print("-------")
        print(rank)  # 상품 순번
        print(f"brand: {brand}")
        print(f"name_en: {name_en}")
        print(f"name_ko: {name_ko}")
        print(f"amount: {amount}")
        print(f"link: {url+link}")
        print("-------")

# ========================================
# **4. MySQL 데이터베이스 연결**
# ========================================

# MySQL 데이터베이스 연결 설정
connection = pymysql.connect(
    host = '127.0.0.1',  # 로컬호스트(내 PC의 데이터베이스 서버) 주소
    user = 'root',  # MySQL 로그인 계정 (root 사용자)
    password = '1234',  # MySQL 로그인 비밀번호
    db = 'kream',  # 사용할 데이터베이스 이름 (kream)
    charset = 'utf8mb4'  # 문자 인코딩 방식 (한글을 지원하는 utf8mb4 사용)
)

# ========================================
# **5. MySQL에 데이터 저장**
# ========================================

# cursor = connection.cursor()  # 데이터베이스와 상호작용할 커서(cursor)를 생성
# cursor.close() # 커서 사용 후 종료해야함

# SQL 쿼리 실행 함수 정의
def exceute_query(connection, query, args=None ) :
    """
    데이터베이스에 SQL 쿼리를 실행하는 함수
    :param connection: MySQL 연결 객체
    :param query: 실행할 SQL 쿼리문 (INSERT, SELECT 등)
    :param args: SQL 쿼리의 파라미터 값 (옵션)
    :return: SELECT 문인 경우 조회 결과 반환, 그 외에는 커밋(commit) 수행
    """
    with connection.cursor() as cursor:  # with 문을 사용하여 자동으로 커서 닫기 (close()해줌)
        cursor.execute(query, args or ()) # 쿼리문을 담아서 데이터베이스 보냄
        
        if query.strip().upper().startswith('select'):  # 만약 SQL 쿼리가 'SELECT' 문으로 시작하면
            return cursor.fetchall() # 접속한 db에 모든 정보를 가져옴  # 모든 결과를 가져와서 반환 (튜플 리스트 형태)
        
        else: # 'SELECT'가 아닌 경우(INSERT, UPDATE, DELETE 등) 변경 사항을 데이터베이스에 반영
            connection.commit()  # 변경 사항 반영

# product_list에 있는 모든 데이터를 items 테이블에 삽입
for i in product_list:
    # 앞에서 정의한 exceute_query 함수를 호출하여 쿼리 실행
    exceute_query (connection, "INSERT INTO items (category, brand, name, price) VALUES (%s, %s, %s, %s)", (i[0], i[1], i[2], i[3]))

# 데이터베이스 연결 종료
connection.close()  # 모든 작업이 끝난 후 데이터베이스 연결을 닫아 리소스 해제