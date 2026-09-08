import pandas as pd

data = {
    "Name": ["Kiko", "Bobo", "Ice"],
    "Age": [4, 5, 3],
    "Weight": [12, 15, 10]
}

df = pd.DataFrame(data)

older = df[(df["Age"] > 3) & (df["Weight"] > 12)]

print(older)