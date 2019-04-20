import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches
import csv

def getData(fileName):

    years = np.zeros(9)
    data10 = {}
    data11 = {}
    data12 = {}
    data13 = {}
    data14 = {}
    data15 = {}
    data16 = {}
    data17 = {}
    data18 = {}
    percentage10 = {}
    percentage11 = {}
    percentage12 = {}
    percentage13 = {}
    percentage14 = {}
    percentage15 = {}
    percentage16 = {}
    percentage17 = {}
    percentage18 = {}

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
                    data10.setdefault(stateName, int(numOfPeople))
                    percentage10.setdefault(stateName, percentage)
                elif year == '2011':
                    years[1] = 2011
                    data11.setdefault(stateName, int(numOfPeople))
                    percentage11.setdefault(stateName, percentage)
                elif year == '2012':
                    years[2] = 2012
                    data12.setdefault(stateName, int(numOfPeople))
                    percentage12.setdefault(stateName, percentage)
                elif year == '2013':
                    years[3] = 2013
                    data13.setdefault(stateName, int(numOfPeople))
                    percentage13.setdefault(stateName, percentage)
                elif year == '2014':
                    years[4] = 2014
                    data14.setdefault(stateName, int(numOfPeople))
                    percentage14.setdefault(stateName, percentage)
                elif year == '2015':
                    years[5] = 2015
                    data15.setdefault(stateName, int(numOfPeople))
                    percentage15.setdefault(stateName, percentage)
                elif year == '2016':
                    years[6] = 2016
                    data16.setdefault(stateName, int(numOfPeople))
                    percentage16.setdefault(stateName, percentage)
                elif year == '2017':
                    years[7] = 2017
                    data17.setdefault(stateName, int(numOfPeople))
                    percentage17.setdefault(stateName, percentage)
                elif year == '2018':
                    years[8] = 2018
                    data18.setdefault(stateName, int(numOfPeople))
                    percentage18.setdefault(stateName, percentage)

    return stateName, years, data10, percentage10, data11, percentage11, data12, percentage12, data13, percentage13, \
           data14, percentage14, data15, percentage15, data16, percentage16, data17, percentage17, data18, percentage18

def getColor(data):

    c = np.arange(1, 10)
    norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
    cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.Greens)
    cmap.set_array([])

    if data < 1400:
        faceColor = cmap.to_rgba(2)
    elif data < 6001:
        faceColor = cmap.to_rgba(4)
    elif data < 9901:
        faceColor = cmap.to_rgba(6)
    elif data < 13501:
        faceColor = cmap.to_rgba(8)
    else:
        faceColor = cmap.to_rgba(10)

    return faceColor

getData('homelessMap.csv')
