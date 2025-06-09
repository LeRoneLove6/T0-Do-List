def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")

def add_task(tasks):
    try:
        task = input("Enter the task: ")
        if not task.strip():
            print("Task cannot be empty.")
        else:
            tasks.append(task)
    except Exception as e:
        print(f"Unexpected error: {e}")
    else:
        if task.strip():
            print("Task added!")
    finally:
        print("Returning to menu...")

def delete_task(tasks):
    try:
        if not tasks:
            print("No tasks to delete.")
            return
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")
        num_input = input("Enter the task number to delete: ")
        if not num_input.isdigit():
            print("Please enter a valid number.")
            return
        num = int(num_input)
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed task: {removed}")
        else:
            print("Task number does not exist.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        print("Returning to menu...")

def main():
    print("Welcome to the To-Do List!")
    tasks = []
    while True:
        show_menu()
        try:
            choice = input("Choose an option (1-4): ")
            if choice == '1':
                add_task(tasks)
            elif choice == '2':
                if not tasks:
                    print("No tasks to view.")
                else:
                    print("\nYour Tasks:")
                    for idx, task in enumerate(tasks, 1):
                        print(f"{idx}. {task}")
            elif choice == '3':
                delete_task(tasks)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid menu option.")
        except Exception as e:
            print(f"Unexpected error: {e}")
        finally:
            pass 

if __name__ == "__main__":
    main()