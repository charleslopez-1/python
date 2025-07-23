def main ():
    intro = ("=" * 3 + " " + "Daily Planner" + " " + "=" * 3)
    print(intro)

    task_counter = int(input("How many tasks do you want to do today?: "))
    task = []

    print("Your task for today are: ")
    for i in range(1, task_counter + 1):
        chores = input(f"Task {i}: ")
        task.append(chores)

    print(f"\nYou have {task_counter} tasks today:")
    for i in range(1, task_counter + 1):
        print(f"Task {i}: {task[i - 1]} ")


if __name__ == "__main__":
    main()