import requests
import re
from bs4 import BeautifulSoup

#https://www.whatismybrowser.com/detect/what-is-my-user-agent/

for i in range(1, 6) : 

    url = "https://www.coupang.com/np/search?rocketAll=false&searchId=8c8b8955abc54f3eb5200ee9b94c651c&q=%EB%85%B8%ED%8A%B8%EB%B6%81&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page={i}&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&searchProductCount=1684303&component=&rating=0&sorter=scoreDesc&listSize=36"
    headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
            , "Accept-Language": "ko-KR,ko;q=0.8,en -US;q=0.5,en;q=0.3"
    }
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    print(res.text)

    items = soup.find_all("dl", attrs={"class":re.compile("^search-product-wrap")})
    print(items[0].find("div", attr={"class":"name"}).get_text())