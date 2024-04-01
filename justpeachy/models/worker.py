"""
Worker Class includes the following attributes:
- id: UUID of the worker
- name: Name of the worker, i.e. John Smith
- role: The role of the worker, i.e. UX Designer
- Goal: the objective of the worker, its job functions
- Backstory: additional details about the worker, its resume or the job description
- Tools: a list of tools which the worker has access to
- skills: a list of skills which the user has access too
- version: the version of the worker
- model: the current LLM being used by the worker
- memory: initialization, the short term and long term memory locations for the worker
- team: list of teams the worker is part of
- state: current state of the worker, ENUM: IDLE, ACTIVE, ON_BREAK, INACTIVE, PENDING
- current_env: the ip address or other indicator of the environment/sandbox that the worker is active in, can be list
- environments: [] list of all associated message environments
- history: all actions ever taken by the worker
- tasks: current tasks assigned to the worker
- knowledge: initialization, the knowledge index name for the worker
- conversation: [] a list of conversations the worker has engaged in
- activeHours: the total number of hours the worker has worked
- tokensUtilized: total number of tokens used by the worker
- email: worker's personal email
- phoneNumber: worker's personal phone number
- VirtualIDCard: worker's virtual identification card
- personality: key attributes of the worker's personality
- voice: worker voice file
- profile: profile image for worker

functions:
- function to automatically update version on object change
- function to add tool, skill, or other


worker.hire(): initializes the worker, creating the worker config file and saving to cache and storage
    -creates a canopy knowledge base
    
    
worker.chat(worker, env, convo, msg): chat with the worker directly 
    worker: worker id
    env: enviornment id
    convo: convo id
    msg: message
    from parser parser(msg)



"""
import uuid
from enum import Enum, auto
from utils.redis_utils import RedisUtil
from utils.memory_utils import Memory

class WorkerState(Enum):
    IDLE = auto()
    ACTIVE = auto()
    ON_BREAK = auto()
    INACTIVE = auto()
    PENDING = auto()

class Worker:
    def __init__(self, name, role, goal, backstory, tools, skills, email, phoneNumber, virtualIDCard, personality, voice, profile):
        self.id = uuid.uuid4()
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.tools = tools
        self.skills = skills
        self.version = "00.00.00"
        self.model = None 
        self.memory = Memory(self.id)
        self.team = []
        self.state = WorkerState.IDLE
        self.current_env = None
        self.environments = []
        self.history = []
        self.tasks = []
        self.knowledge = {
            "canopy_index": f"{self.worker_id}",
        }
        self.conversation = []
        self.activeHours = 0
        self.tokensUtilized = 0
        self.email = email
        self.phoneNumber = phoneNumber
        self.VirtualIDCard = virtualIDCard
        self.personality = personality
        self.voice = voice
        self.profile = profile
        self.redis_util = RedisUtil()

    def update_version(self):
        major, minor, patch = map(int, self.version.split("."))
        patch += 1
        if patch == 100:
            patch = 0
            minor += 1
        if minor == 10:
            minor = 0
            major += 1
        self.version = f"{major:02}.{minor:02}.{patch:02}"

    def add_tool(self, tool):
        if tool not in self.tools:
            self.tools.append(tool)

    def add_skill(self, skill):
        if skill not in self.skills:
            self.skills.append(skill)

    def hire(self):
        # Step 1: Update version to indicate a new hire or a significant update
        self.update_version()
        
        # Step 2: Finalize any setup for memory if needed
        # This example assumes Memory class handles its own setup during initialization
        # Any additional setup or validation can be performed here
        
        # Step 3: Save worker information to Redis cache
        self.redis_util.hset(f"worker:{self.id}", mapping={
            "id": str(self.id),
            "name": self.name,
            "role": self.role,
            "goal": self.goal,
            "backstory": self.backstory,
            "tools": ",".join(self.tools),
            "skills": ",".join(self.skills),
            "version": self.version,
            # For complex attributes like 'memory', you may need a serialization strategy
            "state": self.state.name,
            "email": self.email,
            "phoneNumber": self.phoneNumber,
            "personality": self.personality,
            # Additional fields as needed
        })

        print(f"Worker {self.name} hired and initialized. Version: {self.version}")

    def chat(self, worker_id, env_id, convo_id, msg):
        # get worker name, role from worker_id to determine action type and role
        # pass to parser.py action = parser_input(user_message, talisha, content, convo_id, env_id)
        # pass action to memory/shortTerm/queue shortTerm_prompt = queue_manager(action)
        # pass prompt to memory/core.py final_prompt = memory(shortTerm_prompt, longTerm_prompt)
        # pass final memory to decisions/processor.py final_action = processor(final_prompt)
        # if final_action != worker_message, send action back to memory in loop until true
        # return final_action (which will always be a worker_message)
        pass
