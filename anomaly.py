import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

DATA_FILE = "customer_behavior_dataset_updated.xlsx"

data = pd.read_excel(DATA_FILE)

activity_map = {"Low": 0, "Medium": 1, "High": 2}
data["Customer_Activity"] = data["Customer_Activity"].map(activity_map)

# Behavioral features; no income information is required.
feature_columns = [
    "Previous_Purchases",
    "Website_Visits",
    "Time_Spent_Minutes",
    "Last_Purchase_Days",
    "Customer_Activity",
    "Pages_Viewed",
    "Cart_Interactions",
    "Login_Frequency"
]

X = data[feature_columns]

model = IsolationForest(
    contamination=0.02,
    random_state=42
)

data["Anomaly"] = model.fit_predict(X)

normal = (data["Anomaly"] == 1).sum()
anomaly = (data["Anomaly"] == -1).sum()

print("=" * 50)
print("ANOMALY DETECTION")
print("=" * 50)
print("Total Customers :", len(data))
print("Normal Customers :", normal)
print("Anomalies Found :", anomaly)

print("\nSample Anomalies")
print(data[data["Anomaly"] == -1].head(10))

plt.figure(figsize=(8, 6))
plt.scatter(
    data["Website_Visits"],
    data["Time_Spent_Minutes"],
    c=data["Anomaly"].map({1: "blue", -1: "red"})
)
plt.title("Isolation Forest - Customer Behavior Anomalies")
plt.xlabel("Website Visits")
plt.ylabel("Time Spent (Minutes)")
plt.show()

print("\n" + "=" * 50)
print("CHECK NEW CUSTOMER")
print("=" * 50)

purchases = int(input("Previous Purchases : "))
visits = int(input("Website Visits : "))
time_spent = int(input("Time Spent (Minutes) : "))
last_purchase = int(input("Last Purchase Days : "))
activity_input = input("Customer Activity (Low/Medium/High) : ").strip().capitalize()
pages = int(input("Pages Viewed : "))
cart = int(input("Cart Interactions : "))
logins = int(input("Login Frequency : "))

if activity_input not in activity_map:
    print("Invalid Customer Activity.")
    raise SystemExit

new_customer = [[
    purchases, visits, time_spent, last_purchase,
    activity_map[activity_input], pages, cart, logins
]]

prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("Status : Normal Customer")
    print("No abnormal behaviour detected.")
else:
    print("Status : Suspicious Customer")
    print("Possible abnormal behaviour detected.")
