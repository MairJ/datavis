import streamlit as st
import pandas as pd
import os
#import matplotlib.pyplot as plt

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)
# st.write(file_name_list) # Test

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

el_list = df.columns.tolist()[27:80]
x_axis = st.selectbox('Select Element', el_list)

options = st.multiselect('select location', file_name_list)#, file_name_list[0])

st.write('You selected:', options)

x = [1,2,3,4,5,6]
y = [1,2,3,4,5,6]

p = figure(
  title = 'simple line example',
  x_axis_label = 'x',
  y_axis_label = 'y'
)
st.bokeh_chart(p, use_container_width = 2)


"""
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='options',
    mime='text/csv',
)
"""
"""
datasheet_list = file_name_list
def plot_datasheets(el_x, el_y, datasheet_list):
    for i in datasheet_list:
        plt.scatter(data[el_x]/10000, data[el_y]/10000, label = i[:-4])
    plt.xlabel(el_x + ' (wt%)')
    plt.ylabel(el_y+ ' (wt%)')
    plt.legend()
    plt.show()

plot_datasheets('Mg', 'Si', datasheet_list)
"""
