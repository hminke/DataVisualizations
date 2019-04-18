import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Rectangle

FRAME_DELTA = 500       # milliseconds
animationYear = 1999
fig, ax, = plt.subplots()
animationTitle = ax.text(0.5, 0.85, "", transform=ax.transAxes, ha="center")
index = 0
N = 15
ind = np.arange(N)
width = 0.75
animate01 = Rectangle((-.35, 0), width, 0)
animate02 = Rectangle((.65, 0), width, 0)
animate03 = Rectangle((1.65, 0), width, 0)
animate04 = Rectangle((2.65, 0), width, 0)
animate05 = Rectangle((3.65, 0), width, 0)
animate06 = Rectangle((4.65, 0), width, 0)
animate07 = Rectangle((5.65, 0), width, 0)
animate08 = Rectangle((6.65, 0), width, 0)
animate09 = Rectangle((7.65, 0), width, 0)
animate10 = Rectangle((8.65, 0), width, 0)
animate11 = Rectangle((9.65, 0), width, 0)
animate12 = Rectangle((10.65, 0), width, 0)
animate13 = Rectangle((11.65, 0), width, 0)
animate14 = Rectangle((12.65, 0), width, 0)
animate15 = Rectangle((13.65, 0), width, 0)
years = np.zeros(19)
foodName = []
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
    animate01.set_height(0)
    animate02.set_height(0)
    animate03.set_height(0)
    animate04.set_height(0)
    animate05.set_height(0)
    animate06.set_height(0)
    animate07.set_height(0)
    animate08.set_height(0)
    animate09.set_height(0)
    animate10.set_height(0)
    animate11.set_height(0)
    animate12.set_height(0)
    animate13.set_height(0)
    animate14.set_height(0)
    animate15.set_height(0)

    ax.add_patch(animate01)
    ax.add_patch(animate02)
    ax.add_patch(animate03)
    ax.add_patch(animate04)
    ax.add_patch(animate05)
    ax.add_patch(animate06)
    ax.add_patch(animate07)
    ax.add_patch(animate08)
    ax.add_patch(animate09)
    ax.add_patch(animate10)
    ax.add_patch(animate11)
    ax.add_patch(animate12)
    ax.add_patch(animate13)
    ax.add_patch(animate14)
    ax.add_patch(animate15)

    return animationTitle, animate01, animate02, animate03, animate04, animate05, animate06, animate07, animate08, \
           animate09, animate10, animate11, animate12, animate13, animate14, animate15

def update(price):
    global animationYear
    animationTitle.set_text('Food Imports for {}'.format(animationYear))
    animate01.set_height(price[0])
    animate02.set_height(price[1])
    animate03.set_height(price[2])
    animate04.set_height(price[3])
    animate05.set_height(price[4])
    animate06.set_height(price[5])
    animate07.set_height(price[6])
    animate08.set_height(price[7])
    animate09.set_height(price[8])
    animate10.set_height(price[9])
    animate11.set_height(price[10])
    animate12.set_height(price[11])
    animate13.set_height(price[12])
    animate14.set_height(price[13])
    animate15.set_height(price[14])

    animationYear += 1
    if animationYear > 2017:
        animationYear = 1999
    return animationTitle, animate01, animate02, animate03, animate04, animate05, animate06, animate07, animate08, \
           animate09, animate10, animate11, animate12, animate13, animate14, animate15

ax.set_ylabel('Price ($) in Millions')
ax.set_xticks(ind)
ax.set_xticklabels(('Live\nmeat\nanimals', 'Meats', 'Fish\nand\nshellfish', 'Dairy', 'Vegies', 'Fruits', 'Nuts',
                    'Coffee,\ntea, and\nspices', 'Grains', 'Veg.\noils', 'Sugar\nand\ncandy',
                    'Cocoa\nand\nchoc.', 'Other\nedible\nprod.', 'Bev.', '  Liquors'))
ani = animation.FuncAnimation(fig, update, frames=dataSet, init_func=init, interval=FRAME_DELTA, blit=True)
plt.show()
