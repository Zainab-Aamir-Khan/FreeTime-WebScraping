from bs4 import BeautifulSoup
import lxml
import requests

url = requests.get("https://toscrape.com/").text
soup = BeautifulSoup(url, 'lxml')
print(requests.get("https://toscrape.com/").status_code)
