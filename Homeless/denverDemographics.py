import numpy as np
import matplotlib.pyplot as plt

def getData(fileName):
    graphData = []
    percentageData = []
    category = []
    data = open(fileName, "r")

    for line in data:
        word = line.split(' : ')
        value = word[1].split(' ')
        category.append(word[0])
        graphData.append(int(value[0]))
        percentageData.append(value[1])

    return graphData, percentageData, category

demographicsData, demographicsPercentages, demographicsCategories = getData('denverDemographics.txt')
genderData, genderPercentage, genderCategories = getData('GenderOfHomeless.txt')
ageData, agePercentage, ageCategories = getData('AgeOfHomeless.txt')
raceData, racePercentage, raceCategories = getData('RaceOfHomeless.txt')

plt.subplot(2, 2, 1)
y1_pos = np.arange(len(demographicsData))
width = 0.5

graph1 = plt.barh(y1_pos, demographicsData, align='center')
plt.yticks(y1_pos, demographicsCategories)
plt.xlabel('People')
plt.figtext(0.30, 0.95, 'Demographics of the Homeless in Denver', fontsize=26)

plt.subplot(2, 2, 2)
y2_pos = np.arange(len(genderData))

graph2 = plt.barh(y2_pos, genderData,  align='center', color='red')
plt.yticks(y2_pos, genderCategories)
plt.xlabel('People')

plt.subplot(2, 2, 3)
y3_pos = np.arange(len(ageData))

graph3 = plt.barh(y3_pos, ageData, align='center', color='green')
plt.yticks(y3_pos, ageCategories)
plt.xlabel('People')
plt.ylabel('Age')

plt.subplot(2, 2, 4)
y4_pos = np.arange(len(raceData))

graph4 = plt.barh(y4_pos, raceData, align='center', color='purple')
plt.yticks(y4_pos, raceCategories)
plt.xlabel('People')

plt.figtext(0.38, 0.56, '{} {}'.format(demographicsData[0], demographicsPercentages[0]), color='white',
            fontweight='bold')
plt.figtext(0.33, 0.64, '{} {}'.format(demographicsData[1], demographicsPercentages[1]), fontweight='bold')
plt.figtext(0.405, 0.725, '{} {}'.format(demographicsData[2], demographicsPercentages[2]), fontweight='bold',
            color='white')
plt.figtext(0.213, 0.825, '{} {}'.format(demographicsData[3], demographicsPercentages[3]), fontweight='bold')
plt.figtext(0.685, 0.565, '{} {}'.format(genderData[0], genderPercentage[0]), fontweight='bold')
plt.figtext(0.822, 0.68, '{} {}'.format(genderData[1], genderPercentage[1]), fontweight='bold', color='white')
plt.figtext(0.555, 0.81, '{} {}'.format(genderData[2], genderPercentage[2]), fontweight='bold')
plt.figtext(0.202, 0.13, '{} {}'.format(ageData[0], agePercentage[0]), fontweight='bold')
plt.figtext(0.172, 0.195, '{} {}'.format(ageData[1], agePercentage[1]), fontweight='bold')
plt.figtext(0.4, 0.263, '{} {}'.format(ageData[2], agePercentage[2]), fontweight='bold', color='white')
plt.figtext(0.253, 0.33, '{} {}'.format(ageData[3], agePercentage[3]), fontweight='bold')
plt.figtext(0.16, 0.41, '{} {}'.format(ageData[4], agePercentage[4]), fontweight='bold')
plt.figtext(0.825, 0.125, '{} {}'.format(raceData[0], racePercentage[0]), fontweight='bold', color='white')
plt.figtext(0.688, 0.18, '{} {}'.format(raceData[1], racePercentage[1]), fontweight='bold')
plt.figtext(0.555, 0.237, '{} {}'.format(raceData[2], racePercentage[2]), fontweight='bold')
plt.figtext(0.58, 0.29, '{} {}'.format(raceData[3], racePercentage[3]), fontweight='bold')
plt.figtext(0.56, 0.345, '{} {}'.format(raceData[4], racePercentage[4]), fontweight='bold')
plt.figtext(0.615, 0.415, '{} {}'.format(raceData[5], racePercentage[5]), fontweight='bold')

plt.show()
