import requests
import getpass
<<<<<<< HEAD
import urllib2
from bs4 import BeautifulSoup
=======
from bs4 import BeautifulSoup

>>>>>>> FETCH_HEAD
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

htmlFile = open("test.html", "w")
htmlFile.write(toparse)
htmlFile.close()

<<<<<<< HEAD
=======
# setting up beautiful soup 
soup = BeautifulSoup(open("test.html"))
soup.prettify()

#comment

htmlFile = open("test.html", "w")
htmlFile.write(soup.find("div", {"class": "wiki-content"}).prettify().encode('utf-8'))
htmlFile.close()








>>>>>>> FETCH_HEAD

soup = BeautifulSoup("test.html")
print(soup.prettify())
#melanie was here
#phil was here
#derek was here
