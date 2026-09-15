import streamlit as st

st.title("🐧 Penguin Age")

age = st.number_input("How old is your penguin?", min_value=0, max_value=20)

st.write("Your penguin is", age, "years old! 🐧")