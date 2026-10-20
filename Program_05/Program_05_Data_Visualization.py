
#==============================================================
# Name: B.Reddy Lohith
# Roll No: 23102A010287
# Branch: CSE(AI/ML)
# Section: B4
#==============================================================

# PROGRAM 5: DATA VISUALIZATION
# Topic: Data Visualization with Matplotlib and Seaborn
# Case Study: Creating Different Types of Statistical Graphs
# AIM: To visualize data using line plots, bar plots,
#      histograms, scatter plots, and box plots.

#==============================================================
# IMPORT REQUIRED LIBRARIES
#==============================================================

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

print("\n" + "=" * 70)
print("DATA VISUALIZATION USING MATPLOTLIB AND SEABORN")
print("=" * 70)


#==============================================================
# A. LINE PLOT
#==============================================================

print("\nA. LINE PLOT")
print("-" * 70)

# Define X-axis and Y-axis values
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create the line plot
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker="o")

# Add title, axis labels, and grid
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Save the graph in the current folder
plt.savefig("line_plot.png")
plt.close()

print("Line plot generated and saved as line_plot.png")


#==============================================================
# B. BAR PLOT
#==============================================================

print("\nB. BAR PLOT")
print("-" * 70)

# Create a DataFrame containing categories and values
df = pd.DataFrame({
    "Category": ["A", "B", "C"],
    "Values": [10, 20, 15]
})

# Create the bar plot
ax = df.plot(
    kind="bar",
    x="Category",
    y="Values",
    legend=False,
    figsize=(8, 5)
)

# Add chart title and axis labels
ax.set_title("Bar Plot")
ax.set_xlabel("Category")
ax.set_ylabel("Values")

# Save the graph
plt.savefig("bar_plot.png")
plt.close()

print("Bar plot generated and saved as bar_plot.png")


#==============================================================
# C. HISTOGRAM AND DENSITY PLOT
#==============================================================

print("\nC. HISTOGRAM AND DENSITY PLOT")
print("-" * 70)

# Generate 1000 random values from a normal distribution
data = np.random.randn(1000)

# Create a histogram with a KDE density curve
plt.figure(figsize=(8, 5))
sns.histplot(data, kde=True)

# Add chart title and axis labels
plt.title("Histogram and Density")
plt.xlabel("Values")
plt.ylabel("Frequency")

# Save the graph
plt.savefig("histogram_density.png")
plt.close()

print("Histogram generated and saved as histogram_density.png")


#==============================================================
# D. SCATTER PLOT
#==============================================================

print("\nD. SCATTER PLOT")
print("-" * 70)

# Generate 50 random X-axis and Y-axis values
x = np.random.rand(50)
y = np.random.rand(50)

# Create the scatter plot
plt.figure(figsize=(8, 5))
plt.scatter(x, y)

# Add title and axis labels
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

# Save the graph
plt.savefig("scatter_plot.png")
plt.close()

print("Scatter plot generated and saved as scatter_plot.png")


#==============================================================
# E. BOX PLOT
#==============================================================

print("\nE. BOX PLOT")
print("-" * 70)

# Generate random data for four groups
box_data = np.random.randn(100, 4)

# Create the box plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=box_data)

# Add chart title and axis labels
plt.title("Box Plot")
plt.xlabel("Groups")
plt.ylabel("Values")

# Save the graph
plt.savefig("box_plot.png")
plt.close()

print("Box plot generated and saved as box_plot.png")


#==============================================================
# FINAL OUTPUT
#==============================================================

print("\n" + "=" * 70)
print("ALL VISUALIZATIONS GENERATED SUCCESSFULLY")
print("Five graph images have been saved in the current folder.")
print("=" * 70)
