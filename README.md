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
Django: The web framework used for building the application.
Django Rest Framework: For creating RESTful APIs.
PostgreSQL: The database used for storing task data.
Docker: For containerization and easy deployment.
Installation
To set up the Task Manager locally, follow these steps:

Clone the repository:

bash

Verify

Open In Editor
Edit
Copy code
git clone https://github.com/vikivuki2003/task_manager.git
cd task_manager
Set up a virtual environment:

bash

Verify

Open In Editor
Edit
Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install dependencies:

bash

Verify

Open In Editor
Edit
Copy code
pip install -r requirements.txt
Set up the database:

Make sure PostgreSQL is installed and running.
Create a new database for the application.
Update the database settings in settings.py.
Run migrations:

bash

Verify

Open In Editor
Edit
Copy code
python manage.py migrate
Run the development server:

bash

Verify

Open In Editor
Edit
Copy code
python manage.py runserver
Access the application: Open your web browser and go to http://127.0.0.1:8000/.

Usage
Creating a Task: Send a POST request to /api/tasks/ with the task details.
Retrieving Tasks: Send a GET request to /api/tasks/ to retrieve all tasks.
Updating a Task: Send a PUT request to /api/tasks/{id}/ with the updated task details.
Deleting a Task: Send a DELETE request to /api/tasks/{id}/ to remove a task.
