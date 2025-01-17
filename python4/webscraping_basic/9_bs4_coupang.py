import requests
import re
from bs4 import BeautifulSoup

#https://www.whatismybrowser.com/detect/what-is-my-user-agent/

url = "https://www.coupang.com/np/search?rocketAll=false&searchId=8c8b8955abc54f3eb5200ee9b94c651c&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page=1&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=1684303&component=&rating=0&sorter=scoreDesc&listSize=36"
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
         , "Accept-Language": "ko-KR,ko;q=0.8,en -US;q=0.5,en;q=0.3"
}
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

print(res.text)

items = soup.find_all("dl", attrs={"class":re.compile("^search-product-wrap")})
print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:
    name = item.find("div", attrs={"class":"name"}).get_text()
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rate = item.find("em", attrs = {"class":"rating"}).get_text()
    if rate:
        rate = rate.get_text() 
    else:
        rate ="평점 없음"

    rate_cnt = item.find("span", attrs={"class":"rating-total-count"}).get_text() 

    if rate_cnt:
        rate_cnt = rate_cnt.get_text() 
    else:
        rate_cnt ="평점 수 없음"

    print(name, price, rate, rate_cnt)