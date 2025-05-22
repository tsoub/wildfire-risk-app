import folium

def generate_map(lat, lon, address):
    m = folium.Map(location=[lat, lon], zoom_start=13)
    folium.Marker([lat, lon], tooltip=address).add_to(m)
    return m
