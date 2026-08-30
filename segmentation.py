import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

DATA_FILE = "customer_behavior_dataset_updated.xlsx"

data = pd.read_excel(DATA_FILE)

activity_map = {"Low": 0, "Medium": 1, "High": 2}
data["Customer_Activity"] = data["Customer_Activity"].map(activity_map)

# Segment customers using behavior instead of income.
feature_columns = [
    "Previous_Purchases",
    "Website_Visits",
    "Time_Spent_Minutes",
    "Discount_Percent",
    "Pages_Viewed",
    "Cart_Interactions",
    "Login_Frequency"
]

X = data[feature_columns]

# Scaling prevents large-valued features from dominating distance calculations.
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

data["Cluster"] = kmeans.fit_predict(X_scaled)

# Give clusters descriptive names based on behavioral profiles.
cluster_means = data.groupby("Cluster")[feature_columns].mean()
engagement_score = (
    cluster_means["Previous_Purchases"] +
    cluster_means["Website_Visits"] +
    cluster_means["Time_Spent_Minutes"] / 10 +
    cluster_means["Pages_Viewed"] / 5 +
    cluster_means["Cart_Interactions"] +
    cluster_means["Login_Frequency"]
)

ordered_clusters = engagement_score.sort_values().index.tolist()

cluster_names = {
    ordered_clusters[0]: "Low Engagement Customer",
    ordered_clusters[1]: "Regular Customer",
    ordered_clusters[2]: "Highly Engaged Customer"
}

data["Customer_Segment"] = data["Cluster"].map(cluster_names)

print("=" * 60)
print("CUSTOMER SEGMENTATION")
print("=" * 60)
print("\nCustomer Count in Each Segment\n")
print(data["Customer_Segment"].value_counts())

plt.figure(figsize=(8, 6))
for segment in [
    "Low Engagement Customer",
    "Regular Customer",
    "Highly Engaged Customer"
]:
    temp = data[data["Customer_Segment"] == segment]
    plt.scatter(
        temp["Website_Visits"],
        temp["Time_Spent_Minutes"],
        label=segment
    )

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Website Visits")
plt.ylabel("Time Spent (Minutes)")
plt.legend()
plt.grid(True)
plt.show()

print("\nCustomer Segmentation Completed Successfully")
