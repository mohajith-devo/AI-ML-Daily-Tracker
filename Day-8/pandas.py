"""
Day 9: Pandas Practice Log
Topics: DataFrames, Indexing, Filtering, Grouping, Missing Data, Sorting

"""

import pandas as pd
import numpy as np

print("=== Pandas Practice Log ===\n")

# ---------------------------------------------------------
# 1. CREATING A DATAFRAME
# ---------------------------------------------------------
print("--- 1. Creating a DataFrame ---")

# Create a dictionary of data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 28, 32],
    'City': ['New York', 'London', 'Paris', 'London', 'New York'],
    'Salary': [70000, 80000, 90000, 75000, 85000],
    'Bonus': [5000, 6000, 7000, None, 8000]  # None represents missing data
}

# Create DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
# Expected Output:
# Original DataFrame:
#      Name  Age      City  Salary  Bonus
# 0   Alice   25  New York   70000   5000.0
# 1     Bob   30    London   80000   6000.0
# 2  Charlie   35     Paris   90000   7000.0
# 3   David   28    London   75000      NaN
# 4     Eve   32  New York   85000   8000.0

# ---------------------------------------------------------
# 2. BASIC SELECTION & SLICING
# ---------------------------------------------------------
print("\n--- 2. Basic Selection & Slicing ---")

# Select a single column
print("\nSelecting 'City' column:")
cities = df['City']
print(cities)
# Expected Output:
# Selecting 'City' column:
# 0       New York
# 1         London
# 2          Paris
# 3         London
# 4       New York
# Name: City, dtype: object

# Select multiple columns
print("\nSelecting 'Name' and 'Salary' columns:")
subset = df[['Name', 'Salary']]
print(subset)
# Expected Output:
# Selecting 'Name' and 'Salary' columns:
#      Name  Salary
# 0   Alice   70000
# 1     Bob   80000
# 2  Charlie   90000
# 3   David   75000
# 4     Eve   85000

# Select a specific row by index
print("\nSelecting row 2 (Charlie):")
print(df.iloc)
# Expected Output:
# Selecting row 2 (Charlie):
# Name        Charlie
# Age                35
# City          Paris
# Salary          90000
# Bonus            7000
# Name: 2, dtype: object

# ---------------------------------------------------------
# 3. FILTERING (Conditional Selection)
# ---------------------------------------------------------
print("\n--- 3. Filtering Data ---")

# Filter: People older than 30
print("\nPeople older than 30:")
older = df[df['Age'] > 30]
print(older)
# Expected Output:
# People older than 30:
#      Name  Age    City  Salary  Bonus
# 2  Charlie   35   Paris   90000   7000.0
# 4      Eve   32  New York   85000   8000.0

# Filter: People in London
print("\nPeople in London:")
londoners = df[df['City'] == 'London']
print(londoners)
# Expected Output:
# People in London:
#   Name  Age   City  Salary  Bonus
# 1  Bob   30  London   80000   6000.0
# 3 David 28  London   75000    NaN

# Filter: Salary > 80000 AND Age < 35
print("\nSalary > 80000 AND Age < 35:")
high_low = df[(df['Salary'] > 80000) & (df['Age'] < 35)]
print(high_low)
# Expected Output:
# Salary > 80000 AND Age < 35:
#   Name  Age      City  Salary  Bonus
# 4  Eve   32  New York   85000   8000.0

# ---------------------------------------------------------
# 4. HANDLING MISSING DATA
# ---------------------------------------------------------
print("\n--- 4. Handling Missing Data ---")

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())
# Expected Output:
# Missing values in each column:
# Name      0
# Age       0
# City      0
# Salary    0
# Bonus     1
# dtype: int64

# Fill missing Bonus with 0
print("\nFilling missing Bonus with 0:")
df_filled = df.fillna({'Bonus': 0})
print(df_filled)
# Expected Output:
# Filling missing Bonus with 0:
#      Name  Age      City  Salary  Bonus
# 0   Alice   25  New York   70000   5000.0
# 1     Bob   30    London   80000   6000.0
# 2  Charlie   35     Paris   90000   7000.0
# 3   David   28    London   75000      0.0
# 4     Eve   32  New York   85000   8000.0

# ---------------------------------------------------------
# 5. CREATING NEW COLUMNS & CALCULATIONS
# ---------------------------------------------------------
print("\n--- 5. New Columns & Calculations ---")

# Create a new column: Total Income (Salary + Bonus)
df['Total_Income'] = df['Salary'] + df['Bonus']
print("\nDataFrame with Total_Income:")
print(df[['Name', 'Salary', 'Bonus', 'Total_Income']])
# Expected Output:
# DataFrame with Total_Income:
#      Name  Salary  Bonus  Total_Income
# 0   Alice   70000   5000.0        75000.0
# 1     Bob   80000   6000.0        86000.0
# 2  Charlie   90000   7000.0        97000.0
# 3   David   75000      0.0         75000.0
# 4     Eve   85000   8000.0        93000.0

# ---------------------------------------------------------
# 6. GROUPING & AGGREGATION
# ---------------------------------------------------------
print("\n--- 6. Grouping & Aggregation ---")

# Group by City and calculate average Salary
print("\nAverage Salary by City:")
avg_salary = df.groupby('City')['Salary'].mean().reset_index()
print(avg_salary)
# Expected Output:
# Average Salary by City:
#       City  Salary
# 0  London   77500.0
# 1   New York   77500.0
# 2    Paris   90000.0

# Group by City and get count and max Salary
print("\nCount and Max Salary by City:")
grouped = df.groupby('City').agg({'Name': 'count', 'Salary': 'max'}).reset_index()
grouped.columns = ['City', 'Employee_Count', 'Max_Salary']
print(grouped)
# Expected Output:
# Count and Max Salary by City:
#       City  Employee_Count  Max_Salary
# 0  London               2       80000
# 1   New York            2       85000
# 2    Paris               1       90000

# ---------------------------------------------------------
# 7. SORTING
# ---------------------------------------------------------
print("\n--- 7. Sorting ---")

# Sort by Salary (Descending)
print("\nSorted by Salary (High to Low):")
sorted_df = df.sort_values(by='Salary', ascending=False)
print(sorted_df[['Name', 'Salary']])
# Expected Output:
# Sorted by Salary (High to Low):
#      Name  Salary
# 2  Charlie   90000
# 4      Eve   85000
# 1      Bob   80000
# 3    David   75000
# 0    Alice   70000

# ---------------------------------------------------------
# 8. BASIC STATISTICS ON DATAFRAME
# ---------------------------------------------------------
print("\n--- 8. Basic Statistics ---")

print("\nStatistical Summary:")
print(df.describe())
# Expected Output:
# Statistical Summary:
#                Age       Salary         Bonus   Total_Income
# count     5.000000     5.000000        5.000000       5.000000
# mean     30.000000   80000.000000   5200.000000    85200.000000
# std       3.872983    7905.694936   1303.840482    8455.234903
# min      25.000000   70000.000000      0.000000    75000.000000
# 25%      27.000000   73750.000000   5000.000000    77500.000000
# 50%      30.000000   80000.000000   6000.000000    86000.000000
# 75%      33.000000   83750.000000   7000.000000    90500.000000
# max      35.000000   90000.000000   8000.000000    97000.000000

