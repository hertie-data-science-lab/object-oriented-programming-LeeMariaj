# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
import numpy as np
from Creatures import Bear
from Creatures import Fish

class River:
    
    def __init__(self, n_room, n_bears, n_fish, n_rounds):
        x = list(range(n_room))
        for i in range(len(x)):
            x[i] = "~~~"
        self.eco = x

    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.eco, "\n")
        print("===================")

trial = River(10)
trial.display()