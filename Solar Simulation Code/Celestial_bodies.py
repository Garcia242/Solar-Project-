import math 
import numpy as np

np.set_printoptions(threshold=np.inf)
import random 
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class celestial_bodies (object):
    
    def __init__ (self, name, mass, radius, colour, timestep, g):
    
        #creates the basic properties for the bodies from input 
        
        self.name = name 
        
        self.mass = float (mass)
        
        self.radius = float(radius)
        
        self.colour = colour.strip() 
        
        self.timestep = timestep 
        
        self.position = np.array([self.radius, 0])
        
        self.gravitational_constant = g
        
    
    def initialization(self, other):
        
        #creates the basic vectorial properties from the bodies using a central object they can relate to eg:Sun
        
        self.position = np.array([self.radius, 0])
        
        self.external_mass = float(other.mass)
        
        self.external_position = other.position 
        
        self.radiusmag = np.linalg.norm(self.position)
        
        distance = self.position - self.external_position
        
        distance_mag = np.linalg.norm(distance)
        
        self.year = 0
        
        
        if distance_mag == 0 : #avoids division by zero
            self.velocity = np.array([0.1,0.1])
            
        else :
            
            # we consider the intial velocity to always be in the why direction
            distance = self.position - self.external_position
            
            distance_mag = np.linalg.norm(distance)
            
            self.vmag = math.sqrt((self.external_mass * self.gravitational_constant)/distance_mag)
            
            self.velocity = np.array([0,self.vmag])
            
        
        distance = self.position - self.external_position
        
        distance_mag = np.linalg.norm(distance)
        
        if distance_mag == 0: #avoids division by zero
            
            self.acceleration = np.array([0,0])
        
        else:
            

            self.acceleration =  - (self.gravitational_constant * self.external_mass)/((distance_mag)**3) * distance
        
        self.acceleration_old = self.acceleration 
        
        
    def update_position(self) :
        
        #updates the position of the body considering its current and previous velocities 

            #we need to find the previous position in order to be able to determine when the planet has finished its orbit - used to count peridos  
            self.position_old = self.position
            
            # from Beeman integration method
            self.position = self.position + self.velocity * self.timestep + (1/6)*(4*self.acceleration - self.acceleration_old)*self.timestep**2                  
        
        
    def update_velocity(self, other) : 

        #updates the velocity ate each timestep
        #also updates acceleration since the Beeman process uses 3 different acceleration, the process can be simplified by having this 3 accelerations reatributed everytime we calculate the velocity
            self.a_next = self.update_acceleration(other)
            
            self.velocity = self.velocity + (1/6)*(2*self.a_next + 5*self.acceleration - self.acceleration_old)*self.timestep
            
            self.acceleration_old = self.acceleration
            
            self.acceleration = self.a_next
            
            
            
    def update_acceleration(self,other) :
        
            #returns an acceleration based on the current position of the body and the object that is interaction with it 
            
            self.external_mass = float(other.mass)
        
            distance = self.position - other.position  
            
            distance_mag = np.linalg.norm(distance)
            
            if distance_mag == 0:
                
                acceleration = 0
            
            else :
            
                acceleration = - ((self.gravitational_constant * self.external_mass)/(distance_mag)**3) * distance
            
            return acceleration 
        
    def year_count(self):
        #helps counting the years and determining the orbital períod for a given body
        
        # when the planet crosses the x axis from negative to positive it completes an orbit 
        
        if (self.position_old[1] < 0.0 and self.position[1] >= 0.0):
            
            
            self.year +=1
            
            return True
        
        else:
            
            return False
    
    def kinetic_energy (self):
        
        #calculates the kinetic energy of the body
        
        k = (1/2) * np.linalg.norm(self.velocity) * self.mass 
        
        return k 

