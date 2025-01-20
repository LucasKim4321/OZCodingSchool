from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
ChromeDriverManager().install()

browser = webdriver.Chrome