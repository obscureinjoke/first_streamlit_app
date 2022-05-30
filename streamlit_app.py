import streamlit as st
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

st.title('New Diner!')

st.header('Menu')

st.text('Food items!')

st.dataframe(my_fruit_list)
