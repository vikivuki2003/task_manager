from datetime import datetime
from typing import List, Dict, Any
from task import Task


class TaskManager:
    """Manages a list of tasks."""

    def __init__(self) -> None:
        """Initializes a task manager instance."""
        self.tasks: List[Task] = []  # List to store tasks
        self.next_id: int = 1  # Next available task ID

    def load_tasks(self, tasks: List[Dict]) -> None:
        """Loads tasks from a list and updates their IDs.
        Args:
            tasks (List[Dict]): A list of task data dictionaries.
        """
        for task_data in tasks:
            try:
                task = Task(**task_data)
                self.tasks.append(task)
                self.next_id = max(self.next_id, task.id + 1)
            except Exception as e:
                print(f"Error loading task: {e}")

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> None:
        """Adds a new task.
        Args:
            title (str): The title of the task.
            description (str): The description of the task.
            category (str): The category of the task.
            due_date (str): The due date of the task in YYYY-MM-DD format.
            priority (str): The priority of the task.
        Raises:
            ValueError: If title or priority is empty or if a task with the same title exists.
        """
        if not title or not priority:
            raise ValueError("Title and priority cannot be empty.")

            # Check for duplicates by title
        if any(task.title == title for task in self.tasks):
            raise ValueError("A task with the same title already exists.")

        task = Task(self.next_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.next_id += 1
        print('Task added successfully.')

    def view_tasks(self) -> List[Dict[str, Any]]:
        """Views all tasks.
        Returns:
            List[Dict]: A list of all tasks as dictionaries.
        """
        if not self.tasks:
            return 'No tasks found.'
        return [task.to_dict() for task in self.tasks]

    def edit_task(self, task_id: int) -> None:
        """Edits an existing task by its ID.
        Args:
            task_id (int): The ID of the task to edit.
        Raises:
            ValueError: If the task is not found.
        """
        task = next((task for task in self.tasks if task.id == task_id), None)
        if not task:
            raise ValueError("Task not found.")

        new_title = input("Enter new title (leave blank to keep current): ") or task.title
        new_description = input("Enter new description (leave blank to keep current): ") or task.description
        new_category = input("Enter new category (leave blank to keep current): ") or task.category

        new_due_date_input = input("Enter new due date (YYYY-MM-DD, leave blank to keep current): ")
        if new_due_date_input:
            try:
                new_due_date = datetime.strptime(new_due_date_input, '%Y-%m-%d').date()
            except ValueError:
                print("Invalid date format. Keeping current due date.")
                new_due_date = task.due_date
        else:
            new_due_date = task.due_date

        new_priority = input("Enter new priority (high / medium / low, leave blank to keep current): ") or task.priority
        new_status = input("Enter new status (completed / not completed, leave blank to keep current): ") or task.status

        task.title = new_title
        task.description = new_description
        task.category = new_category
        task.due_date = new_due_date
        task.priority = new_priority
        task.status = new_status

        print(f"Task '{task.title}' edited successfully.")

    def delete_task(self, task_id: int) -> None:
        """Deletes an existing task by its ID.
        Args:
            task_id (int): The ID of the task to delete.
        Raises:
            ValueError: If the task does not exist.
        """
        task = next((task for task in self.tasks if task.id == task_id), None)
        if not task:
            raise ValueError(f'Task with ID {task_id} does not exist. Please enter a valid ID.')

        self.tasks.remove(task)
        print('Task deleted!')

    def search_task(self, category: str) -> List[Task]:
        """Searches for tasks by category.
        Args:
            category (str): The category to search for.
        Returns:
            List[Task]: A list of tasks that match the category.
        """
        if not category:
            raise ValueError("Search category cannot be empty.")

        results = [task for task in self.tasks if category.lower() in task.category.lower()]
        if results:
            for task in results:
                print(task.to_dict())  # Print the details of each found task
        else:
            print('No tasks found.')
        return results

    def get_tasks(self) -> List[Dict[str, Any]]:
        """Returns a list of all tasks as dictionaries for JSON serialization.
        Returns:
            List[Dict]: A list of tasks represented as dictionaries.
        """
        return [task.to_dict() for task in self.tasks]

