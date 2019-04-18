import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches

fig = plt.figure()
ax = plt.axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())

data = open("motorcycleRegistration.txt", "r")
shapeName = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapeName)
registration = {}
colorRange = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

for line in data:
    word = line.split(' : ')
    registration.setdefault(word[0], float(word[1]))

c = np.arange(1, 18)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.Blues)
cmap.set_array([])

for state in shpreader.Reader(states_shp).records():

    edgeColor = 'black'

    try:
        stateDens = registration[state.attributes['name']]
    except:
        stateDens = 0

    if stateDens < 45000:
        faceColor = cmap.to_rgba(1)
    elif stateDens < 90000:
        faceColor = cmap.to_rgba(2)
    elif stateDens < 135000:
        faceColor = cmap.to_rgba(3)
    elif stateDens < 180000:
        faceColor = cmap.to_rgba(4)
    elif stateDens < 225000:
        faceColor = cmap.to_rgba(5)
    elif stateDens < 270000:
        faceColor = cmap.to_rgba(6)
    elif stateDens < 315000:
        faceColor = cmap.to_rgba(7)
    elif stateDens < 360000:
        faceColor = cmap.to_rgba(8)
    elif stateDens < 405000:
        faceColor = cmap.to_rgba(9)
    elif stateDens < 450000:
        faceColor = cmap.to_rgba(10)
    elif stateDens < 495000:
        faceColor = cmap.to_rgba(11)
    elif stateDens < 540000:
        faceColor = cmap.to_rgba(12)
    elif stateDens < 585000:
        faceColor = cmap.to_rgba(13)
    elif stateDens < 630000:
        faceColor = cmap.to_rgba(14)
    elif stateDens < 675000:
        faceColor = cmap.to_rgba(15)
    elif stateDens < 720000:
        faceColor = cmap.to_rgba(16)
    elif stateDens < 765000:
        faceColor = cmap.to_rgba(17)
    else:
        faceColor = cmap.to_rgba(18)

    ax.add_geometries([state.geometry], ccrs.PlateCarree(), facecolor=faceColor, edgecolor=edgeColor)

range1 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(1))
range2 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(2))
range3 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(3))
range4 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(4))
range5 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(5))
range6 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(6))
range7 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(7))
range8 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(8))
range9 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(9))
range10 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(10))
range11 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(11))
range12 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(12))
range13 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(13))
range14 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(14))
range15 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(15))
range16 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(16))
range17 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(17))
range18 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(18))

labels = ['< 45,000', '45,000 - 89,999', '90,000 - 134,999', '135,000 - 179,999', '180,000 - 224,999',
          '225,000 - 269.999', '270,000 - 314,999', '315,000 - 359,999', '360,000 - 404,999', '405,000 - 449,999',
          '450,000 - 494,999', '495,000 - 539,999', '540,000 - 584,999', '585,000 - 629,999', '630,000 - 674,999',
          '675,000 - 719,999', '720,000 - 764,999', '> 764,999']

plt.title('Motorcycle Registrations per U.S. state', y=.9, x=.875)
plt.legend([range1, range2, range3, range4, range5, range6, range7, range8, range9, range10, range11, range12, range13,
           range14, range15, range16, range17, range18], labels, loc='upper left', fancybox=True,
           bbox_to_anchor=(-0.25, 1.0))
ax.outline_patch.set_visible(False)
plt.show()
