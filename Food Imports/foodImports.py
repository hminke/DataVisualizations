import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()

with open("food_imports.csv", 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        foodName = row['Food Type']
        del(row['Food Type'])
        color = np.random.rand(3,)
        for year, dollarAmount in row.items():
            temp = dollarAmount.replace(',', '')
            if len(temp) != 0:
                dollarAmount = float(temp)
                ax.scatter(year, dollarAmount, color=color, picker=1, label=foodName)

def onpick(event):
    category = event.artist.get_label()
    x = event.artist.get_offsets()
    dollar = int(x.item(0) + 1999)
    print("Category: {},\nYear: {},\n$ Million: {}\n".format(category, dollar, x.item(1)))

plt.xlabel('Year')
plt.ylabel('$ Millions')
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
