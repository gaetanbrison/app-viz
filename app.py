
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
from PIL import Image



image_nyu = Image.open("nyu.png")
st.image(image_nyu, width=100)

st.title("Wine exploration")


df =pd.read_csv("winequality-red.csv")

num = st.number_input('No of rows',5,10)
st.dataframe(df.head(num))

st.dataframe(df.describe())


dfnull = df.isnull().sum()/len(df)*100
totalmiss = dfnull.sum().round(2)

st.write("This the percentage of missing values",totalmiss)




st.write(" Visualization Part")

list_variables = df.columns
user_selection = st.multiselect("Select two variables",list_variables,["quality","chlorides"])

quality_min, quality_max = st.sidebar.slider('Select Quality Range', min_value=int(df['quality'].min()), max_value=int(df['quality'].max()), value=(int(df['quality'].min()), int(df['quality'].max())))
citric_acid_min, citric_acid_max = st.sidebar.slider('Select Citric Acid Range', min_value=float(df['citric acid'].min()), max_value=float(df['citric acid'].max()), value=(float(df['citric acid'].min()), float(df['citric acid'].max())))

filtered_df = df[(df['quality'] >= quality_min) & (df['quality'] <= quality_max) &  (df['chlorides'] >= citric_acid_min) & (df['chlorides'] <= citric_acid_max) ]


tab1, tab2 = st.tabs(["Line Chart","Bar Chart"])

tab1.title("Line Chart")
tab1.line_chart(data=filtered_df, x=user_selection[0],y=user_selection[1])

tab2.title("Line Chart")
tab2.bar_chart(data=filtered_df, x=user_selection[0],y=user_selection[1])


if st.button("Generate Report"):
  import streamlit.components.v1 as components

  st.title("Sweetviz Report of the Data")
  report_path="report.html"
  HtmlFile = open(report_path,'r',encoding='utf-8')
  source_code = HtmlFile.read()
  components.html(source_code,height=1000,width=1000)

