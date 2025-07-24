def main():
    
    print("Welcome to my guessing game!")
    target = 87
    while True:
        try:
            guess = int(input("Please enter the lucky number (1 - 100): "))
            if guess == target:
                print("You have won 1000 dollars!")
            else:
                print("Try again")
        except ValueError:
            print("Please enter a valid number!")
            
if __name__ == "__main__":
    main()