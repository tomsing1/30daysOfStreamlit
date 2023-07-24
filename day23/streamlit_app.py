import streamlit as st

st.title('st.experimental_get_query_params')
with st.expander('About this app'):
    st.write("`st.experimental_get_query_params` allows the retrieval of query \
    parameters directly from the URL of the user's browser.")

st.header('1. Instructions')
st.markdown('''
    In the above URL bar of your internet browser, append the following:
    `?name=Jack&surname=Beanstalk`
    after the base URL `http://localhost:8501?firstname=Jack`
    such that it becomes
    `http://localhost:8501?firstname=Jack&surname=Beanstalk`
    ''')

st.header('2. Contents of st.experimental_get_query_params')
params = st.experimental_get_query_params()
st.write(params)

st.header('3. Retrieving and displaying information from the URL')

firstname = params['firstname'][0]
surname = params['surname'][0]

st.write(f'Hello **{firstname} {surname}**, how are you?')