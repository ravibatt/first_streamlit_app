import streamlit
import pandas


streamlit.title('My Parents New Healthy Diner')

streamlit.title('Breakfast Menu')

streamlit.title('🥣 Omega 3 and Blue Berry Oatmeal')
streamlit.title('🥗 Kale, Spinach, and Rocket Smoothe')
streamlit.title('🐔 Hard-Boiled Free Range Egg')
streamlit.title('🥑🍞 Avacado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
