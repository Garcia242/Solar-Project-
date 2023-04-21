#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:08:58 2023

@author: guilhermegarcia
"""

from Project1 import animation

#runs the experiments for experiment 2 

#runs an animation for the Solar system accounting only for the gravitational effects of the Sun and returns the orbital periods of the planets 

def main():
    
    #animation function requires you to input the timstep in seconds that you wish the simulation to run
    #lower timesteo mean higher resolution and better results
    #10000 was found to be the best time step for this experiment (balance between time taken and resolution presented)
    a = animation(10000)
    
    #creates the visual representation and returns the values of the periods of oscilation using this simulation
    a.printing_sun()

main ()