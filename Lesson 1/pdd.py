import pandas as pd
import numpy as np

# ==========================================
# Step 1: Import Pandas
# ==========================================
print("--- Step 1: Import Pandas ---")
print("Pandas imported successfully as pd.\n")

# ==========================================
# Step 2: Create a Pandas Series
# ==========================================
print("--- Step 2: Create a Pandas Series ---")
marks_list = [85, 90, 78, 92, 88]
student_names = ["Alice", "Bob", "Charlie", "David", "Eve"]

# Creating a Series where student names are the indices
marks_series = pd.Series(marks_list, index=student_names, name="Marks")
print(marks_series)
print("\n")

# ==========================================
# Step 3: Build a DataFrame
# ==========================================
print("--- Step 3: Build a DataFrame ---")
data = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math": [85, 90, 78, 92, 88],
    "Science": [92, 81, 85, 89, 94],
    "Attendance": [95, 88, 92, 90, 96]
}

df = pd.DataFrame(data)
print(df)
print("\n")

# ==========================================
# Step 4: Read and View Data
# ==========================================
print("--- Step 4: Read and View Data ---")
# Save DataFrame to CSV
file_name = "student_marks.csv"
df.to_csv(file_name, index=False)

# Read it back using pd.read_csv()
df_read = pd.read_csv(file_name)

print("First few rows (head):")
print(df_read.head(2))
print("\nLast few rows (tail):")
print(df_read.tail(2))
print("\nDataFrame Info:")
df_read.info()
print("\n")

# ==========================================
# Step 5: Clean Missing Data
# ==========================================
print("--- Step 5: Clean Missing Data ---")
# Creating a DataFrame with missing values (NaN)
data_with_missing = {
    "Student": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Math": [85, np.nan, 78, 92, np.nan],
    "Science": [92, 81, np.nan, 89, 94]
}

df_missing = pd.DataFrame(data_with_missing)
print("Original DataFrame with Missing Values:")
print(df_missing)

# Replace missing marks with 0 using fillna(0)
df_cleaned = df_missing.fillna(0)
print("\nCleaned DataFrame (Missing values replaced with 0):")
print(df_cleaned)
print("\n")

# ==========================================
# Step 6: Add Total and Average Columns
# ==========================================
print("--- Step 6: Add Total and Average Columns ---")
# Using the cleaned marks dataframe (Math and Science columns)
df_cleaned["Total"] = df_cleaned["Math"] + df_cleaned["Science"]
df_cleaned["Average"] = df_cleaned["Total"] / 2

print("DataFrame with Total and Average Columns:")
print(df_cleaned)