import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.title("Streamlit Assignment")
salary_data=pd.read_csv('Salary_Data.csv')
st.write(salary_data)

# Create user selections using Streamlit
x_var = st.selectbox("Select x-axis variable", list(salary_data.columns))
y_var = st.selectbox("Select y-axis variable", list(salary_data.columns))
color_var = st.selectbox("Select color variable", ["None"] + list(salary_data.columns))

# Create a line chart using Altair
line_chart = alt.Chart(salary_data).mark_line().encode(
    x=x_var,
    y=y_var,
    color=color_var if color_var != "None" else alt.value("steelblue")
).properties(
    title=f"{y_var} by {x_var}"
)

# Display the line chart using Streamlit
st.altair_chart(line_chart, use_container_width=True)

