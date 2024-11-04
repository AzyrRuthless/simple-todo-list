tasks = []

def add_task(task):
    tasks.append(task)
    print(f"'{task}' has been added to the list.")

def view_tasks():
    print("Here are your tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def main():
    while True:
        print("\nOptions:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            task = input("Enter a new task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
