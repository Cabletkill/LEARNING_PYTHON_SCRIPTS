from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page
'''
html="<table><tr><td>Pizza Place </td><td>Orders</td><td>Slices</td></tr><tr><td>Domino'sPizza</td><td>10</td><td>100</td><tr/><tr><td>Litle Caesars</td><td>12</td><td>144</td></tables>"
table=BeautifulSoup(html,'html5lib')
table_row=table.find_all(name='tr' )

print(table_row)
x=int(input('Digite a pesquisa:'))
first_row = table_row[x]
print(first_row)
print(first_row.td)
'''

page = requests.get(('')).text
#Creates a BeautifulSoup object
soup = BeautifulSoup(page,'https://www.metropoles.com/colunas/entre-eixos/preco-dos-carros-dispara-inflacao-falta-de-insumos-lucro-de-acionistas')
#Pulls all instances of <a> tag
artists = soup.find_all('a')
#Clears data of all tags
for artist in artists:
    names=artist.contents[0]
    fulllink = artist.get('href')
    print(names)
    print(fulllink)