import requests
import getpass
from bs4 import BeautifulSoup

s = requests.Session()

usernameInput = raw_input("Enter Confluence username:")
passwordInput = getpass.getpass("Enter password:")

loginCred = {"os_username": usernameInput, "os_password": passwordInput, "login": "Log In", "os_destination": "/dashboard.action"}
loginurl = "http://wiki.cengage.com/login.action?os_destination=%2Fdashboard.action"
glossaryurl = "http://wiki.cengage.com/display/NG/MindTap+Glossary"

# login to comfluence using loginCred
resp = s.post(loginurl, data=loginCred)

# store the response of getting the glossary url
resp = s.get(glossaryurl)

# store html as string
toparse = resp.text.encode('utf-8')

htmlFile = open("test.html", "w")
htmlFile.write(toparse)
htmlFile.close()

# setting up beautiful soup 
soup = BeautifulSoup(open("test.html"))
soup.prettify()

print(soup.find("div", {"class": "wiki-content"}).prettify())







