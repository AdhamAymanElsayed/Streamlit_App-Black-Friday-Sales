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
radio = st.sidebar.radio('',('Univariate','Bivariate','Multivariate'))
if radio == 'Univariate':
    st.header('Univariate')
    st.subheader('Categorical Variables')
    st.write('_________')     
    box1 = st.selectbox('Select Column',('Gender','Age','City Category','Marital Status','Stay in Current City Years','Occupation'))

    if box1 =='Gender':
        fig1 = px.pie(df , values= df['Gender'].value_counts().values,names =df['Gender'].value_counts().index,hole=.4,title='Percentage of Gender')
        st.plotly_chart(fig1)
    elif box1 =='Age':
        fig2 = px.pie(df , values= df['Age'].value_counts().values,names =df['Age'].value_counts().index ,hole=.4,title='Percentage of Age')
        st.plotly_chart(fig2)
    elif box1 =='City Category':
        fig3 = px.pie(df , values= df['City_Category'].value_counts().values,names =df['City_Category'].value_counts().index ,hole=.4,title='Percentage of City Category')
        st.plotly_chart(fig3)
    elif box1 =='Marital Status':
        fig4 = px.pie(df , values= df['Marital_Status'].value_counts().values,names =['Single','Married'] ,hole=.4,title='Percentage of Marital Status')
        st.plotly_chart(fig4)
    elif box1 =='Stay in Current City Years':
        fig5 = px.pie(df , values= df['Stay_In_Current_City_Years'].value_counts().values,names =df['Stay_In_Current_City_Years'].value_counts().index ,hole=.4,title='Percentage of Stay in Current City Years')
        st.plotly_chart(fig5)
    elif box1 == 'Occupation':
        fig7 = px.pie(df , values= df['Occupation'].value_counts().values,names =df['Occupation'].value_counts().index ,hole=.4,title='Percentage of Occupation')
        st.plotly_chart(fig7)
    
    st.write('_______')
    st.subheader('Numerical Variables')
    st.write('_________')
    
    st.write('Purchase')
    fig6 = px.histogram(data_frame=df,x='Purchase')
    st.plotly_chart(fig6)
elif radio == 'Bivariate':
    st.header('Bivariate')
    st.write('_________')

    Top_Id_purchased = df.groupby('Product_ID')['Purchase'].sum().sort_values(ascending  = False).head(10)
    fig9 = plt.figure(figsize=(10,5))
    plt.title('Highest Product ID are Purchesed')
    plt.xticks(rotation = -20)
    plt.ylabel('Purchase')
    sns.barplot(data=df, x=Top_Id_purchased.index ,y=Top_Id_purchased.values)
    st.pyplot(fig9)
    st.write('_________')

    Top_Id_purchased2 = df.groupby('User_ID')['Purchase'].sum().sort_values(ascending  = False).head(10)
    fig8 = plt.figure(figsize=(10,5))
    plt.title('Highest User ID are Purchese')
    plt.xticks(rotation = -20)
    plt.ylabel('Purchase')
    sns.barplot(data=df, x=Top_Id_purchased2.index ,y=Top_Id_purchased2.values,order=Top_Id_purchased2.index)
    st.pyplot(fig8)
    st.write('_________')
    #fig8 = px.bar(data_frame=df, x=Top_Id_purchased2.index ,y=Top_Id_purchased2.values,title='Highest User ID are Purchesed',labels =dict(x = 'User ID',y = 'Purchase'),color_discrete_sequence=[ "Green"])
    #fig8.update_xaxes(tickangle=25)
    #t.plotly_chart(fig8)

    fig10 = plt.figure(figsize=(10,5))
    plt.title('Purchese VS Age')
    plt.ylabel('Purchase')
    sns.barplot(data=df, x='Age' ,y='Purchase',estimator='sum')
    st.pyplot(fig10)
    st.write('_________')

    #fig10 =px.bar(data_frame=df,x='Age',y='Purchase',color_discrete_sequence=[ "Red"],title='Purchese VS Age')
    #st.plotly_chart(fig10)
    fig11 = plt.figure(figsize=(10,5))
    plt.title('Purchese VS Gender')
    plt.ylabel('Purchase')
    sns.barplot(data=df, x='Gender' ,y='Purchase',estimator='sum')
    st.pyplot(fig11)
    st.write('_________')

    #fig11 =px.bar(data_frame=df,x='Gender',y='Purchase',color_discrete_sequence=[ "Red"],title='Purchese VS Gender')
    #st.plotly_chart(fig11)
    fig12 = plt.figure(figsize=(10,5))
    plt.title('Purchese VS Marital Status')
    plt.ylabel('Purchase')
    sns.barplot(data=df, x='Marital_Status' ,y='Purchase',estimator='sum')
    st.pyplot(fig12)
    st.write('_________')   

    #fig12 =px.bar(data_frame=df,x='Marital_Status',y='Purchase',color_discrete_sequence=[ "Red"],title='Purchese VS Marital Status')
    #st.plotly_chart(fig12)
    fig12 = plt.figure(figsize=(10,5))
    plt.title('Purchese VS City Category')
    plt.ylabel('Purchase')
    sns.barplot(data=df, x='City_Category' ,y='Purchase',estimator='sum')
    st.pyplot(fig12)
    st.write('_________')

    #fig13 =px.bar(data_frame=df,x='City_Category',y='Purchase',color_discrete_sequence=[ "Red"],title='Purchese VS City Category')
    #st.plotly_chart(fig13)
    fig13 = plt.figure(figsize=(10,5))
    plt.title('Purchese VS Occupation')
    plt.ylabel('Purchase')
    sns.barplot(data=df, x='Occupation' ,y='Purchase',estimator='sum')
    st.pyplot(fig13)
    #st.write('_________')    



elif radio == 'Multivariate':
    st.header('Multivariate')
    st.write('_________')
    fig15 = plt.figure(figsize=(10,5))
    plt.title('Product_category vs Purchase with respect to Gender')
    
    sns.barplot(data=df, x  = 'Product_Category' , y = 'Purchase' , hue= 'Gender')
    st.pyplot(fig15)
    st.write('_______')
    fig16 =plt.figure(figsize=(10,5))
    plt.title('Product_category vs Purchase with respect to City Category')
    sns.barplot(data=df , x  = 'Product_Category' , y = 'Purchase' , hue= 'City_Category')
    st.pyplot(fig16)
    st.write('_______')
    fig17 =plt.figure(figsize=(10,5))
    plt.title('Age vs Purchase with respect to Gender')
    sns.barplot(data=df , x  = 'Age' , y = 'Purchase' , hue= 'Gender')
    st.pyplot(fig17)
    st.write('_______')
    fig18 =plt.figure(figsize=(10,5))
    plt.title('Product_category vs Purchase with respect to Age')
    sns.barplot(data=df , x  = 'Product_Category' , y = 'Purchase' , hue= 'Age')
    st.pyplot(fig18)
    

