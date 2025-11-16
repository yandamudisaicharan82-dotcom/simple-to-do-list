# Simple To-Do List Application (Console-based)

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def show_menu():
    print("\n--- TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\nYour Tasks:")
            if len(tasks) == 0:
                print("No tasks yet!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")

        elif choice == "2":
            task = input("Enter new task: ")
            tasks.append(task)
            save_tasks(tasks)
            print("Task added!")

        elif choice == "3":
            if len(tasks) == 0:
                print("No tasks to remove!")
            else:
                for i, task in enumerate(tasks, start=1):
                    print(f"{i}. {task}")
                try:
                    num = int(input("Enter task number to remove: "))
                    removed = tasks.pop(num - 1)
                    save_tasks(tasks)
                    print(f"Removed: {removed}")
                except (IndexError, ValueError):
                    print("Invalid choice!")

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    main()
