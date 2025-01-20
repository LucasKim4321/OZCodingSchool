from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
ChromeDriverManager().install()

# path 에러 생길 시
# 1. 상대경로 설정
# path = './chromedriver'

#2. 절대경로 설정
# import os
# path = os.getcwd() + '/chromedriver'

browser = webdriver.Chrome

browser.back() # 뒤로가기
browser.forward() # 앞으로가기
browser.refresh() # 새로고침