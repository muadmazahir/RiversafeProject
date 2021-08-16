from flask import Flask, render_template, request, abort
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/",  methods=["GET", "POST"])
def welcome():
    if request.method == "POST":
        #Getting url from user input
        url = request.form['url']

        #Calling scrap_web() to scrab the site. It returns the content of the site.
        content = scrap_web(url)

        #we check if content was scraped successfully 
        if (content):
            # Calling the write_file() to write the contents of the site to a file. 
            # We pass as parameters a file name, which we have hard coded for now, and the contents that was previously scraped.
            write_file("SiteData", content)

            #returns the welcome page and passes the url as data.
            return render_template( 
            "welcome.html",
            url = url,
            content = content)
        else:
            #returns the welcome page and passes an error message as data.
            return render_template( 
            "welcome.html",
            error_message = "Invalid URL")

       
    else:
        return render_template( "welcome.html")



#Method to scrap the site of the give URl
def scrap_web(url):
    try:
        html_content  = requests.get(url).text
        soup = BeautifulSoup(html_content , 'html.parser')
        
        #Create a string called content and attach the title from the page to it
        content = soup.title.text + '\n'
        
        #Attach paragraphs to the content string and break line after each paragraph
        for paragraph in soup.find_all("p"):
            content += paragraph.text + '\n'

        return content
    except:
        return False



#A method that takes the structured content as input and outputs it as a file
def write_file(file_name, content):
    try:
        f = open(file_name, 'w', encoding="utf-8")
        f.write(content)
    except:
        abort(404)


if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')