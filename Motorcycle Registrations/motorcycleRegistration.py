import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.patches as mpatches

fig = plt.figure()
ax = plt.axes([0, 0, 1, 1], projection=ccrs.LambertConformal())
ax.set_extent([-160, -72, 20, 72], ccrs.Geodetic())

data = open("motorcycleRegistration.txt","r")
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
        colorRange[0] = faceColor
    elif stateDens < 90000:
        faceColor = cmap.to_rgba(2)
        colorRange[1] = faceColor
    elif stateDens < 135000:
        faceColor = cmap.to_rgba(3)
        colorRange[2] = faceColor
    elif stateDens < 180000:
        faceColor = cmap.to_rgba(4)
        colorRange[3] = faceColor
    elif stateDens < 225000:
        faceColor = cmap.to_rgba(5)
        colorRange[4] = faceColor
    elif stateDens < 270000:
        faceColor = cmap.to_rgba(6)
        colorRange[5] = faceColor
    elif stateDens < 315000:
        faceColor = cmap.to_rgba(7)
        colorRange[6] = faceColor
    elif stateDens < 360000:
        faceColor = cmap.to_rgba(8)
        colorRange[7] = faceColor
    elif stateDens < 405000:
        faceColor = cmap.to_rgba(9)
        colorRange[8] = faceColor
    elif stateDens < 450000:
        faceColor = cmap.to_rgba(10)
        colorRange[9] = faceColor
    elif stateDens < 495000:
        faceColor = cmap.to_rgba(11)
        colorRange[10] = faceColor
    elif stateDens < 540000:
        faceColor = cmap.to_rgba(12)
        colorRange[11] = faceColor
    elif stateDens < 585000:
        faceColor = cmap.to_rgba(13)
        colorRange[12] = faceColor
    elif stateDens < 630000:
        faceColor = cmap.to_rgba(14)
        colorRange[13] = faceColor
    elif stateDens < 675000:
        faceColor = cmap.to_rgba(15)
        colorRange[14] = faceColor
    elif stateDens < 720000:
        faceColor = cmap.to_rgba(16)
        colorRange[15] = faceColor
    elif stateDens < 765000:
        faceColor = cmap.to_rgba(17)
        colorRange[16] = faceColor
    else:
        faceColor = cmap.to_rgba(18)
        colorRange[17] = faceColor

    ax.add_geometries([state.geometry], ccrs.PlateCarree(), facecolor=faceColor, edgecolor=edgeColor)

# range1 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(1))
# range2 = mpatches.Rectangle((0, 0), 1, 1, faceCcolor=cmap.to_rgba(2))
# range3 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(3))
# range4 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(4))
# range5 = mpatches.Rectangle((0, 0), 1, 1, facecolor=cmap.to_rgba(5))
# range6 = cmap.to_rgba(6)
# range7 = cmap.to_rgba(7)
# range8 = cmap.to_rgba(8)
# range9 = cmap.to_rgba(9)
# range10 = cmap.to_rgba(10)
# range11 = cmap.to_rgba(11)
# range12 = cmap.to_rgba(12)
# range13 = cmap.to_rgba(13)
# range14 = cmap.to_rgba(14)
# range15 = cmap.to_rgba(15)
# range16 = cmap.to_rgba(16)
# range17 = cmap.to_rgba(17)
# range18 = cmap.to_rgba(18)

labels = ['< 45,000', '45,000 - 89,999', '90,000 - 134,999', '135,000 - 179,999', '180,000 - 224,999',
          '225,000 - 269.999', '270,000 - 314,999', '315,000 - 359,999', '360,000 - 404,999', '405,000 - 449,999',
          '450,000 - 494,999', '495,000 - 539,999', '540,000 - 584,999', '585,000 - 629,999', '630,000 - 674,999',
          '675,000 - 719,999', '720,000 - 764,999', '> 764,999']

plt.title('Motorcycle Registrations per U.S. state', y=.875, x=.875)
plt.legend()
ax.outline_patch.set_visible(False)
plt.show()
