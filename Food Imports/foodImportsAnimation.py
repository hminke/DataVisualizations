import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

FRAME_DELTA = 700       # milliseconds
animationYear = 1999
fig, ax, = plt.subplots()
# animationTitle = ax.text(0.5, 0.85, "", transform=ax.transAxes, ha="center")
index = 0
N = 15
ind = np.arange(N)
width = 0.75
animate = plt.bar(ind, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], width)
years = np.zeros(19)
dataYear = 0
category = ''
foodName = []
plotCategory = []
data99 = np.zeros(15)
data00 = np.zeros(15)
data01 = np.zeros(15)
data02 = np.zeros(15)
data03 = np.zeros(15)
data04 = np.zeros(15)
data05 = np.zeros(15)
data06 = np.zeros(15)
data07 = np.zeros(15)
data08 = np.zeros(15)
data09 = np.zeros(15)
data10 = np.zeros(15)
data11 = np.zeros(15)
data12 = np.zeros(15)
data13 = np.zeros(15)
data14 = np.zeros(15)
data15 = np.zeros(15)
data16 = np.zeros(15)
data17 = np.zeros(15)

with open("food_imports.csv", 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        foodName.append(row['Food Type'])
        del(row['Food Type'])
        for year, dollarAmount in row.items():
            temp = dollarAmount.replace(',', '')
            if len(temp) != 0:
                if year == '1999':
                    data99[index] = temp
                    years[0] = year
                elif year == '2000':
                    data00[index] = temp
                    years[1] = year
                elif year == '2001':
                    data01[index] = temp
                    years[2] = year
                elif year == '2002':
                    data02[index] = temp
                    years[3] = year
                elif year == '2003':
                    data03[index] = temp
                    years[4] = year
                elif year == '2004':
                    data04[index] = temp
                    years[5] = year
                elif year == '2005':
                    data05[index] = temp
                    years[6] = year
                elif year == '2006':
                    data06[index] = temp
                    years[7] = year
                elif year == '2007':
                    data07[index] = temp
                    years[8] = year
                elif year == '2008':
                    data08[index] = temp
                    years[9] = year
                elif year == '2009':
                    data09[index] = temp
                    years[10] = year
                elif year == '2010':
                    data10[index] = temp
                    years[11] = year
                elif year == '2011':
                    data11[index] = temp
                    years[12] = year
                elif year == '2012':
                    data12[index] = temp
                    years[13] = year
                elif year == '2013':
                    data13[index] = temp
                    years[14] = year
                elif year == '2014':
                    data14[index] = temp
                    years[15] = year
                elif year == '2015':
                    data15[index] = temp
                    years[16] = year
                elif year == '2016':
                    data16[index] = temp
                    years[17] = year
                elif year == '2017':
                    data17[index] = temp
                    years[18] = year
        index = index + 1

dataSet = [data99, data00, data01, data02, data03, data04, data05, data06, data07, data08, data09, data10, data11,
           data12, data13, data14, data15, data16, data17]

def init():                     # init function for the animation
    ax.set_xlim(-1, 15)
    ax.set_ylim(0.0, 25000)
    return animate

def update(price):
    global animate
    global animationYear
    # animationTitle.set_text('Food Imports for {}'.format(animationYear))
    animate = ax.bar(ind, price, width)
    # plt.draw()
    animationYear = animationYear + 1
    if animationYear > 2017:
        animationYear = 1999
    return animate

ax.set_ylabel('Price ($) in Millions')
ax.set_xticks(ind)
ax.set_xticklabels(('Live\nmeat\nanimals', 'Meats', 'Fish\nand\nshellfish', 'Dairy', 'Vegies', 'Fruits', 'Nuts',
                    'Coffee,\ntea, and\nspices', 'Grains', 'Veg.\noils', 'Sugar\nand\ncandy',
                    'Cocoa\nand\nchoc.', 'Other\nedible\nprod.', 'Bev.', '  Liquors'))
ax.set_title('Food Imports from 1999 - 2017')

ani = animation.FuncAnimation(fig, update, frames=dataSet, init_func=init, interval=FRAME_DELTA, blit=True)
plt.show()
