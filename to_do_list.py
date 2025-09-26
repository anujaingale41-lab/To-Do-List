#todo list
import os

TODO_FILE = "todo.txt"

def show_menu():
    print("\n📋 To-Do List Manager")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Mark task as complete")
    print("5. Exit")

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter the task: ")
    tasks = load_tasks()
    tasks.append("[ ] " + task)
    save_tasks(tasks)
    print("Task added!")

def remove_task():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter the task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_complete():
    tasks = load_tasks()
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            if tasks[task_num - 1].startswith("[✓]"):
                print("Task is already marked as complete.")
            else:
                tasks[task_num - 1] = tasks[task_num - 1].replace("[ ]", "[✓]", 1)
                save_tasks(tasks)
                print("Task marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_complete()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
