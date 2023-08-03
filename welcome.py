import streamlit as st
import pandas as pd
import os
#import pyplot from matplotlib as plt

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)
st.write(file_name_list)

  #df = pd.read_csv('Bastar Craton.csv')
  #st.dataframe(df)

#el_list = df.columns.tolist()[27:80]
#x_axis = st.selectbox('Select Element', el_list)



