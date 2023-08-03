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
x_axis = st.selectbox('Select Element', el_list)
el1, el2 = st.multiselect('Select elements for x and y axes', el_list[:2], default=el_list[:2])

x = df.loc[5:26, el1]
y = df.loc[5:26, el2]

p = figure(title='Simple line example', x_axis_label=el1, y_axis_label=el2)

p.circle(x, y, legend_label="Data Points")

st.bokeh_chart(p, use_container_width=True)
