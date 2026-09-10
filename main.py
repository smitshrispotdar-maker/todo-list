tasks = []


def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")


def add_task():
    task = input("Enter your task: ").strip()

    if task:
        tasks.append(task)
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")


def view_tasks():
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, 1):
        print(f"{index}. {task}")


def delete_task():
    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_number = int(input("Enter task number to delete: "))

        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task}' deleted successfully!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    actions = {
        "1": add_task,
        "2": view_tasks,
        "3": delete_task
    }

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "4":
            print("Thank you for using the To-Do List!")
            break

        action = actions.get(choice)

        if action:
            action()
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()

