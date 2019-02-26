import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
y = np.zeros(19)
x = np.zeros(19)
index = 0
N = 19
ind = np.arange(N)
width = 0.5
global category1
global category1FoodName
global category2
global category2FoodName
global category3
global category3FoodName
global category4
global category4FoodName
global category5
global category5FoodName

with open("food_imports.csv", 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        foodName = row['Food Type']
        del(row['Food Type'])
        for year, dollarAmount in row.items():
            temp = dollarAmount.replace(',', '')
            if len(temp) != 0:
                y[index] = float(temp)
                x[index] = int(year)
                index = index + 1
        if foodName == 'Live meat animals':
            category1 = y
            category1FoodName = foodName
        elif foodName == 'Meats':
            category2 = y
            category2FoodName = foodName
        elif foodName == 'Fish and shellfish 2/':
            category3 = y
            category3FoodName = foodName
        elif foodName == 'Dairy':
            category4 = y
            category4FoodName = foodName
        elif foodName == 'Vegetables':
            category5 = y
            category5FoodName = foodName
        index = 0

def onpick(event):
    category = event.artist.get_label()
    x = event.artist.get_offsets()
    dollar = int(x.item(0) + 1999)
    print("Category: {},\nYear: {},\n$ Million: {}\n".format(category, dollar, x.item(1)))

category1Plot = ax.bar(x, category1, picker=1, label=category1FoodName)
category2Plot = ax.bar(x, category2, picker=1, label=category2FoodName, bottom=category1)
category3Plot = ax.bar(x, category3, picker=1, label=category3FoodName, bottom=category1+category2)
category4Plot = ax.bar(x, category4, picker=1, label=category4FoodName, bottom=category1+category2+category3)
category5Plot = ax.bar(x, category5, picker=1, label=category5FoodName,
                       bottom=category1+category2+category3+category4)

plt.xlabel('Year')
plt.ylabel('$ Millions')
plt.xticks(x)
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
