import requests
from bs4 import BeautifulSoup

base = "https://www.elev8con.com/speakers/"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
page = requests.get("https://www.elev8con.com/speakers", allow_redirects=True, headers=headers)
page.raise_for_status()
print(page.status_code)

if (page.status_code==200):
    soup = BeautifulSoup(page.content, 'html.parser',).findAll('h4')

else:
    print("Page not found")

name=[]
for s in soup:
    name.append(s.text)

for x in name:
    file = open("Elev8con.txt", "a", encoding="utf-8")
    file.write(x+'\n')
    file.close()