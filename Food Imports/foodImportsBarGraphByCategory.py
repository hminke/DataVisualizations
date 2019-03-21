import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
index = 0
N = 15
ind = np.arange(N)
width = 0.04
msg = ax.annotate('Click bars for annotation', xy=(0, 0), xytext=(6, 20000))

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

def onpick(event):
    global msg
    amount = event.artist.get_height()
    if amount in data99:
        dataYear = 1999
        a = np.where(data99 == amount)[0]
        print(a[0])
        foodType = foodName[a[0]]
    elif amount in data00:
        dataYear = 2000
        a = np.where(data00 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data01:
        dataYear = 2001
        a = np.where(data01 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data02:
        dataYear = 2002
        a = np.where(data02 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data03:
        dataYear = 2003
        a = np.where(data03 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data04:
        dataYear = 2004
        a = np.where(data04 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data05:
        dataYear = 2005
        a = np.where(data05 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data06:
        dataYear = 2006
        a = np.where(data06 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data07:
        dataYear = 2007
        a = np.where(data07 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data08:
        dataYear = 2008
        a = np.where(data08 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data09:
        dataYear = 2009
        a = np.where(data09 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data10:
        dataYear = 2010
        a = np.where(data10 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data11:
        dataYear = 2011
        a = np.where(data11 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data12:
        dataYear = 2012
        a = np.where(data12 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data13:
        dataYear = 2013
        a = np.where(data13 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data14:
        dataYear = 2014
        a = np.where(data14 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data15:
        dataYear = 2015
        a = np.where(data15 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data16:
        dataYear = 2016
        a = np.where(data16 == amount)[0]
        foodType = foodName[a[0]]
    elif amount in data17:
        dataYear = 2017
        a = np.where(data17 == amount)[0]
        foodType = foodName[a[0]]
    msg.remove()
    msg = ax.annotate("Category: {},\nYear: {},\nPrice ($) in Millions: {}\n".format(foodType, dataYear, amount),
                      xy=(0, 0), xytext=(6, 18000))
    plt.show()

year99 = ax.bar(ind - width*9.5, data99, width, picker=1)
year00 = ax.bar(ind - width*8.5, data00, width, picker=1)
year01 = ax.bar(ind - width*7.5, data01, width, picker=1)
year02 = ax.bar(ind - width*6.5, data02, width, picker=1)
year03 = ax.bar(ind - width*5.5, data03, width, picker=1)
year04 = ax.bar(ind - width*4.5, data04, width, picker=1)
year05 = ax.bar(ind - width*3.5, data05, width, picker=1)
year06 = ax.bar(ind - width*2.5, data06, width, picker=1)
year07 = ax.bar(ind - width*1.5, data07, width, picker=1)
year08 = ax.bar(ind - width/2, data08, width, picker=1)
year09 = ax.bar(ind + width/2, data09, width, picker=1)
year10 = ax.bar(ind + width*1.5, data10, width, picker=1)
year11 = ax.bar(ind + width*2.5, data11, width, picker=1)
year12 = ax.bar(ind + width*3.5, data12, width, picker=1)
year13 = ax.bar(ind + width*4.5, data13, width, picker=1)
year14 = ax.bar(ind + width*5.5, data14, width, picker=1)
year15 = ax.bar(ind + width*6.5, data15, width, picker=1)
year16 = ax.bar(ind + width*7.5, data16, width, picker=1)
year17 = ax.bar(ind + width*8.5, data17, width, picker=1)

ax.set_ylabel('Price ($) in Millions')
ax.set_title('Food Imports by Category from 1999 - 2017')
ax.set_xticks(ind)
ax.set_xticklabels(('Live\nmeat\nanimals', 'Meats', 'Fish\nand\nshellfish', 'Dairy', 'Vegies', 'Fruits', 'Nuts',
                    'Coffee,\ntea, and\nspices', 'Grains', 'Veg.\noils', 'Sugar\nand\ncandy',
                    'Cocoa\nand\nchoc.', 'Other\nedible\nprod.', 'Bev.', '  Liquors'))
ax.legend((year99, year00, year01, year02, year03, year04, year05, year06, year07, year08, year09, year10, year11,
           year12, year13, year14, year15, year16, year17), ('1999', '2000', '2001', '2002', '2003', '2004', '2005',
                                                             '2006', '2007', '2008', '2009', '2010', '2011', '2012',
                                                             '2013', '2014', '2015', '2016', '2017'))
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
