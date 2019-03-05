import csv
import numpy as np
import matplotlib.pyplot as plt

fig, ax, = plt.subplots()
y = np.zeros(19)
years = np.zeros(19)
categoryFoodName = [None] * 15
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
global category6
global category6FoodName
global category7
global category7FoodName
global category8
global category8FoodName
global category9
global category9FoodName
global category10
global category10FoodName
global category11
global category11FoodName
global category12
global category12FoodName
global category13
global category13FoodName
global category14
global category14FoodName
global category15
global category15FoodName

with open("food_imports.csv", 'r') as fil:
    data = csv.DictReader(fil, delimiter=',')
    for row in data:
        foodName = row['Food Type']
        del(row['Food Type'])
        for year, dollarAmount in row.items():
            temp = dollarAmount.replace(',', '')
            if len(temp) != 0:
                y[index] = float(temp)
                years[index] = int(year)
                index = index + 1
        if foodName == 'Live meat animals':
            category1 = y
            category1FoodName = foodName
            categoryFoodName[0] = foodName
        elif foodName == 'Meats':
            category2 = y
            category2FoodName = foodName
            categoryFoodName[1] = foodName
        elif foodName == 'Fish and shellfish 2/':
            category3 = y
            category3FoodName = foodName
            categoryFoodName[2] = foodName
        elif foodName == 'Dairy':
            category4 = y
            category4FoodName = foodName
            categoryFoodName[3] = foodName
        elif foodName == 'Vegetables':
            category5 = y
            category5FoodName = foodName
            categoryFoodName[4] = foodName
        elif foodName == 'Fruits':
            category6 = y
            category6FoodName = foodName
            categoryFoodName[5] = foodName
        elif foodName == 'Nuts':
            category7 = y
            category7FoodName = foodName
            categoryFoodName[6] = foodName
        elif foodName == 'Coffee, tea, and spices':
            category8 = y
            category8FoodName = foodName
            categoryFoodName[7] = foodName
        elif foodName == 'Grains':
            category9 = y
            category9FoodName = foodName
            categoryFoodName[8] = foodName
        elif foodName == 'Vegetable oils':
            category10 = y
            category10FoodName = foodName
            categoryFoodName[9] = foodName
        elif foodName == 'Sugar and candy':
            category11 = y
            category11FoodName = foodName
            categoryFoodName[10] = foodName
        elif foodName == 'Cocoa and chocolate':
            category12 = y
            category12FoodName = foodName
            categoryFoodName[11] = foodName
        elif foodName == 'Other edible products':
            category13 = y
            category13FoodName = foodName
            categoryFoodName[12] = foodName
        elif foodName == 'Beverages 3/':
            category14 = y
            category14FoodName = foodName
            categoryFoodName[13] = foodName
        elif foodName == 'Liquors':
            category15 = y
            category15FoodName = foodName
            categoryFoodName[14] = foodName

        index = 0

category1Plot = ax.bar(years, category1, picker=1, label=category1FoodName)
category2Plot = ax.bar(years, category2, picker=1, label=category2FoodName, bottom=category1)
category3Plot = ax.bar(years, category3, picker=1, label=category3FoodName, bottom=category1+category2)
category4Plot = ax.bar(years, category4, picker=1, label=category4FoodName, bottom=category1+category2+category3)
category5Plot = ax.bar(years, category5, picker=1, label=category5FoodName,
                       bottom=category1+category2+category3+category4)
category6Plot = ax.bar(years, category6, picker=1, label=category6FoodName,
                       bottom=category1+category2+category3+category4+category5)
category7Plot = ax.bar(years, category7, picker=1, label=category7FoodName,
                       bottom=category1+category2+category3+category4+category5+category6)
category8Plot = ax.bar(years, category8, picker=1, label=category8FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7)
category9Plot = ax.bar(years, category9, picker=1, label=category9FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8)
category10Plot = ax.bar(years, category10, picker=1, label=category10FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8+
                              category9)
category11Plot = ax.bar(years, category11, picker=1, label=category11FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8+
                              category9+category10)
category12Plot = ax.bar(years, category12, picker=1, label=category12FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8+
                              category9+category10+category11)
category13Plot = ax.bar(years, category13, picker=1, label=category13FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8+
                              category9+category10+category11+category12)
category14Plot = ax.bar(years, category14, picker=1, label=category14FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8+
                              category9+category10+category11+category12+category13)
category15Plot = ax.bar(years, category15, picker=1, label=category15FoodName,
                       bottom=category1+category2+category3+category4+category5+category6+category7+category8+
                              category9+category10+category11+category12+category13+category14)
plt.ylabel('$ Millions')
plt.title('Food Imports by Year')
plt.xticks(years)
plt.legend(loc='upper left', bbox_to_anchor=(0., 1.1))
plt.show()
