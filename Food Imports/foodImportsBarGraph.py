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

with open("food_imports.csv", 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        foodName = row['Food Type']
        del(row['Food Type'])
        color = np.random.rand(3,)
        for year, dollarAmount in row.items():
            temp = dollarAmount.replace(',', '')
            if len(temp) != 0:
                y[index] = float(temp)
                x[index] = int(year)
                index = index + 1
        if foodName == 'Live meat animals':
            category1 = y
            ax.bar(x, y, picker=1, label=foodName, color='SkyBlue')
        elif foodName == 'Meats':
            ax.bar(x, y, picker=1, label=foodName, color='IndianRed', bottom=category1)
        index = 0

def onpick(event):
    category = event.artist.get_label()
    x = event.artist.get_offsets()
    dollar = int(x.item(0) + 1999)
    print("Category: {},\nYear: {},\n$ Million: {}\n".format(category, dollar, x.item(1)))

plt.xlabel('Year')
plt.ylabel('$ Millions')
plt.xticks(x)
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
