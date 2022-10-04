import requests
from bs4 import BeautifulSoup
url="https://unsplash.com"

# parse the html content on home page of unsplash
r=requests.get(url)
htmlContent=r.content
soup=BeautifulSoup(htmlContent,'html.parser')

# get links for all categories in unsplash
anchors=soup.find_all("a",class_="p7ajO")

categories=[]
for link in anchors:
    categories.append(url+link.get('href'))

# delete unwanted hyperlinks
del categories[0]
del categories[0]

# request to extract image links from every category
db=[]
for cat in categories:
    req=requests.get(cat)
    content=req.content
    sp=BeautifulSoup(content,'html.parser')
    imgLinks=sp.find_all("img",class_="YVj9w")
    imgLinksList=[]
    for links in imgLinks:
        temp=links.get('src')
        imgLinksList.append(temp.split("?")[0])
    db.append(imgLinksList)
    
#Printing all the image links

for cat in db:
    for c in cat:
        print(c)
    print("\n")
