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

x = df[el1]/1e4  # Selecting the entire column for x axis
y = df[el2]/1e4  # Selecting the entire column for y axis

p = figure(title='Simple line example', x_axis_label=el1, y_axis_label=el2)

p.circle(x, y, legend_label="Data Points")

st.bokeh_chart(p, use_container_width=True)
