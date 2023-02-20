# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""
# Importing the created classes
from Creatures import Bear
from Creatures import Fish
from Creatures import Water

# Importing needed packages
import random

# Creating the River Class
class River:
    def __init__(self, n_room, n_bears, n_fish, n_rounds):
        # Establishing base variables
        self.n_room = n_room # Establishing n_room
        self.n_bears = n_bears # Establishing n_bears
        self.n_fish = n_fish # Establishing n_fish
        self.n_rounds = n_rounds # Establishing n_rounds
        self.x = list(range(self.n_room)) # Generate a list with n_room amount of spaces
        y = random.sample(range(self.n_room), self.n_room) # generate a list fom 0 to n_room, and shuffle it

        # Populating the river
        water_spots = [] # Create an empty list to deposit the location of water spots
        j = 0 # set variable j to 0
        if self.n_bears + self.n_fish > n_room: # Ensuring the number of creatures doesn't exceed the number of spaces in the river
            print("Error: more space or less creatures needed")
        else:
            for i in y: # Go through the shuffled list
                if j < n_bears: # To the first n_bears positions
                    self.x[i] = Bear() # assign bear
                    j = j + 1 # increase j
                elif j < (n_bears + n_fish): # To the next n_fish positions
                    self.x[i] = Fish() # assign fish
                    j = j + 1 # increase j
                else: # Remaining spaces
                    self.x[i] = Water() # assign as water
                    water_spots.append(i) # make a list with the index of said spots
        # Generate a new variable called water, which saves the water positions
        self.water = water_spots

        # Generate a new variable z which has the labels for each of the elements in the list x
        self.z = list(range(self.n_room)) # generate a list with n_room amount of spaces
        for l in range(len(self.z)):
            self.z[l] = self.x[l].label

        # Making the Simulation
        for i in range(self.n_rounds): # For as many rounds as established
            p = random.randint(0,(self.n_room)) # Select a random position

            if self.x[p].hp == 0: # If the position has water
                #print message
                print("========== Round ", i + 1," =========")
                print("Ecosystem status: Everyone remained still\n")
                # skip to next round
                continue

            elif p > 0 and p < self.n_room: # if the position is in the middle
                d = random.choice(("l", "r")) # choose a direction randomly
                if d == "l": # if it chooses to go to the left
                    if self.x[p].hp > self.x[p-1].hp: # and the hp of the selected is > than the one in the new spot
                        self.x[p-1] = self.x[p] # replace the selected one with the one in the new position
                        self.x[p] = Water() # place water in the newly empty spot
                        self.water.append(p) # add that location to the water list

                    elif self.x[p].hp < self.x[p-1].hp: # and the hp of the selected is < than the one in the new spot
                        self.x[p] = Water() # replace the empty spot with water
                        self.water.append(p) # place water in the newly empty spot

                    elif self.x[p].hp == self.x[p-1].hp: # and they are the same class
                        e = random.choice(range(len(self.water))) # select a random position with water
                        f = self.water.pop(e) # Drop that position from the water list
                        self.x[f] = self.x[p] # Place the creature in said spot

                else: # if it chooses to go to the right
                    if self.x[p].hp > self.x[p+1].hp: # and the hp of the selected is > than the one in the new spot
                        self.x[p+1] = self.x[p] # replace the selected one with the one in the new position
                        self.x[p] = Water() # place water in the newly empty spot
                        self.water.append(p) # add that location to the water list

                    elif self.x[p].hp < self.x[p+1].hp: # and the hp of the selected is < than the one in the new spot
                        self.x[p] = Water() # replace the empty spot with water
                        self.water.append(p) # place water in the newly empty spot

                    else: # and they are the same class
                        e = random.choice(range(len(self.water))) # select a random position with water
                        f = self.water.pop(e) # Drop that position from the water list
                        self.x[f] = self.x[p] # Place the creature in said spot

            elif (p == 0): # If it selected the left-most position
                if self.x[p].hp > self.x[p+1].hp: # and the hp of the selected is > than the one in the new spot
                    self.x[p+1] = self.x[p] # replace the selected one with the one in the new position
                    self.x[p] = Water() # place water in the newly empty spot
                    self.water.append(p) # add that location to the water list

                elif self.x[p].hp < self.x[p+1].hp: # and the hp of the selected is < than the one in the new spot
                    self.x[p] = Water() # replace the empty spot with water
                    self.water.append(p) # add that location to the water list

                elif self.x[p].hp == self.x[p+1].hp: # and they are the same class
                    e = random.choice(range(len(self.water))) # select a random position with water
                    f = self.water.pop(e) # Drop that position from the water list
                    self.x[f] = self.x[p] # Place the creature in said spot

            elif p == self.n_room: # If it selected the right-most position
                if self.x[p].hp > self.x[p-1].hp: # and the hp of the selected is > than the one in the new spot
                    self.x[p-1] = self.x[p] # replace the selected one with the one in the new position
                    self.x[p] = Water() # place water in the newly empty spot
                    self.water.append(p) # add that location to the water list

                elif self.x[p].hp < self.x[p-1].hp: # and the hp of the selected is < than the one in the new spot
                    self.x[p] = Water() # replace the empty spot with water
                    self.water.append(p) # add that location to the water list

                elif self.x[p].hp == self.x[p-1].hp: # and they are the same class
                    e = random.choice(range(len(self.water))) # select a random position with water
                    f = self.water.pop(e) # Drop that position from the water list
                    self.x[f] = self.x[p] # Place the creature in said spot

            for l in range(len(self.z)): # Generate a label list
                self.z[l] = self.x[l].label

            # Print the results of the round
            print("========== Round ", i + 1," =========")
            print("Ecosystem status:\n")
            print(self.z, "\n")