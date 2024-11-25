import os
import json

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.file_name = "tasks.txt"

    def add_task(self, description):
        self.tasks.append({"description": description, "completed": False})
        print("Task added successfully.")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Removed task: {removed_task['description']}")
        else:
            print("Invalid task index.")

    def view_tasks(self):
        print(self.tasks)
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['description']} - {status}")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task index.")

    def save_tasks(self):
        with open(self.file_name, "w") as file:
            json.dump(self.tasks, file)
        print("Tasks saved successfully.")

    def load_tasks(self):
        if os.path.exists(self.file_name):
            with open(self.file_name, "r") as file:
                self.tasks = json.load(file)
            print("Tasks loaded successfully.")
        else:
            print("No saved tasks found.")
