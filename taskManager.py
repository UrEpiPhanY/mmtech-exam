from task import Task
from taskMethods import create_task, get_all_tasks, update_task, delete_task, get_task, update_progress
import datetime

#region Task Manager Startup
def show_menu():
    print("\n=== Task Manager CLI ===")
    print("1. Create Task")
    print("2. View All Tasks")
    print("3. View Task by ID")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Update Task Progress")
    print("7. Exit")
#endregion

#region Input Helpers
def get_input(label, required=True, validator=None):
    """Prompt input with cancel and validation."""
    value = input(f"{label}: ").strip()
    if not value:
        if required:
            print("\nOperation cancelled.")
        return None
    if validator:
        try:
            return validator(value)
        except Exception as e:
            print(f"Invalid {label.lower()}: {e}")
            return None
    return value

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

def validate_status(status):
    options = ["Pending", "In Progress", "Completed"]
    if status not in options:
        raise ValueError("Choose from: " + ", ".join(options))
    return status

def validate_priority(priority):
    options = ["Low", "Medium", "High"]
    if priority not in options:
        raise ValueError("Choose from: " + ", ".join(options))
    return priority
#endregion

#region Core CLI Functions
def create_task_cli():
    print("\nLeave any field blank to cancel task creation.")
    title = get_input("\nTitle")
    if title is None: return

    description = get_input("Description")
    if description is None: return

    due_date = get_input("Due Date (YYYY-MM-DD)", validator=parse_date)
    if due_date is None: return

    priority = get_input("Priority (Low/Medium/High)", validator=validate_priority)
    if priority is None: return

    status = get_input("Status (Pending/In Progress/Completed)", validator=validate_status)
    if status is None: return

    task = Task(
        task_id=None,
        title=title,
        description=description,
        due_date=due_date,
        priority_level=priority,
        status=status
    )

    print("\nPreview Task:")
    print(task)

    confirm = input("\nConfirm creation? (y/n): ").strip().lower()
    if confirm == 'y':
        create_task(task)
        print("Task created successfully!")
    else:
        print("Task creation cancelled.")

def view_all_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return

    sort_order = input("Sort by (1) Newest first or (2) Oldest first? [1/2]: ").strip()

    try:
        tasks.sort(key=lambda task: task.created_at, reverse=(sort_order == '1'))
    except AttributeError:
        print("Warning: Some tasks are missing 'created_at' field. Showing unsorted.")
    
    for task in tasks:
        print(task)

def view_task_by_id():
    task_id = get_input("\nEnter Task ID", validator=int)
    if task_id is None: return

    task = get_task(task_id)
    if task:
        print(task)
    else:
        print("\nTask not found.")

def update_task_cli():
    task_id = get_input("\nTask ID to update", validator=int)
    if task_id is None: return

    task = get_task(task_id)
    if not task:
        print("\nTask not found.")
        return

    print("\nLeave all fields blank to cancel the update.")

    title = input("\nNew Title: ").strip()
    description = input("New Description: ").strip()
    due_date_raw = input("New Due Date (YYYY-MM-DD): ").strip()
    priority = input("New Priority (Low/Medium/High): ").strip()
    status = input("New Status (Pending/In Progress/Completed): ").strip()

    if not any([title, description, due_date_raw, priority, status]):
        print("\nUpdate cancelled.")
        return

    updates = {}
    if title:
        updates['title'] = title
    if description:
        updates['description'] = description
    if due_date_raw:
        try:
            updates['due_date'] = parse_date(due_date_raw)
        except ValueError:
            print("\nInvalid date format.")
            return
    if priority:
        try:
            updates['priority_level'] = validate_priority(priority)
        except ValueError as e:
            print(e)
            return
    if status:
        try:
            updates['status'] = validate_status(status)
        except ValueError as e:
            print(e)
            return

    update_task(task_id, **updates)
    print("Task updated.")

def delete_task_cli():
    task_id = get_input("\nTask ID to delete", validator=int)
    if task_id is None: return

    delete_task(task_id)
    print("\nTask deleted.")

def update_task_progress_cli():
    task_id = get_input("\nEnter Task ID", validator=int)
    if task_id is None: return

    task = get_task(task_id)
    if not task:
        print("\nTask not found.")
        return

    print(f"Current status: {task.status}")
    status = get_input("\nNew Status (In Progress / Completed)", validator=validate_status)
    if status is None: return

    update_progress(task_id, status)
    print("\nTask progress updated.")
#endregion

#region Main Loop
def main():
    while True:
        show_menu()
        choice = input("\nChoose an option (1-7): ").strip()

        if choice == '1':
            create_task_cli()
        elif choice == '2':
            view_all_tasks()
        elif choice == '3':
            view_task_by_id()
        elif choice == '4':
            update_task_cli()
        elif choice == '5':
            delete_task_cli()
        elif choice == '6':
            update_task_progress_cli()
        elif choice == '7':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Try again.")
#endregion

if __name__ == "__main__":
    main()
