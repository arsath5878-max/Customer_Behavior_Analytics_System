import pandas as pd

# Load Dataset
data = pd.read_excel("customer_purchase_dataset.xlsx")

print("=" * 60)
print("        DATASET LOADED SUCCESSFULLY")
print("=" * 60)
print("\nDataset Shape")
print(data.shape)

print("\nRows :", data.shape[0])
print("Columns :", data.shape[1])


# Display First 5 Records

print("\nFirst 5 Records")
print(data.head())


# Display Last 5 Records

print("\nLast 5 Records")
print(data.tail())

# Column Names

print("\nColumn Names")
print(data.columns.tolist())

# Data Types
print("\nData Types")
print(data.dtypes)

# Dataset Information
print("\nDataset Information")
print(data.info())

# Missing Values
print("\nMissing Values")
print(data.isnull().sum())

# Duplicate Records
print("\nDuplicate Records")
print(data.duplicated().sum())


# Statistical Summary
print("\nStatistical Summary")
print(data.describe())

print("\nModule 2 Completed Successfully")
