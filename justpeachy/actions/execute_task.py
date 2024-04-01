"""
function that just calls the execute task function
creates & sends action to the history

def execute_task(task, creator, worker)
    additional_info = true
    while additional_info is true
        question = task + "does this task require additional info" (prompt)
        response = inner_thought(question)
        if response == "yes"
            creator_question = prompt(to generate follow up question for creator)
            new_info = send_message(creator, creator_question)
            task += " " + new_info
        else:
            additional_info = false
    task_queue = sub_tasks(task)
    final_output = process_tasks(task_queue)
    mark_task_complete(task, final_output)
    return "task has been completed"
    
                
def process_tasks(task_queue):
    while task_queue:
        sub_task = task_queue.pop(0)
        final_action = execute_sub_task(sub_task)
        is final_action == 'send_message':
            update_task_status(sub_task, final_action)
        else:
            task_queue.insert(0, sub_task)
            continue
    final_output = compile_final_output()
    return final_output

    
def sub_tasks(task):
    break down tasks into sub-tasks
    uses a small, fast, fine-tuned LLM to do this
    prompt: 
            main task: {{task}}
            Objective:
            Break down the above taks into detailed sub-tasks to ensure comprehensive coverage of all aspects necessary for completing the project.
            Each sub-task should represent a distinct, manageable component of the overall task.
    should be returned in a json object sub_tasks = task, description
    for task in sub_tasks, prioritize(task) ==> this enriches the sub-tasks w/ priority and dependencies
    all tasks get added to the queue_cache (an in-memory redis store)
    
def execute_sub_task(sub_task):
    action = parser_input(sub_task)
    shortTerm_prompt = queue_manager(action)
    final_prompt = memory(shortTerm_prompt, longTerm_prompt)
    final_Action = processor(final_prompt)
    return final_action
    
def update_task_status(sub-task, final_action):
    just gets the sub-task json object and changes the status to complete
    removes it from the queue
    final_action is stored in redis cache
    
def mark_task_complete(final_output):
    gets the original task from the cache
    updates it w/ status = complete 
    return success

def complile_final_output():
    gets all the task actions from the cache
    compliles them into one result using the worker
    returns final_output
"""