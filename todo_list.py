import sys
from typing import List, Dict, Union, Optional

# Type alias for task structure
Task = Dict[str, Union[str, bool]]

tasks: List[Task] = []

def get_valid_index(prompt_text: str) -> Optional[int]:
    """
    Prompts user for an index, validates it against the task list,
    and returns the 0-based index or None.
    """
    try:
        raw_input = input(prompt_text)
        if raw_input.lower() == 'q':
            return None
            
        index = int(raw_input) - 1
        if 0 <= index < len(tasks):
            return index
        else:
            print("❌ Invalid task number.")
            return None
    except ValueError:
        print("❌ Invalid input. Please enter a number.")
        return None

def add_task() -> None:
    while True:
        description = input("Enter the task description (or 'q' to cancel): ")
        if description.lower() == 'q':
            return
            
        if description.strip():
            tasks.append({"description": description, "completed": False})
            print(f"✅ Task '{description}' added!")
            break
        print("⚠️ Description cannot be empty.")

def view_tasks() -> None:
    print("\n--- Your To-Do List ---")
    if not tasks:
        print("✨ Looks empty here! Time to add some tasks. ✨")
    else:
        for i, task in enumerate(tasks, 1):
            status_marker = "[X]" if task["completed"] else "[ ]"
            print(f"{i}. {status_marker} {task['description']}")
    print("-----------------------\n")

def mark_task_complete() -> None:
    view_tasks()
    if not tasks:
        return

    index = get_valid_index("Enter number to mark complete (or 'q' to cancel): ")
    if index is not None:
        if tasks[index]["completed"]:
            print(f"👍 Task '{tasks[index]['description']}' is already complete!")
        else:
            tasks[index]["completed"] = True
            print(f"🎉 Task '{tasks[index]['description']}' marked as complete!")

def remove_task() -> None:
    view_tasks()
    if not tasks:
        return

    index = get_valid_index("Enter number to remove (or 'q' to cancel): ")
    if index is not None:
        removed = tasks.pop(index)
        print(f"🗑️ Task '{removed['description']}' removed.")

def main() -> None:
    print("\n🚀 Welcome to your Refactored To-Do List! 🚀")

    while True:
        print("\n--- Menu ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Remove Task")
        print("5. Quit")
        print("------------")
        
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_task_complete()
        elif choice == "4":
            remove_task()
        elif choice == "5":
            print("\n👋 Goodbye!")
            sys.exit()
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    main()
