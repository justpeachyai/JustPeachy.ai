"""
Semantic Router to determine first pass actions

Available Actions to take:
- send_message(user, environment): user can be human or AI
- inner_thought(message): internal monologue 
- tool_use(tool): use a tool 
- skill_use(skill): utilize a skill
- create_task(task): create a new task to be completed later
- execute_task(task): executes a task
- archivalMemoryInsert - insert memories into archival database
- archivalMemorySearch - search memories in archival database
- ConversationSearch - search conversations in SQL database
- externalKnowledge - look up addiitonal information from Canopy (knowledge Database)

Each is pre-trained and has a benchmark for the router itself (one for training, one for real world)
"""