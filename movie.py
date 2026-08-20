import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Alek\Desktop\IMDB Dataset.csv")

print("First 3 rows:")
print(df.head(3))

print("\nLast 3 rows:")
print(df.tail(3))

print("\nDataset Information:")
print(df.info())

print("\nNull Values:")
print(df.isnull().sum())

print("\nRows 41 to 75:")
subset = df.iloc[40:75]
print(subset)

print("\nMovie with highest number of votes:")
highest_votes = df.loc[df["No_of_Votes"].idxmax()]
print(highest_votes)

sns.boxplot(data=df[["IMDB_Rating", "Runtime"]])

plt.title("Boxplot of IMDB Rating and Runtime")
plt.show()

sns.scatterplot(data=df, x="Runtime", y="IMDB_Rating")

plt.xlabel("Runtime")
plt.ylabel("IMDB Rating")
plt.title("IMDB Rating vs Runtime")
plt.show()

plt.hist(df["IMDB_Rating"], bins=10)

plt.xlabel("IMDB Rating")
plt.ylabel("Number of Movies")
plt.title("Distribution of IMDB Ratings")
plt.show()

plt.hist(df["Runtime"], bins=10)

plt.xlabel("Runtime")
plt.ylabel("Number of Movies")
plt.title("Distribution of Runtime")
plt.show()

sns.countplot(data=df, x="Certificate")

plt.xlabel("Certificate")
plt.ylabel("Number of Movies")
plt.title("Number of Movies by Certificate")
plt.show()