import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
msg = ax.annotate('Click points for annotation', xy=(0, 0), xytext=(2, 20000))

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
    global msg
    category = event.artist.get_label()
    x = event.artist.get_offsets()
    dollar = int(x.item(0) + 1999)
    msg.remove()
    msg = ax.annotate("Category: {},\nYear: {},\n$ Million: {}\n".format(category, dollar, x.item(1)),
                      xy=(0, 0), xytext=(2, 18000))

plt.xlabel('Year')
plt.ylabel('$ Millions')
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
