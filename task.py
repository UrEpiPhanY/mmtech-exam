from datetime import datetime

class Task:
    def __init__(self, task_id, title, description, due_date, 
                 priority_level='Low', status='Pending', created_at=None):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date  # Should be a datetime.date object
        self.priority_level = priority_level  # 'Low', 'Medium', 'High'
        self.status = status  # 'Pending', 'In Progress', 'Completed'
        self.created_at = created_at or datetime.now()

    def __str__(self):
        return f"[{self.task_id}] {self.title} ({self.status}) - " \
               f"Due: {self.due_date}, Priority: {self.priority_level}"
