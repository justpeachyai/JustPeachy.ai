"""
Finetuning w/ GANs
All actions are sent to the feedback worker
This is a worker specifically trained to interpret explict and non-explicit feedback
-- It waits for 100 actions before running a training loops

This feedback worker uses this information to create a training data set
It fine-tunes the model w/ the training dataset
Compares its performance to previous performance
If the model improved by at least 5% then the model is updated
If the model did not improve it waits until a training loop produces favorable output before updating

**point is to move knowledge from external sources to internal ones**
"""