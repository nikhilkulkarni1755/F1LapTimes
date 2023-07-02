#Authors: Sameer Kulkarni, Shrikrishna Kulkarni and Nikhil Kulkarni

import pandas as pd
import matplotlib.pyplot as plt
import requests
from lxml.html.soupparser import fromstring
from bs4 import BeautifulSoup

print("Does lap time decrease as the race goes on?")

#data source: https://ergast.com/api/f1/2023/last/laps/6

#lap and lap time relation

#x axis lap

#y axis lap time

url = "https://ergast.com/api/f1/2023/last/laps/1"
response = requests.get(url).text

soup = BeautifulSoup(response, 'xml')

times = soup.find_all('Timing')
#print(len(times))

for data in times:
    #print(data)
    #print(data['driverId'])
    print(data['time'])
    #print(data['position'])
    #print(data['lap'])
    #print(data['lap'])

#df_laptimes = pd.DataFrame.from_dict(dic_entries)
#df_laptimes