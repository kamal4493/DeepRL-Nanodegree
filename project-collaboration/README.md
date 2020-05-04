[//]: # (Image References)

[image1]: static/learned_agent.gif "Trained Agent"
[image2]: static/loss_plot.png "Loss plot"


# Project 3: Collaboration and Competition

### Introduction


![Trained Agent][image1]

In this environment, two agents control rackets to bounce a ball over a net. If an agent hits the ball over the net, it receives a reward of +0.1.  If an agent lets a ball hit the ground or hits the ball out of bounds, it receives a reward of -0.01.  Thus, the goal of each agent is to keep the ball in play.

The observation space consists of 24 variables corresponding to the position and velocity of the ball and racket. Each agent receives its own, local observation.  Two continuous actions are available, corresponding to movement toward (or away from) the net, and jumping. 

The task is episodic, and in order to solve the environment, your agents must get an average score of +0.5 (over 100 consecutive episodes, after taking the maximum over both agents). Specifically,

- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent. This yields 2 (potentially different) scores. We then take the maximum of these 2 scores.
- This yields a single **score** for each episode.

The environment is considered solved, when the average (over 100 episodes) of those **scores** is at least +0.5.

### Getting Started

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux_NoVis.zip) to obtain the "headless" version of the environment.  You will **not** be able to watch the agent without enabling a virtual screen, but you will be able to train the agent.  (_To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above._)

2. Place the file in  `data/` folder, and unzip (or decompress) the file. _You can also use any other file path_

3. Update the environment file path in `Tennis.ipynb` file at `env = UnityEnvironment(file_name="data/Tennis")`

### Dependencies
1. Follow the project setup instructions from the  `DRLND Github`: [click here](https://github.com/udacity/deep-reinforcement-learning)


### Instructions

Follow the instructions in `Tennis.ipynb` to get started with training your own agent!  

## Project structure

1. `ddpg_agent.py`: This file contains the code for the deep deterministic policy gradient agent. It consists of three classes _Agent_ , _OUNOISE_ and _ReplayBuffer_. _Agent_ interacts with the underlying environment, I didnot use _OUNOISE_ for this task as noise from normal distribution worked well. Feel free to use _OUNOISE_ and _ReplayBuffer_ is used for experience Replay i.e caching a buffer of memories

2. `model.py`: This file contains the code for the actor and critic feed forward neural network that is used by the agent for computing a mapping from state to action and computing state_action value. _customise this as you like_ 

3. `Tennis.ipynb`: This jupyter notebook contains code for the _Agent_ interaction with the unity _tennis_ environment. It includes exploring the environment and training an agent on it.

### Results

With the model used in the project, the agent was able to solve the environment in 547 episodes

![Loss plot][image2]
