from bs4 import BeautifulSoup 
import requests

URL = 'https://news.naver.com/main/ranking/popularDay.naver'

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
# 봇이 아니라고 치팅해야만 언론사에서 제재하지 않음.

res = requests.get(URL, headers = header)
soup = BeautifulSoup(res.text, "html.parser")

rankingnews_boxs = soup.select("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div > div")

for rankingnews_box in rankingnews_boxs:
  rankingnews_name = rankingnews_box.select_one('a > strong').txt
  rankingnews_lists = rankingnews_box.select('ul > li')
  for rankingnews_list in rankingnews_lists:
    rank =  rankingnews_list.select_one('em').txt
    title = rankingnews_list.select_one('div > a').txt
    url =   rankingnews_list.select_one('div > a')['href']
    print(rank, title, url)