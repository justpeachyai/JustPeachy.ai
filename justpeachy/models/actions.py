"""
Action Class
- _id: UUID
- type: ENUM (user_message, system_message, worker_message, function, tool, skill, thought)
- role: role of the action
- content: content of the action
- created_at: datetime timestamp
- conversation_id: conversation which the action belongs to, if any
- environment_id: environment which the action belongs to
- feedback: feedback on the action

Actions get added to a worker history, and environment
"""
import uuid
from datetime import datetime
from enum import Enum, auto

class ActionType(Enum):
    USER_MESSAGE = auto()
    SYSTEM_MESSAGE = auto()
    WORKER_MESSAGE = auto()
    FUNCTION = auto()
    TOOL = auto()
    SKILL = auto()
    THOUGHT = auto()

class Action:
    def __init__(self, type, role, content, conversation_id=None, environment_id=None, feedback=None):
        self._id = uuid.uuid4()
        self.type = type
        self.role = role
        self.content = content
        self.created_at = datetime.now()
        self.conversation_id = conversation_id
        self.environment_id = environment_id
        self.feedback = feedback
