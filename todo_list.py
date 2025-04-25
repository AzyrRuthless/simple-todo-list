import time # Just for a small effect if needed, not strictly necessary for core logic

# Store tasks as a list of dictionaries to include completion status
# Each task will look like: {'description': 'Do laundry', 'completed': False}
tasks = []

def add_task(description):
    """Adds a new task dictionary to the list."""
    # Basic validation: ensure description is not empty
    if not description.strip():
        print("Task description cannot be empty.")
        return
    task = {"description": description, "completed": False}
    tasks.append(task)
    print(f"✅ Task '{description}' added!")

def view_tasks():
    """Displays the current list of tasks with their status."""
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("✨ Looks empty here! Time to add some tasks. ✨")
    else:
        for i, task in enumerate(tasks, 1):
            # Determine the status marker based on the 'completed' key
            status_marker = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status_marker} {task['description']}")
    print("-----------------------\n")

def mark_task_complete():
    """Marks a specific task as complete."""
    view_tasks() # Show tasks first for user to see numbers
    if not tasks: # No tasks to mark
        return

    try:
        task_num_str = input("Enter the number of the task to mark as complete: ")
        # Convert input to an integer and adjust for 0-based index
        task_index = int(task_num_str) - 1

        # Check if the provided index is valid
        if 0 <= task_index < len(tasks):
            if tasks[task_index]["completed"]:
                 print(f"👍 Task '{tasks[task_index]['description']}' is already complete!")
            else:
                tasks[task_index]["completed"] = True
                print(f"🎉 Task '{tasks[task_index]['description']}' marked as complete!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        # Handle cases where input is not a number
        print("Invalid input. Please enter a number.")

def remove_task():
    """Removes a specific task from the list."""
    view_tasks() # Show tasks first
    if not tasks: # No tasks to remove
        return

    try:
        task_num_str = input("Enter the number of the task to remove: ")
        task_index = int(task_num_str) - 1

        if 0 <= task_index < len(tasks):
            # Use pop to remove the task and get its description for the message
            removed_task = tasks.pop(task_index)
            print(f"🗑️ Task '{removed_task['description']}' removed.")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    """Main function to run the to-do list application."""
    print("\n🚀 Welcome to your Enhanced To-Do List! 🚀")

    while True:
        # Display menu options
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Quit")
        print("------------")
        choice = input("Choose an option (1-5): ")

        # Process user choice
        if choice == "1":
            task_desc = input("Enter the task description: ")
            add_task(task_desc)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("\n👋 Goodbye! Keep crushing those tasks!")
            break # Exit the main loop
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Standard Python entry point check
if __name__ == "__main__":
    main()
    
