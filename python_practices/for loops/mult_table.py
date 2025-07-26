def main ():
    
    while True:
        try:
            num = int(input("What multiplication table do you want to generate?: "))
            limit = int(input(f"{num} x up to? "))
            print(f"Multiplication table of {num} up to {limit}")
        except ValueError:
            print("Please enter an integer")
            continue
        
        for i in range(1, limit + 1):
            print(f"{num} x {i} = {num * i}")
        while True:
            choice = (input("Do you want to try another number? (yes/y or no/n) ")).lower()
            if choice in ["y", "yes"]:
                break
            elif choice in ["n", "no"]:
                print("Thank you! Exiting program...")
                exit()

            else:
                print("Invalid input! please enter \"yes/y\" or \"no/n\"")
            continue
if __name__ == "__main__":
    main()