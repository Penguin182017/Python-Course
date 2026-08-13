import pandas as pd

#series
# data = [100, 102, 104, 202, 204]

# series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e'])
# print('Normal:')
# print(series)

# series.loc['c'] = 200

# print('Now c = 200:')
# print(series)
# print()
# print("a:")
# print(series.loc['a'])
# print()
# print("c")
# print(series.iloc[2])
# print()
# print("Greater or equal to 200:")
# print(series[series >= 200])

# calories = {"Day 1": 1750, "Day 2": 2100, "Day 3": 1700}
# series = pd.Series(calories)

# print(series)

# series.loc["Day 3"] += 500

# print(series.loc["Day 3"])
# print("Days he sticked to his diet:")
# print(series.loc[series < 2000])
# print("Days he cheated on his diet")
# print(series.loc[series >= 2000])


#data frame
# data = {"Name": ["Spongebob", 'Patrick', 'Squidward'],
#         "Age": [30, 35, 50]

# }

# df = pd.DataFrame(data, index=['Employee 1', 'Employee 2', 'Employee 3'])

# df["Job"] = ['Cook', 'N/A', 'Cashier']

# new_rows = pd.DataFrame([{"Name": "Sandy", 'Age': 28, 'Job': "Engineer"},
#                          {"Name": "Eugene", 'Age': 60, 'Job': "Manager"}],
#                        index=['Employee 4', 'Employee 5'])
# df = pd.concat([df, new_rows])
# print()
# print(data.iloc[0])

# print(df)


# importing
df = pd.read_csv(r'C:\Users\Alek\Desktop\data1.txt', index_col="Name")
# print(df.to_string())

# SELECTIONS BY COLUMN
# print(df['Name'])
# print(df['Height'])
# print(df['Weight'])
# print(df[['Name', 'Height', "Weight"]])

#SELECTION BY ROW/S
# print(df.loc["Charizard":"Blastoise", ["Height", "Weight"]])
# print(df.iloc[0:11:2, 0:3])

# pokemon = input("Enter a Pokemon name: ")

# try:
#     print(df.loc[pokemon])
# except KeyError:
#     print(f"{pokemon} not found") 


