import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches

fig = plt.figure()
ax = plt.axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())

data = open("opioidUsage.txt","r")
shapeName = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapeName)
opioidUsage = {}

for line in data:
    word = line.split(' : ')
    opioidUsage.setdefault(word[0], float(word[1]))

c = np.arange(1, 20)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.Oranges)
cmap.set_array([])

for state in shpreader.Reader(states_shp).records():

    edgeColor = 'black'

    try:
        stateDens = opioidUsage[state.attributes['name']]
    except:
        stateDens = 0

    if stateDens < 3:
        faceColor = cmap.to_rgba(1)
    elif stateDens < 6:
        faceColor = cmap.to_rgba(2)
    elif stateDens < 9:
        faceColor = cmap.to_rgba(3)
    elif stateDens < 12:
        faceColor = cmap.to_rgba(4)
    elif stateDens < 15:
        faceColor = cmap.to_rgba(5)
    elif stateDens < 18:
        faceColor = cmap.to_rgba(6)
    elif stateDens < 21:
        faceColor = cmap.to_rgba(7)
    elif stateDens < 24:
        faceColor = cmap.to_rgba(8)
    elif stateDens < 27:
        faceColor = cmap.to_rgba(9)
    elif stateDens < 30:
        faceColor = cmap.to_rgba(10)
    elif stateDens < 33:
        faceColor = cmap.to_rgba(11)
    elif stateDens < 36:
        faceColor = cmap.to_rgba(12)
    else:
        faceColor = cmap.to_rgba(13)

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

labels = ['< 3', '3 - 5', '6 - 8', '9 - 11', '12 - 14', '15 - 17', '18 - 20', '21 - 23', '24 - 26', '27 - 29',
          '30 - 32', '33 - 35', '> 36']

plt.title('U.S. Opioid Use Per State', y=.9, x=.875)
plt.legend([range1, range2, range3, range4, range5, range6, range7, range8, range9, range10, range11, range12, range13],
           labels, loc='upper left', fancybox=True, bbox_to_anchor=(-0.25, 1.0))
ax.outline_patch.set_visible(False)
plt.show()
