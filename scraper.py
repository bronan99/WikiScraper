import requests

s = requests.Session()

loginCred = {"os_username": "mmanko", "os_password":"Cengage1", "login": "Log In", "os_destination": "/dashboard.action"}
loginurl = "http://wiki.cengage.com/login.action?os_destination=%2Fdashboard.action"
glossaryurl = "http://wiki.cengage.com/display/NG/MindTap+Glossary"

resp = s.post(loginurl, data=loginCred)
resp = s.get(glossaryurl)

print((resp.text).encode('utf-8'));

