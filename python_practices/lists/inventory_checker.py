def main():

    inventory = ["apple", "banana", "orange", "apple", "banana", "apple"]
    print("\nApple ===== Banana ===== Orange\n")
    while True:
        item = input("What item do you want to check the stocks? ").lower()
        
        if item in inventory:
            count = inventory.count(item)
            print(f"{item.capitalize()} stocks: {count}")
        else:
            print(f"{item.capitalize()} is not in stock!")

        while True:
            choice = input("Do you want to check other stocks? (y/n): ").lower()
            if choice in ['y']:
                break
            elif choice in ['n']:
                return
            else: 
                print("Please input y or n!")
                continue

    
    # item = input("What item do you want to check the stocks? ").lower()
    # if item == "apple":
    #     app = inventory.count("apple")
    #     print(f"Apple stocks: {app}")
    # elif item == "banana":
    #     bann = inventory.count("banana")
    #     print(f"Banana stocks: {bann}")
    # elif item == "orange":
    #     oran = inventory.count("orange")
    #     print(f"Orange stocks: {oran}")
    
    







if __name__ == "__main__":
    main()