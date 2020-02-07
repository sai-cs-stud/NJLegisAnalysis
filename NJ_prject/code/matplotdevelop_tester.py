import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.io.shapereader as shpreader
import matplotlib.pyplot as plt

def createMap():
	reader = shpreader.Reader('/Users/Sainayan/Downloads/countyl010g_shp_nt00964/countyl010g.shp')
	reader2= shpreader.Reader('/Users/Sainayan/Downloads/statesp010g.shp_nt00938/statesp010g.shp')
	counties = list(reader.geometries())
	states=list(reader2.geometries())
	COUNTIES = cfeature.ShapelyFeature(counties, ccrs.PlateCarree())
	STATES = cfeature.ShapelyFeature(states, ccrs.PlateCarree())

	plt.figure(figsize=(10, 6))
	ax = plt.axes(projection=ccrs.PlateCarree())

	source ='nationalmap.gov'
	ax.add_feature(cfeature.LAND.with_scale('50m'))
	ax.add_feature(cfeature.OCEAN.with_scale('50m'))
	ax.add_feature(cfeature.LAKES.with_scale('50m'))
	#ax.add_feature(cfeature.RIVERS.with_scale('50m'),edgecolor='black')
	ax.add_feature(COUNTIES, facecolor='none', edgecolor='gray')
	ax.add_feature(STATES, facecolor='none', edgecolor='black')
	#stext = AnchoredText('Source: {}'' '.format(source), loc=4, prop={'size': 12}, frameon=True)
	ax.coastlines('50m')
	#ax.add_artists(stext)

	ax.set_extent([-83, -65, 33, 44])
	plt.show()

createMap()