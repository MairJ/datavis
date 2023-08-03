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

selected_file = st.selectbox('Select a CSV file', file_name_list)
df = pd.read_csv(selected_file)
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
el1 = st.selectbox('Select Element_X', el_list)
el2 = st.selectbox('Select Element_Y', el_list)

x = df[el1]  # Selecting the entire column for x axis
y = df[el2]  # Selecting the entire column for y axis

mean_y = np.mean(y)
std_y = np.std(y)

# Calculate upper and lower bounds for ± standard deviation
upper_bound = mean_y + std_y
lower_bound = mean_y - std_y

p = figure(title='Mean and ± Standard Deviation', x_axis_label=el1, y_axis_label=el2)

# Plot the mean as a line
p.line(x, mean_y, line_color='blue', legend_label='Mean')

# Plot the upper bound of standard deviation as a line
p.line(x, upper_bound, line_color='green', line_dash='dashed', legend_label='Upper Bound')

# Plot the lower bound of standard deviation as a line
p.line(x, lower_bound, line_color='red', line_dash='dashed', legend_label='Lower Bound')

# Add data points to the plot
p.circle(x, y, legend_label="Data Points")

st.bokeh_chart(p, use_container_width=True)
