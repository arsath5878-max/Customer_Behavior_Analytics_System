import os

while True:

    print("\n" + "="*60)
    print(" AI CUSTOMER PURCHASE PREDICTION SYSTEM ")
    print("="*60)

    print("1.  Dataset")
    print("2. Data Preprocessing")
    print("3. Exploratory Data Analysis")
    print("4. Product recommendation")
    print("5. Customer Segmentation")
    print("6. Anomaly Detection")
    print("7.churn Prediction")
    print("8.  Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":
        os.system("python dataset.py")

    elif choice == "2":
        os.system("python preprocessing.py")

    elif choice == "3":
        os.system("python EDA.py")

    elif choice == "4":
        os.system("python recommendation.py")

    elif choice == "5":
        os.system("python segmentation.py")

    elif choice == "6":
        os.system("python anomaly.py")
        
    elif choice == "7":
        os.system("python churn.py")
        
    elif choice == "8":
        print("\nThank You")
        print("Project Completed Successfully")
        break


    else:
        print("\nInvalid Choice")