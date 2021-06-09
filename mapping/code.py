import folium
import pandas as pd 

data = pd.read_csv("mapping-data/Volcanoes.txt")

map = folium.Map(location = [48.7767982,-121.8109970], zoom_start = 10, tiles = "stamen terrain")

lat = list(data.LAT)
lon = list(data.LON)
name = list(data.NAME)

fg = folium.FeatureGroup(name = "main feature group")

for i in range(len(lat)):
    fg.add_child(folium.map.Marker(location = [lat[i], lon[i]], 
                                    popup = name[i], 
                                    icon = folium.Icon(color = "red")))

map.add_child(fg)

map.save("map.html")
