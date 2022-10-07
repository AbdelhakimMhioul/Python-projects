import requests
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q=python+programming"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
results = soup.find_all("div", {"class": "ZINbbc"})
links = []

for result in results:
    try:
        link = result.find("a", href=True)
        title = result.find("div", {"class": "vvjwJb"}).get_text()
        description = result.find("div", {"class": "s3v9rd"}).get_text()
        if link != '' and title != '' and description != '':
            links.append({
                "title": title,
                "link": link['href'],
                "description": description
            })
    except:
        continue

for item in links:
    print(item)
