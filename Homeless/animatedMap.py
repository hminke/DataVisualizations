import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches
import csv
import matplotlib.animation as animation


c = np.arange(1, 10)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.Reds)
cmap.set_array([])
fig = plt.figure()
ax = plt.axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())
shapeName = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapeName)
animationYear = 2010
animationTitle = ax.text(0.55, 0.95, "", transform=ax.transAxes, ha="center", fontsize=22, fontweight='bold')

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

    return data10, percentage10, data11, percentage11, data12, percentage12, data13, percentage13, data14, percentage14,\
           data15, percentage15, data16, percentage16, data17, percentage17, data18, percentage18

def getColor(data):

    global cmap

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

def init():                     # init function for the animation
    global cmap
    animate = []

    ax.set_extent([-125, -66.5, 20, 50], ccrs.Geodetic())

    for state in shpreader.Reader(states_shp).records():
        edgeColor = 'black'
        animate.append(ax.add_geometries([state.geometry], ccrs.LambertConformal, edgeColor=edgeColor))
    animate.append(animationTitle)
    return animate

def update(data):
    global animationYear
    animate = []
    animationTitle.set_text('Homeless People in the U.S. in {}'.format(animationYear))

    # animationTitle.set_text('Food Imports for {}'.format(animationYear))
    for state in shpreader.Reader(states_shp).records():

        edgeColor = 'black'

        try:
            stateDens = data[state.attributes['name']]
        except:
            stateDens = 0

        color = getColor(stateDens)
        animate.append(ax.add_geometries([state.geometry], ccrs.PlateCarree(), faceColor=color, edgeColor=edgeColor,
                                         label=state))

    animate.append(animationTitle)
    animationYear += 1
    if animationYear > 2018:
        animationYear = 2010

    return animate

def show(fileName):

    data10, percentage10, data11, percentage11, data12, percentage12, data13, percentage13, data14, percentage14,\
    data15, percentage15, data16, percentage16, data17, percentage17, data18, percentage18 = getData(fileName)

    dataSet = [data10, data11, data12, data13, data14, data15, data16, data17, data18]
    FRAME_DELTA = 1500
    range1 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(2))
    range2 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(4))
    range3 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(6))
    range4 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(8))
    range5 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(10))

    labels = ['< 1,400', '2,901 - 6,000', '6,001 - 9,900', '9,901 - 13,500', '> 13,500']

    plt.legend([range1, range2, range3, range4, range5], labels, loc='upper left', fancybox=True,
               bbox_to_anchor=(0, 0.25), fontsize=16)
    ax.outline_patch.set_visible(False)
    ani = animation.FuncAnimation(fig, update, frames=dataSet, init_func=init, interval=FRAME_DELTA, blit=True)
    plt.show()

show('homelessMap.csv')
