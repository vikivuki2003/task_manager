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
        task = Task(self.next_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        self.next_id += 1
        print('Task added successfully.')

    def view_tasks(self):
        if not self.tasks:
            print('No tasks found.')
            return
        for task in self.tasks:
            print(vars(task))

    def edit_task(self, task_id):
        """Edits an existing task by its ID."""
        task = next((task for task in self.tasks if task.id == task_id), None)
        if task:
            print('Editing task:', task.title)
            task.title = input("Enter new task title (leave empty for no changes): ") or task.title
            task.description = input("Enter new task description (leave empty for no changes): ") or task.description
            task.category = input("Enter new category (leave empty for no changes): ") or task.category
            new_due_date = input("Enter new due date (YYYY-MM-DD, leave empty for no changes): ")
            if new_due_date:  # If a new due date is entered
                task.due_date = datetime.strptime(new_due_date, '%Y-%m-%d')
            task.priority = input(
                "Enter new priority (low, medium, high, leave empty for no changes): ") or task.priority
            print("Task updated!")
        else:
            print("Task not found.")

    def delete_task(self, task_id):
        """Deletes an existing task by its ID."""
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

    def get_tasks(self):
        """Returns a list of all tasks as dictionaries for JSON serialization.
        Returns:  list: A list of tasks represented as dictionaries."""
        return [task.to_dict() for task in self.tasks]



