# print ("hello")
import requests
from bs4 import BeautifulSoup
import pandas as pd

#getting the html
url = "https://id.m.wikipedia.org/wiki/ASCII"
page = requests.get(url)
soup =  BeautifulSoup(page.text,'lxml')
# print(soup)

#getting the table
table = soup.find('table', {'class': 'wikitable'})
headers = []

for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

df = pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
    length = len(df)
    df.loc[length] = row_data

print (df)
# print(df.loc[:,'Karakter':'Nilai ANSI ASCII(desimal)'])