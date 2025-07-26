def main():

    steps_daily = [2000, 3500, 4000, 4350, 2040, 5000]
    total = 0
    average = 0
    
    for step in steps_daily:
        total += step
        
    average = total / len(steps_daily)

    print(total)
    print(f"{average:.2f}")


    



if __name__ == "__main__":
    main()