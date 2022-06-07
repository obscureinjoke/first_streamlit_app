import streamlit as st
import pandas
import requests

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/watermelon)
st.title('New Diner!')

st.header('Menu')

st.text('Food items!')
st.text(fruityvice_response)
fruits_selected=st.multiselect("Pick some fruits!",list(my_fruit_list.index), ['Avocado'],['Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)
