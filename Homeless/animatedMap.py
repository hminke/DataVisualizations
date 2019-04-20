import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches
import csv

def getData(fileName):

    years = np.zeros(9)
    data10 = np.zeros(50)
    data11 = np.zeros(50)
    data12 = np.zeros(50)
    data13 = np.zeros(50)
    data14 = np.zeros(50)
    data15 = np.zeros(50)
    data16 = np.zeros(50)
    data17 = np.zeros(50)
    data18 = np.zeros(50)
    percentage10 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage11 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage12 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage13 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage14 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage15 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage16 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage17 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
    percentage18 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '',
                    '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

    with open(fileName, 'r') as fil:
        data = csv.DictReader(fil, delimiter=',')
        i = 0

        for row in data:
            stateName = row['State']
            del (row['State'])
            for year, people in row.items():
                temp = people.split(' ')
                numOfPeople = temp[0]
                percentage = temp[1]
                if year == '2010':
                    years[0] = 2010
                    data10[i] = int(numOfPeople)
                    percentage10[i] = percentage
                elif year == '2011':
                    years[1] = 2011
                    data11[i] = int(numOfPeople)
                    percentage11[i] = percentage
                elif year == '2012':
                    years[2] = 2012
                    data12[i] = int(numOfPeople)
                    percentage12[i] = percentage
                elif year == '2013':
                    years[3] = 2013
                    data13[i] = int(numOfPeople)
                    percentage13[i] = percentage
                elif year == '2014':
                    years[4] = 2014
                    data14[i] = int(numOfPeople)
                    percentage14[i] = percentage
                elif year == '2015':
                    years[5] = 2015
                    data15[i] = int(numOfPeople)
                    percentage15[i] = percentage
                elif year == '2016':
                    years[6] = 2016
                    data16[i] = int(numOfPeople)
                    percentage16[i] = percentage
                elif year == '2017':
                    years[7] = 2017
                    data17[i] = int(numOfPeople)
                    percentage17[i] = percentage
                elif year == '2018':
                    years[8] = 2018
                    data18[i] = int(numOfPeople)
                    percentage18[i] = percentage
            i += 1

    return stateName, years, data10, percentage10, data11, percentage11, data12, percentage12, data13, percentage13, \
           data14, percentage14, data15, percentage15, data16, percentage16, data17, percentage17, data18, percentage18

getData('homelessMap.csv')
