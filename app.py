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

rules = pd.read_csv("Notebooks/datasets/rules.csv")
df = pd.DataFrame(rules)
 

var = df[df['antecedents']==selected_option]

var2 = var.sort_values(by = "support", ascending=False)

toprecommendations =  var2.head(5)

#error - when you try to compare a pandas column to a list but they have different lengths
# plotting of bar chart
bar_chart = px.bar(toprecommendations, x='support', y='consequents', orientation='h')
bar_chart.update_layout(yaxis=dict(autorange="reversed"))

st.plotly_chart(bar_chart)
 
# creating shopping lis with top recommendations
selected_option_2 = st.selectbox("Select recommendation to add to list:",toprecommendations["consequents"])
st.write("You selected: ", selected_option_2)

shopping_list = []
shopping_list.append(selected_option_2)

st.write(shopping_list)