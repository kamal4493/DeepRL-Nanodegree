import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            seed (int): Random seed
        """
        super(QNetwork, self).__init__()
        self.seed = torch.manual_seed(seed)
        "*** YOUR CODE HERE ***"
        hidden_dim = 64

        self.hidden1 = nn.Linear(state_size, hidden_dim)
        self.hidden2 = nn.Linear(hidden_dim, hidden_dim)
        #self.hidden3 = nn.Linear(hidden_dim, 16)
        self.out = nn.Linear(hidden_dim, action_size)
        
    def forward(self, state):
        """Build a network that maps state -> action values."""
        x = F.relu(self.hidden1(state))
        x = F.relu(self.hidden2(x))
        #x = F.relu(self.hidden3(x))
        x = self.out(x)
        
        return x
