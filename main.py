import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.elnekhelytechnology.com/index.php?search=graphics+Card&submit_search=&route=product%2Fsearch&page=2"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/100.0.4896.88 Safari/537.36 "
}
response = requests.get(url=url, headers=header).text

soup = BeautifulSoup(response, 'html.parser')

items = soup.select("div h4 > a")
prices = soup.find_all("span", class_="price-new")

names = [name.get_text() for name in items]
links = [item["href"] for item in items]
prices = [price.get_text().strip() for price in prices]

data = {
    "Names": names,
    "Links": links,
    "Prices": prices,
}

df = pd.DataFrame(data)
df.to_csv("Data.csv", index=False)