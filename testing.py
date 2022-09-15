from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://naver.com"
browser = webdriver.Chrome()
browser.get(url)

element = browser.find_element(By.CLASS_NAME, 'link_login')

element.click()