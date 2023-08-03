import streamlit as st
import pandas as pd
import os
import numpy as np
from bokeh.plotting import figure

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

    std_choice = st.radio("Select Number of Standard Deviations", [1, 2, 3], index=1)

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
