"""
Task class includes the following attributes:
- ID: UUID
- workerID: id of the worker in which the task is assigned to
- completed_at: time the task was completed
- status: ENUM (IN_PROGRESS, COMPLETED, FAILED, PENDING, REVIEW)
- recurring: boolean to describe if and when the task recurs
- scheduled: datetime of scheduled task
- description: short description of the task
- actions: [] list of all actions taken for the task
- created_at: datetime
- updated_at: datetime

task.execute(max_iterations, approval, creator):
    max_iterations: signifies how many times or how long a task can repeat the loop before failure
    approval: BOOLEAN, TRUE by default, if FALSE then status automatically updated to COMPLETED
    
    task gets sent to actions/execute_task execute_task(task.self, creator)
    return task has been started, please check for updates in the task manager
    (task info gets sent to the message broker)

"""