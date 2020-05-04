import numpy as np
from collections import defaultdict

class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.

        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        self.eps = 1
        self.alpha = 1
        self.counter = 1
        
    def get_state_probs(self, Q_s):
        """
        """
        eps = self.eps
        nA = self.nA
        g_prob = (1 - eps) + eps/nA # greedy probability
        ng_prob = eps/nA

        prob = np.array([ng_prob] * nA)
        g_a = np.argmax(Q_s) #greedy action

        prob[g_a] = g_prob

        return prob
    
    def select_action(self, state):
        """ Given the state, select an action.

        Params
        ======
        - state: the current state of the environment

        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        # NOTE to future self: since Q is a default dict, for states not present in it will have a numpy of zeros
        Q = self.Q
        probs = self.get_state_probs(Q[state])
        a = np.random.choice(np.arange(self.nA), p = probs)
        
        return a

    def step(self, state, action, reward, next_state, done):
        """ Update the agent's knowledge, using the most recently sampled tuple.

        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        Q = self.Q
        alpha = self.alpha
        gamma = 0.9
        if done:
            estimated_gt = reward
        else:
            #estimated_gt = reward + gamma *   np.max(Q[next_state]) 
            estimated_gt = reward + gamma *   self.expected_qval(Q[next_state])
        Q[state][action] = Q[state][action] + alpha *(estimated_gt  - Q[state][action])
        self.counter += 1
        self.eps = self.eps/self.counter
        
    def expected_qval(self, Q_s):
        # expected sarsa algo
        prob = self.get_state_probs(Q_s)
        
        return np.average(Q_s, weights=prob)