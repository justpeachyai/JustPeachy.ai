"""
Recall Storage Class:
- The complete event history, this includes all of the actions that the worker has ever taken, for all conversations not just the one that the worker is currently in
- READ only via functions
- Can be written to via the queue manager
- Is a SQL database w/ datetime stamps

Functions:
- initalize database
- queries w/ filters by action, action role, or datetime
- write to database
"""