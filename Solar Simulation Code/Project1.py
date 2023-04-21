#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 09:30:48 2023

@author: guilhermegarcia
"""
import math 
import numpy as np
np.set_printoptions(threshold=np.inf)

import random 
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Celestial_bodies import celestial_bodies

from inheritance_celestial_bodies import celestial_bodies_inheritance



class animation(object):
        
        def __init__(self, timestep):
            
            #sets up the planets and all their basic characteristics 
            
            self.timestep = int(timestep)
            
            inputdata = []
            
            #reads the data from a file 
            filename = "project_data.txt"
            filein = open(filename, "r")
        
            for line in filein.readlines():
                if (not line.startswith("#")):
                    inputdata.append(line)
            filein.close()
            
            #constants and conversion units used 
            
            g = float(inputdata[0])
            mass_conversion = float(inputdata[1])
            au_conversion= float(inputdata[2])
            
            self.gravitational_constant = g
            
            # creating the planets - celestial bodies we will be using during the simulation
            
            self.bodies = []
            
            self.bodies_inheritance = []
            
            self.bodies_sun = []
            
            
            for i in range(3, len(inputdata), 4):
                name = inputdata[i]
                mass = float(inputdata[i+1])* mass_conversion
                orbit = float(inputdata[i+2])* au_conversion
                colour = inputdata[i+3]
                
                # creates the planets classes , each class will be used for a different experiment 
                
                self.bodies.append(celestial_bodies(name, mass, orbit, colour,self.timestep, g))
                self.bodies_inheritance.append(celestial_bodies_inheritance(name, mass, orbit, colour,self.timestep,g))
                self.bodies_sun.append(celestial_bodies(name, mass, orbit, colour,self.timestep, g))
            
            
            # we must intialize the planets with their position in relation to the sun
            
            for i in range (0,len(self.bodies)):
                self.bodies[i].initialization(self.bodies[0])
                self.bodies_inheritance[i].initialization(self.bodies_inheritance[0])
                self.bodies_sun[i].initialization(self.bodies_sun[0])
            
           #creating the patches for the different animation functions
            self.patches = []
            
            self.patches_inheritance = []
            
            self.patches_sun = []
            
            #creating lists to store the energy data for the different experiments 
            self.energies= []
            
            self.energies_inheritance = []
            
            self.energies_sun = []
            
            #creating lists to store the time data for different experiments 
            self.times = []
        
            self.times_inheritance = []
            
            self.times_sun = []
        

            
        def initialize (self):
            
            return self.patches 
        
        def initialize_inheritance (self):
            
            return self.patches_inheritance
        
        def initialize_sun(self):
            
            return self.patches_sun
        
        def energy (self, a):
            #calculates total energy of the system at a given time
            k = 0
            
            u = 0
            
            for i in range (0, len(a)):
                
                #calculationg kinetic energy
                
                k += a[i].kinetic_energy()
                
                for k in range (0, len(a)):
                    
                    #getting potential energy
                    
                    if (k != i):
                        
                        distance = a[i].position - a[k].position  
                        
                        distance_mag = np.linalg.norm(distance)
                        
                        u -= self.gravitational_constant * a[i].mass  * a[k].mass * (1/distance_mag)
                
            # for the total potential energy we're double counting the energy of each bond thus we need to correct for this
                
            u = u/2
            
            total_energy = k + u 
            
            return total_energy
        
        
        def animate (self, frame_idx):
            
            # animation class for the first experiment 
            
            
            #get time in seconds
            
            time = (frame_idx ) * self.timestep
            
            # translate time into Earth Years 
            
            time_earth = time/(60*60*24*365.25) 
            

   # to get the velocity in each interaction we have to calculate the effects relative to every planet position and update it at once
   #once we know the final values of velocity and acceleration we can get the position
   #all velocities must be update simultaneously as well as all accelerations
            
           #updatins accelerations and velocities 
            for i in range (0, len(self.bodies)):
                
                for k in range (0, len(self.bodies)):
                    
                    if (i != k):
                        
                           self.bodies[i].update_velocity(self.bodies[k])
            #Updating positions
            for i in range (0, len(self.bodies)):
                self.bodies[i].update_position()
           
                self.patches[i].center = self.bodies[i].position
            
            # when a body crosses the x-axis an year for that body as passed - we can use it to calculate the period of oscilation
            for i in range (0, len(self.bodies)):
                
                if self.bodies[i].year_count() == True:
                    
                    period = time_earth/self.bodies[i].year
                    
                    print (self.bodies[i].name + " períod of oscilation is " + "%.3f"%float(period) + " Earth years.")
            # for every timestep we get the total energy of the system and the real time it corresponds to
            self.energies.append(self.energy(self.bodies))
            
            self.times.append(frame_idx * self.timestep)
            
                
            return self.patches
        
        def animate_inheritance (self, frame_idx):
            
            #animation class for experience 3 where we use the Euler's integration method instead of the Beeman method
            
            #get time in seconds
            
            time = (frame_idx ) * self.timestep
            
            # translate time into Earth Years 
            
            time_earth = time/(60*60*24*365) 
            
            for i in range (0, len(self.bodies_inheritance)):
                
                for k in range (0, len(self.bodies_inheritance)):
                    
                    if (i != k):
                            
                            
                            self.bodies_inheritance[i].update_acceleration(self.bodies_inheritance[k])
                            self.bodies_inheritance[i].update_velocity()
                        
                            
            
            for i in range (0, len(self.bodies_inheritance)):
                self.bodies_inheritance[i].update_position()
           
                self.patches_inheritance[i].center = self.bodies_inheritance[i].position
            
            
            self.energies_inheritance.append(self.energy(self.bodies_inheritance))
            
            self.times_inheritance.append(frame_idx * self.timestep)
            
            return self.patches_inheritance
        
        def animate_sun (self, frame_idx):
            
            # animation class for experiment 2 where we calculate only the gravitational effect of the Sun
            
            #get time in seconds
            
            time = (frame_idx ) * self.timestep
            
            # translate time into Earth Years 
            
            time_earth = time/(60*60*24*365.25) 
            
            #time_earth = time 
            
            
            for i in range (0, len(self.bodies)):
                            
                            self.bodies_sun[i].update_velocity(self.bodies_sun[0]) # we only update the planets in terms of the Sun 
                
            for i in range (0, len(self.bodies)):
                self.bodies_sun[i].update_position()
           
                self.patches_sun[i].center = self.bodies_sun[i].position
            
                
            for i in range (0, len(self.bodies)):
                
                if self.bodies_sun[i].year_count() == True:
                    
                    period = time_earth/self.bodies_sun[i].year
                    
                    print (self.bodies_sun[i].name + " períod of oscilation is " + "%.3f"%float(period) + " Earth years.")
            
            self.energies_sun.append(self.energy(self.bodies))
            
            self.times_sun.append(frame_idx * self.timestep)
                
            return self.patches_sun
            

        def printing(self):
            
            #Function that returns the visual representation for experiment 1 
            
           # to find the radius of orbit we need to consider the maximum radius of oscilation, thus the radius of the outermost planet 
            
            maximum_distance = np.linalg.norm(self.bodies[-1].position)
            
            fig, ax = plt.subplots()
                        
            self.patches = []
            self.patches_inheritance = []
            for i in range (0, len(self.bodies)):
            #creating the objects that will be shown in the animation 
                if (i==0):
                    
                    self.patches.append(plt.Circle(self.bodies[i].position, radius = maximum_distance*0.04 , color = self.bodies[i].colour, animated = True ))
            
                else :
                
                    self.patches.append(plt.Circle(self.bodies[i].position, radius = maximum_distance*0.02 , color = self.bodies[i].colour, animated = True ))
                
            for i in range (0,len(self.bodies)):
                
                ax.add_patch(self.patches[i])
            
          
           
            plt.axis('scaled')
            
            plt.xlim(-1e12,1e12)
            plt.ylim(-1e12,1e12)
           
            self.anim = FuncAnimation(fig, self.animate, init_func= self.initialize, frames = 1000000, repeat = True, interval = 1, blit= True)

            plt.show()
        
        def printing_inheritance(self):
            
            #Returns visual representation for experiment 3 
            
            maximum_distance = np.linalg.norm(self.bodies_inheritance[-1].position)
            
            fig, ax = plt.subplots()
            
            self.patches_inheritance = []
            
            
            
            for i in range (0, len(self.bodies_inheritance)):
                
                print(self.bodies_inheritance[i].velocity)
                
                print (self.bodies_inheritance[i].acceleration)
                
                print (self.timestep)
                
                if (i==0):
                    
                    self.patches_inheritance.append(plt.Circle(self.bodies_inheritance[i].position, radius = maximum_distance*0.04 , color = self.bodies_inheritance[i].colour, animated = True ))
            
                else :
                
                    self.patches_inheritance.append(plt.Circle(self.bodies_inheritance[i].position, radius = maximum_distance*0.02 , color = self.bodies_inheritance[i].colour, animated = True ))
                
            for i in range (0,len(self.bodies_inheritance)):
                
                ax.add_patch(self.patches_inheritance[i])
           
            plt.axis('scaled')
            
            plt.xlim(-1e12,1e12)
            plt.ylim(-1e12,1e12)
            
            self.anim = FuncAnimation(fig, self.animate_inheritance, init_func= self.initialize_inheritance, frames = 1000000, repeat = True, interval = 1, blit= True)
            
            plt.show()
            
        def printing_sun(self):
            
            #returns visual representation for experiment 2 
             
            # to find the radius of orbit we need to consider the maximum radius of oscilation, thus the radius of the outermost planet 
             
             maximum_distance = np.linalg.norm(self.bodies_sun[-1].position)
             
             fig, ax = plt.subplots()
                         
             self.patches = []
             self.patches_inheritance = []
             self.patches_sun = []
             for i in range (0, len(self.bodies_sun)):
                 
                 if (i==0):
                     
                     self.patches_sun.append(plt.Circle(self.bodies_sun[i].position, radius = maximum_distance*0.04 , color = self.bodies_sun[i].colour, animated = True ))
             
                 else :
                 
                     self.patches_sun.append(plt.Circle(self.bodies_sun[i].position, radius = maximum_distance*0.02 , color = self.bodies_sun[i].colour, animated = True ))
                 
             for i in range (0,len(self.bodies_sun)):
                 
                 ax.add_patch(self.patches_sun[i])
             
           
            
             plt.axis('scaled')
             
             plt.xlim(-1e12,1e12)
             plt.ylim(-1e12,1e12)
            
             self.anim = FuncAnimation(fig, self.animate_sun, init_func= self.initialize_sun, frames = 1000000, repeat = True, interval = 1, blit= True)
             
             plt.show()
            
        def energy_graph_no_animation(self):
            
            #retruns an energy graph for a fixed time range withou the need to run an animation or visual representaion 
            
            
            for j in range (0, 1000000):
                
                time_initial = time.time()
                 
                # energy for the normal case of experiment 1 
                for i in range (0, len(self.bodies)):
                        
                    for k in range (0, len(self.bodies)):
                            
                            if (i != k):
                                
                                   self.bodies[i].update_velocity(self.bodies[k])
                    
                    for i in range (0, len(self.bodies)):
                        self.bodies[i].update_velocity
                
                self.energies.append(self.energy(self.bodies))
                
                self.times.append(j * self.timestep)
            
            # energy for the Euler's method 
                for i in range (0, len(self.bodies_inheritance)):
                    
                    for k in range (0, len(self.bodies_inheritance)):
                        
                        if (i != k):
                                
                                
                                self.bodies_inheritance[i].update_acceleration(self.bodies_inheritance[k])
                                self.bodies_inheritance[i].update_velocity()
                            
                                
                
                for i in range (0, len(self.bodies_inheritance)):
                    self.bodies_inheritance[i].update_position()
                    
                self.energies_inheritance.append(self.energy(self.bodies_inheritance))
                
                # enrgy for the case were only the sun is considered - not necessary in this case an wont print in the graphic because the result is commented - nice feature that can be used in the future
                for i in range (1, len(self.bodies)):
                    

                    self.bodies[i].update_velocity(self.bodies[0])
                
                for i in range (0, len(self.bodies)):
                    self.bodies[i].update_position()
               
                
                    
                self.energies_sun.append(self.energy(self.bodies))
                
                time_final = time.time()
                
                final_time = time_initial - time_final 
                
                total_time = final_time * 1000000
                    
                
            #prints a graph of the enrgies to check if the total energy of the system is conserved 
            
            plt.plot(self.times, self.energies, label = "Beeman")   
            plt.plot(self.times, self.energies_inheritance, label = "Euler")
            #plt.plot(self.times, self.energies_sun, label = "Beeman")  
            plt.xlabel("Time (s)")
            plt.ylabel('Total Energy of the system (J)')
            
            plt.legend ()
            plt.show()
            
        def energy_graph(self):
            
            # Prints the energy graph for when the animation is run
            # Can print it for the Beeman case, the Euler's case or both 
            # Doesn't allow for a good selection of a time range so its good for quick analysis and conclusions, previous function is better for including in a report 
                
            plt.plot(self.times, self.energies) 
            plt.plot(self.times_inheritance, self.energies_inheritance)                 
            plt.xlabel("Time (s)")
            plt.ylabel('Total Energy of the system (J)')
                
            plt.show()
        
        
                        
                

