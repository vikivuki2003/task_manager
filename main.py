import json
import os
import time
from datetime import datetime

from task_manager import TaskManager


def load_tasks_from_file(filename):
    """Loads tasks from a json file"""
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []

def save_tasks_to_file(filename, tasks):
    """Saves tasks to a json file"""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(tasks, file, ensure_ascii=False, indent=4)

def main():
    task_manager = TaskManager()
    task_manager.load_task(load_tasks_from_file('tasks.json'))

    while True:  # Loop for the menu options
        print("\nTask Manager")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Edit a task")
        print("4. Delete a task")
        print("5. Search tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_manager.view_tasks()

        if choice == '2':
            title = input("Enter a title: ")
            description = input("Enter a description: ")
            category = input("Enter a category: ")

            while True:
                due_date = input("Enter a due date (YYYY-MM-DD): ")
                try:
                    datetime.strptime(due_date, "%Y-%m-%d")
                    break  # выход из цикла, если дата корректная
                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

            priority = input("Enter a priority: ")

            task_manager.add_task(title, description, category, due_date, priority)
            time.sleep(2)

        elif choice == '3':
            task_id = int(input("Enter task ID to edit: "))
            task_manager.edit_task(task_id)
            time.sleep(2)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            task_manager.delete_task(task_id)
            time.sleep(2)

        elif choice == '5':
            query = input("Enter a keyword to search: ")
            task_manager.search_task(query)

        elif choice == '6':
            save_tasks_to_file('tasks.json', task_manager.get_tasks())
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()



