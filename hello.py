import requests
from bs4 import BeautifulSoup

url = input("Enter URl: ")

getpage= requests.get(url)

getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

content = str(getpage_soup.prettify())


f = open('workfile2', 'w', encoding="utf-8")
f.write(content)