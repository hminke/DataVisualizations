import calendar as cal
import matplotlib.pyplot as plt

cal.setfirstweekday(6)  # Setting Sunday as the first day
weekdays = 'Sun Mon Tues Wed Thurs Fri Sat'.split()
months = 'January February March April May June July August September October November December'.split()

class MyCalendar(object):

    #Todo: Make read method to read and sort data
    # Put read file method in __init__ method
    # Add data portion to show method

    def __init__(self, year, month, fileName):
        self.year = year
        self.month = month
        self.calendar = cal.monthcalendar(year, month)  #creates a list of lists for each week



    def addColor(self, data, day):

        if data < 51:
            color = 'lime'
        elif data < 101:
            color = 'yellow'
        elif data < 151:
            color = 'orange'
        elif data < 201:
            color = 'r'
        elif data < 301:
            color = 'darkviolet'
        else:
            color = 'maroon'

        return color

    def show(self):
        # Create the calendar
        fig, axs = plt.subplots(len(self.calendar), 7, sharex=True, sharey=True)
        for week, ax_row in enumerate(axs):
            for week_day, ax in enumerate(ax_row):
                ax.set_xticks([])
                ax.set_yticks([])
                if self.calendar[week][week_day] != 0:
                    ax.text(0.02, 0.98, str(self.calendar[week][week_day]), verticalalignment='top',
                            horizontalalignment='left')

        # Use the titles of the first row as the weekdays
        for number, day in enumerate(weekdays):
            axs[0][number].set_title(day)

        # Place subplots in a close grid
        fig.subplots_adjust(hspace=0)
        fig.subplots_adjust(wspace=0)
        fig.suptitle(months[self.month - 1] + ' ' + str(self.year), fontsize=20, fontweight='bold')
        plt.show()

february = MyCalendar(2017, 2) #February 2017
february.addColor(51, 6)
february.show()
