"""
A fine-tuned reward model that rewards or punishes the workers' responses
- If a human gives negative feedback, the worker receives penalty
- If the human gives positive feedback, the worker receives an reward
- If the human gices non-explicit feedback is it handled by the feedback_intereprer
"""
