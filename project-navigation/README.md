[//]: # (Image References)

[image1]: static/agent_learned_resized.gif "Trained Agent"
[image2]: static/agent_random.gif "Trained Agent"
[image3]: static/loss_plot.png "Loss plot"

# Project 1: Navigation

### Introduction
The aim of the project is to train an agent to navigate (and collect bananas!) in a large, square world.
The figuures show the difference between a random and a trained agent.

![Random agent][image2]  ![Trained Agent][image1]

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana.  Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.  

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

### Getting Started

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)
    
    (_For Windows users_) Check out [this link](https://support.microsoft.com/en-us/help/827218/how-to-determine-whether-a-computer-is-running-a-32-bit-version-or-64) if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

    (_For AWS_) If you'd like to train the agent on AWS (and have not [enabled a virtual screen](https://github.com/Unity-Technologies/ml-agents/blob/master/docs/Training-on-Amazon-Web-Service.md)), then please use [this link](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux_NoVis.zip) to obtain the environment.

2. Place the file in  `data/` folder, and unzip (or decompress) the file. _You can also use any other file path_

3. Update the environment file path in `Navigation.ipynb` file at `env = UnityEnvironment(file_name="/data/Banana_Linux_NoVis/Banana.x86_64")`

### Dependencies
1. Follow the project setup instructions from the  `DRLND Github`: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

### Instructions

Follow the instructions in `Navigation.ipynb` to get started with training your own agent!  

### Project structure

1. `dqn_agent.py`: This file contains the code for the deep q learning agent. It consists of two classes _Agent_ and _ReplayBuffer_. _Agent_ interacts with the underlying environment and _ReplayBuffer_ is used for experience Replay i.e caching a buffer of memories

2. `model.py`: This file contains the code for a feed forward neural network that is used by the agent for computing a mapping from state to action. _customise this as you like_ 

3. `Navigation.ipynb`: This jupyter notebook contains code for the _Agent_ interaction with the unity _banana_ environment. It includes exploring the environment and training an agent on it.

### Results

With the model used in the project, the agent was able to solve the environment in 445 episodes

![Loss plot][image3]
