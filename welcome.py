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

options = st.multiselect('select location', file_name_list, file_name_list[0])

st.write('You selected:', options)

"""
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='options',
    mime='text/csv',
)
"""
