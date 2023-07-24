import streamlit as st

st.header("st.selectbox")
color = st.selectbox("What is your favorite color?", ("red", "blue", "green"))
st.write("Your favorite color is", color)
