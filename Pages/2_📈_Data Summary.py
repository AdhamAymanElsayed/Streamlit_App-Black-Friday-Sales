import streamlit as st
import numpy as np
import pandas as pd
df = pd.read_csv('Clean.csv')
df = df.astype({'User_ID':'object','Marital_Status':'object','Product_Category':'object','Occupation':'object'},errors='ignore')


st.header('About Dataset')
st.write('________')
st.subheader('Dataset history:')

x = '''A retail company “ABC Private Limited” wants to understand the customer purchase behaviour (specifically, purchase amount) against various products of different categories. They have shared purchase summary of various customers for selected high volume products from last month.

The dataset also contains customer demographics (age, gender, marital status, city type, stay in current city), product details (product id and product category) and Total purchase amount from last month.'''
st.write(x)
df = pd.read_csv('clean.csv',index_col='Unnamed: 0')
df = df.astype({'User_ID':'object','Marital_Status':'object','Product_Category':'object','Occupation':'object'},errors='ignore')
st.write('-------------------------------------------------')
st.subheader('Target Cloumn')
st.write('Purchase column is the Target Variable')
st.write('_________')
st.subheader('Data Header:')
st.write(df.head())
st.write('___')

st.subheader('Data Statistics:')
st.write(df.describe())
st.write('___')
st.subheader('Conclusion:')
st.write(


    '''
* Males of age between 18-45 are purchasing more number of products.

* Though the more number of purchases are made by males, the average money spent on each procuct by both males and females is same.

* The number of purchases and the total money spent is more for the age groups between 18-45 with 26-35 being the most.

* More than 59% people are unmarried and 60% of the revenue comes from unmarried people.

* People who stayed for 1 year are purchasing more items. And everyone are purchasing more or less same price items.

* Products of category [5,1,8] are being purchased more.

* Product with ids [P00265242, P00110742, P00025442] are being purchased more.'''
)