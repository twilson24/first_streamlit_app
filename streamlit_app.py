import streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header("Breakfast Menu")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 HAvocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
fruits_selected = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Let's put a pick list here so they can pick the fruit they want to include 



# Display the table on the page.
streamlit.dataframe(fruits_to_show)
