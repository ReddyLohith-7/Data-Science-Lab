
#==============================================================
# Name: B.Reddy Lohith
# Roll No: 23102A010287
# Branch: CSE(AI/ML)
# Section: B4
#==============================================================

#==============================================================
# Program 3: Data Cleaning and Preparation
# Case Study: Handling Missing Data, Transformation,
#             Outlier Detection and Text Manipulation
# AIM: To perform data cleaning and preparation using
# NumPy, pandas and regular expressions.
#==============================================================


#==============================================================
# IMPORT REQUIRED LIBRARIES
#==============================================================

# NumPy is used for numerical operations and missing values.
import numpy as np

# pandas is used to create and manipulate DataFrames.
import pandas as pd

# re is used for regular expression operations on text.
import re


#==============================================================
# A. HANDLE MISSING DATA
#==============================================================

print("\n")
print("=" * 70)
print("A. HANDLE MISSING DATA")
print("=" * 70)

# Create a dictionary containing missing values (NaN).
data = {
    'A': [1, 2, np.nan],
    'B': [4, np.nan, np.nan]
}

# Convert the dictionary into a DataFrame.
df = pd.DataFrame(data)

# Display the original data.
print("\nORIGINAL DATAFRAME")
print("-" * 70)
print(df)

# Display True/False values indicating missing data locations.
print("\nMISSING VALUE LOCATIONS")
print("-" * 70)
print(df.isna())

# Remove rows containing missing values.
df_clean = df.dropna()

# Replace missing values with 0.
df_filled = df.fillna(0)

# Display the DataFrame after removing missing values.
print("\nDATAFRAME AFTER REMOVING MISSING VALUES")
print("-" * 70)
print(df_clean)

# Display the DataFrame after filling missing values.
print("\nDATAFRAME AFTER FILLING MISSING VALUES WITH ZERO")
print("-" * 70)
print(df_filled)


#==============================================================
# B. DATA TRANSFORMATION
#==============================================================

print("\n")
print("=" * 70)
print("B. DATA TRANSFORMATION")
print("=" * 70)

# Create a DataFrame containing gender categories.
df = pd.DataFrame({
    'gender': ['male', 'female', 'male']
})

# Convert categorical values into numerical values.
# male = 0, female = 1
df['gender_num'] = df['gender'].map({
    'male': 0,
    'female': 1
})

# Rename the gender column to Gender.
df_renamed = df.rename(columns={
    'gender': 'Gender'
})

# Display the transformed DataFrame.
print("\nTRANSFORMED DATAFRAME")
print("-" * 70)
print(df_renamed)


#==============================================================
# C. OUTLIER DETECTION
#==============================================================

print("\n")
print("=" * 70)
print("C. OUTLIER DETECTION")
print("=" * 70)

# Create a 100-row, 3-column dataset of random values.
data = pd.DataFrame(np.random.randn(100, 3))

# Identify values greater than 3 or less than -3.
outliers = (data > 3) | (data < -3)

# Display the number of outliers in each column.
print("\nNUMBER OF OUTLIERS IN EACH COLUMN")
print("-" * 70)
print(outliers.sum())


#==============================================================
# D. REGEX FOR TEXT MANIPULATION
#==============================================================

print("\n")
print("=" * 70)
print("D. REGEX FOR TEXT MANIPULATION")
print("=" * 70)

# Create text containing spaces, a tab and a newline.
text = "This  is\t a\n test"

# Split the text using one or more whitespace characters.
split_text = re.split(r'\s+', text)

# Display the original and split text.
print("\nORIGINAL TEXT")
print("-" * 70)
print(repr(text))

print("\nTEXT AFTER SPLITTING")
print("-" * 70)
print(split_text)


#==============================================================
# END OF PROGRAM
#==============================================================

print("\n")
print("=" * 70)
print("DATA CLEANING AND PREPARATION COMPLETED")
print("=" * 70)
