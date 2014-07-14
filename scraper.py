import requests
import getpass
import csv
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

tabledata = soup.findAll("td", {"class": "confluenceTd"})

# create a dictionary from tabledata of glossary terms/definitions
count = 1
d = {}
key = ""

for data in tabledata:
	if count%2 == 0:
		soup1 = data.findAll("span")
		soupList = ""
		for line in soup1:
			soupList += line.string.encode('ascii', 'ignore')
		d[key] = soupList
		key = ""
	else:
		key = data.span.string
	count +=1

print(d)

# write dictionary to csv 
with open('output.csv','wb') as f:
    w = csv.writer(f)
    w.writerows(d.items())	

#melanie was here
#phil was here
#derek was here
#htmlFile.write(soup.find("td", {"class": "confluenceTd"}).prettify().encode('utf-8'))

