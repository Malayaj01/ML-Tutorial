import streamlit as st

st.title("Streamlit Text input ")

name = st.text_input("enter your name")

if name:
    st.write(f"Hello, {name}")

age = st.slider("Select Your age", 0,100,25)

st.write(f'Your age is {age}')

options = ["Python","C++","Java","Javascript"]
choice = st.selectbox("Choose your Fav Language :",options)
st.write(f"Your Selected {choice}")