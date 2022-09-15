
import sys
from selenium import webdriver

import requests
from bs4 import BeautifulSoup
# Current Kospi crawling
url = "https://finance.naver.com/sise/sise_index.naver?code=KOSPI"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
res = requests.get(url, headers=head)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# find Kospi rate from the web
stock_change = soup.select("div.quotient")
stock_value = soup.find(id= "now_value")
kospi = stock_value.string

print("Current Status of KOSPI: ", kospi)



