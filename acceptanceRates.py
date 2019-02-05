#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np

N = 6
femaleRejected = [0, 0, 0, 0, 0, 0]
maleRejected = [0, 0, 0, 0, 0, 0]
femaleAdmitted = [0, 0, 0, 0, 0, 0]
maleAdmitted = [0, 0, 0, 0, 0, 0]
ind = np.arange(N)
width = 0.45
data = open("berkley.txt","r");

for line in data:
    words = line.split(',')
    if words[0] == "Rejected":
        if words[1] == "Female":
            if words[2] == "A":
                femaleRejected[0] = float(words[3])
            elif words[2] == "B":
                femaleRejected[1] = float(words[3])
            elif words[2] == "C":
                femaleRejected[2] = float(words[3])
            elif words[2] == "D":
                femaleRejected[3] = float(words[3])
            elif words[2] == "E":
                femaleRejected[4] = float(words[3])
            elif words[2] == "F":
                femaleRejected[5] = float(words[3])
        elif words[1] == "Male":
            if words[2] == "A":
                maleRejected[0] = float(words[3])
            elif words[2] == "B":
                maleRejected[1] = float(words[3])
            elif words[2] == "C":
                maleRejected[2] = float(words[3])
            elif words[2] == "D":
                maleRejected[3] = float(words[3])
            elif words[2] == "E":
                maleRejected[4] = float(words[3])
            elif words[2] == "F":
                maleRejected[5] = float(words[3])
    if words[0] == "Admitted":
        if words[1] == "Female":
            if words[2] == "A":
                femaleAdmitted[0] = float(words[3])
            elif words[2] == "B":
                femaleAdmitted[1] = float(words[3])
            elif words[2] == "C":
                femaleAdmitted[2] = float(words[3])
            elif words[2] == "D":
                femaleAdmitted[3] = float(words[3])
            elif words[2] == "E":
                femaleAdmitted[4] = float(words[3])
            elif words[2] == "F":
                femaleAdmitted[5] = float(words[3])
        elif words[1] == "Male":
            if words[2] == "A":
                maleAdmitted[0] = float(words[3])
            elif words[2] == "B":
                maleAdmitted[1] = float(words[3])
            elif words[2] == "C":
                maleAdmitted[2] = float(words[3])
            elif words[2] == "D":
                maleAdmitted[3] = float(words[3])
            elif words[2] == "E":
                maleAdmitted[4] = float(words[3])
            elif words[2] == "F":
                maleAdmitted[5] = float(words[3])

fig, ax = plt.subplots()
admittedMales = ax.bar(ind - width/2, maleAdmitted, width, color='SkyBlue')
admittedFemales = ax.bar(ind - width/2, femaleAdmitted, width, bottom=maleAdmitted)
rejectedMales = ax.bar(ind + width/2, maleRejected, width, color='IndianRed')
rejectedFemales = ax.bar(ind + width/2, femaleRejected, width, bottom=maleRejected)

ax.set_ylabel('Number Of Students')
ax.set_title('Acceptance Rates at UC Berkley')
ax.set_xticks(ind)
ax.set_xticklabels(('Dept. A', 'Dept. B', 'Dept. C', 'Dept. D', 'Dept. E', 'Dept. F'))
ax.legend((admittedMales[0], admittedFemales[0], rejectedMales[0], rejectedFemales[0]),
          ('Men Admitted', 'Women Admitted', 'Men Rejected', 'Women Rejected'))

plt.show()


