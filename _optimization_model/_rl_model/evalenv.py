#!/usr/bin/env python3
import sys
import json
import numpy as np
from cartpole import *

######## Defining Environment Storage

def evalenv(s):
 obsfile = s["Custom Settings"]["Input"]
 comparison = s["Custom Settings"]["Comparison"]
 states = []
 observation = []

 
 obsidx = -1
 if comparison == "action":
     obsidx = 4
 elif comparison == "position":
     obsidx = 7 # pole angle
 else:
     print("Error, 'Comparison' not recognized")
     sys.exit()
     #obsidx = 3 # pole velocity
 
 with open(obsfile) as json_file:
    data = json.load(json_file)
    states = data["States"][0]
    observation = data["Actions"][0]

 suml2 = 0.0

 for i, state in enumerate(states):

    s["State"] = state

    # Getting new action
    s.update()
 
    action = s["Action"]

    # Compare with observations
    reward = np.linalg.norm(np.array(observation[i])-np.array(action))
    s["Reward"] = reward

 # Done
 s["Termination"] = "Terminal"
