import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.amazon.in/s?k=iphone&crid=V25FRP97E1B5&sprefix=iphone%2Caps%2C224&ref=nb_sb_noss_2"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())

data = {
    "Names": [],
    "Prices": []
}

spans = soup.find_all(class_="a-size-medium a-color-base a-text-normal")
for span in spans:
    names = span.get_text()
    data["Names"].append(names)

spans2 = soup.find_all(class_="a-price-whole")
for span in spans2:
    prices = span.get_text()
    data["Prices"].append(prices)

df = pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)