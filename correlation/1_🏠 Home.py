import altair as alt
import streamlit as st
import numpy as np
import pandas as pd
st.set_page_config(
	page_title="Guess the correlation!",
	page_icon="🎯",
	layout="wide",
	initial_sidebar_state="expanded",
	menu_items={
		"About": "A streamlit example app, inspired by Omar Wagih's " \
		"[original _Guess the correlation_](https://www.guessthecorrelation.com/) " \
		"application."
	}
)

# function definitions
def dataset(n=200):
	rng = np.random.default_rng()
	corr = rng.uniform(low=-0.9999, high=0.9999)
	cov = [[1, corr], [corr, 1]]
	L = np.linalg.cholesky(cov)
	uncorrelated = np.random.standard_normal((2, n))
	return np.dot(L, uncorrelated).T
	
def correlation(data):
	return np.round(np.corrcoef(data.T)[0, 1], 2)

def scatter_plot():
	df = pd.DataFrame(st.session_state['data'], columns = ['x', 'y'])
	return alt.Chart(df).mark_circle(size=100).encode(x='x', y='y').configure_point(size=20)

def results():
	off_by = round(abs(st.session_state['cor'] - st.session_state['guess']), 2)
	if off_by < 0.1:
		st.session_state['coins'] += 1
		st.session_state['streak'] = True
		st.session_state['streak_length'] += 1
		return (
			True,
			f"🤩 Amazing! The true correlation coefficient is {st.session_state['cor']}"
		)
	else:
		st.session_state['coins'] -= 1
		st.session_state['streak'] = False
		st.session_state['streak_length'] = 0
		return (
			False,
			f"😢 Sorry! The true correlation coefficient is {st.session_state['cor']}"
		)

# persistent variables
with st.sidebar:
	st.subheader("Settings")
	st.session_state['n'] = st.number_input('Number of data points', 2, 1000, 100)
if not 'data' in st.session_state:
	st.session_state['data'] = dataset(st.session_state['n'])
if not 'cor' in st.session_state:
	st.session_state['cor'] = correlation(st.session_state['data'])
if not 'guessed' in st.session_state:
	st.session_state['guessed'] = False
if not 'streak' in st.session_state:
	st.session_state['streak'] = False
if not 'streak_length' in st.session_state:
	st.session_state['streak_length'] = 0
if not 'coins' in st.session_state:
	st.session_state['coins'] = 3

# page content
st.title("🎯 Guess the correlation")
st.write(
	'The goal of this app is to develop intuition about the',
	'[Pearson correlation coefficient](https://en.wikipedia.org/wiki/Pearson_correlation_coefficient).'
	)
st.write(
	'The plot below shows', st.session_state['n'], 'points. Your task is to guess the',
	'correlation coefficient between the `x` and `y` variables.',
	'Correlations can be positive or negative, e.g. fall between -1 and +1.'
)
st.write(
	'If your guess is within 0.1 of the true correlation, you win and gain a coin.\n',
	'Otherwise, you loose a coin. The game ends when you have run out of coins!'
)
st.write(
	'🪙', st.session_state['coins']
)
st.write(
	'🍀 Streak:', st.session_state['streak_length']
)

st.altair_chart(scatter_plot())

if st.session_state['coins'] == 0:
	st.warning('Game over')
	st.stop()
if not st.session_state['guessed']:
	col1, col2 = st.columns([0.5, 0.5])
	with col1:
		with st.form('user_input'):
			st.number_input('Your guess:', format = '%.2f', min_value = -1.0, max_value = 1.0,
			key='guess')
			submit = st.form_submit_button('Submit!')
			if submit:
				st.session_state['guessed'] = True
				st.experimental_rerun()	

if st.session_state['guessed']:
	if 'guess' in st.session_state:
		success, message = results()
		if success:
			st.success(message)
		else:
			st.warning(message)
	with st.form('try_again'):
		restart = st.form_submit_button('Try again!')
		if restart:
			del st.session_state['guessed']
			del st.session_state['data']
			del st.session_state['cor']
			st.experimental_rerun()	
