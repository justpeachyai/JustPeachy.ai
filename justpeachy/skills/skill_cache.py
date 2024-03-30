"""
The skill cache is a redis store of skills currently being used by the worker
This way the worker only has to ping the registry for the first time
"""