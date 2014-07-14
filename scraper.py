import requests
import getpass
from bs4 import BeautifulSoup

s = requests.Session()

usernameInput = raw_input("Enter Confluence username:")
passwordInput = getpass.getpass("Enter password:")

loginCred = {"os_username": usernameInput, "os_password": passwordInput, "login": "Log In", 
             "os_destination": "/dashboard.action"}
loginurl = "http://wiki.cengage.com/login.action?os_destination=%2Fdashboard.action"
glossaryurl = "http://wiki.cengage.com/display/NG/MindTap+Glossary"

# login to comfluence using loginCred
resp = s.post(loginurl, data=loginCred)

# store the response of getting the glossary url
resp = s.get(glossaryurl)

# store html as string
toparse = resp.text.encode('utf-8')

htmlFile = open("glossary.html", "w")
htmlFile.write(toparse)
htmlFile.close()


# setting up beautiful soup 
soup = BeautifulSoup(open("glossary.html"))
soup.prettify()

htmlFile = open("glossary.html", "w")
htmlFile.write(soup.find("div", {"class": "wiki-content"}).prettify().encode('utf-8'))
htmlFile.close()

tabledata = soup.findAll("td", {"class": "confluenceTd"})

count = 1
d = {}
key = ""

for data in tabledata:
	if count%2 == 0:
		soup1 = data.findAll("span")
		soupList = []
			for line in soup1 :
			soupList += line
		d[key] = soupList
		key = ""
	else:
		key = data.span.string
	count +=1

print(d)	

#melanie was here
#phil was here
#derek was here
#htmlFile.write(soup.find("td", {"class": "confluenceTd"}).prettify().encode('utf-8'))

