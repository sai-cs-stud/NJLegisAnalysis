import pandas as pd 


df = pd.read_csv('https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/NJ_prject/Pandas/County_municipality.csv')
df_crime = pd.read_csv('https://raw.githubusercontent.com/sai-cs-stud/NJLegisAnalysis/master/NJ_prject/Pandas/NJ_Crime_2012.csv')
df_crime['County_Municipality'] = df_crime['County']+' '+df_crime['Municipality']
df_crime = df_crime.replace(to_replace ="Township",value ="Twp")
df_crime = df_crime.replace(to_replace ="-",value ="0")

county_to_municipality = {}
county_list= df.keys().tolist()


for county_name in county_list:
    df_clean = df.dropna(how='any', subset=[county_name])
    df_clean = df_clean.replace(to_replace ="Township",value ="Twp")
    municipality_name = df_clean[county_name].tolist()
    df_curr=(df_crime[df_crime['County'] == county_name]).set_index('Municipality')
    municipality_value = {i : df_curr.loc[i,'Violent Crimes'] for i in municipality_name}
    county_to_municipality[county_name] = municipality_value
county_to_municipality.items()
#print(county_to_municipality)   

summary={}
for county_name in county_to_municipality.keys():
    new_list = 0
    for values in county_to_municipality[county_name].values():
        new_list+=int(values)
    summary.update({county_name:new_list})
print(summary.items())