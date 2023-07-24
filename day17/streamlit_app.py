import streamlit as st
import os

st.title('st.secrets')

st.write('Message:', st.secrets['message'])
# secrets stored outside a section in the TOML file are exported as environmental variables
st.write('Environmental variable', os.environ['message'])

# secrets within a section are not exported, but are still available via st.secrets
st.write('Another message:', st.secrets['non_environment']['message'])
