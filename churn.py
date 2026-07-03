import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

from sklearn.metrics import accuracy_score

# Load Dataset


data = pd.read_excel("customer_purchase_dataset_v2_with_churn.xlsx")

print("="*60)
print("CUSTOMER CHURN PREDICTION SYSTEM")
print("="*60)


# Encode Categorical Columns


encoder = LabelEncoder()
categorical_columns = [
    "Gender",
    "Occupation",
    "City",
    "Product_Category",
    "Purchase",
    "Customer_Activity",
    "Churn"
]

for col in categorical_columns:
    data[col] = encoder.fit_transform(data[col])


# Features & Target


X = data[
[
"Annual_Income",
"Previous_Purchases",
"Website_Visits",
"Time_Spent_Minutes",
"Last_Purchase_Days",
"Customer_Activity",
"Satisfaction_Rating"
]
]

y = data["Churn"]

# Train Test Split


X_train,X_test,y_train,y_test=train_test_split(
X,
y,
test_size=0.20,
random_state=42
)
xgb=XGBClassifier(
use_label_encoder=False,
eval_metric="logloss",
random_state=42
)
xgb.fit(X_train,y_train)

xgb_acc=accuracy_score(
y_test,
xgb.predict(X_test)
)

print("\nMODEL ACCURACY")
print("-"*40)

print(f"XGBoost : {xgb_acc*100:.2f}%")

# User Input

print("\n"+"="*60)
print("ENTER CUSTOMER DETAILS")
print("="*60)

customer_id=input("Customer ID : ")
income=float(input("Annual Income : "))
previous=int(input("Previous Purchases : "))
visits=int(input("Website Visits : "))
time_spent=int(input("Time Spent (Minutes) : "))
last_purchase=int(input("Last Purchase Days : "))
activity=input("Customer Activity (Low/Medium/High) : ")
rating=int(input("Satisfaction Rating (1-5) : "))

# Encode Activity

activity_map={"Low":0,"Medium":1,"High":2}

activity=activity_map[activity.capitalize()]

new_customer=[[
income,
previous,
visits,
time_spent,
last_purchase,
activity,
rating
]]

prediction=xgb.predict(new_customer)
probability=xgb.predict_proba(new_customer)
risk=max(probability[0])*100

print("\n"+"="*60)
print("CUSTOMER CHURN REPORT")
print("="*60)
print("Customer ID :",customer_id)

if prediction[0]==1:
    print("Risk Level : HIGH")
else:
    print("Risk Level : LOW")

print(f"Probability : {risk:.2f}%")
print("\nReason(s)")

if last_purchase>90:
    print("• No purchase in last 90 days")
if visits<10:
    print("• Low activity")
if rating<=2:
    print("• Low satisfaction rating")
if previous<5:
    print("• Very few previous purchases")

print("\nRecommendation")

if prediction[0]==1:
    print("✔ Send discount coupon")
    print("✔ Offer loyalty rewards")
    print("✔ Send personalized email")
else:
    print("✔ Customer is active")
    print("✔ Continue regular engagement")
