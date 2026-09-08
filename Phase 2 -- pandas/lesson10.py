import pandas as pd

data = {
    "Name": ["Kiko", "Bobo", "Ice"],
    "Age": [4, 5, 3],
    "Weight": [12, 15, 10]
}

df = pd.DataFrame(data)

print(df["Weight"].count())