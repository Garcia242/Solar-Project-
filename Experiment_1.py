#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:01:28 2023

@author: guilhermegarcia
"""

from Project1 import animation 

# peforms the tasks for experiment 1 

#creates a simulation of the Solar Systrem using the beeman integrator, generates a graphic of the energy of the system, returns the orbital periods
def main():
    
    #animation function requires you to input the timstep in seconds that you wish the simulation to run
    #lower timesteo mean higher resolution and better results
    #10000 was found to be the best time step for this experiment (balance between time taken and resolution presented)
    a = animation(10000)
    
    #runs a simulation for the Solar System bodies and returns its orbital periods
    a.printing()
    
    #plots the total energy of the system for the time the simultion has run. 
    #To observe the energy conservation it is necessary to let the program run for some time, preferably until jupiter has completed one orbit
    a.energy_graph()
    
main()