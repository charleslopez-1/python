def main ():
    
    while True:
        try:
            num = int(input("What multiplication table do you want to generate?: "))
            print(f"Multiplication table of {num}")
        except ValueError:
            print("Please enter an integer")
            continue

        for i in range(1,10 + 1,1):
            print(f"{num} x {i} = {num * i}")
    

if __name__ == "__main__":
    main()