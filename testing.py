import sys
from selenium import webdriver

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=748105&weekday=thu"
head = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}
res = requests.get(url, headers=head)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

cartoons = soup.find_all("td", attrs={"class": "title"})
ratings = soup.find_all("div", attrs={"class": "rating_type"})

avg = 0

for cartoon, rating in zip(cartoons, ratings):
    title = cartoon.a.string
    link = "https://comic.naver.com" + cartoon.a["href"]
    rate = rating.strong.string

    avg += float(rate)

    print(title, link, rate)

print("평점 평균 : {:.2f}".format(avg/len(cartoons)))