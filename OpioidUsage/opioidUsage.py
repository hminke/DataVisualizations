import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

fig = plt.figure()
ax = plt.axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())

data = open("opioidUsage.txt","r")
shapeName = 'admin_1_states_provinces_lakes_shp'
states_shp = shpreader.natural_earth(resolution='110m', category='cultural', name=shapeName)
stateName = []
opioidUsage = {}

for line in data:
    word = line.split(' : ')
    opioidUsage.setdefault(word[0], float(word[1]))

c = np.arange(1,6)
norm = mpl.colors.Normalize(vmin=c.min(), vmax=c.max())
cmap = mpl.cm.ScalarMappable(norm=norm, cmap=mpl.cm.GnBu)
cmap.set_array([])

for state in shpreader.Reader(states_shp).records():

    edgeColor = 'black'

    try:
        stateDens = opioidUsage[state.attributes['name']]
    except:
        stateDens = 0

    if stateDens < 5:
        faceColor = cmap.to_rgba(1)
    elif stateDens < 10:
        faceColor = cmap.to_rgba(2)
    elif stateDens < 15:
        faceColor = cmap.to_rgba(3)
    elif stateDens < 20:
        faceColor = cmap.to_rgba(4)
    elif stateDens < 25:
        faceColor = cmap.to_rgba(5)
    elif stateDens < 30:
        faceColor = cmap.to_rgba(6)
    elif stateDens < 35:
        faceColor = cmap.to_rgba(7)
    else:
        faceColor = cmap.to_rgba(8)

    ax.add_geometries([state.geometry], ccrs.PlateCarree(), facecolor=faceColor, edgecolor=edgeColor)

plt.title('U.S. Opioid Use Per State')
ax.outline_patch.set_visible(False)
plt.show()
