import streamlit as st
import pandas as pd
import numpy as np

# title
st.title("Hello Stremlit")

st.write("This is simple text")

# dataframe
df = pd.DataFrame({
    'first column': [1,2,3,4,5],
    'second column': [10,20,30,40,50]
})

# Display

st.write("Here is the DataFrame")
st.write(df)

# create a line chart
chart_data = pd.DataFrame(
    np.random.randn(20,3), columns=['a','b','c']
)
st.write(chart_data)
st.line_chart(chart_data)