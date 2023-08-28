import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError


streamlit.title('My Parents New Healthy Diner')

streamlit.title('Breakfast Menu')

streamlit.title('🥣 Omega 3 and Blue Berry Oatmeal')
streamlit.title('🥗 Kale, Spinach, and Rocket Smoothe')
streamlit.title('🐔 Hard-Boiled Free Range Egg')
streamlit.title('🥑🍞 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
# create the repeatable code block (called a function)
def get_fruityvise_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
streamlit.header("Fruityvice Fruit Advice!")
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information.")
  else:
      back_from_function =  get_fruityvise_data(fruit_choice) 
      streamlit.dataframe(back_from_function)

except URLError as e:
    streamlit.error()
    streamlit.stop()

#import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_data_row = my_cur.fetchone()
#streamlit.text("Hello from Snowflake:")
#streamlit.text(my_data_row)

#my_cur = my_cnx.cursor()
#my_cur.execute("select * from fruit_load_list")


streamlit.header("The fruit load list contains:")
# Snowflake related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
        
# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"]) 
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
def  insert_row_snowflake(new_fruit):
    with my_cnx.cursor as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thanks for adding" + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a FRuit to the list'):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function=insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

#this will not work correctly, but just go with it for now


