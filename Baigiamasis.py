#Libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd
   
#Webscraping

r = requests.get('https://rrr.lt/naudotos-autodalys/honda/cr-v-1995-2001#parts-1')
bs = BeautifulSoup(r.text, 'html.parser')
results = bs.find_all('div', attrs={'class': 'products_slider__hold'})
records = []

#Database

for result in results:
    url = result.find('a')['href']
    records.append(url)
df = pd.DataFrame(records, columns=['Nuorodos'])
df.to_csv('Naujausios_detales.csv',mode='a', index = False, header=False, sep=',', encoding = 'utf-8')
        
#Duplicate removal        

data = pd.read_csv('Naujausios_detales.csv')
data.drop_duplicates(subset ="Nuorodos", keep = "first", inplace = True)
data.to_csv('Naujausios_detales.csv', index = False)

#Automation

#Automation is done trough windows scheduler




