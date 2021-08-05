import argparse
from bs4 import BeautifulSoup

import requests


parser = argparse.ArgumentParser()

parser.add_argument("--url")

args = parser.parse_args()
url = args.url

getpage= requests.get(url)

getpage_soup= BeautifulSoup(getpage.text, 'html.parser')

content = str(getpage_soup.prettify())


f = open('CommandlineExample', 'w', encoding="utf-8")
f.write(content)