
#==============================================================
# Name: B.Reddy Lohith
# Roll No: 23102A010287
# Branch: CSE(AI/ML)
# Section: B4
#==============================================================

#==============================================================
# Program 4: Data Wrangling
# Case Study: Hierarchical Indexing, Stack, Unstack,
#             Merge and Combine Operations
# AIM: To perform data wrangling using pandas and NumPy
#      by applying hierarchical indexing, reshaping and
#      combining DataFrames.
#==============================================================


#==============================================================
# IMPORT REQUIRED LIBRARIES
#==============================================================

# pandas is used for data manipulation and analysis.
import pandas as pd

# NumPy is used for numerical operations and random values.
import numpy as np


#==============================================================
# A. HIERARCHICAL INDEXING
#==============================================================

print("\n")
print("=" * 70)
print("A. HIERARCHICAL INDEXING")
print("=" * 70)

# Create a Series with random values and a two-level index.
# The first level contains labels a, b and c.
# The second level contains index values 1 and 2.
data = pd.Series(
    np.random.randn(6),
    index=[
        ['a', 'a', 'b', 'b', 'c', 'c'],
        [1, 2, 1, 2, 1, 2]
    ]
)

# Display the complete Series.
print("\nORIGINAL SERIES")
print("-" * 70)
print(data)

# Display all values belonging to first-level index 'b'.
print("\nVALUES FOR INDEX b")
print("-" * 70)
print(data['b'])

# Display values where the second-level index equals 1.
print("\nVALUES WITH SECOND INDEX = 1")
print("-" * 70)
print(data[:, 1])


#==============================================================
# B. STACK AND UNSTACK
#==============================================================

print("\n")
print("=" * 70)
print("B. STACK AND UNSTACK")
print("=" * 70)

# Convert the hierarchical Series into a DataFrame.
# unstack() moves the inner index level into columns.
df = data.unstack()

# Display the unstacked DataFrame.
print("\nUNSTACKED DATAFRAME")
print("-" * 70)
print(df)

# Convert the DataFrame back into a Series.
# stack() moves the column labels back into an index level.
print("\nSTACKED SERIES")
print("-" * 70)
print(df.stack())


#==============================================================
# C. MERGE AND COMBINE
#==============================================================

print("\n")
print("=" * 70)
print("C. MERGE AND COMBINE")
print("=" * 70)

# Create the first DataFrame containing missing values.
df1 = pd.DataFrame({
    'a': [1, np.nan, 3],
    'b': [4, 5, 6]
})

# Create the second DataFrame containing missing values.
df2 = pd.DataFrame({
    'a': [7, 8, 9],
    'b': [np.nan, 11, 12]
})

# Display the first DataFrame.
print("\nFIRST DATAFRAME")
print("-" * 70)
print(df1)

# Display the second DataFrame.
print("\nSECOND DATAFRAME")
print("-" * 70)
print(df2)

# combine_first() fills missing values in df1
# with corresponding non-missing values from df2.
merged = df1.combine_first(df2)

# Display the combined DataFrame.
print("\nCOMBINED DATAFRAME")
print("-" * 70)
print(merged)


#==============================================================
# END OF PROGRAM
#==============================================================

print("\n")
print("=" * 70)
print("DATA WRANGLING COMPLETED")
print("=" * 70)
