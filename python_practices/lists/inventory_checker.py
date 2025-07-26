def main():

    inventory = ["apple", "banana", "orange", "apple", "banana", "apple"]
    item = input("What item do you want to check the stocks? ").lower()
    
    if item in inventory:
        count = inventory.count(item)
        print(f"{item.capitalize()} stocks: {count}")
    else:
        print(f"{item.capitalize()} is not in stock!")
    

    
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