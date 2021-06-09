import folium
import pandas as pd 

def determinate_color_and_radius(elev) -> str:
    ret_col: str = "red"
    ret_radius: int = 15
    if elev <= 1000:
        ret_col = "green"
        ret_radius = 5
    elif elev <= 3000:
        ret_col = "orange"
        ret_radius = 10

    return ret_col, ret_radius

data = pd.read_csv("mapping-data/Volcanoes.txt")

map = folium.Map(location = [48.7767982,-121.8109970], zoom_start = 10, tiles = "stamen terrain")

lat = list(data.LAT)
lon = list(data.LON)
name = list(data.NAME)
elev = list(data.ELEV)

fg = folium.FeatureGroup(name = "main feature group")

for i in range(len(lat)):
    # fg.add_child(folium.map.Marker(location = [lat[i], lon[i]], 
    #                                 popup = name[i], 
    #                                 icon = folium.Icon(color = "red")))
    col, rad = determinate_color_and_radius(elev[i])
    fg.add_child(folium.CircleMarker(location = [lat[i], lon[i]],
                                    popup = name[i],
                                    radius = rad,
                                    color = col,
                                    fill = True,
                                    fill_opacity = 1))

fg.add_child(folium.GeoJson(data = open("mapping-data/world.json", 'r', encoding = "utf-8-sig").read(),
                            style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fg)
map.add_child(folium.LayerControl())

map.save("map.html")
