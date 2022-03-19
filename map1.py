import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
  if elevation < 1000:
    return 'purple'
  elif 1000 <= elevation < 3000:
    return 'orange'
  else:
    return 'red'
map = folium.Map(location=[39.10, -94.67], zoom_start=6, tiles="Stamen Terrain")
fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):

    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(str(el)+" meters",parse_html=True), fill_color=color_producer(el), color = 'grey', fill=True, fill_opacity=0.7))
fgp = folium.FeatureGroup(name="Population color")
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), style_function=lambda x: {'fillColor':'pink' if x['properties']['POP2005'] < 10000000 else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map1.html")