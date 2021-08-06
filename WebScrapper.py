import requests
from bs4 import BeautifulSoup
import argparse

#Method to scrap the site of the give URl
def ScrapWeb(url):
    getpage= requests.get(url).text
    getpage_soup= BeautifulSoup(getpage, 'html.parser')
    
    #Create a string called content and attach the titlte from the page to it
    content = getpage_soup.title.text + '\n'
    
    #Attach paragraphs to the content string and break line after each paragraph
    for paragraph in getpage_soup.find_all("p"):
        content += paragraph.text + '\n'

    return content


#User Input method. Used if command line argument is not provided.
def UserInput():
    url = input("Enter URl: ")
    content = ScrapWeb(url)

    f = open('UserInputExample', 'w', encoding="utf-8")
    f.write(content)


#command line argument method. Used if command line argument is provided.
def CommandLineInput(url):
    content = ScrapWeb(url)

    f = open('CommandlineExample', 'w', encoding="utf-8")
    f.write(content)


#Main method
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    args = parser.parse_args()
    url = args.url

    #condition looks for command line argument. If provided calls the command line argument method. If not uses the user input method
    if url == None:
        UserInput()
    else:
        CommandLineInput(url)

if __name__ == "__main__":
    main()