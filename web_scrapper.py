import requests
from bs4 import BeautifulSoup
import os

class WebScrapper():
    def __init__(self, url):
        self.url = url
        self.content =""

    #Method to scrap the site of the give URl
    def scrap_web(self):
        html_content  = requests.get(self.url).text
        soup = BeautifulSoup(html_content , 'html.parser')
        
        #Create a string called content and attach the titlte from the page to it
        self.content = soup.title.text + '\n'
        
        #Attach paragraphs to the content string and break line after each paragraph
        for paragraph in soup.find_all("p"):
            self.content += paragraph.text + '\n'


    #A method that takes the structured content as input and outputs it as a file
    def write_file(self, file_name):
        f = open(file_name, 'w', encoding="utf-8")
        f.write(self.content)

    def delete_file(self, file_name):
        os.remove(file_name)

    def get_content(self):
        return self.content

