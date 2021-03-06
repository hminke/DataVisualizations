import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches

fig = plt.figure()
ax = plt.axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())

data = open("motorcycleRegistrationPerCapita.txt", "r")
shapeName = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapeName)
registration = {}
colorRange = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

for line in data:
    word = line.split(' : ')
    registration.setdefault(word[0], float(word[1]))

c = np.arange(1, 10)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.Blues)
cmap.set_array([])

for state in shpreader.Reader(states_shp).records():

    edgeColor = 'black'

    try:
        stateDens = registration[state.attributes['name']]
    except:
        stateDens = 0

    if stateDens > 170:
        faceColor = cmap.to_rgba(1)
    elif stateDens > 150:
        faceColor = cmap.to_rgba(2)
    elif stateDens > 130:
        faceColor = cmap.to_rgba(3)
    elif stateDens > 110:
        faceColor = cmap.to_rgba(4)
    elif stateDens > 90:
        faceColor = cmap.to_rgba(5)
    elif stateDens > 70:
        faceColor = cmap.to_rgba(6)
    elif stateDens > 50:
        faceColor = cmap.to_rgba(7)
    elif stateDens > 30:
        faceColor = cmap.to_rgba(8)
    else:
        faceColor = cmap.to_rgba(9)

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

labels = ['> 170', '151 - 170', '131 - 150', '111 - 130', '91 - 110', '71 - 90', '51 - 70', '31 - 50', '< 31']

plt.title('People per Motorcycle per U.S. state', y=.9, x=.875)
plt.legend([range1, range2, range3, range4, range5, range6, range7, range8, range9], labels, loc='upper left',
           fancybox=True, bbox_to_anchor=(-0.25, 1.0))
ax.outline_patch.set_visible(False)
plt.show()
