import streamlit as st

st.title('st.form')

st.header('1. Example of using `with` notation')
st.subheader('Coffee machine')
with st.form("form1"):
    st.write('**Order your coffee**')
    bean = st.selectbox('Coffee bean', ('Arabica', 'Robusta'))
    roast = st.selectbox('Coffee roast', ('Light', 'Medium', 'Dark'))
    method = st.selectbox('Brewing method', ('Areopress', 'Drip', 'French press', 'Moka pot', 'Siphon'))
    serving = st.selectbox('Serving format', ('Hot', 'Iced', 'Frappe'))
    milk = st.select_slider('Milk intensity', ('None', 'Low', 'Medium', 'High'), 'None' )
    own_cup = st.checkbox('Bring own cup')
    submitted = st.form_submit_button("Submit")
if submitted:
    st.markdown(f'''
    ☕ You have ordered:
    - Coffee bean: `{bean}`
    - Coffee roast: `{roast}`
    - Brewing: `{method}`
    - Serving type: `{serving}`
    - Milk: `{milk}`
    - Bring own cup: `{own_cup}`
    ''')
else:
    st.write('☝️ Place your order!')
    
    
st.header('2. Example of object notation')
form2 = st.form('form2')
value = form2.slider('Select a value')
submitted2 = form2.form_submit_button("Submit")
st.write(f'Selected value: `{value}`')
