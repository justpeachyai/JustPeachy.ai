"""
def execute_task(task):
    1. New task queue is intialized in the cache
    2. sub-task module (small, fast, fine-tuned LLM) breaks down the task into sub-tasks
    3. sub-task module prioiritizes tasks and add to the queue (cache)
    4. worker checks if the queue is empty
        - YES: compile final output & mark final task as complete
        - NO: loops each subtask through the primary worker module
    5. Benchmark: 
        - How many loops did it take to complete the sub-task?
        - Was the task approved or did it have to be executed again?
        - 
"""