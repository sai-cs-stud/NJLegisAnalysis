import pandas as pd 
import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/NJ_prject/Pandas/test_1.csv')
#df_new.head()
df_c = pd.read_csv('https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/NJ_prject/Pandas/County_markers%20-%20Sheet1%20(4).csv')
df_l = pd.read_csv('https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/NJ_prject/Pandas/County_lines%20-%20Sheet1%20(42).csv')
#County = df_new["County"].values.tolist()
# values = range(len(fips))
# fig = ff.create_choropleth(fips=fips, values=values,scope = ["New Jersey"])
#print(County)
#df.query('Index == %d' %1)

# len(fips)

# df_new['text'] = df_new['County'].astype(str)+'<br>Median family income'+df_new['Median family income'].astype(str)
# limits = [[50000,60000],[60000,70000],[70000,80000],[80000,90000],[90000,100000]]
colors=["#ff0040","#ff4000","#ff0000","#ff8000","#ffbf00","#ffff00","#bfff00","#80ff00","#40ff00","#00ff00","#00ff40","#00ff80","#00ffbf","#00ffff","#00bfff","#0080ff","#0040ff","#0000ff","#4000ff","#8000ff","#bf00ff","#ff00ff"]

#print(len(colors))
# cities = []
# scale = 5000
fig = go.Figure()
for i in range(22):
	df_all = df.query('Index ==%s' %i)
	fig.add_trace(go.Scattergeo(
		#locationmode= 'USA-states',
		showlegend = False,
		lon = df_all['Longitude'],
		lat = df_all['Latitude'],
		text = df_all['County'],
		mode='markers',
		marker = dict(
			size = df_all['Population']/20000,
			color = colors[i],
			line_color = 'rgb(40,40,40)',
			line_width = 1.0
		),
		geo = 'geo'))
"""fig.add_trace(go.Scattergeo(
	showlegend = False,
	lon = df_c['Lon'],
	lat = df_c['Lat'],
	mode='markers',
	marker = dict(
		size = 0,
		color = 'white',
		line = dict(
			width = 0,
			color = 'black')
		),
	geo = 'geo'))"""
for i in range(len(df_l)):
    fig.add_trace(
        go.Scattergeo(
            locationmode = 'USA-states',
            lon = [df_l['start_lon'][i], df_l['end_lon'][i]],
            lat = [df_l['start_lat'][i], df_l['end_lat'][i]],
            mode = 'lines',
            line = dict(width = 1,color = 'red'),
        )
    )
fig.update_layout(
	geo = go.layout.Geo(
		resolution = 110,
		scope = 'usa',
		countrycolor = 'red',
		showcoastlines =True,
		projection = go.layout.geo.Projection(
			scale = 11
		),
		center = {'lat':40.2,'lon':-74.871826}
	),
	#legend_traceorder = 'reversed'
)
fig.show()