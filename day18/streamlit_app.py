import streamlit as st
import pandas as pd

st.title('st.file_uploader')
st.subheader('CSV file upload')

uploaded_file = st.file_uploader('Choose a CSV file')
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("DataFrame")
    st.write(df)
    st.subheader("Descriptive statistics")
    st.write(df.describe())
else:
    st.write("Please upload a CSV file :point_up:")