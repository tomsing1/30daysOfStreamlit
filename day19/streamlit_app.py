import streamlit as st

st.set_page_config(layout="wide")

st.title('How to layout your Streamlit app')

with st.expander('About this app'):
    st.write('This app shows the various ways on how you can layout your Streamlit app.')
    st.image('https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png', width=250)


with st.sidebar:
    st.header("Input")
    name = st.text_input('What is your name?')
    emoji = st.selectbox('Choose an emoji', ['', '😄', '😆', '😊', '😍', '😴', '😕', '😱'])
    food = st.selectbox('What is your favorite food?', ['', 'Tom Yum Kung', 'Burrito', 'Lasagna', 'Hamburger', 'Pizza'])

st.header('Output')
col1, col2, col3 = st.columns(3)
with col1:
    if name:
        st.write(f'👋 Welcome {name}!')
    else:
        st.write('👈 Please enter your **name**!')
with col2:
    if emoji:
        st.write(f'{emoji} is your favorite emoji!')
    else:
        st.write('👈 Please choose an **emoji**!')
with col3:
    if food:
        st.write(f'🍴 **{food}** is your favorite **food**')
    else:
        st.write('👈 Please choose your favorite **food**!')