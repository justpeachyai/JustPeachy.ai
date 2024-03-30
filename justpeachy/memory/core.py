'''
Core Memory function that takes in all of the memory information and combines it into a singular prompt

{{prompts.mem_base}} (the base prompt used to describe how memory works and how the worker should use it)
{{shortTerm.SystemContext}} (the core memory of the worker's persona and the person with whom they are speaking)
{{Memory Functions}} (all of the functions in which the worker has access to in order to adjust their memory)
{{queue.control Flow}} (how the memory is handled, defined in the queue)
{{tools}} (tools in which the worker has access to)
{{skills}} (skills the worker has access to)
{{shortTerm.queue}} (FIFO Queue of the current conversation)
{{shortTerm.WorkingContext}} (memory scratchpad, where info from long term memory goes)

- function that counts the tokens and updates the system messages
'''