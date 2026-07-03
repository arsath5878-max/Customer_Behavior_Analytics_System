import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Load Dataset
data = pd.read_excel("customer_purchase_dataset.xlsx")
print("="*60)
print("DATASET LOADED")
print("="*60)


# Missing Values
print("\nMissing Values")
print(data.isnull().sum())

# Duplicate Records
duplicates = data.duplicated().sum()
print("\nDuplicate Records :", duplicates)
data = data.drop_duplicates()

# Encode Categorical Columns
encoder = LabelEncoder()

categorical_columns = [
    "Gender",
    "Occupation",
    "City",
    "Product_Category",
    "Purchase"
]

for column in categorical_columns:
    data[column] = encoder.fit_transform(data[column])

print("\nCategorical Columns Encoded Successfully")

# Features and Target
X = data.drop(["Customer_ID", "Purchase"], axis=1)
y = data["Purchase"]
print("\nFeatures Shape :", X.shape)
print("Target Shape :", y.shape)


# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTrain Shape :", X_train.shape)

print("Test Shape :", X_test.shape)

print("\npreprocessing3 Completed Successfully")