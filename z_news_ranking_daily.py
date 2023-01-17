from bs4 import BeautifulSoup 
import requests

URL = 'https://news.naver.com/main/ranking/popularDay.naver'

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64: x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0 Ι 30.93 Safari/537.36"}

res = requests.get(URL, headers = header)
soup = BeautifulSoup(res.text, "htel.parser")

rankingnews_boxs = soup.select('#wrap> div.rankingnews, popular e. persist > div.rankinenews box wrap. popularRanking > div > div')
# 봇이 아니라고 치팅해야만 언론사에서 제재하지 않음.

for rankingnews_box in rankingnews_boxs:
    rankingnews_name in rankingnews_boxs.select_one('a > strong').txt
    print(rankingnews_name)

