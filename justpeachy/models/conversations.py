"""
Class for conversations
- _id: UUID
- members: [] who is part of the conversation, both human and ai
- actions: [] list of action_ids for the conversation
- topic: topic of the conversation
"""
import uuid

class Conversation:
    def __init__(self, topic, members=None):
        self._id = uuid.uuid4()
        self.members = members if members is not None else []
        self.actions = []
        self.topic = topic

    def add_member(self, member_id):
        """Add a member to the conversation."""
        if member_id not in self.members:
            self.members.append(member_id)

    def remove_member(self, member_id):
        """Remove a member from the conversation."""
        self.members = [member for member in self.members if member != member_id]

    def log_action(self, action_id):
        """Log an action taken in the conversation by adding its ID."""
        self.actions.append(action_id)

    def set_topic(self, topic):
        """Set or update the topic of the conversation."""
        self.topic = topic

    def get_info(self):
        """Return a summary of the conversation information."""
        return {
            "id": str(self._id),
            "members": self.members,
            "actions": self.actions,
            "topic": self.topic
        }
