from datetime import datetime

from task import Task

class TaskManager:
    """Manages a list of tasks."""

    def __init__(self):
        """Initializes a task manager instance."""
        self.tasks = []
        self.next_id = 1

    def load_task(self, tasks):
        """Loads tasks from a list and updates their IDs."""
        for task_data in tasks:
            task = Task(**task_data)
            self.tasks.append(task)
            self.next_id = max(self.next_id, task.id + 1)

    def add_task(self, title, description, category, due_date, priority):
        """Adds a new task."""

        due_date = datetime.strptime(due_date, "%Y-%m-%d")
        if not title or not priority:
            raise ValueError("Title and priority cannot be empty.")
        task = Task(self.next_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.next_id += 1
        print('Task added successfully.')

    def view_tasks(self):
        if not self.tasks:
            return 'No tasks found.'
        task_list = [vars(task) for task in self.tasks]
        return task_list

    def edit_task(self, task_id):
        """Edits an existing task by its ID."""
        task = next((task for task in self.tasks if task.id == task_id), None)
        if not task:
            raise ValueError("Task not found.")

        new_title = input("Enter new title (leave blank to keep current): ") or task.title
        new_description = input("Enter new description (leave blank to keep current): ") or task.description
        new_category = input("Enter new category (leave blank to keep current): ") or task.category
        new_due_date = input(
            "Enter new due date (YYYY-MM-DD, leave blank to keep current): ") or task.due_date.strftime('%Y-%m-%d')
        new_priority = input("Enter new priority (leave blank to keep current): ") or task.priority

        task.title = new_title
        task.description = new_description
        task.category = new_category
        task.due_date = datetime.strptime(new_due_date, '%Y-%m-%d')  # Преобразуем строку в datetime
        task.priority = new_priority

        print(f"Task '{task.title}' edited successfully.")

    def delete_task(self, task_id):
        """Deletes an existing task by its ID."""

        if not any(task.id == task_id for task in self.tasks):
            raise ValueError(f'Task with ID {task_id} does not exist. Please enter a valid ID.')

        self.tasks = [task for task in self.tasks if task.id != task_id]
        print('Task deleted!')

    def search_task(self, query):
        """Searches for tasks by a keyword.
        Args: query (str): The keyword to search for in task titles, descriptions, or categories.
        """
        results = [task for task in self.tasks if query.lower() in task.title.lower()
                   or query.lower() in task.description.lower()
                   or query.lower() in task.category.lower()]

        if results:
            for task in results:
                print(vars(task))
        else:
            print('No tasks found.')

        return results

    def get_tasks(self):
        """Returns a list of all tasks as dictionaries for JSON serialization.
        Returns:  list: A list of tasks represented as dictionaries."""
        return [task.to_dict() for task in self.tasks]



