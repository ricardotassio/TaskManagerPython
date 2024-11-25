import TaskManager

def main():
    manager = TaskManager.TaskManager()

    def display_menu():
        print("\n" + "-" * 30)
        print("TO-DO LIST MANAGER")
        print("-" * 30)
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Save Tasks")
        print("6. Load Tasks")
        print("7. Quit")
        print("-" * 30)

    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            manager.view_tasks()
        elif choice == '2':
            description = input("Enter the task description: ")
            manager.add_task(description)
        elif choice == '3':
            try:
                index = int(input("Enter the task index to remove: "))
                manager.remove_task(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '4':
            try:
                index = int(input("Enter the task index to mark as completed: "))
                manager.mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == '5':
            manager.save_tasks()
        elif choice == '6':
            manager.load_tasks()
        elif choice == '7':
            save = input("Save tasks before quitting? (y/n): ")
            if save.lower() == 'y':
                manager.save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        # Wait for the user to press 'M' to return to the menu
        while True:
            back_to_menu = input("\nPress 'M' to go back to the menu: ").strip().lower()
            if back_to_menu == 'm':
                break
            else:
                print("Invalid input. Please press 'M' to go back to the menu.")

if __name__ == "__main__":
    main()
