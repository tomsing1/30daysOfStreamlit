import streamlit as st

st.header("st.checkbox")
st.write("What would you like to order?")
icecream = st.checkbox("Ice cream")
coffee = st.checkbox("Coffee")
cola = st.checkbox("Cola")

if icecream:
    st.write("Great! Here's some more :icecream:")
if coffee:
    st.write("Here is your coffee.")
if cola:
    st.write("Enjoy your coke!")