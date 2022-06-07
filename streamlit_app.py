import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

my_cnx=snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list")
got_row = my_cur.fetchall()
st.header('List contains:')
st.dataframe(got_row)
#st.write(got_row)

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')

# get_fruit=st.text_input('What fruit would you like to know about?', 'Kiwi')
# st.write('User entered ',get_fruit)
# fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+get_fruit)
# fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())

add_fruit=st.text_input('What fruit would you like to add?', 'jackfruit')
st.header("User added "+add_fruit)

# st.title('New Diner!')

# st.header('Menu')

# st.text('Food items!')
# st.text(fruityvice_response.json())
# fruits_selected=st.multiselect("Pick some fruits!",list(my_fruit_list.index), ['Avocado'],['Strawberries'])
# fruits_to_show=my_fruit_list.loc[fruits_selected]
# st.dataframe(fruityvice_normalised)
