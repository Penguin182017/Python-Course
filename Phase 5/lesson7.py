import streamlit as st

st.title("🐧 Penguin Selector")

penguin = st.selectbox(
    "Choose a penguin:",
    ["Kiko", "Bobo", "Ice"]
)

st.write("You selected:", penguin)