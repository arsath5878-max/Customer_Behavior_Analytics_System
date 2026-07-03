import pandas as pd

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score
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


# Features and Target
X = data.drop(["Customer_ID", "Purchase"], axis=1)

y = data["Purchase"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

# Logistic Regression


lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)

lr_pred = lr.predict(X_test)

lr_acc = accuracy_score(y_test, lr_pred)

# Decision Tree

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

dt_acc = accuracy_score(y_test, dt_pred)

# Random Forest
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

# XGB
xgb = XGBClassifier()
xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)
xgb_acc = accuracy_score(y_test, xgb_pred)

# Results

print("="*50)
print("MODEL ACCURACY")
print("="*50)

print(f"Logistic Regression : {lr_acc*100:.2f}%")
print(f"Decision Tree       : {dt_acc*100:.2f}%")
print(f"Random Forest       : {rf_acc*100:.2f}%")
print(f"XGBoost             : {xgb_acc*100:.2f}%")