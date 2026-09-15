import streamlit as st

days = [1, 2, 3, 4, 5]
books = [2, 4, 3, 6, 8]

st.title("📚 Reading Dashboard")

st.line_chart(books)
