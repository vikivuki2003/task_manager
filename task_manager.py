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


