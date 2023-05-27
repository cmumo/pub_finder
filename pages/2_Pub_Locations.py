import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

df = pd.read_csv('openpubs_cleaned.csv')

st.header("Google maps not working? Don't worry. Use this site to find the nearest pub")
st.subheader("Use the filters below to see nearby pubs")

def uk_viz(a, b):
    num = df[df[a] == b]
    st.write("There are a total of {} Pubs available at  {}".format(len(num), b))
    m = folium.Map(location=[num.latitude.mean(), num.longitude.mean()], zoom_start=13)
    folium.Marker(location=[num.latitude.mean(), num.longitude.mean()], icon=folium.Icon(icon='star', color='red'), popup='Your Location', size=155).add_to(m)

    for i, row in num.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=f"<strong>{row['name']}</strong><br>{row['postcode']}<br>Address is -<br>{row['address']}",
            icon=folium.Icon(icon='beer', prefix='fa', color='green')
        ).add_to(m)
    folium_static(m)

st.header("Pub Location Filter")
option = st.radio(label="Filter pubs by: ",
                options=["Name", "Postcode", "Local Authority"], index=0, key="filter")

if option == "Name":
    loc = df["name"].unique()
    st.subheader("Do you know the pub by name?")
    location = st.selectbox("Choose the name of the pub: ", loc)
    button = st.button("Search")
    if button:
        uk_viz("name", location)

elif option == "Postcode":
    loc = df["postcode"].unique()
    st.subheader("Do you know the pubs based on postal code?")
    location = st.selectbox("Choose the postal code of the pub: ", loc)
    button = st.button("Search")
    if button:
        uk_viz("postcode", location)

elif option == "Local Authority":
    loc = df["local_authority"].unique()
    st.subheader("Find the pubs based on location")
    location = st.selectbox("Choose the location of the pub: ", loc)
    button = st.button("Search")
    if button:
        uk_viz("local_authority", location)
