import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lon = data["LON"]
lat = data["LAT"]
nam = data["NAME"]
elev = data["ELEV"]
map = folium.Map(location=[45, -122], zoom_start=6, tiles="Stamen Terrain")

def color_producer(el):
    if el < 1000:
        return 'green'
    elif 1000 <= el < 3000:
        return 'orange'
    else:
        return 'red'

fgv = folium.FeatureGroup(name="Volcanoes")
for lt, ln, nam, el in zip(lat, lon, nam, elev):
    b = "Volcano name: " + nam + " \n"
    c = "Elevation: " + str(el) + " m"
    a=b + c
    fgv.add_child(folium.CircleMarker(location=[lt, ln],
                                     radius=5+el*0.001,
                                     popup=a,
                                     fill_color=color_producer(el),
                                     color='grey',
                                     fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=(open('world.json', 'r', encoding='utf-8-sig').read()),
                            style_function=lambda x: {'fillColor':'yellow'
                            if x['properties']['POP2005'] < 10000000
                            else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000
                            else 'red' }))

map.add_child(fgp)
map.add_child(fgv)
map.add_child((folium.LayerControl()))

map.save("Map1.html")
