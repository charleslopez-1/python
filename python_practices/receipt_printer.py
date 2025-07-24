def main ():
        
    print("=" * 3 + " " + "Welcome to Lalaine's Coffee Shop" + " " + "=" * 3 + "\n")
        
    name = input("Please enter your name: ")
    print(f"Good day {name}! Kindly complete your order\n")

    while True:
        try:
            item = input("Enter item name: ").title()
            qnty = int(input("Enter its quantity: "))
            srp = float(input("Enter price: "))
            payment = float(input("Enter payment: " ))
        except ValueError:
            print("Please enter a valid input!")
            continue

        discount = .20
        total_bill =  qnty * srp
        discount_bill = 0
        final_bill = total_bill

        if total_bill >= 500:
            discount_bill = total_bill * discount
            final_bill = total_bill - discount_bill
        if payment > final_bill:
            change = payment - final_bill
            
        print("\n\t=== Your receipt === ")
        print(f"Item name:                  {item}")
        print(f"Quantity:                   {qnty}")
        print(f"Price:                  PHP {srp}")
        print(f"Payment:                PHP {payment}")
        print(f"Total Bill:             PHP {total_bill}")
        print(f"Discount:               PHP {discount_bill:.2f}")
        print(f"Discounted Total Bill:  PHP {final_bill:.2f}")
        print(f"Change:                 PHP {change:.2f}\n")
        print("Thank you for ordering!")
        while True:
            choice = input("Do you want to try another order?: ").lower()
            if choice in ["yes", 'y']:
                break
            elif choice in ["no", 'n']:
                print("Exiting program...")
                return
            else:
                print("Please enter a valid input (yes / no or y / n)")
                continue
if __name__ == "__main__":
    main()

    