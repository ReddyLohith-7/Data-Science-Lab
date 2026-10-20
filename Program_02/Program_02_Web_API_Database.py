# Data Science - Program 2
# Interacting with Web APIs and Databases
# Roll no : 23102A010287
# Name    : B.Reddy Lohith
# Section : B4

# Import the requests library to send HTTP requests
import requests

# Import pandas for DataFrame operations
import pandas as pd

# GitHub API URL for pandas issues
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'

# Send GET request to GitHub API
response = requests.get(url)

# Convert JSON response to Python object
issues = response.json()

# Create DataFrame from issues data
df_issues = pd.DataFrame(issues)

# Display selected columns from first 5 records
print(df_issues[['id', 'title', 'state', 'created_at']].head())

# Import SQLite library
import sqlite3

# Connect to database (creates file if it does not exist)
conn = sqlite3.connect('students.db')

# Create cursor object
cursor = conn.cursor()

# Create students table if it does not already exist
cursor.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER, name TEXT)")

# Insert first record
cursor.execute("INSERT INTO students VALUES (1, 'John')")

# Save changes
conn.commit()

# Insert second record
cursor.execute("INSERT INTO students VALUES (2, 'Joy')")

# Save changes
conn.commit()

# Read table data into DataFrame
df = pd.read_sql_query('SELECT * FROM students', conn)

# Display table data
print(df)

# Update student name
cursor.execute("UPDATE students SET name = 'Alice' WHERE id = 1")

# Delete student with id 1
cursor.execute("DELETE FROM students WHERE id = 1")

# Save changes
conn.commit()

# Close database connection
conn.close()
