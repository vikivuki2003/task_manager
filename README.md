# *Task manager application*

# **Overview**
The Task Manager is a simple yet powerful application designed to help users manage their tasks efficiently. It allows users to create, update, delete, and track tasks with various attributes such as title, description, due date, priority, and status. This project is built using Python and Django, leveraging the Django Rest Framework for API development.

# **Features**
Task Management: Create, read, update, and delete tasks.
Attributes: Each task can have a title, description, due date, priority, and status.
API Integration: RESTful API for easy integration with other applications.
User Authentication: Secure user authentication to protect user data.

Technologies Used
Python: The primary programming language for the application.

Installation
To set up the Task Manager locally, follow these steps:

Clone the repository:
git clone https://github.com/vikivuki2003/task_manager.git

cd task_manager

Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:
pip install -r requirements.txt

Usage
Creating a Task: Send a POST request to /api/tasks/ with the task details.
Retrieving Tasks: Send a GET request to /api/tasks/ to retrieve all tasks.
Updating a Task: Send a PUT request to /api/tasks/{id}/ with the updated task details.
Deleting a Task: Send a DELETE request to /api/tasks/{id}/ to remove a task.
