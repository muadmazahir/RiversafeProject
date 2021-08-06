import requests
from bs4 import BeautifulSoup
import argparse

def ScrapWeb(url):
    getpage= requests.get(url).text
    getpage_soup= BeautifulSoup(getpage, 'html.parser')
    
    content = getpage_soup.title.text + '\n'

    for paragraph in getpage_soup.find_all("p"):
        content += paragraph.text + '\n'
        
    return content

def UserInput():
    url = input("Enter URl: ")
    content = ScrapWeb(url)

    f = open('UserInputExample', 'w', encoding="utf-8")
    f.write(content)

def CommandLineInput(url):
    content = ScrapWeb(url)

    f = open('CommandlineExample', 'w', encoding="utf-8")
    f.write(content)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    args = parser.parse_args()
    url = args.url

    if url == None:
        UserInput()
    else:
        CommandLineInput(url)

if __name__ == "__main__":
    main()