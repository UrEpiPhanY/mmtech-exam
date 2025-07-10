from taskSql import get_connection
from task import Task
from mysql.connector import Error

def create_task(task: Task):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO tasks (title, description, due_date, priority_level, status, created_at)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = (
            task.title,
            task.description,
            task.due_date,
            task.priority_level,
            task.status,
            task.created_at,
        )
        cursor.execute(sql, values)
        conn.commit()
    except Error as e:
        print(f"Error creating task: {e}")
    finally:
        cursor.close()
        conn.close()

def get_task(task_id: int) -> Task:
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks WHERE task_id = %s", (task_id,))
        row = cursor.fetchone()
        return Task(**row) if row else None
    except Error as e:
        print(f"Error fetching task: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

def get_all_tasks() -> list:
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM tasks")
        rows = cursor.fetchall()
        return [Task(**row) for row in rows]
    except Error as e:
        print(f"rror fetching tasks: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def update_task(task_id: int, **kwargs):
    try:
        allowed_fields = ['title', 'description', 'due_date', 'priority_level', 'status']
        updates = []
        values = []

        for key, value in kwargs.items():
            if key in allowed_fields:
                updates.append(f"{key} = %s")
                values.append(value)

        if not updates:
            print("No valid fields to update.")
            return

        values.append(task_id)
        sql = f"UPDATE tasks SET {', '.join(updates)} WHERE task_id = %s"

        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
    except Error as e:
        print(f"Error updating task: {e}")
    finally:
        cursor.close()
        conn.close()

def delete_task(task_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE task_id = %s", (task_id,))
        conn.commit()
    except Error as e:
        print(f"Error deleting task: {e}")
    finally:
        cursor.close()
        conn.close()

def update_progress(task_id: int, status: str):
    allowed = ["In Progress", "Completed"]
    if status not in allowed:
        print("Status not allowed.")
        return
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE tasks SET status = %s WHERE task_id = %s",
            (status, task_id)
        )
        conn.commit()
    except Exception as e:
        print(f"Error updating task progress: {e}")
    finally:
        cursor.close()
        conn.close()
