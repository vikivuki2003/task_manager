import pytest
from datetime import datetime
from task_manager import TaskManager

@pytest.fixture
def task_manager() -> TaskManager:
    """Creates and returns a TaskManager instance pre-populated with test data."""
    manager = TaskManager()
    manager.add_task('Test Task', 'Description', 'Work', '2024-12-12', 'High')
    return manager

@pytest.fixture
def sample_task() -> dict:
    """Returns a sample task for testing."""
    return {
        'title': 'Sample Task',
        'description': 'Sample Description',
        'category': 'Personal',
        'due_date': '2024-12-15',
        'priority': 'Medium'
    }

def test_add_task(task_manager: TaskManager, sample_task: dict) -> None:
    """Tests adding a new task and verifies its attributes."""
    initial_count = len(task_manager.tasks)
    task_manager.add_task(**sample_task)
    new_task = task_manager.tasks[-1]  # Get the last added task
    assert len(task_manager.tasks) == initial_count + 1
    assert new_task.title == sample_task['title']
    assert new_task.description == sample_task['description']
    assert new_task.category == sample_task['category']
    assert new_task.due_date == datetime.strptime(sample_task['due_date'], '%Y-%m-%d')
    assert new_task.priority == sample_task['priority']

def test_view_task(task_manager: TaskManager) -> None:
    """Tests viewing tasks and checks output."""
    output = task_manager.view_tasks()
    assert len(output) > 0

    first_task = output[0]
    assert first_task['title'] == 'Test Task'
    assert first_task['description'] == 'Description'
    assert first_task['category'] == 'Work'
    assert first_task['due_date'] == datetime.strptime('2024-12-12', '%Y-%m-%d')
    assert first_task['priority'] == 'High'

def test_edit_task(task_manager: TaskManager, monkeypatch) -> None:
    """Tests editing an existing task."""
    task = task_manager.tasks[0]
    # Mocking user input for editing the task
    monkeypatch.setattr('builtins.input', lambda prompt: "New Edited Title" if "title" in prompt else task.due_date.strftime('%Y-%m-%d'))

    task_manager.edit_task(task.id)

    # Verifying that the task's title has been updated
    assert task.title == "New Edited Title"
    assert task.due_date == datetime.strptime(task.due_date.strftime('%Y-%m-%d'), '%Y-%m-%d')

def test_delete_task(task_manager: TaskManager) -> None:
    """Tests deleting a task and ensures the correct task is removed."""
    initial_count = len(task_manager.tasks)
    task_id_to_delete = task_manager.tasks[0].id
    task_manager.delete_task(task_id_to_delete)

    # Verifying the task count and ensuring the deleted task is no longer present
    assert len(task_manager.tasks) == initial_count - 1
    assert all(task.id != task_id_to_delete for task in task_manager.tasks)

def test_search_task(task_manager: TaskManager) -> None:
    """Tests searching for a task and checks for correct results."""
    result = task_manager.search_task('Test')
    assert len(result) > 0
    assert all('Test' in task.title for task in result)

def test_edit_nonexistent_task(task_manager: TaskManager) -> None:
    """Tests editing a non-existent task gracefully."""
    with pytest.raises(ValueError):
        task_manager.edit_task(-1)  # Attempt to edit a task with an invalid ID

def test_add_task_with_empty_fields(task_manager: TaskManager) -> None:
    """Tests adding a task with missing fields."""
    initial_count = len(task_manager.tasks)
    with pytest.raises(ValueError):
        task_manager.add_task('', 'Description', 'Work', '2024-12-12', '')  # Empty title and priority