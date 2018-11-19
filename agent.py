"""The package describes AI agent based on pyTorch."""
import torch
import torch.nn as nn
import torch.nn.functional as F


class Agent(nn.Module):
    """Class for AI agent."""

    def __init__(self, env):
        """Construct an agent."""
        super(Agent, self).__init__()
        self.actions = env.actions
        self.states = env.states

        self.input_size = len(env.states)
        self.hidden_size = 100
        self.output_size = len(env.actions)

        self.fc1 = nn.Linear(self.input_size, self.hidden_size)
        self.fc2 = nn.Linear(self.hidden_size, self.output_size)

    def forward(self, state):
        """Forward pass of nn."""
        # state to one-hot
        x = [0.0] * self.input_size
        x[self.states.index(state)] = 1.0
        x = torch.FloatTensor(x)

        # forward pass
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))

        # choice
        return self.actions[x.argmax()]
