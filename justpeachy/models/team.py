"""
Team Class
- _id: UUID
- members: [] list of workerIDs
- name: name of team (i.e. software development team)
- backstory: description of the team
- goal: overall goal of the team
- enviornment: primary location of the team (i.e discord, default, video, etc)
- SOP: standard operating procedures for team to follow
- projects: [] list of projects assigned to team


team = {
    id:
    members: []
    project_description:
    sop:
}

team.kickoff():
    initializes the team
    creates team default/main environment (where msgs and actions are published)
    decides SOP

team.chat(env, project, msg):
    post a message to project env for all workers to see
    
def standard_operating_procedure():
    return nodes
"""
import uuid

class Team:
    def __init__(self, name, backstory, goal, environment, SOP):
        self._id = uuid.uuid4()
        self.members = []  # List of Worker IDs
        self.name = name
        self.backstory = backstory
        self.goal = goal
        self.environment = environment  # Primary location of the team
        self.SOP = SOP  # Standard Operating Procedures
        self.projects = []  # List of Project IDs

    def kickoff(self):
        """Initializes the team and sets up the default/main environment."""
        # Implementation of environment setup (e.g., creating a Discord server, setting up channels)
        # Implementation of SOP decision process
        # This is a placeholder for actual logic to create environment and decide SOP
        print(f"Team {self.name} initialized with environment {self.environment}.")

    def add_member(self, worker_id):
        """Add a member to the team."""
        if worker_id not in self.members:
            self.members.append(worker_id)

    def remove_member(self, worker_id):
        """Remove a member from the team."""
        self.members = [member for member in self.members if member != worker_id]

    def add_project(self, project_id):
        """Assign a project to the team."""
        if project_id not in self.projects:
            self.projects.append(project_id)

    def chat(self, env, project, msg):
        """Post a message to a project environment for all team members to see."""
        # This method should integrate with your messaging system
        # For now, it's a placeholder showing the intended action
        print(f"Message in {env} for project {project}: {msg}")

    def standard_operating_procedure(self):
        """Return the standard operating procedures for the team."""
        return self.SOP

    def get_info(self):
        """Return a summary of the team information."""
        return {
            "id": str(self._id),
            "name": self.name,
            "members": self.members,
            "backstory": self.backstory,
            "goal": self.goal,
            "environment": self.environment,
            "SOP": self.SOP,
            "projects": self.projects
        }
