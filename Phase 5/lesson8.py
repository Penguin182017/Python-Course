import streamlit as st
import pandas as pd

st.title("🐧 Penguin Data")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.dataframe(df)
