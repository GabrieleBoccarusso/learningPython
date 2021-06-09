import folium
map = folium.Map(location = [30, 50], zoom_start = 6, tiles = "stamen terrain")

fg = folium.FeatureGroup(name = "main feature group")

fg.add_child(folium.map.Marker(location = [30, 40], 
                                popup = "hi", 
                                icon = folium.Icon(color = "red")))

map.add_child(fg)

map.save("map.html")
