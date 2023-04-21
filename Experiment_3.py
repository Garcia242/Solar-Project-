#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:17:44 2023

@author: guilhermegarcia
"""

from Project1 import animation

# Runs the tasks for experiment 3 

# Calculates the position of the bodies using the Euler's method instead of Beeman's , runs a simulation for both and returns a graph of their energies to test energy conservation

def main():
    
    #animation function requires you to input the timstep in seconds that you wish the simulation to run
    #lower timesteo mean higher resolution and better results
    #10000 was found to be the best time step for this experiment (balance between time taken and resolution presented)
    a = animation(10000)
    
    #visual representation of Beeman's method 
    a.printing()

    # visual representation of Euler's method
    a.printing_inheritance()
    
    #Prints visual representation for the visual simulations just run- tricky to get the same time interval for both simulations
    a.energy_graph()

    #Prints the enrgy graphs for both methods for a fixed time of about 300years for a time step of 10000
    #runs trough a loop of 1000000 interactions so the choice of timestep may effect the time span - this solves the problem with plotting the graph
    #for the time the animations have been running
    a.energy_graph_no_animation()

main()