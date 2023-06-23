import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Clean.csv')
df = df.astype({'User_ID':'object','Marital_Status':'object','Product_Category':'object','Occupation':'object'},errors='ignore')

st.title('Black Friday Sales Dataset Analysis')
st.write('_____')

choose  = st.selectbox('Choose View to show dataset.',('Hidden','View'))
if choose == 'View':
    st.dataframe(df)

st.write('_________')
radio = st.radio('',('Univariate','Bivariate','Multivariate'))
if radio == 'Univariate':
    st.header('Univariate')
    st.subheader('Categorical Variables')
    st.write('_________')     
    box1 = st.selectbox('Select Column',('Gender','Age','City_Category','Marital_Status'))

    fig1 = px.pie(df , values= df[box1].value_counts().values,names =df[box1].value_counts().index,hole=.4,title=f'Percentage of {box1}')
    st.plotly_chart(fig1)
        
    st.write('_______')
    st.subheader('Numerical Variables')
    st.write('_________')
        
    st.write('Purchase')
    fig2 = px.histogram(data_frame=df,x='Purchase')
    st.plotly_chart(fig2)

elif radio == 'Bivariate':
    st.header('Bivariate')
    st.write('_________')
    box2 = st.selectbox('Select Column',('Product_ID','User_ID'))
    Top_Id_purchased = df.groupby(box2)['Purchase'].sum().sort_values(ascending  = False).head(10)
    fig3 = px.bar(data_frame=df, x=Top_Id_purchased.index ,y=Top_Id_purchased.values,title=f'Highest {box2} are Purchesed',color_discrete_sequence=[ "Purple"],labels =dict(x = box2,y = 'Purchase'))
    fig3.update_xaxes(tickangle=-25)
    st.plotly_chart(fig3)
    st.write('_________')

    box3 = st.selectbox('Select Column with respect to target column purchase',('Gender','Age','City_Category','Marital_Status',))
    fig4 =px.bar(data_frame=df,x=box3,y='Purchase',title=f'Purchese VS {box3}')
    st.plotly_chart(fig4)
  
elif radio == 'Multivariate':
    st.header('Multivariate')
    st.write('_________')

    box4 = st.selectbox('Select Column with respect to target column purchase',('Gender','Age','City_Category'))
    fig5 =px.bar(data_frame=df,x='Product_Category',y='Purchase',color=box4,title=f'Product_category vs Purchase with respect to {box4}')
    st.plotly_chart(fig5)







    

