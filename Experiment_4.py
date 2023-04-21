#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:28:54 2023

@author: guilhermegarcia
"""

from project2 import animation

#runs the tasks for experiment 4 

#finds the best velocity for a sattelite to Mars and the best launch angle 

def main():
    
    
    #animation function requires you to input the timstep in seconds that you wish the simulation to run
    #lower timesteo mean higher resolution and better results
    #10000 was found to be the best time step for this experiment (balance between time taken and resolution presented)
    a = animation(10000)
    
    #finds the best velocity within a velocity range for a given increment in velocities and a fixed increment on theta
    #the smaller the increments the more the resolution will be more (more velocity combinations will be tested ) 
    
    #need to insert the following values (velocity_min, velocity_max, v_increment, theta_increment) this is made interactive so it is possible to do multiple surveys were the velocity range decreases but the resolution increases 
    # the survey with highest resolution I made had the values (4.25e3, 5e3,5,4) - returned the best velocity of 4675 ms^-1 and launch angle of 72 degrees 
    #that one takes about 7 hours to run so the user can choose they're own ranges to test and increments to test
    a.velocity_total_survey(4.25e3, 5e3,5,4)
    
    
    #visual representation for a given launch velocity and launch angle 
    # the ideal velocity found was 4675 ms^-1 with a launch angle of 72 degrees 
    #sattelite is the second blue dot that leaves the Earth
    a.printing(4675,72)
    
    #returns the values when the sattelite hits mars and its minimum distance for the visual representation above 
    a.satelite_values()
    

main ()