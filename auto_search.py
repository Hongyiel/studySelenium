from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "http://naver.com"
browser = webdriver.Chrome()
browser.get(url)

element = browser.find_element(By.ID, 'query')

element.send_keys("라인")
element.send_keys(Keys.ENTER)