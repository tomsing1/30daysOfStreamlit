import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

def example_data(n, corr):
	rng = np.random.default_rng()
	cov = [[1, corr], [corr, 1]]
	L = np.linalg.cholesky(cov)
	uncorrelated = np.random.standard_normal((2, n))
	dat = np.dot(L, uncorrelated).T
	return pd.DataFrame(dat, columns = ['x', 'y'])


st.header("Welcome!")
st.write(
	'The goal of this app is to develop intuition about the [Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).'
)
st.subheader("Examples")
correlations = (0.99, -0.99, 0.75, -0.75, 0.5, -0.5, 0.25, -0.25)

cols = st.columns([0.4, 0.1, 0.4, 0.1])
for i in range(len(correlations)):
	correlation = correlations[i]
	with cols[(i % 2) * 2]:
		df = example_data(100, correlation)
		title = 'Correlation coefficient:' + str(correlation)
		st.altair_chart(
			alt.Chart(df, title=title).mark_circle(size=100).encode(x='x', y='y').configure_point(size=20),
			use_container_width=True
		)
