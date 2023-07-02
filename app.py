import pandas as pd
import streamlit as st
import plotly.express as px

#set the title of page
st.set_page_config(page_title="Shopping list using recommendations")
st.header("Shopping list using recommendations")
st.subheader("Create your own shopping list without any miss...")

#run command - streamlit run app.py
items_set = "Notebooks/datasets/Items_sets.csv"
data = pd.read_csv(items_set)

#unique items list
products_data  = "Notebooks/datasets/products.csv"
products = pd.read_csv(products_data)

#drop down for select product
selected_option = st.selectbox("Select product to view recommendations:",products)
st.write("You selected: ", selected_option)

print(selected_option)
#plot a bar chart


