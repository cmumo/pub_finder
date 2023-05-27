import streamlit as st
import pandas as pd
import numpy as np
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

df = pd.read_csv('openpubs_cleaned.csv')

st.title("-- Nearest Pub Finder --")

st.header("Search for pubs around")
error_msg1 = "Latitude should be between 49.8924 and 60.7650."
lat = st.number_input("Enter Your Latitude:", min_value=49.8924, max_value=60.7650, step=0.0001, format="%.4f")

if not 49.8924 <= lat <= 60.7650:
    st.error(error_msg1)

error_msg2 = "Longitude should be between -7.3845 and 1.7578."
long = st.number_input("Enter Your Longitude:", min_value=-7.3845, max_value=1.7578, step=0.0001, format="%.4f")

if not -7.3845 <= long <= 1.7578:
    st.error(error_msg2)

ans = np.array([lat, long])
arr = np.transpose(np.array([df.latitude, df.longitude]))

dis = np.sqrt(np.sum((arr - ans) ** 2, axis=1))
dis = dis.tolist()
newdis = [round(i, 4) for i in dis]
df["Distance"] = newdis
top_5_pubs = df.sort_values(by='Distance').head(5)
st.write("We have found the 5 Nearest Pubs from your location")

st.subheader("5 Nearest Pubs")
rg = top_5_pubs[["name", "postcode", "latitude", "longitude", "local_authority", "Distance"]]
st.dataframe(rg)

m = folium.Map(location=[lat, long], zoom_start=13)
folium.Marker(location=[lat, long], icon=folium.Icon(icon='star', color='red'), popup='You are here').add_to(m)

for i, row in top_5_pubs.iterrows():
    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=f"<strong>{row['name']}</strong><br>{row['postcode']}<br>{row['Distance']} kilometers away",
        icon=folium.Icon(icon='beer', prefix='fa', color='green')
    ).add_to(m)

folium_static(m)

st.header("Enjoy!")
st.balloons()

