"""
This is the main LLM core processor, it makes the final decision on which action it should take
It is accompanied by a semantic router and a graph of thoughts 

1. Memory Prompt is sent to fine-tuned semantic router, tuned on each possible action
    router{{prompt}} 
2. Return suggested route
    tool(web_search)
3. Graph of thoughts verifies that route and returns this verification information to the user to better fine tune
    Is tool(web_search) the best action to take for {{prompt}}?
    Yes
4. Accuracy is stored as a benchmark for each route
    router(tool(web_search)) accuracy = 99.9%
    PASS
    **For routers who are at 90% or better, worker does not have to await GoT to proceed w/ action,
        GoT is used for further benchmarking, and if it drops below must await again**
5. Final action or loop is performed
** make sure to save action to the environment - handled in each individual function **
"""