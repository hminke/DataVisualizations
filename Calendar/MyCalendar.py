import calendar as cal
import matplotlib.pyplot as plt
import numpy as np

#I used code from https://stackoverflow.com/questions/42171990/create-a-one-month-calendar-with-events-on-it-in-python
#to create a calendar and modified it to meet the needs of this project.

cal.setfirstweekday(6)  # Setting Sunday as the first day
weekdays = 'Sun Mon Tues Wed Thurs Fri Sat'.split()
months = 'January February March April May June July August September October November December'.split()

class MyCalendar(object):

    particleCount = {}

    #Todo: Add data portion to show method

    def __init__(self, year, month, fileName):

        temp = fileName.split('.')
        self.year = year
        self.month = month
        self.calendar = cal.monthcalendar(year, month)  #creates a list of lists for each week
        self.title = temp[0]

        data = open(fileName, "r")

        for line in data:
            word = line.split(' : ')
            day = word[0].split('/')
            self.particleCount.setdefault(int(day[1]), float(word[1]))

    def addColor(self, data):

        calendarData = np.zeros((172, 256, 3))

        if data <51:
            for i in range(172):
                for j in range(256):
                    for k in range(3):
                        if k == 0:
                            calendarData[i][j][k] = 0
                        elif k == 1:
                            calendarData[i][j][k] = 1
                        elif k == 2:
                            calendarData[i][j][k] = 0
        elif data < 101:
            for i in range(172):
                for j in range(256):
                    for k in range(3):
                        if k == 0:
                            calendarData[i][j][k] = 1
                        elif k == 1:
                            calendarData[i][j][k] = 1
                        elif k == 2:
                            calendarData[i][j][k] = 0
        elif data < 151:
            for i in range(172):
                for j in range(256):
                    for k in range(3):
                        if k == 0:
                            calendarData[i][j][k] = 1
                        elif k == 1:
                            calendarData[i][j][k] = 0.6
                        elif k == 2:
                            calendarData[i][j][k] = 0.2
        elif data < 201:
            for i in range(172):
                for j in range(256):
                    for k in range(3):
                        if k == 0:
                            calendarData[i][j][k] = 1
                        elif k == 1:
                            calendarData[i][j][k] = 0
                        elif k == 2:
                            calendarData[i][j][k] = 0
        elif data < 301:
            for i in range(172):
                for j in range(256):
                    for k in range(3):
                        if k == 0:
                            calendarData[i][j][k] = 0.6
                        elif k == 1:
                            calendarData[i][j][k] = 0
                        elif k == 2:
                            calendarData[i][j][k] = 0.6
        else:
            for i in range(172):
                for j in range(256):
                    for k in range(3):
                        if k == 0:
                            calendarData[i][j][k] = 0.6
                        elif k == 1:
                            calendarData[i][j][k] = 0
                        elif k == 2:
                            calendarData[i][j][k] = 0.298

        return calendarData

    def show(self):
        # Create the calendar
        fig, axs = plt.subplots(len(self.calendar), 7, sharex=True, sharey=True)
        for week, ax_row in enumerate(axs):
            for weekDay, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.calendar[week][weekDay] != 0:
                    calendarData = self.particleCount.get(self.calendar[week][weekDay])
                    dataColor = self.addColor(calendarData)
                    ax.imshow(dataColor)
                    # ax.imshow(np.zeros((172, 256, 3), dtype=np.float32))
                    ax.text(0.02, 0.98, str(self.calendar[week][weekDay]), verticalalignment='top',
                            horizontalalignment='left')

        # Use the titles of the first row as the weekdays
        for number, day in enumerate(weekdays):
            axs[0][number].set_title(day)

        # Place subplots in a close grid
        fig.subplots_adjust(hspace=0)
        fig.subplots_adjust(wspace=0)
        fig.suptitle(months[self.month - 1] + ' ' + str(self.year), fontsize=14)
        plt.title(self.title, fontweight='bold', x=-2.5, y=-0.5, fontsize=20)
        plt.show()

february = MyCalendar(2016, 2, "Air Pollution in Mumbai.txt")
february.show()
