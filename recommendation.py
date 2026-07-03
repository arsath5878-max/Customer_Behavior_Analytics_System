
import pandas as pd

# Load Dataset

data = pd.read_excel("customer_purchase_dataset_v2_with_churn.xlsx")

print("=" * 60)
print("      PRODUCT RECOMMENDATION SYSTEM")
print("=" * 60)

# Get Customer ID


customer_id = input("Enter Customer ID (Example: C00001): ").strip()

customer = data[data["Customer_ID"] == customer_id]

if customer.empty:
    print("\nCustomer Not Found!")
    exit()


# Get Customer Details


category = customer.iloc[0]["Product_Category"]

print("\nCustomer ID :", customer_id)
print("Previous Purchased Category :", category)

# Product Recommendation Dictionary


recommendations = {

    "Electronics": [
        "Laptop Bag",
        "Wireless Mouse",
        "Keyboard",
        "USB Hub",
        "Webcam"
    ],

    "Clothing": [
        "Jeans",
        "Jacket",
        "Sports Shoes",
        "Watch",
        "Cap"
    ],

    "Books": [
        "Machine Learning",
        "Python Programming",
        "SQL Guide",
        "Java Programming",
        "Data Science Handbook"
    ],

    "Sports": [
        "Cricket Bat",
        "Football",
        "Sports Shoes",
        "Gym Gloves",
        "Yoga Mat"
    ],

    "Furniture": [
        "Office Chair",
        "Study Table",
        "Bookshelf",
        "Desk Lamp",
        "Computer Table"
    ],

    "Groceries": [
        "Rice",
        "Milk",
        "Cooking Oil",
        "Vegetables",
        "Fruits"
    ],

    "Beauty": [
        "Face Wash",
        "Shampoo",
        "Moisturizer",
        "Perfume",
        "Sunscreen"
    ],

    "Toys": [
        "Building Blocks",
        "Puzzle",
        "Remote Car",
        "Doll",
        "Teddy Bear"
    ]
}


# Display Recommendations


print("\n" + "=" * 60)
print("RECOMMENDED PRODUCTS")
print("=" * 60)

if category in recommendations:

    print("\nRecommended Products\n")

    for i, product in enumerate(recommendations[category], start=1):
        print(f"{i}. {product}")

else:
    print("No Recommendations Available")

print("\nRecommendation Completed Successfully")