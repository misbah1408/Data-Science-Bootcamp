import streamlit as st
import pandas as pd

st.title("Streamlit Widget Demo")

# Text input
name = st.text_input("Enter your name")

# Number input
age = st.number_input("Enter your age", min_value=0, max_value=120)

# Checkbox
likes_python = st.checkbox("Do you like Python?")

# Radio buttons
language = st.radio("Select your favorite language", ["Python", "JavaScript", "C++", "Java"])

# Selectbox (dropdown)
country = st.selectbox("Select your country", ["USA", "India", "Germany", "Canada", "Other"])

# Slider
satisfaction = st.slider("How satisfied are you with Streamlit?", 0, 10, 5)

# Button
if st.button("Submit"):
    st.subheader("Your Input Summary:")
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Likes Python: {'Yes' if likes_python else 'No'}")
    st.write(f"Favorite Language: {language}")
    st.write(f"Country: {country}")
    st.write(f"Satisfaction: {satisfaction}/10")


upload_file = st.file_uploader("Choose a csv file", type='csv',)

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df)