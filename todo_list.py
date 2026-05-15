import os

# List to store tasks
tasks = []


# Function to clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Function to view tasks
def view_tasks():
    print("\n===== YOUR TASKS =====")

    if not tasks:
        print("  No tasks yet!")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"  {i}. {task}")

    print("======================\n")


# Function to add a task
def add_task():
    task = input("Enter task: ").strip()

    if task:
        tasks.append(task)
        print(f"✓ Task added: '{task}'")
    else:
        print("Task cannot be empty.")


# Function to delete a task
def delete_task():
    view_tasks()

    if not tasks:
        return

    try:
        num = int(input("Enter task number to delete: "))

        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"✓ Deleted: '{removed}'")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# Main program
def main():

    while True:
        print("\n============================")
        print("   SIMPLE TO-DO LIST CLI")
        print("============================")

        print("\nMENU:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")

        choice = input("\nChoose an option (1-4): ").strip()

        if choice == '1':
            clear()
            view_tasks()

        elif choice == '2':
            clear()
            add_task()

        elif choice == '3':
            clear()
            delete_task()

        elif choice == '4':
            print("\nGoodbye! Good luck with your submission! 👋\n")
            break

        else:
            print("Invalid choice. Please enter 1-4.")


# Run program
if __name__ == "__main__":
    main()