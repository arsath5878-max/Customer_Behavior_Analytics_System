import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "customer_behavior_dataset_updated.xlsx"
data = pd.read_excel(DATA_FILE)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nDataset Shape :", data.shape)

plt.figure(figsize=(8, 5))
plt.hist(data["Age"], bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Customers")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["Website_Visits"], bins=10, edgecolor="black")
plt.title("Website Visit Distribution")
plt.xlabel("Website Visits")
plt.ylabel("Customers")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["Time_Spent_Minutes"], bins=10, edgecolor="black")
plt.title("Time Spent Distribution")
plt.xlabel("Time Spent (Minutes)")
plt.ylabel("Customers")
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 5))
plt.hist(data["Pages_Viewed"], bins=10, edgecolor="black")
plt.title("Pages Viewed Distribution")
plt.xlabel("Pages Viewed")
plt.ylabel("Customers")
plt.grid(True)
plt.show()

gender = data["Gender"].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(gender, labels=gender.index, autopct="%1.1f%%", startangle=90)
plt.title("Gender Distribution")
plt.show()

purchase = data["Purchase"].value_counts()
plt.figure(figsize=(6, 5))
plt.bar(purchase.index.astype(str), purchase.values)
plt.title("Purchase Distribution")
plt.xlabel("Purchase")
plt.ylabel("Customers")
plt.show()

category = data["Product_Category"].value_counts()
plt.figure(figsize=(10, 5))
plt.bar(category.index, category.values)
plt.xticks(rotation=45)
plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Customers")
plt.show()

print("\nEDA Completed Successfully")
