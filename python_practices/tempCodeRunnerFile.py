choice = input("Do you want to play again? (y/n): ").lower()
            if choice in ['y']:
                break
            elif choice in ['n']:
                print("Thank you for playing")
                return
            else:
                print("Please enter a valid input y or n!")
                continue