import streamlit as st
import requests

st.title("🏀 Bored API app")

with st.sidebar:
    st.subheader("Input")
    selected_type = st.selectbox(
        "Select and activity type",
        [
            "education",
            "recreational",
            "social",
            "diy",
            "charity",
            "cooking",
            "relaxation",
            "music",
            "busywork",
        ],
    )

suggested_activity_url = f"http://www.boredapi.com/api/activity?type={selected_type}"
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

col1, col2 = st.columns(2)
with col1:
    with st.expander("About this app"):
        st.markdown(
            """Are you bored? The **Bored API app** provides suggestions on activities
               that you can do when you are bored. This app is powered by the Bored API.
            """
        )
with col2:
    with st.expander("JSON data"):
        st.write(suggested_activity)

st.header("Suggested activity")
st.info(suggested_activity["activity"])
m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Number of Participants", suggested_activity["participants"])
with m2:
    st.metric("Type of Activity", suggested_activity["type"].capitalize())
with m3:
    st.metric("Price", suggested_activity["price"])
