[//]: # (Image References)

[image1]: static/learned_agent.gif "Trained Agent"
[image3]: static/loss_plot.png "Loss plot"

# Project 2: Continuous Control

### Introduction
 ![Trained Agent][image1]

In this environment, a double-jointed arm can move to target locations. A reward of **`+0.1`** is provided for each step that the agent's hand is in the goal location. Thus, the goal of your agent is to maintain its position at the target location for as many time steps as possible.

The observation space consists of 33 variables corresponding to position, rotation, velocity, and angular velocities of the arm. Each action is a vector with four numbers, corresponding to torque applicable to two joints. Every entry in the action vector should be a number between **`-1`** and **`1`**.

### Distributed Training

This project solves the multi agent version of the [Reacher](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Learning-Environment-Examples.md#reacher) environment. It contains 20 identical agents, each with its own copy of the environment. 

The environment was trained using **`DDPG`** Model  

#### Environment Solution

The agents  must get an average score of +30 (over 100 consecutive episodes, and over all agents). Specifically,
- After each episode, we add up the rewards that each agent received (without discounting), to get a score for each agent.  This yields 20 (potentially different) scores.  We then take the average of these 20 scores. 
- This yields an **average score** for each episode (where the average is over all 20 agents).

The environment is considered solved, when the average (over 100 episodes) of those average scores is at least +30. 

### Getting Started


1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:

    - **_Version 1: One (1) Agent_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

    - **_Version 2: Twenty (20) Agents_**
        - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux.zip)
        - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher.app.zip)
        - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86.zip)
        - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux_NoVis.zip) (version 1) or [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/Reacher_Linux_NoVis.zip) (version 2) to obtain the "headless" version of the environment.  You will **not** be able to watch the agent without enabling a virtual screen, but you will be able to train the agent.  (_To watch the agent, you should follow the instructions to [enable a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md), and then download the environment for the **Linux** operating system above._)


2. Place the file in  `data/` folder, and unzip (or decompress) the file. _You can also use any other file path_

3. Update the environment file path in `Continuous_Control.ipynb` file at `env = UnityEnvironment(file_name="data/Reacher.x86_64")`

### Dependencies
1. Follow the project setup instructions from the  `DRLND Github`: [click here](https://github.com/udacity/deep-reinforcement-learning)

### Instructions

Follow the instructions in `Continuous_Control.ipynb` to get started with training your own agent!  

### Project structure

1. `ddpg_agent.py`: This file contains the code for the deep deterministic policy gradient agent. It consists of three classes _Agent_ , _OUNOISE_ and _ReplayBuffer_. _Agent_ interacts with the underlying environment,  _OUNOISE_ is used for exploration and _ReplayBuffer_ is used for experience Replay i.e caching a buffer of memories

2. `model.py`: This file contains the code for a actor and critic feed forward neural network that is used by the agent for computing a mapping from state to action and computing state_action value. _customise this as you like_ 

3. `Continuous_Control.ipynb`: This jupyter notebook contains code for the _Agent_ interaction with the unity _reacher_ environment. It includes exploring the environment and training an agent on it.

### Results

With the model used in the project, the agent was able to solve the environment in 273 episodes

![Loss plot][image3]
