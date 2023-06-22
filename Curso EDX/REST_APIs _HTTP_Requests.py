''''
HTTP Protocol

import requests
url='http://www.ibm.com/'
r=requests.get(url)
r.status_code:200
print(r.status_code)
''' #HTTP Protocol
'''
from ibm_watson import SpeechToTextV1
import json
'''#ibm_watso

import requests
from bs4 import BeautifulSoup
page = requests.get(('https://g1.globo.com/?utm_source=globo.com&utm_medium=header')).text
#Creates a BeautifulSoup object
soup = BeautifulSoup(page,'html.perser')

#Pulls all instances of <a> tag
artists = soup.find_all('a')

#Clears data of all tags
for artist in artists:
    names=artist.contents[0]
    fulllink = artist.get('href')
    print(names)
    print(fulllink)