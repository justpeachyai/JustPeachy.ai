"""
Parser function takes any input by a human or output by a worker 
and transforms it into an action (models.action) JSON object

{
    action: user_message
    role: talisha
    content: "I really like the way @becky did the color gradient on this hero image"
    datetime: timestamp
}
{
    action: worker_message
    role: UI Designer
    content: "The updated graphic has been emailed to @talisha. Would you like a copy of it as well? "
    datetime: timestamp
}

- Are generated from human inputs
- Are generated from worker outputs via the LLM processor
- ALL actions are added to worker history

def parser(input)
    returns json
    to be used in the memory prompt chain
"""
import json
from datetime import datetime
from models.action import ActionType, Action

def parse_input(action_type, role, content, conversation_id=None, environment_id=None):
    """
    Parses input from a human or worker output into an Action JSON object.

    Parameters:
        action_type (ActionType): The type of action (e.g., USER_MESSAGE, WORKER_MESSAGE).
        role (str): The role of the person or worker initiating the action.
        content (str): The content of the message.
        conversation_id (str, optional): The ID of the conversation this action belongs to.
        environment_id (str, optional): The environment ID where this action takes place.

    Returns:
        str: A JSON string representing the action.
    """
    # Create an Action instance
    action = Action(
        type=action_type,
        role=role,
        content=content,
        conversation_id=conversation_id,
        environment_id=environment_id
    )
    
    # Convert the Action instance to a dictionary, omitting the _id for simplicity
    action_dict = {
        "action": action.type.name,
        "role": action.role,
        "content": action.content,
        "datetime": action.created_at.isoformat(),
        "conversation_id": action.conversation_id,
        "environment_id": action.environment_id,
        "feedback": action.feedback
    }
    
    # Convert the dictionary to a JSON string
    return json.dumps(action_dict, ensure_ascii=False)