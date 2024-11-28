from datetime import datetime

class Task:
    """Represents a task.
        Attributes:
            id (int): A unique identifier for the task.
            title (str): The title of the task.
            description (str): The description of the task.
            category (str): The category of the task.
            due_date (datetime): The due date of the task.
            priority (str): The priority level of the task.
            status (str): The status of the task (completed/not completed).
        """

    def __init__(self, id, title, description, category, due_date, priority, status="Не выполнена"):
        """Initializes a new instance of the Task class."""
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = datetime.strptime(due_date, '%Y-%m-%d')
        self.priority = priority
        self.status = status

    def __str__(self):
        """Returns a string representation of the task."""
        return (f'{self.id} / {self.title} / {self.description} / '
                f'{self.category} / {self.due_date} / {self.priority} / {self.status}')

    def mark_as_done(self):
        """Marks the task as completed."""
        self.status = 'Выполнена'

    def to_dict(self):
        """Converts the task to a dictionary for JSON serialization.
        Returns: A dictionary representation of the task.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'due_date': self.due_date,
            'priority': self.priority,
            'status': self.status
        }