import streamlit as st
import pandas as pd
import pyplot from matplotlib as plt

st.write('hello world')

df = pd.read_csv('Bastar Craton.csv')
st.dataframe(df)

