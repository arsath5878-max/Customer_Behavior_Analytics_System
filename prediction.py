import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

data = pd.read_excel("customer_behavior_dataset_updated.xlsx")

encoder = LabelEncoder()
for col in ["Gender", "Occupation", "City", "Product_Category"]:
    data[col] = encoder.fit_transform(data[col])

data["Purchase"] = data["Purchase"].map({"No": 0, "Yes": 1})

X = data.drop(["Customer_ID", "Purchase"], axis=1)
y = data["Purchase"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=2000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42),
    "XGBoost": XGBClassifier(eval_metric="logloss", random_state=42)
}

results = []

for name, model in models.items():
    model.fit(X_train, y_train)
    pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, pred)
    precision = precision_score(y_test, pred, zero_division=0)
    recall = recall_score(y_test, pred, zero_division=0)
    f1 = f1_score(y_test, pred, zero_division=0)

    results.append([name, accuracy, precision, recall, f1])

    print("\n", name)
    print("Accuracy :", f"{accuracy * 100:.2f}%")
    print("Precision:", f"{precision * 100:.2f}%")
    print("Recall   :", f"{recall * 100:.2f}%")
    print("F1 Score :", f"{f1 * 100:.2f}%")
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, pred))

print("\nMODEL COMPARISON")
print("-" * 70)
print("Model\t\t\tAccuracy\tPrecision\tRecall\tF1 Score")

for result in results:
    print(f"{result[0]:20} {result[1]:.2%}\t\t{result[2]:.2%}\t\t{result[3]:.2%}\t{result[4]:.2%}")

best = max(results, key=lambda x: x[4])

print("\nBEST MODEL:", best[0])
print("F1 Score:", f"{best[4] * 100:.2f}%")
