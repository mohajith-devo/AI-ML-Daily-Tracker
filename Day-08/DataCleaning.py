"""
Data Cleaning Practice Log
Topic: Handling Missing Values, Duplicates, Grouping & Aggregation

"""

import pandas as pd
import numpy as np

print("=== My Practice Log ===\n")

# --- 1. RAW DATA SETUP ---
print("--- 1. Setting up Raw Data ---")
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Laptop", "Monitor", "Mouse", "Laptop", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Electronics", "Accessories", "Electronics", "Audio"],
    "Price": [1200, 25, 75, 1200, 300, 25, 1150, np.nan],
    "Stock": [10, 50, 30, 5, 15, 45, 2, 20],
    "Rating": [4.5, 4.0, np.nan, 4.8, 4.2, 4.1, 4.9, 4.3]
}

df = pd.DataFrame(data)
print("Original Data (Dirty):")
print(df)
print("-" * 40)

# --- 2. LEVEL 1: CLEANING MISSING VALUES & DUPLICATES ---
print("\n--- 2. Level 1: Cleaning Data ---")

# Step 2a: Check Missing Values
print("Checking for missing values:")
print(df.isnull().sum())

# Step 2b: Fill Missing Values
print("\nFilling missing 'Price' with Mean and 'Rating' with Median...")
avg_price = df['Price'].mean()
median_rating = df['Rating'].median()

df['Price'] = df['Price'].fillna(avg_price)
df['Rating'] = df['Rating'].fillna(median_rating)

# Step 2c: Remove Duplicates
print("Removing duplicate rows...")
original_rows = len(df)
df = df.drop_duplicates()
duplicates_removed = original_rows - len(df)
print(f"Removed {duplicates_removed} duplicate rows.")

# Step 2d: Verify Cleaned Data
print("\nCleaned Data (No NaN, No Duplicates):")
print(df)
print("-" * 40)

# --- 3. LEVEL 2: DATA MANIPULATION ---
print("\n--- 3. Level 2: Creating New Columns & Filtering ---")

# Step 3a: Create 'Total_Value' Column
print("Creating 'Total_Value' column (Price * Stock)...")
df['Total_Value'] = df['Price'] * df['Stock']
print(df[['Product', 'Price', 'Stock', 'Total_Value']])

# Step 3b: Filter High Stock Items
print("\nFiltering products with Stock > 20:")
high_stock_items = df[df['Stock'] > 20]
print(high_stock_items[['Product', 'Stock']])

# Step 3c: Convert Data Types
print("\nConverting 'Price' to Integer...")
df['Price'] = df['Price'].astype(int)
print(f"Data Types:\n{df.dtypes}")
print("-" * 40)

# --- 4. LEVEL 3: GROUPING & ANALYSIS ---
print("\n--- 4. Level 3: Grouping & Aggregation ---")

# Step 4a: Group by Category
print("Grouping by 'Category' to find Average Price and Total Stock...")
category_stats = df.groupby('Category').agg({
    'Price': 'mean',
    'Stock': 'sum',
    'Total_Value': 'sum'
})

# Round the average price to 2 decimal places for readability
category_stats['Price'] = category_stats['Price'].round(2)

print("\nCategory Statistics:")
print(category_stats)

# Step 4b: Find Top Product
print("\nFinding the product with the highest Total_Value...")
top_product = df.loc[df['Total_Value'].idxmax()]
print(f"Top Product: {top_product['Product']}")
print(f"Total Value: ${top_product['Total_Value']}")
print("-" * 40)

# --- 5. SAVE RESULTS ---
print("\n--- 5. Saving Results to CSV ---")
df.to_csv("cleaned_products.csv", index=False)
category_stats.to_csv("category_summary.csv")
print("✅ Saved 'cleaned_products.csv' and 'category_summary.csv'")

print("\n=== Day 9 Practice Completed Successfully! ===")

"""=== Day 9: My Practice Log ===

--- 1. Setting up Raw Data ---
Original Data (Dirty):
      Product     Category   Price  Stock  Rating
0      Laptop  Electronics  1200.0     10     4.5
1       Mouse  Accessories    25.0     50     4.0
2    Keyboard  Accessories    75.0     30     NaN
3      Laptop  Electronics  1200.0      5     4.8
4     Monitor  Electronics   300.0     15     4.2
5       Mouse  Accessories    25.0     45     4.1
6      Laptop  Electronics  1150.0      2     4.9
7  Headphones        Audio     NaN     20     4.3
----------------------------------------

--- 2. Level 1: Cleaning Data ---
Checking for missing values:
Product     0
Category    0
Price       1
Stock       0
Rating      1
dtype: int64

Filling missing 'Price' with Mean and 'Rating' with Median...
Removing duplicate rows...
Removed 0 duplicate rows.

Cleaned Data (No NaN, No Duplicates):
      Product     Category        Price  Stock  Rating
0      Laptop  Electronics  1200.000000     10     4.5
1       Mouse  Accessories    25.000000     50     4.0
2    Keyboard  Accessories    75.000000     30     4.3
3      Laptop  Electronics  1200.000000      5     4.8
4     Monitor  Electronics   300.000000     15     4.2
5       Mouse  Accessories    25.000000     45     4.1
6      Laptop  Electronics  1150.000000      2     4.9
7  Headphones        Audio   567.857143     20     4.3
----------------------------------------

--- 3. Level 2: Creating New Columns & Filtering ---
Creating 'Total_Value' column (Price * Stock)...
      Product        Price  Stock   Total_Value
0      Laptop  1200.000000     10  12000.000000
1       Mouse    25.000000     50   1250.000000
2    Keyboard    75.000000     30   2250.000000
3      Laptop  1200.000000      5   6000.000000
4     Monitor   300.000000     15   4500.000000
5       Mouse    25.000000     45   1125.000000
6      Laptop  1150.000000      2   2300.000000
7  Headphones   567.857143     20  11357.142857

Filtering products with Stock > 20:
    Product  Stock
1     Mouse     50
2  Keyboard     30
5     Mouse     45

Converting 'Price' to Integer...
Data Types:
Product            str
Category           str
Price            int64
Stock            int64
Rating         float64
Total_Value    float64
dtype: object
----------------------------------------

--- 4. Level 3: Grouping & Aggregation ---
Grouping by 'Category' to find Average Price and Total Stock...

Category Statistics:
              Price  Stock   Total_Value
Category                                
Accessories   41.67    125   4625.000000
Audio        567.00     20  11357.142857
Electronics  962.50     32  24800.000000

Finding the product with the highest Total_Value...
Top Product: Laptop
Total Value: $12000.0
----------------------------------------

--- 5. Saving Results to CSV ---
✅ Saved 'cleaned_products.csv' and 'category_summary.csv"""