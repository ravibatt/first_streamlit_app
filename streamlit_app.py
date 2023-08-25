import streamlit
import requests
import pandas


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

#fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#streamlit.text(fruityvice_response)
#streamlit.dataframe(fruits_to_show)

