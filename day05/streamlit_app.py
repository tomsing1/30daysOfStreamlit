import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header("st.write")

# Example 1
st.write("## Display text")
st.write("Hello, *World!* :sunglasses:")

st.write("## Display numbers")
st.write(1234)

st.write("## Display DataFrame")
df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
st.write(df)

st.write("## Accept multiple arguments")
st.write("Below is a DataFrame", df, "Above is a DataFrame")

st.write("## Display charts")
df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
    .interactive()
)
st.write(c)
