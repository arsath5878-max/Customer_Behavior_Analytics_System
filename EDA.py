
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel("customer_purchase_dataset.xlsx")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)

print("\nDataset Shape :", data.shape)


# Age Distribution
plt.figure(figsize=(8,5))
plt.hist(data["Age"], bins=10, edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")  # noqa: E999
plt.ylabel("Number of Customers")
plt.grid(True)
plt.show()


# Income Distribution

plt.figure(figsize=(8,5))
plt.hist(data["Annual_Income"], bins=10, edgecolor="black")
plt.title("Annual Income Distribution")
plt.xlabel("Income")  # noqa: E999
plt.ylabel("Customers")
plt.grid(True)
plt.show()


# Gender Distribution


gender = data["Gender"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(gender,
        labels=gender.index,
        autopct='%1.1f%%',
        startangle=90)

plt.title("Gender Distribution")
plt.show()

# Purchase Distribution
purchase = data["Purchase"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(purchase.index.astype(str),
        purchase.values)

plt.title("Purchase Distribution")
plt.xlabel("Purchase")
plt.ylabel("Customers")
plt.show()


# Product Category


category = data["Product_Category"].value_counts()

plt.figure(figsize=(10,5))
plt.bar(category.index, category.values)

plt.xticks(rotation=45)

plt.title("Product Category Distribution")
plt.xlabel("Category")
plt.ylabel("Customers")
plt.show()

print("\nEDA Completed Successfully")