from web_scrapper import WebScrapper
import argparse

#Main method
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url")
    args = parser.parse_args()
    url = args.url

    #condition looks for command line argument. If not provided, asks user to input a url. 
    if url == None:
        url = input("Enter URl: ")
    
    #Creates WebScrapper instance and calls scrap_web and write_file method
    web_scrapper = WebScrapper(url)
    web_scrapper.scrap_web()
    web_scrapper.write_file('Content')

if __name__ == "__main__":
    main()