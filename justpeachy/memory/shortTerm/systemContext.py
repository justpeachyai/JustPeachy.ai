"""
SystemContext Class:

Held in-context inside the system message. Refers to the system block, which provides essential, foundational context to the AI. This isnlcudes the persona information,
essential user details, and any other baseline data necessary for the AI's basic functional

- persona: the persona of the worker (name, role, backstory, personality type, tone, voice, image)
- user: the information about the user in which the worker is speaking, can be human or ai

This information is passed to the core memory.
"""