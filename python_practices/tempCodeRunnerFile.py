while True:
        try:
            num = int(input("What multiplication table do you want to generate?: "))
            print(f"Multiplication table of {num}")
        except ValueError:
            print("Please enter an integer")

            for i in range(1,10 + 1,1):
                print(f"{num} x {i} = {num * i}")