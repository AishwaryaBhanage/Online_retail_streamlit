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

st.dataframe(data)

#plot a bar chart
st.pyplot()