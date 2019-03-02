import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
msg = ax.annotate('Click points for annotation', xy=(0, 0), xytext=(10, 20000))
legendInfo = [None] * 15
category = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
dollar = 0
index = 0

with open("food_imports.csv", 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        foodName = row['Food Type']
        del(row['Food Type'])
        color = np.random.rand(3,)
        for year, dollarAmount in row.items():
            temp = dollarAmount.replace(',', '')
            if len(temp) != 0:
                dollar = float(temp)
                if year == '1999':
                    legendInfo[index] = ax.scatter(year, dollar, color=color, picker=1, label=foodName)
                    category[index] = foodName
                    index = index + 1
                else:
                    ax.scatter(year, dollar, color=color, picker=1, label=foodName)

def onpick(event):
    global msg
    categories = event.artist.get_label()
    x = event.artist.get_offsets()
    amount = int(x.item(0) + 1999)
    msg.remove()
    msg = ax.annotate("Category: {},\nYear: {},\n$ Million: {}\n".format(categories, amount, x.item(1)),
                      xy=(0, 0), xytext=(4, 18000))

plt.xlabel('Year')
plt.ylabel('$ Millions')
plt.legend((legendInfo[0], legendInfo[1], legendInfo[2], legendInfo[3], legendInfo[4],
            legendInfo[5], legendInfo[6], legendInfo[7], legendInfo[8], legendInfo[9],
            legendInfo[10], legendInfo[11], legendInfo[12], legendInfo[13], legendInfo[14]),
           (category[0], category[1], category[2], category[3], category[4], category[5],
            category[6], category[7], category[8], category[9], category[10], category[11],
            category[12], category[13], category[14]), loc='upper left', bbox_to_anchor=(0., 1.15))
fig.canvas.mpl_connect('pick_event', onpick)

plt.show()
