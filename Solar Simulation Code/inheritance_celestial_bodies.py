#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 16:41:23 2023

@author: guilhermegarcia
"""
import math 
import numpy as np
np.set_printoptions(threshold=np.inf)
import random 
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class celestial_bodies_inheritance (object):
    
    #uses the Euler integration methode to update velocity, position and acceleration of the planets 
    
    def __init__ (self, name, mass, radius, colour,timestep,g):
        
    
        self.mass = float (mass)
        
        self.radius = float(radius)
        
        self.colour = colour.strip()
        
        self.timestep = timestep
        
        self.position = np.array([self.radius, 0])
        
        self.name = name 
        
        self.gravitational_constant = g
    
    def initialization(self, other):
        
        #creates the vectorial quantities neesd for the objects 
        
        self.position = np.array([self.radius, 0])

        self.external_mass = float(other.mass)
        
        self.external_position = other.position 
        
        self.radiusmag = np.linalg.norm(self.position)
        
        
        distance = self.position - self.external_position
        
        distance_mag = np.linalg.norm(distance)
        
        print(distance_mag)
        
        if distance_mag == 0 :  #avoids double counting 
            self.velocity = np.array([0,0])
            
        else :
            
            distance = self.position - self.external_position
            
            distance_mag = np.linalg.norm(distance)
            
            self.vmag = math.sqrt((self.external_mass * self.gravitational_constant)/distance_mag)
            
            self.velocity = np.array([0,self.vmag])
        
        if distance_mag == 0:
            
            self.acceleration = np.array([0,0])
        
        else:
            
            distance = self.position - self.external_position
            
            distance_mag = np.linalg.norm(distance)
            
            self.acceleration =  - (self.gravitational_constant * self.external_mass)/((distance_mag)**3) * distance
    
    
    # in this case position, acceleration and velocity are updated individually and should be all updated at once like in the Celestial Bodies Class 
    
    def update_position(self) :
        
            
            self.position = self.position + self.velocity * self.timestep 
        
        
    def update_velocity(self) : #we must start by updating acceleration, then velocity then position 
            
            self.velocity = self.velocity + self.acceleration * np.array([self.timestep]) 
            
        
    def update_acceleration(self,other) :
        
            self.external_mass = float(other.mass)
            
            distance = self.position - self.external_position 
            
            distance_mag = np.linalg.norm(distance)
            
            if distance_mag == 0:
                
                self.acceleration = (0,0)
            
            else:
            
                self.acceleration = - ((self.gravitational_constant * self.external_mass)/(distance_mag)**3) * distance
   
    
   
    def kinetic_energy (self):
    #calculates kinetic energy of the body - not necessary just felt should be included since the previous ceestial bodies class also has this characteristic 
        k = (1/2) * np.linalg.norm(self.velocity) * self.mass 
        
        return k 