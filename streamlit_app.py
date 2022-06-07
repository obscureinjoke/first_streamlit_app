import streamlit as st
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalised
  


# my_cur = my_cnx.cursor()

# st.header('List contains:')
# st.dataframe(got_row)
# st.write(got_row)
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("SELECT * from fruit_load_list")
    return my_cur.fetchall()

if st.button('Get Fruit Load List'):
  my_cnx=snowflake.connector.connect(**st.secrets["snowflake"])
  my_data_rows=get_fruit_load_list()
  st.dataframe(my_data_rows)


st.header('Fruit advice!')
try:
  fruit_choice=st.text_input('What fruit would you like to know about?')
  if not fruit_choice:
    st.error("Please enter a type of fruit.")
  else:
   # fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
   # fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())
    back_from_function=get_fruityvice_data(fruit_choice)
   # st.dataframe(fruityvice_normalised)
    st.dataframe(back_from_function)
 
except URLError as e:
  st.error()
#my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
#my_fruit_list=my_fruit_list.set_index('Fruit')

# get_fruit=st.text_input('What fruit would you like to know about?', 'Kiwi')
# st.write('User entered ',get_fruit)
# fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+get_fruit)
# fruityvice_normalised=pandas.json_normalize(fruityvice_response.json())

#add_fruit=st.text_input('What fruit would you like to add?', 'jackfruit')
#st.header("User added "+add_fruit)

# st.title('New Diner!')

# st.header('Menu')

# st.text('Food items!')
# st.text(fruityvice_response.json())
# fruits_selected=st.multiselect("Pick some fruits!",list(my_fruit_list.index), ['Avocado'],['Strawberries'])
# fruits_to_show=my_fruit_list.loc[fruits_selected]
# st.dataframe(fruityvice_normalised)
