import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

Start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(Start_url)
#print(page)

soup = bs(page.text,'html.parser')

star_table = soup.find('table')
temp_list = []
table_rows = star_table.find_all('tr')
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    temp_list.append(row)
print(temp_list)

star_name = []
distance = []
radius = []
mass = []
luminosity = []

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    luminosity.append(temp_list[i][7])

df = pd.DataFrame(list(zip(star_name, distance, mass, radius, luminosity)),
columns = ['Star_name', 'Distance', 'Mass', 'Radius', 'Luminosity'])
print(df.head())

df.to_csv('Bright_stars.csv')