import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

DATA_FILE = "customer_behavior_dataset_updated.xlsx"

print("|" * 60)
print("CUSTOMER CHURN PREDICTION SYSTEM")
print("|" * 60)

data = pd.read_excel(DATA_FILE)

# Encode the behavioral category consistently
activity_map = {"Low": 0, "Medium": 1, "High": 2}
data["Customer_Activity"] = data["Customer_Activity"].map(activity_map)

# Encode target
churn_map = {"No": 0, "Yes": 1}
data["Churn"] = data["Churn"].map(churn_map)

# Behavioral features - Annual Income is intentionally not used
feature_columns = [
    "Age",
    "Previous_Purchases",
    "Website_Visits",
    "Time_Spent_Minutes",
    "Discount_Percent",
    "Last_Purchase_Days",
    "Customer_Activity",
    "Satisfaction_Rating",
    "Pages_Viewed",
    "Cart_Interactions",
    "Login_Frequency"
]

X = data[feature_columns]
y = data["Churn"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

xgb = XGBClassifier(
    eval_metric="logloss",
    random_state=42
)

xgb.fit(X_train, y_train)

predictions = xgb.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print("\nMODEL ACCURACY")
print("-" * 40)
print(f"XGBoost : {accuracy * 100:.2f}%")

print("\n" + "=" * 60)
print("ENTER CUSTOMER DETAILS")
print("=" * 60)

customer_id = input("Customer ID : ")
age = int(input("Age : "))
previous = int(input("Previous Purchases : "))
visits = int(input("Website Visits : "))
time_spent = int(input("Time Spent (Minutes) : "))
discount = float(input("Discount Percent : "))
last_purchase = int(input("Last Purchase Days : "))
activity_input = input("Customer Activity (Low/Medium/High) : ").strip().capitalize()
rating = int(input("Satisfaction Rating (1-5) : "))
pages = int(input("Pages Viewed : "))
cart = int(input("Cart Interactions : "))
logins = int(input("Login Frequency : "))

if activity_input not in activity_map:
    print("Invalid Customer Activity. Use Low, Medium, or High.")
    raise SystemExit

activity = activity_map[activity_input]

new_customer = pd.DataFrame([[
    age, previous, visits, time_spent, discount, last_purchase,
    activity, rating, pages, cart, logins
]], columns=feature_columns)

prediction = int(xgb.predict(new_customer)[0])
probability = xgb.predict_proba(new_customer)[0]
churn_probability = probability[1]

print("\n" + "=" * 60)
print("CUSTOMER CHURN REPORT")
print("=" * 60)
print("Customer ID :", customer_id)

if prediction == 1:
    print("Risk Level : HIGH")
else:
    print("Risk Level : LOW")

print(f"Churn Probability : {churn_probability * 100:.2f}%")

print("\nChurn Risk Factors")
factor_found = False

if last_purchase > 90:
    print("• Long gap since last purchase")
    factor_found = True
if visits < 10:
    print("• Low website activity")
    factor_found = True
if rating <= 2:
    print("• Low satisfaction rating")
    factor_found = True
if previous < 5:
    print("• Very few previous purchases")
    factor_found = True
if logins < 5:
    print("• Low login frequency")
    factor_found = True
if pages < 10:
    print("• Low number of pages viewed")
    factor_found = True

if not factor_found:
    print("• No major rule-based risk indicators detected")

print("\nRecommendation")

if prediction == 1:
    print("✔ Send discount coupon")
    print("✔ Offer loyalty rewards")
    print("✔ Send personalized email")
else:
    print("✔ Customer is active")
    print("✔ Continue regular engagement")
