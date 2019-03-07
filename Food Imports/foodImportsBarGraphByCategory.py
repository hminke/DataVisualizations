import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
index = 0
N = 15
ind = np.arange(N)
width = 0.05

years = np.zeros(19)
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

ax.bar(ind - width*1.5, data99, width, picker=1)
ax.bar(ind - width/2, data00, width, picker=1)
ax.bar(ind + width/2, data01, width, picker=1)
ax.bar(ind + width*1.5, data02, width, picker=1)

# category5Plot = ax.bar(years, category5, picker=1, label=category5FoodName,
#                        bottom=category1+category2+category3+category4)
# category6Plot = ax.bar(years, category6, picker=1, label=category6FoodName,
#                        bottom=category1+category2+category3+category4+category5)
# category7Plot = ax.bar(years, category7, picker=1, label=category7FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6)
# category8Plot = ax.bar(years, category8, picker=1, label=category8FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7)
# category9Plot = ax.bar(years, category9, picker=1, label=category9FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8)
# category10Plot = ax.bar(years, category10, picker=1, label=category10FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8+
#                               category9)
# category11Plot = ax.bar(years, category11, picker=1, label=category11FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8+
#                               category9+category10)
# category12Plot = ax.bar(years, category12, picker=1, label=category12FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8+
#                               category9+category10+category11)
# category13Plot = ax.bar(years, category13, picker=1, label=category13FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8+
#                               category9+category10+category11+category12)
# category14Plot = ax.bar(years, category14, picker=1, label=category14FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8+
#                               category9+category10+category11+category12+category13)
# category15Plot = ax.bar(years, category15, picker=1, label=category15FoodName,
#                        bottom=category1+category2+category3+category4+category5+category6+category7+category8+
#                               category9+category10+category11+category12+category13+category14)
plt.ylabel('Price ($) per Million')
plt.title('Food Imports by Category')
#plt.xticks()
#plt.legend(loc='upper left', bbox_to_anchor=(0., 1.1))
plt.show()
