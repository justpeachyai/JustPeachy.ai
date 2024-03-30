"""
Project Class:
- _id: UUID
- name: name of project
- description: description of the project
- tasks: [] list of all the task ids associated with the project
- team_id: team id assigned to the project
- created_at: datetime
- status: ENUM (IN_PROGRESS, COMPLETED, FAILED, PENDING, REVIEW)
- progress: percentage of progress made on the project
- deadline: datetime in which the project needs to be completed
- estimate: estimated time until project completition by function

* function to determine the progress of the project by completed tasks/all tasks

"""
import uuid
from datetime import datetime
from enum import Enum, auto

class ProjectStatus(Enum):
    IN_PROGRESS = auto()
    COMPLETED = auto()
    FAILED = auto()
    PENDING = auto()
    REVIEW = auto()

class Project:
    def __init__(self, name, description, team_id, deadline, estimate):
        self._id = uuid.uuid4()
        self.name = name
        self.description = description
        self.tasks = []  # List of task IDs
        self.team_id = team_id
        self.created_at = datetime.now()
        self.status = ProjectStatus.PENDING
        self.progress = 0  # Initial progress is 0%
        self.deadline = deadline
        self.estimate = estimate

    def add_task(self, task_id):
        """Add a task to the project."""
        if task_id not in self.tasks:
            self.tasks.append(task_id)

    def remove_task(self, task_id):
        """Remove a task from the project."""
        self.tasks = [task for task in self.tasks if task != task_id]

    def update_status(self, new_status):
        """Update the project status."""
        if isinstance(new_status, ProjectStatus):
            self.status = new_status

    def calculate_progress(self, completed_tasks):
        """Calculate the progress of the project based on completed tasks."""
        if self.tasks:
            self.progress = (len(completed_tasks) / len(self.tasks)) * 100
        else:
            self.progress = 0
        return self.progress

    def get_info(self):
        """Return a summary of the project information."""
        return {
            "id": str(self._id),
            "name": self.name,
            "description": self.description,
            "team_id": self.team_id,
            "created_at": self.created_at,
            "status": self.status.name,
            "progress": self.progress,
            "deadline": self.deadline,
            "estimate": self.estimate
        }
