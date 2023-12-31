import streamlit as st
import pandas as pd
import os
import numpy as np
from bokeh.plotting import figure
import folium
from streamlit_folium import folium_static

tab1, tab2, tab3 = st.tabs(["select", "datavis", "map"])

with tab1:
    file_name_list = []
    for i in os.listdir():
        if i.endswith('.csv'):
            file_name_list.append(i)
    
    selected_files = st.multiselect('Select CSV files', file_name_list)

with tab2:
    if selected_files:
        dfs = [pd.read_csv(file) for file in selected_files]
        df = pd.concat(dfs, ignore_index=True)
    
        el_list = df.columns.tolist()[27:80]
        
        col1, col2, col3 = st.columns(3)
    
        with col1:
            el1 = st.selectbox('Select Element_X', el_list)
    
        with col2:
            el2 = st.selectbox('Select Element_Y', el_list)
            
        with col3:
            std_choice = st.radio("Select Number of Standard Deviations", [1, 2, 3], index=1)
    
        x = df[el1] / 1e4  # Selecting the entire column for x axis and scaling by 1e4
        y = df[el2] / 1e4  # Selecting the entire column for y axis and scaling by 1e4
    
        mean_y = np.mean(y)
        std_y = np.std(y)
    
        # Calculate upper and lower bounds for ± standard deviation
        upper_bound = mean_y + std_choice * std_y
        lower_bound = mean_y - std_choice * std_y
    
        p = figure(title='Mean and ± Standard Deviation', x_axis_label=el1, y_axis_label=el2)
    
        # Plot the mean as a line
        p.line(x, mean_y, line_color='blue', legend_label='Mean '+ el2)
    
        # Plot the upper bound of standard deviation as a line
        p.line(x, upper_bound, line_color='green', line_dash='dashed', legend_label='Upper Bound')
    
        # Plot the lower bound of standard deviation as a line
        p.line(x, lower_bound, line_color='red', line_dash='dashed', legend_label='Lower Bound')

    # Add data points to the plot
    p.circle(x, y, legend_label="Data Points")
    st.bokeh_chart(p, use_container_width=True)

with tab3:
    if selected_files:
        df_map = df[['Latitude (Min)', 'Longitude (Min)', el1, el2]]
        df_map.columns = ['Latitude', 'Longitude', el1, el2]

        # Center the map at the mean of the data points
        center = [df_map['Latitude'].mean(), df_map['Longitude'].mean()]
        m = folium.Map(location=center, zoom_start=10)

        # Add data points to the map
        for idx, row in df_map.iterrows():
            popup_text = f"{el1}: {row[el1]}, {el2}: {row[el2]}"
            folium.Marker(location=[row['Latitude'], row['Longitude']], popup=popup_text).add_to(m)

        # Display the map
        folium_static(m)
