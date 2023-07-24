Today, we are watching [Ken Jee's tutorial](https://www.youtube.com/watch?v=Yk-unX4KnV4).
Here are some notes:

1. Set up a new conda environment for each streamlit project.
  - install dependencies with `pip` e.g. `streamlit`, `plotly`, etc
  - choose an IDE, e.g. VScode, spyder, etc.
2. Download the CSV files (in this case from kaggle) and store them in a local directory.
3. Start the script by importing the necessary libraries, e.g.

  ```python
  import pandas as pd
  import numpy as np
  import plotly.graph_objects as go
  import plotly.express as px
  from datetime import datetime
  ```
  
4. Create a `load_data()` function that
  - Reads the datasets into memory via `pd.read_csv`
  - Wrangles the datasets, e.g. format date columns, etc and add derived columns.
5. Add the `@st.cache` decorator to the `load_data()` definition to instruct streamlit to
   cache its output.
6. Engineer the desired metrics
  - Create a copy of the original dataset with `df.copy()`
  - Calculate metrics from the available measurements
  - Use `pd.DateOffset(months=6)` to identify videos published in the last 6 months.
7. Add a side bar to the page with `add_sidebar = st.sidebar.selectbox`.
  - Create conditional outputs depending on the value of `add_sidebar`.

  ```python
  if add_sidebar == "Aggregate Metrics":
      st.write('Agg')  # replace with desired plots & other output elements
  if add_sidebar == "Individual Video Analysis":
      st.write('Ind')
  ```

8. Define columns with `st.columns()` and display one metric in each of them
  - Apparently columns can be modified with a context manager. e.g.

    ```python
    with columns[0]:
        st.metric('test')
    ```
    
9. Display a table of metrics for all videos by
  - Subsetting a dataframe to the relevant columns
  - Displaying it with `st.dataframe()`
10. Create [stylers](https://pandas.pydata.org/docs/user_guide/style.html#Styler-Object-and-HTML)
   to format each of the columns in the dataframe.
11. Switch to the view for individual videos and add a selection box with `st.selectbox()`.
12. Create a bar chart by
  - Filtering the data to the selected video.
  - Creating a plot with plotly express via `px.bar()`
  - Passing it to streamlit via `st.plotly_chart()`.
13. Create a line chart by
  - Calculating cumulative metrics for each video, e.g. different percentiles of viewers.
  - Initiating a plotly figure with `figure = go.Figure()`
  - Adding separate traces for each metric to the figure with `figure.add_trace(go.Scatter())`
  - Updating the layout with a title via `figure.update_layout(title = "test", xaxis_titel="")`
  - Displaying the chart with `st.plotly_chart(figure)`
14. Publish the streamlit app in `Streamlit Cloud`
  - Use `pip freeze` to create a `requirements.txt` files
    - Manually check and remove e.g. modules specific to Windows
  - Deposit the script, the `requirements.txt` and the data files in a public github repository.
  - Deploy the github repository into [streamlit cloud](https://streamlit.io/cloud)

  
