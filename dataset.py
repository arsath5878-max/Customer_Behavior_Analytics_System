import pandas as pd

DATA_FILE = "customer_behavior_dataset_updated.xlsx"

data = pd.read_excel(DATA_FILE)

print("=" * 60)
print("        DATASET LOADED SUCCESSFULLY")
print("=" * 60)

print("\nDataset Shape")
print(data.shape)

print("\nRows :", data.shape[0])
print("Columns :", data.shape[1])

print("\nFirst 5 Records")
print(data.head())

print("\nLast 5 Records")
print(data.tail())

print("\nColumn Names")
print(data.columns.tolist())

print("\nData Types")
print(data.dtypes)

print("\nMissing Values")
print(data.isnull().sum())

print("\nDuplicate Records")
print(data.duplicated().sum())

print("\nStatistical Summary")
print(data.describe())

print("\nDataset Module Completed Successfully")
