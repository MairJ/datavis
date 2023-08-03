import streamlit as st
import pandas as pd
import geopandas as gpd
import os
import folium

file_name_list = []
for i in os.listdir():
    if i.endswith('.csv'):
        file_name_list.append(i)

# st.write(file_name_list) # Test

selected_files = st.multiselect('Select CSV files', file_name_list)
if selected_files:
    dfs = [pd.read_csv(file) for file in selected_files]
    df = pd.concat(dfs, ignore_index=True)

    el_list = df.columns.tolist()[27:80]

    col1, col2 = st.columns(2)

    with col1:
        el1 = st.selectbox('Select Element_X', el_list)

    with col2:
        el2 = st.selectbox('Select Element_Y', el_list)

    x = df[el1] / 1e4  # Selecting the entire column for x axis and scaling by 1e4
    y = df[el2] / 1e4  # Selecting the entire column for y axis and scaling by 1e4

    st.write("Data Points:")
    st.write(pd.DataFrame({el1: x, el2: y}))

    # Create a GeoDataFrame for the selected data points
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(x, y))

    # Center the map at the mean of the data points
    center = [gdf.geometry.y.mean(), gdf.geometry.x.mean()]
    m = folium.Map(location=center, zoom_start=10)

    # Add data points to the map
    for idx, row in gdf.iterrows():
        folium.Marker(location=[row['Latitude (Min)'], row['Longitude (Min)']],
                      popup=f"{el1}: {row[el1]}, {el2}: {row[el2]}").add_to(m)

    # Display the map
    folium_static(m)
