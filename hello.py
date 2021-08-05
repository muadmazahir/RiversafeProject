import pip._vendor.requests as requests

url = input("Enter URl: ")
print(url)


getpage= requests.get(url)

content = str(getpage.text)


f = open('workfile', 'w', encoding="utf-8")
f.write(content)