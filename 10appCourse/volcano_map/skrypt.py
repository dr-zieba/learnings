import folium
import pandas
import json


#read data from Volcanoes.txt
data = pandas.read_csv(r"C:\Users\zieba\Desktop\python\10appCourse\volcano_map\Volcanoes.txt")

#creates a map with start points
map = folium.Map(location=[37.75, -122.43],zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanos")

#html for popup windows
popup_html = '''<h4>Volcano information:</h4>
Height %s m
'''
#go thru file
for index, row in data.iterrows():
    lat = row['LAT'] #get Latitude
    long = row['LON'] #get Longitude
    name = row['ELEV'] #get height

    #define a color of a marker
    if name > 4000:
        h_color="red"
    elif 1000 <= name <=3999:
        h_color="orange"
    else:
        h_color="green"

    #creates an iframe for popup
    iframe = folium.IFrame(html=popup_html % str(name),width=200, height=100 )
    #adds elements to a map
    fgv.add_child(folium.Circle(radius=5000,location=[lat,long], popup=folium.Popup(iframe), color=h_color, fill=True))

fgp = folium.FeatureGroup(name="Population")

geo_json = r"C:\Users\zieba\Desktop\python\10appCourse\volcano_map\world.json"

fgp.add_child(folium.GeoJson(data=open(geo_json, 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

#,style_function=lambda x: {'fillcolor':'green'}
#if x['properties']['POP2005'] > 1000000 else 'orange' if 1000000 <= x['properties']['POP2005'] < 2000000 else 'red'
#add to FeatureGroup
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
#saves map to a file
map.save(r"C:\Users\zieba\Desktop\python\10appCourse\volcano_map\map.html")
