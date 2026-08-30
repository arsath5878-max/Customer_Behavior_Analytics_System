import pandas as pd
from sklearn.model_selection import train_test_split

DATA_FILE = "customer_behavior_dataset_updated.xlsx"

data = pd.read_excel(DATA_FILE)

print("=" * 60)
print("DATA PREPROCESSING")
print("=" * 60)

print("\nMissing Values")
print(data.isnull().sum())

duplicates = data.duplicated().sum()
print("\nDuplicate Records :", duplicates)

data = data.drop_duplicates()

# Encode categorical values with explicit mappings where appropriate.
activity_map = {"Low": 0, "Medium": 1, "High": 2}
purchase_map = {"No": 0, "Yes": 1}
churn_map = {"No": 0, "Yes": 1}

data["Customer_Activity"] = data["Customer_Activity"].map(activity_map)
data["Purchase"] = data["Purchase"].map(purchase_map)
data["Churn"] = data["Churn"].map(churn_map)

print("\nCategorical Columns Encoded Successfully")

# For the purchase prediction module.
X = data.drop(["Customer_ID", "Purchase"], axis=1)
y = data["Purchase"]

print("\nFeatures Shape :", X.shape)
print("Target Shape :", y.shape)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTrain Shape :", X_train.shape)
print("Test Shape :", X_test.shape)

print("\nPreprocessing Completed Successfully")
