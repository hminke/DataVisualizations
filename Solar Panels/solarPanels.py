#!/usr/bin/python
import csv
import matplotlib.pyplot as plt
import numpy as np

N = 16
ind = np.arange(N)
width = 0.5
day = {}
watts = {}
singleDay = {}
dailyWatts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('June2017.csv', 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        day = row['date']
        singleDay = day.split()
        hour = singleDay[1].split(':')
        watts = float(row['watts'])

        if hour[0] == '06':
            dailyWatts[0] = (dailyWatts[0] + watts) / 2.0
        elif hour[0] == '07':
            dailyWatts[1] = (dailyWatts[1] + watts) / 2.0
        elif hour[0] == '08':
            dailyWatts[2] = (dailyWatts[2] + watts) / 2.0
        elif hour[0] == '09':
            dailyWatts[3] = (dailyWatts[3] + watts) / 2.0
        elif hour[0] == '10':
            dailyWatts[4] = (dailyWatts[4] + watts) / 2.0
        elif hour[0] == '11':
            dailyWatts[5] = (dailyWatts[5] + watts) / 2.0
        elif hour[0] == '12':
            dailyWatts[6] = (dailyWatts[6] + watts) / 2.0
        elif hour[0] == '13':
            dailyWatts[7] = (dailyWatts[7] + watts) / 2.0
        elif hour[0] == '14':
            dailyWatts[8] = (dailyWatts[8] + watts) / 2.0
        elif hour[0] == '15':
            dailyWatts[9] = (dailyWatts[9] + watts) / 2.0
        elif hour[0] == '16':
            dailyWatts[10] = (dailyWatts[10] + watts) / 2.0
        elif hour[0] == '17':
            dailyWatts[11] = (dailyWatts[11] + watts) / 2.0
        elif hour[0] == '18':
            dailyWatts[12] = (dailyWatts[12] + watts) / 2.0
        elif hour[1] == '19':
            dailyWatts[13] = (dailyWatts[13] + watts) / 2.0
        elif hour[0] == '20':
            dailyWatts[14] = (dailyWatts[14] + watts) / 2.0

        #print(hour)
#print(dailyWatts)

p1 = plt.bar(ind, dailyWatts, width)

plt.ylabel('Watts')
plt.title('Average Watts Generated each Day')
plt.xticks(ind, ('6\nAM', '7\nAM', '8\nAM', '9\nAM', '10\nAM', '11\nAM',
                 '12\nPM', '1\nPM', '2\nPM', '3\nPM', '4\nPM', '5\nPM',
                 '6\nPM', '7\nPM', '8\nPM', '9\nPM'))
plt.show()
