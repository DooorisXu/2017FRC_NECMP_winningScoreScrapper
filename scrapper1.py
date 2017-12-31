#this code gets the winning score of the each match in the FRC 2017NECMP

#in the terminal
install requests
install bs4
python

#in the python terminal 
from bs4 import BeautifulSoup
import requests

url = "https://www.thebluealliance.com/event/2017necmp"
r = requests.get(url)

BeautifulSoup(r.content)

links = soup.find_all("a")

for link in links:
	print(link.text, link.get("href"))

for link in links.get("href"):
    "<a href='%s'>%s</a>" %(link.get("href"),link.text)

g_data = soup.find_all("span",{"class" : "winner"})
print(g_data)

#returns the content 
for item in g_data:
	print(item.text)

#returns a list
for item in g_data:
	print(item.contents)

#prints the content of each item, if there are more than one element 
for item in g_data:
	print(item.contens[0].text)

