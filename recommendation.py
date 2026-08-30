import pandas as pd

DATA_FILE = "customer_behavior_dataset_updated.xlsx"
data = pd.read_excel(DATA_FILE)

print("=" * 60)
print("      PRODUCT RECOMMENDATION SYSTEM")
print("=" * 60)

customer_id = input("Enter Customer ID (Example: C00001): ").strip()
customer = data[data["Customer_ID"] == customer_id]

if customer.empty:
    print("\nCustomer Not Found!")
    raise SystemExit

category = customer.iloc[0]["Product_Category"]

print("\nCustomer ID :", customer_id)
print("Previous Purchased Category :", category)

recommendations = {
    "Electronics": ["Laptop Bag", "Wireless Mouse", "Keyboard", "USB Hub", "Webcam"],
    "Clothing": ["Jeans", "Jacket", "Sports Shoes", "Watch", "Cap"],
    "Books": ["Machine Learning", "Python Programming", "SQL Guide", "Java Programming", "Data Science Handbook"],
    "Sports": ["Cricket Bat", "Football", "Sports Shoes", "Gym Gloves", "Yoga Mat"],
    "Furniture": ["Office Chair", "Study Table", "Bookshelf", "Desk Lamp", "Computer Table"],
    "Groceries": ["Rice", "Milk", "Cooking Oil", "Vegetables", "Fruits"],
    "Beauty": ["Face Wash", "Shampoo", "Moisturizer", "Perfume", "Sunscreen"],
    "Toys": ["Building Blocks", "Puzzle", "Remote Car", "Doll", "Teddy Bear"]
}

print("\n" + "=" * 60)
print("RECOMMENDED PRODUCTS")
print("=" * 60)

if category in recommendations:
    for i, product in enumerate(recommendations[category], start=1):
        print(f"{i}. {product}")
else:
    print("No Recommendations Available")

print("\nRecommendation Completed Successfully")
