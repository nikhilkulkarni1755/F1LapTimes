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
base_url = "https://ergast.com/api/f1/2023/"

#Austrian Grand Prix is Round 9
#race integer variable
#https://ergast.com/api/f1/2023/9/laps/1
race = 1
laps = "/laps/"
#lapNumber = 1
#response = requests.get(url).text

urls = []
counter = 0
for offset in range(1, 71):
    urls.append(base_url + str(race) + laps + str(offset))
    print(urls[counter])
    counter+=1

for url in urls:
    response = requests.get(url).text
    soup = BeautifulSoup(response, 'xml')
    times = soup.find_all('Timing')
    for data in times:
        #print(data)
        #print(data['driverId'])
        lap = data['lap']
        #print(data['time'])
        f = open("data/" + str(lap) + "race" + str(race) + ".txt", "a")
        print(data['time'])
        f.write(data['time'])
        f.close()
        #print(data['position'])
        #print(data['lap'])
        #print(data['lap'])

#print(len(times))

#for url in urls:

#for data in times:
    #print(data)
    #print(data['driverId'])
#    print(data['time'])
    #print(data['position'])
    #print(data['lap'])
    #print(data['lap'])

#df_laptimes = pd.DataFrame.from_dict(dic_entries)
#df_laptimes