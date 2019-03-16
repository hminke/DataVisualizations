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
msg = ax.annotate('Click bars for annotation', xy=(0, 0), xytext=(0, 0))

category = []
categoryFoodName = []

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
                if year == '1999':
                    categoryFoodName.append(foodName)
        category.append(y)
        index = 0

def onpick(event):
#    global msg
    amount = event.artist.get_height()
    date = int(event.mouseevent.xdata)
    categories = event.artist.get_label()
    # msg.remove()
    # msg = ax.annotate("Category: {},\nYear: {},\n$ Million: {}\n".format(categories, amount, x.item(1)),
    #                   xy=(0, 0), xytext=(4, 18000))

    print(date, amount)

category1Plot = ax.bar(x, category[0], picker=1, label=categoryFoodName[0])
category2Plot = ax.bar(x, category[1], picker=1, label=categoryFoodName[1], bottom=category[0])
# category3Plot = ax.bar(x, category[2], picker=1, label=categoryFoodName[2], bottom=category[0]+category[1])
# category4Plot = ax.bar(x, category[3], picker=1, label=categoryFoodName[3], bottom=category[0]+category[1]+category[2])
# category5Plot = ax.bar(x, category[4], picker=1, label=categoryFoodName[4],
#                        bottom=category[0]+category[1]+category[2]+category[3])
# category6Plot = ax.bar(x, category[5], picker=1, label=categoryFoodName[5],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4])
# category7Plot = ax.bar(x, category[6], picker=1, label=categoryFoodName[6],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5])
# category8Plot = ax.bar(x, category[7], picker=1, label=categoryFoodName[7],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6])
# category9Plot = ax.bar(x, category[8], picker=1, label=categoryFoodName[8],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7])
# category10Plot = ax.bar(x, category[9], picker=1, label=categoryFoodName[9],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7]+category[8])
# category11Plot = ax.bar(x, category[10], picker=1, label=categoryFoodName[10],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7]+category[8]+category[9])
# category12Plot = ax.bar(x, category[11], picker=1, label=categoryFoodName[11],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7]+category[8]+category[9]+category[10])
# category13Plot = ax.bar(x, category[12], picker=1, label=categoryFoodName[12],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7]+category[8]+category[9]+category[10]+category[11])
# category14Plot = ax.bar(x, category[13], picker=1, label=categoryFoodName[13],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7]+category[10]+category[9]+category[10]+category[11]+category[12])
# category15Plot = ax.bar(x, category[14], picker=1, label=categoryFoodName[14],
#                        bottom=category[0]+category[1]+category[2]+category[3]+category[4]+category[5]+category[6]+
#                               category[7]+category[8]+category[9]+category[10]+category[11]+category[12]+category[13])

plt.xlabel('Year')
plt.ylabel('Price ($) per Million')
plt.title('Food Imports by Year')
plt.xticks(x)
plt.legend(loc='upper left', bbox_to_anchor=(0., 1.1))
fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
