import streamlit as st
import pandas as pa

my_fruit_list = pa.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.title('New Diner!')

st.header('Menu')

st.text('Food items!')
streamlit.dataframe(my_fruit_list)
