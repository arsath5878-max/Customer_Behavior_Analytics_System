import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import IsolationForest

# Load Dataset


data = pd.read_excel("customer_purchase_dataset.xlsx")


# Encode Categorical Columns


encoder = LabelEncoder()

columns = [
    "Gender",
    "Occupation",
    "City",
    "Product_Category",
    "Purchase"
]

for col in columns:
    data[col] = encoder.fit_transform(data[col])



X = data[
    [
        "Annual_Income",
        "Previous_Purchases",
        "Website_Visits",
        "Time_Spent_Minutes"
    ]
]


# Isolation Forest Model


model = IsolationForest(
    
    contamination=0.02,
    random_state=42
    
)

data["Anomaly"] = model.fit_predict(X)


# Count Normal and Anomaly


normal = (data["Anomaly"] == 1).sum()
anomaly = (data["Anomaly"] == -1).sum()

print("=" * 50)
print("ANOMALY DETECTION")
print("=" * 50)

print("Total Customers :", len(data))
print("Normal Customers :", normal)
print("Anomalies Found :", anomaly)

# Display First 10 Anomalies
print("\nSample Anomalies")

print(data[data["Anomaly"] == -1].head(10))


# Scatter Plot


colors = data["Anomaly"].map({1: "blue", -1: "red"})

plt.figure(figsize=(8,6))

plt.scatter(
    data["Annual_Income"],
    data["Previous_Purchases"],
    c=colors
)

plt.title("Isolation Forest Anomaly Detection")

plt.xlabel("Annual Income")

plt.ylabel("Previous Purchases")

plt.show()
print("\n")
print("=" * 50)
print("CHECK NEW CUSTOMER")
print("=" * 50)

income = float(input("Enter Annual Income : "))
purchases = int(input("Enter Previous Purchases : "))
visits = int(input("Enter Website Visits : "))
time_spent = int(input("Enter Time Spent (Minutes) : "))

new_customer = [[income, purchases, visits, time_spent]]

prediction = model.predict(new_customer)

print("\n")

if prediction[0] == 1:
    print("Status : Normal Customer")
    print("No abnormal behaviour detected.")
else:
    print("Status : Suspicious Customer")
    print("Possible abnormal behaviour detected.")