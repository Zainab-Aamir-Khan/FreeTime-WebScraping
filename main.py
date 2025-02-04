from bs4 import BeautifulSoup
import lxml
import requests

url = requests.get("https://toscrape.com/").text
soup = BeautifulSoup(url, 'lxml')
# print(requests.get("https://toscrape.com/").status_code)

print("lets get the Book and Quote detail of a website!!!")

main = soup.find('body')
print(main.prettify())


# bookInfo =  main.find_all('div', class_ ='col-md-10')
# print(bookInfo)


