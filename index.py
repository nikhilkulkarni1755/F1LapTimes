#Authors: Sameer Kulkarni, Shrikrishna Kulkarni and Nikhil Kulkarni

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
import requests
from lxml.html.soupparser import fromstring
from bs4 import BeautifulSoup

print("Does lap time decrease as the race goes on?")

# 
url = "https://ergast.com/api/f1/2023/last/laps/1"
base_url = "https://ergast.com/api/f1/2023/"

race = 1
laps = "/laps/"

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
    counter = 0
    for data in times:
        lap = data['lap']

        filename = "race1data/" + str(lap) + "race" + str(race) + ".txt" 
        f = open(filename, "w")
        f.write(data['time'])
        f.close()

times = []

# What are we trying to predict using tf linear regressions?
# we need to analyze what data points we can use to make points
# some different measurable things we can use
# lap time, lap, pit stop (number of stops or avg time taken), qualifying times
