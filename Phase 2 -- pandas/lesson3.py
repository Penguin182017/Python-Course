import pandas as pd

data = {
    "Name": ["Kiko", "Bobo", "Ice"],
    "Age": [4, 5, 3],
    "Weight": [12, 15, 10]
}

df = pd.DataFrame(data)

df['Height'] = [80, 90, 75]

print(df)