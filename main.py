import json
import os
import time
from datetime import datetime
from task_manager import TaskManager

def load_tasks_from_file(filename: str) -> list:
    """Loads tasks from a JSON file."""
    if os.path.exists(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error decoding JSON. Returning empty task list.")
            return []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            return []
    return []

def save_tasks_to_file(filename: str, tasks: list) -> None:
    """Saves tasks to a JSON file."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(tasks, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def get_valid_date(prompt: str) -> str:
    """Prompts user for a valid date."""
    while True:
        date_input = input(prompt)
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Invalid date format. Please enter YYYY-MM-DD.")

def get_valid_priority(prompt: str) -> str:
    """Prompts user for a valid priority."""
    while True:
        priority = input(prompt).lower()
        if priority in ['high', 'medium', 'low']:
            return priority
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")

def main() -> None:
    """Main function to run the task manager."""
    task_manager = TaskManager()
    task_manager.load_tasks(load_tasks_from_file('tasks.json'))

    while True:
        print("\nTask Manager")
        print("1. View all tasks")
        print("2. Add a task")
        print("3. Edit a task")
        print("4. Delete a task")
        print("5. Search tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            result = task_manager.view_tasks()
            if isinstance(result, str):
                print(result)
            else:
                for task in result:
                    print(task)
            time.sleep(2)

        elif choice == '2':
            title = input("Enter a title: ")
            description = input("Enter a description: ")
            category = input("Enter a category: ")
            due_date = get_valid_date("Enter a due date (YYYY-MM-DD): ")
            priority = get_valid_priority("Enter a priority (high / medium / low): ")

            task_manager.add_task(title, description, category, due_date, priority)
            save_tasks_to_file('tasks.json', task_manager.get_tasks())
            time.sleep(2)

        elif choice == '3':
            task_id = int(input("Enter task ID to edit: "))
            task_manager.edit_task(task_id)
            save_tasks_to_file('tasks.json', task_manager.get_tasks())
            time.sleep(2)

        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            confirm = input(f"Are you sure you want to delete task ID {task_id}? (yes/no): ").lower()
            if confirm == 'yes':
                task_manager.delete_task(task_id)
                save_tasks_to_file('tasks.json', task_manager.get_tasks())
                print("Task deleted successfully!")
            time.sleep(2)

        elif choice == '5':
            query = input("Enter a category to search: ")
            task_manager.search_task(query)
            time.sleep(2)

        elif choice == '6':
            confirm = input("Are you sure you want to exit? (yes/no): ").lower()
            if confirm == 'yes':
                save_tasks_to_file('tasks.json', task_manager.get_tasks())
                print("Tasks saved. Exiting...")
                break

        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()