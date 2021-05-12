from requests import get
import json
from bs4 import BeautifulSoup as S
url= get("https://www.flipkart.com/search?q=mi%20phones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off ")
req=url.text
soup=S(req,"html.parser")
brand=soup.findAll("div",{"class":"_4rR01T"})
full=soup.findAll("ul",{"class":"_1xgFaf"})
price=soup.findAll("div",{"class":"_30jeq3 _1_WHN1"})
phone=[]
fullinfo=[]
pri=[]
for i,j,k in zip(brand,full,price):
    phone.append(i.text)
    fullinfo.append(j.text)
    pri.append(k.text)
d={}
for i,j,k in zip(phone,fullinfo,pri):
    d[i]=[j,k]
jstr = json.dumps(d, indent=2)
f=open("flipkart.json","w+")
f.write(jstr)
f.close()