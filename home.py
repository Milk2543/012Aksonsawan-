import streamlit as st
import pandas as pd

st.title("Website Developing using Python")
st.headar("Website Developing using Python")

st.image('./img/11.jpg')
st.subheader("Aksonsawan Deboot")

dt=pd.read_csv('./data/iris-3.csv')
st.header("ข้อมูลดอกไม้")
st.write(dt.head(10))
