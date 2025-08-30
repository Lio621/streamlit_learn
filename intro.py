import streamlit as st
import pandas as pd
import numpy as np
from datetime import date

st.title("Hey I am learning Streamlit!")
st.header("_Streamlit_ is :blue[cool] :sunglasses:")

st.write("""This is my first Streamlit app.
         I am excited to learn more about it!
         Learning a new thing is always fun.""")

enj = st.checkbox("Are you enjoying Streamlit?")

if enj:
    st.write("Yay! Keep enjoying the journey.")

rad = st.radio("Select your favorite color:", ("Red", "Blue", "Green"))

if rad == "Red":
    st.write("Red is a color of passion.")
elif rad == "Blue":
    st.write("Blue is a color of calm.")
else:
    st.write("Green is a color of nature.")

dob = st.date_input("What is yout date of birth:", date(1900, 1, 1), min_value=date(1900, 1, 1), max_value=date.today())
age = date.today().year - dob.year

st.write("Your date of birth is:", dob)
st.write(f"Your age is: {age} years.")

if age < 18:
    st.write("You are a minor.")
else:
    st.write("You are an adult.")