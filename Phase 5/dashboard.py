import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# TITLE
# -------------------------

st.title("🐧 Penguin Data Dashboard")

# -------------------------
# DATA
# -------------------------

data = {
    "Name": ["Kiko", "Bobo", "Ice", "Pingu", "Snowy"],
    "Age": [4, 5, 3, 6, 4],
    "Weight": [12, 15, 10, 18, 13]
}

df = pd.DataFrame(data)

# -------------------------
# NUMBER OF PENGUINS
# -------------------------

st.metric("🐧 Number of Penguins", len(df))

# -------------------------
# DATA TABLE
# -------------------------

st.header("📊 Penguin Data")
st.dataframe(df)

# -------------------------
# AVERAGE WEIGHT
# -------------------------

st.metric(
    "⚖️ Average Weight",
    round(df["Weight"].mean(), 2)
)

# -------------------------
# BAR CHART
# -------------------------

st.header("⚖️ Penguin Weights")

st.bar_chart(
    df.set_index("Name")["Weight"]
)

# -------------------------
# PIE CHART
# -------------------------

st.header("🥧 Penguin Weight Share")

fig, ax = plt.subplots()

ax.pie(
    df["Weight"],
    labels=df["Name"],
    autopct="%1.1f%%"
)

st.pyplot(fig)

# -------------------------
# FIND A PENGUIN
# -------------------------

st.header("🔎 Find a Penguin")

selected = st.selectbox(
    "Choose a penguin:",
    df["Name"]
)

penguin = df[df["Name"] == selected]

st.subheader("🐧 Penguin Details")

st.write(
    "Age:",
    penguin["Age"].iloc[0],
    "years"
)

st.write(
    "Weight:",
    penguin["Weight"].iloc[0],
    "kg"
)

# -------------------------
# AGE FILTER
# -------------------------

st.header("🎂 Age Filter")

min_age = st.slider(
    "Show penguins aged at least:",
    1,
    10,
    3
)

filtered_df = df[df["Age"] >= min_age]

st.dataframe(filtered_df)

# -------------------------
# FILTERED BAR CHART
# -------------------------

st.header("📈 Filtered Penguin Weights")

st.bar_chart(
    filtered_df.set_index("Name")["Weight"]
)

# -------------------------
# SEARCH
# -------------------------

st.header("🔍 Search Penguins")

search = st.text_input(
    "Type a penguin name:"
)

search_df = filtered_df

if search:
    search_df = filtered_df[
        filtered_df["Name"].str.contains(
            search,
            case=False
        )
    ]

st.dataframe(search_df)

# -------------------------
# SEARCH RESULT COUNT
# -------------------------

st.metric(
    "🐧 Penguins Found",
    len(search_df)
)