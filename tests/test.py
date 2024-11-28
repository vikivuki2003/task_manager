import pytest
from datetime import datetime
from task_manager import TaskManager


@pytest.fixture
def task_manager():
    """Creates and returns a TaskManager instance pre-populated with test data."""
    manager = TaskManager()
    manager.add_task('Test Task', 'Description', 'Work', '2024-12-12', 'High')
    return manager

def test_add_task(task_manager):
    """Tests adding a new task and verifies its attributes."""
    initial_count = len(task_manager.tasks)
    task_manager.add_task('Test Task 2', 'New Description', 'Personal', '2024-12-08', 'Medium')
    new_task = task_manager.tasks[-1]  # Get the last added task
    assert len(task_manager.tasks) == initial_count + 1
    assert new_task.title == 'Test Task 2'
    assert new_task.description == 'New Description'
    assert new_task.category == 'Personal'
    assert new_task.due_date == datetime.strptime('2024-12-08', '%Y-%m-%d')
    assert new_task.priority == 'Medium'


def test_view_task(task_manager):
    """Tests viewing task and checks output."""
    task_manager.add_task('Test Task', 'Description', 'Work', '2024-12-12', 'High')

    output = task_manager.view_tasks()
    assert len(output) > 0

    first_task = output[0]
    assert first_task['title'] == 'Test Task'
    assert first_task['description'] == 'Description'
    assert first_task['category'] == 'Work'
    assert first_task['due_date'] == datetime.strptime('2024-12-12', '%Y-%m-%d')
    assert first_task['priority'] == 'High'

def test_edit_task(task_manager, monkeypatch):
    """Tests editing task."""
    task = task_manager.tasks[0]
    old_title = task.title

    monkeypatch.setattr('builtins.input', lambda prompt: "New Edited Title" if "title" in prompt else task.due_date.strftime('%Y-%m-%d'))

    task_manager.edit_task(task.id)

    assert task.title == "New Edited Title"
    assert task.due_date == datetime.strptime(task.due_date.strftime('%Y-%m-%d'), '%Y-%m-%d')


def test_delete_task(task_manager):
    """Tests deleting task and ensures the correct task is removed."""
    initial_count = len(task_manager.tasks)

    task_id_to_delete = task_manager.tasks[0].id
    task_manager.delete_task(task_id_to_delete)

    assert len(task_manager.tasks) == initial_count - 1
    assert all(task.id != task_id_to_delete for task in task_manager.tasks)

def test_search_task(task_manager):
    """Tests searching for a task and checks for correct results."""
    result = task_manager.search_task('Test')
    assert len(result) > 0
    assert all('Test' in task.title for task in result)

def test_edit_nonexistent_task(task_manager):
    """Tests editing a non-existent task gracefully."""
    with pytest.raises(ValueError):
        task_manager.edit_task(-1)

def test_add_task_with_empty_fields(task_manager):
    """Tests adding a task with missing fields."""
    initial_count = len(task_manager.tasks)
    with pytest.raises(ValueError):  # Assuming appropriate exception handling for invalid task creation
        task_manager.add_task('', 'Description', 'Work', '2024-12-12', '')  # Empty title and priority
    assert len(task_manager.tasks) == initial_count  # Count should remain the same