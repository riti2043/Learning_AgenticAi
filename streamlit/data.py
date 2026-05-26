import streamlit as st
import pandas as pd 

st.title("dashboard")
file=st.file_uploader("upload csv file",type=["csv"])

if file:
    df=pd.read_csv(file)
    st.subheader("data preview")
    st.dataframe(df)

if file:
     cities = df["City"].unique()
    selected_city = st.selectbox("Filter by cities", cities)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)