# Task Manager Python

This is a **Command Line Task Manager** built with Python. It allows you to manage tasks with features such as adding, removing, viewing, and marking tasks as completed. Additionally, tasks can be saved and loaded from a file to maintain history.

## Requirements

- Python 3.6 or later installed on your system.

## How to Run the Project

Follow these steps to run the project:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/ricardotassio/TaskManagerPython.git
   cd TaskManagerPython
   ```

2. **Run the program**:
   In the project root directory, run the following command:

   ```bash
   python main.py
   ```

3. **Use the menu to manage your tasks**:
   After starting the program, the following menu will appear:

   ```
   ------------------------------
   TO-DO LIST MANAGER
   ------------------------------
   1. View Tasks
   2. Add Task
   3. Remove Task
   4. Mark Task as Completed
   5. Save Tasks
   6. Load Tasks
   7. Quit
   ------------------------------
   ```

4. **Choose an option**:

   - Enter the number corresponding to the desired action.
   - For example, to add a new task, type `2` and provide the task description.

5. **Return to the main menu**:
   - After entering an option, the program will prompt you to press `M` or `m` to return to the menu.
   - Example:
     ```
     Press 'M' to go back to the menu:
     ```

## Features

- **View Tasks**: Lists all pending or completed tasks.
- **Add Task**: Add a new task to the manager.
- **Remove Task**: Delete a task from the list by its index.
- **Mark Task as Completed**: Change the status of a task to completed.
- **Save Tasks**: Save tasks to the `tasks.txt` file for persistence.
- **Load Tasks**: Load previously saved tasks from the `tasks.txt` file.

## Example Execution

```plaintext
------------------------------
TO-DO LIST MANAGER
------------------------------
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Save Tasks
6. Load Tasks
7. Quit
------------------------------
Choose an option: 2
Enter the task description: Buy groceries
Task added successfully.

Press 'M' to go back to the menu: M
------------------------------
TO-DO LIST MANAGER
------------------------------
1. View Tasks
2. Add Task
3. Remove Task
4. Mark Task as Completed
5. Save Tasks
6. Load Tasks
7. Quit
------------------------------
```
