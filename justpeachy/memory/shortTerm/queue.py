'''
This is the environment in which the worker (or workers) are observing. This can include the following actions: 
- Message: a simple text based message
- Function: a function call
- Tool: a tool use
- Skill: a skill use
- Thought: an internal thought by the ai worker

These actions can be completed by the following roles:
- system: neither human or ai
- user: human
- worker: ai

These actions are parsed into action objects and are added in a FIFO queue
The queue manager is in charge of writing these action to the queue object whihc is utilized by the core memory
the queue manager has an eviction policy (recursive summarization) and adding evicted actions to the {{longTerm.recallStorage}}

Control Flow Class w/ Eviction Policy:
- Defines the max space of the core memory (i.e. the max number of tokens)
- defines the eviction process (i.e. core memory must be kept under 85% utilization)
- Defines the summarization process, which is controlled by a small, fast ai agent

-> (prompt will need editing and testing, use the enviroment not conversation) Your job is to summarize a history of previous messages in a conversation between an AI persona and a human.
The conversation you are given is a from a fixed context window and may not be complete.
Messages sent by the AI are marked with the 'assistant' role.
The AI 'assistant' can also make calls to functions, whose outputs can be seen in messages with the 'function' role.
Things the AI says in the message content are considered inner monologue and are not seen by the user.
The only AI messages seen by the user are from when the AI uses 'send_message'.
Messages the user sends are in the 'user' role.
The 'user' role is also used for important system events, such as login events and heartbeat events (heartbeats run the AI's program without user action, allowing the AI to act without prompting from the user sending them a message).
Summarize what happened in the conversation from the perspective of the AI (use the first person).
Keep your summary less than {WORD_LIMIT} words, do NOT exceed this word limit.
Only output the summary, do NOT include anything else in your output.
'''