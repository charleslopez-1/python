def main ():

    print("Welcome to our Palindrome Checker")
    checker = input("Enter a word to check if it is palindrome: ").replace(" ", "").lower()
    if (checker) == (checker)[::-1]:
        print("This word is a palidrome!")
    else:
        print("Not a palindrome bud!")

main()