import sys

def main():
    print("\nWelcome to MATH CLUB!\n")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    full_name = first_name + " " + last_name

    print("Good day to you! Your full name is:", full_name)
    while True:
            choice = input("Would you like to add a nickname?: ").lower()
            if choice in ["yes", "y"]:
                try:
                    nickname = str(input("Enter your nickname: "))
                    print("Okay Mr.", full_name,"your nickname is", nickname)
                    break
                except ValueError:
                    print("Please enter a valid name using only letters (A-Z)")
            elif choice in ["no", "n"]:
                break
            else:
                print("Only 'yes', 'no', 'n', 'y' are valid inputs!")

    while True:
                try:
                    age = int(input("Please enter your age: "))
                except ValueError:
                    print("Invalid input!, please enter a number!")
                    continue

                if (age < 18):
                    print("You're underage! Exiting program...")
                    sys.exit()
                    
                else:
                    while True:    
                        print("Input two numbers you want to know to sum and product of!")
                        try:
                            x = int(input("First value is: "))
                            y = int(input("Second value is: "))
                        except ValueError:
                            print("Invalid number input, Try again!")
                            continue

                        total_sum = x + y
                        total_product = x * y

                        print("Their sum is:", total_sum)
                        print("Their product is", total_product)
                        if (total_sum % 2 == 0 and total_product % 2 == 0):
                            print("\nBoth result are even number!")
                        else:
                            print("Atleast one result is an odd number")

                        sum_squared = total_sum ** 2
                        prod_squared = total_product ** 2

                        print("The square of your total sum", first_name, "is", sum_squared)
                        print("The square of the product of these two numbers are: ", prod_squared)
                        while True:
                            user_input = input("Do you want to try again? (y/n): ").lower()
                            if user_input in ["no","n"]: 
                                print("Thank you for trying our program! Exiting..")
                                break
                            elif user_input in ["yes", "y"]:
                                break
                            elif user_input not in ["yes", "no", "y", "n"]:
                                print("Valid inputs are only 'yes', 'no', 'y', 'n'")
                                continue
if __name__ == "__main__":
    main()
