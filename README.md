# *Task manager application*

# **Overview**

The Task Manager is a simple yet powerful application designed to help users manage their tasks efficiently. It allows users to create, update, delete, and track tasks with various attributes such as title, description, category, due date, priority, and status. This project is built using Python.

# **Features**

- Task Management: Create, read, update, and delete tasks.
- Attributes: Each task can have a title, description, category, due date, priority, and status.
- Search Functionality: Search tasks by category.
- Data Persistence: Tasks are saved to and loaded from a JSON file.

Technologies Used

Python: The primary programming language for the application.

Installation

To set up the Task Manager locally, follow these steps:

Clone the repository:

git clone https://github.com/vikivuki2003/task_manager.git
cd task_manager

**Set up a virtual environment:**
python -m venv venv

**Install dependencies:**

pip install -r requirements.txt

**Run the application:**

python main.py

**Follow the on-screen prompts to manage your tasks:**

View all tasks: Displays all tasks in the system.
Add a task: Prompts for task details and adds a new task.
Edit a task: Prompts for the task ID and allows editing of task details.
Delete a task: Prompts for the task ID and deletes the specified task.
Search tasks: Prompts for a category and displays tasks that match the category.
Exit: Saves tasks to a JSON file and exits the application.


**Data Storage**

Tasks are stored in a JSON file named tasks.json. The application will automatically load tasks from this file on startup and save any changes when exiting.

**Error Handling**

The application includes basic error handling for invalid inputs, such as:
Invalid date formats.
Invalid priority values.
Attempting to edit or delete non-existent tasks.


**Contributing**
Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
