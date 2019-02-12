import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('food_imports.csv')

data = data.drop(columns=['Unnamed: 1', 'Unnamed: 2'], index=[0, 1, 3])
data = data.set_index('Unnamed: 0')

year_list = list(data)
values_list = data.values.tolist()

def formatDollarAmount( dollarList ):

    for j in range(0, len(dollarList)):
        temp = dollarList[j].replace(',', '')
        dollarList[j] = float(temp)
    return dollarList

x = year_list

fig, ax, = plt.subplots()
y1 = ax.scatter(x, formatDollarAmount(values_list[0]))
y2 = ax.scatter(x, formatDollarAmount(values_list[1]))
y3 = ax.scatter(x, formatDollarAmount(values_list[2]))
y4 = ax.scatter(x, formatDollarAmount(values_list[3]))
y5 = ax.scatter(x, formatDollarAmount(values_list[4]))
y6 = ax.scatter(x, formatDollarAmount(values_list[5]))
y7 = ax.scatter(x, formatDollarAmount(values_list[6]))
y8 = ax.scatter(x, formatDollarAmount(values_list[7]))
y9 = ax.scatter(x, formatDollarAmount(values_list[8]))
y10 = ax.scatter(x, formatDollarAmount(values_list[9]))
y11 = ax.scatter(x, formatDollarAmount(values_list[10]))
y12 = ax.scatter(x, formatDollarAmount(values_list[11]))
y13 = ax.scatter(x, formatDollarAmount(values_list[12]))
y14 = ax.scatter(x, formatDollarAmount(values_list[13]))
ax.set_title('Food Imports by Year')
ax.legend((y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14),
          (data.index[0], data.index[1], data.index[2], data.index[3],
           data.index[4], data.index[5], data.index[6], data.index[7],
           data.index[8], data.index[9], data.index[10], data.index[11],
           data.index[12], data.index[13]))
plt.xlabel('Year')
plt.ylabel('$ Millions')
plt.show()
