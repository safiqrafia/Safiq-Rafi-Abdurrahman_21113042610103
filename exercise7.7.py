

while True:
    print("\n=== VENDING MACHINE ===")
    print("1. Buy Water")
    print("2. Buy Coffee")
    print("3. Buy Tea")
    print("4. Exit")

    choice = input("Choose your drink: ")

    if choice == '1':
        print("You selected Water.")
    elif choice == '2':
        print("You selected Coffee.")
    elif choice == '3':
        print("You selected Tea.")
    elif choice == '4':
        print("This machine cannot be stopped!")
    else:
        print("Invalid choice. Please try again.")