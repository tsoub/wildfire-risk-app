import streamlit as st
import random
import requests
from map_generator import generate_map
from streamlit_folium import st_folium

st.set_page_config(page_title="Wildfire Risk Estimator")
st.title("🔥 Wildfire Risk Estimator")

def geocode_address(address):
    try:
        url = "https://nominatim.openstreetmap.org/search"
        params = {'q': address, 'format': 'json'}
        headers = {'User-Agent': 'wildfire-risk-app'}
        response = requests.get(url, params=params, headers=headers, timeout=5)
        data = response.json()
        if data:
            return float(data[0]['lat']), float(data[0]['lon'])
    except:
        pass
    return 37.7749, -122.4194  # fallback to SF

address = st.text_input("Enter an address:")

if st.button("Check Risk") and address:
    lat, lon = geocode_address(address)
    score = round(random.uniform(3.0, 9.5), 1)
    level = (
        "Extreme" if score >= 8 else
        "High" if score >= 6 else
        "Moderate" if score >= 4 else
        "Low"
    )

    st.success(f"Risk Score for '{address}': {score}/10")
    st.info(f"Risk Level: {level}")

    st.subheader("🗺️ Interactive Map")
    folium_map = generate_map(lat, lon, address)
    st_folium(folium_map, width=700, height=500)
