import streamlit as st

st.header("st.multiselect")
colors = st.multiselect(
    "What are your favorite colors?", ("red", "blue", "green"), ("red", "blue")
)
st.write("Your favorite colors are", colors)
