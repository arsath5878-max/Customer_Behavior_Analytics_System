import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder
from sklearn.cluster import KMeans



data = pd.read_excel("customer_purchase_dataset.xlsx")
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


X = data[[
    "Annual_Income",
    "Previous_Purchases",
    "Website_Visits",
    "Time_Spent_Minutes",
    "Discount_Percent"
]]


kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

data["Cluster"] = kmeans.fit_predict(X)

# Assign Meaningful Names

cluster_names = {
    0: "Premium Customer",
    1: "Budget Customer",
    2: "Regular Customer"
}

data["Customer_Segment"] = data["Cluster"].map(cluster_names)


# Display Customer Count


print("=" * 60)
print("CUSTOMER SEGMENTATION")
print("=" * 60)

print("\nCustomer Count in Each Segment\n")

print(data["Customer_Segment"].value_counts())

# Visualization
colors = {
    "Premium Customer": "red",
    "Regular Customer": "blue",
    "Budget Customer": "green"
}

plt.figure(figsize=(8,6))

for segment in colors:

    temp = data[data["Customer_Segment"] == segment]

    plt.scatter(
        temp["Annual_Income"],
        temp["Previous_Purchases"],
        color=colors[segment],
        label=segment
    )

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income")
plt.ylabel("Previous Purchases")
plt.legend()
plt.grid(True)
plt.show()
print("\nCustomer Segmentation Completed Successfully")