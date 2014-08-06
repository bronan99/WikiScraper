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

test_array = []

headers = soup.findAll("h1")
for count in range(1, len(headers)) :
	category = headers[count].span.string.encode('ascii','ignore')
	print(category)
	tabledata = soup.findAll("td", {"class": "confluenceTd"})
	count = 1
	key = ""
	for data in tabledata:
		if count%2 == 0:
			soup1 = data.findAll("p")
			soup2 = data.findAll('span')
			soupList = ""
			for line in soup1:
				if (type(line.span)) == type(None) :
					soupList += line.string.encode('ascii','ignore')
			for line in soup2 :
				soupList += line.string.encode('ascii','ignore')
			test_array.append({'Category': category,'Term': key, 'Definition': soupList});
			key = ""
		else:
			if(type(data.span)) == type(None) :
				key = data.string.encode('ascii','ignore')
			else:
				key = data.span.string.encode('ascii','ignore')
		count +=1

print(test_array)
fieldnames = ['Category', 'Term', 'Definition']
test_file = open('output.csv','wb')
csvwriter = csv.DictWriter(test_file, delimiter=',', fieldnames=fieldnames)
csvwriter.writerow(dict((fn,fn) for fn in fieldnames))
for row in test_array:
     csvwriter.writerow(row)
test_file.close()




#melanie was here
#phil was here
#derek was here
#htmlFile.write(soup.find("td", {"class": "confluenceTd"}).prettify().encode('utf-8'))
