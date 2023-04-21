#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 09:16:25 2023

@author: guilhermegarcia
"""

# Satelitte simulator 

import math 
import numpy as np
np.set_printoptions(threshold=np.inf)
import random 
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Celestial_bodies import celestial_bodies


class animation(object):
        
        def __init__(self, timestep):
            
            #sets up the planets and all their basic characteristics 
            
            self.timestep = int(timestep)
        
            inputdata = []
        
            filename = "project_data.txt"
            filein = open(filename, "r")
            #reads the data from a file 
            for line in filein.readlines():
                if (not line.startswith("#")):
                    inputdata.append(line)
            filein.close()
            #constants and conversion units used 
            g = float(inputdata[0])
            mass_conversion = float(inputdata[1])
            au_conversion= float(inputdata[2])
            
            self.bodies = []
            # creating the planets - celestial bodies we will be using during the simulation
            for i in range(3, len(inputdata), 4):
                name = inputdata[i]
                mass = float(inputdata[i+1])* mass_conversion
                orbit = float(inputdata[i+2])* au_conversion
                colour = inputdata[i+3]
                
                # print (str(name) + str(mass) + str(orbit) + str(colour))
                self.bodies.append(celestial_bodies(name, mass, orbit, colour,self.timestep, g))
            
            self.gravitational_constant = g 
            
            # we must intialize the planets with their position in relation to the sun
            
            for i in range (0,len(self.bodies)):
                self.bodies[i].initialization(self.bodies[0])
            
           
            # Creating the different list that will store the data that will be used during the simulation
            
            self.patches = []
            
            self.energies= []
            
            self.times = []
            
            self.times_earth = []
            
            self.positions = []
        
            #create your satelitte boddy 
            # from our file we know that the hearth is the 3th body created in the file  
            mass_perseverance = self.bodies[3].mass * 1*10**(-21)
        
            
            self.satelite = celestial_bodies("satelitte", mass_perseverance, self.bodies[3].radius + 1.496e8 , "b" , self.timestep, g)
            
            # Satelite starts from the Earth so it will have the same characteristics of it's orbit 
            #We will need to change it's initial velocity to be the same has the hearth
            # the satelite should be launched with a given velocity however its inital onbe will be the velocity of the Earth
            
            self.satelite.initialization(self.bodies[3])
            
            self.satelite.velocity = np.copy(self.bodies[3].velocity )
            
            self.bodies.append(self.satelite)
            

            
            
        def initialize (self):
            
            return self.patches 
        
            
        def velocity_angle_survey (self, sattelite_velocity, increment):
            
            # finds the best angle for a given velocity modulus to ensure the closest approach distance
            
            
            #frequency for wich we want to test theta
            increment = int(increment)
            
            specific_distances = []
            
            angles = []
            
            v = sattelite_velocity
            
            
            
            
            for theta in range (0, 181, increment):
                
                for i in range (0,len(self.bodies)):
                    self.bodies[i].initialization(self.bodies[0])
                
                self.bodies[-1].initialization(self.bodies[3])
                
                self.bodies[-1].velocity = np.copy(self.bodies[3].velocity )
                
                angles.append(theta)
                
                time_initial = time.time()
                
                minimum_distance = self.simulation_no_animation(v, theta) 
                
                specific_distances.append(minimum_distance)
                
            
            sattelite_distance = min(specific_distances)
            
            sattelite_distance_index = specific_distances.index(sattelite_distance)
                
            launch_angle = angles[sattelite_distance_index]
            
            #print ("The best angle for this velocity is " + str(launch_angle))
            
            #print ("Closest distance to Mars is " + str(sattelite_distance) + "meters")

            
            return sattelite_distance, launch_angle
            
            
        def velocity_total_survey (self, velocity_min, velocity_max, v_increment, theta_increment):
            # for a range of velocities and angles thsi function finds the angle and the velocity for whci the distance to mars is minimal
            
            velocity_min = int(velocity_min)
            
            velocity_max = int(velocity_max)
            
            v_increment = int(v_increment) 
            
            theta_increment = theta_increment 
            
            velocities = []
            
            distances = []
            
            angles = []
            
            for v in range (velocity_min, velocity_max, v_increment):
                
                time_initial = time.time()

                velocities.append(v)
                
                (modulus_distance, best_angle) = self.velocity_angle_survey(v, theta_increment)
                    
                distances.append(modulus_distance)
                
                angles.append(best_angle)
                
                time_final = time.time()
                
                final_time = time_final - time_initial
                
                total_time = final_time * (velocity_max - velocity_min)/v_increment 
                
                print ("This calculations will take " + str(total_time) + " seconds to run")
            
            best_distance = min(distances)
            
            best_distance_index = distances.index(best_distance)
            
            best_angle = angles[best_distance_index]
            
            best_velocity = velocities[best_distance_index]
            
            print ("The closest distance to Mars is " + str(best_distance) + " meters")
            
            print ("The launch angle is " + str(best_angle) + " degrees")
            
            print ("The velocity of launch is " + str(best_velocity) + " ms^-1")

            
            plt.plot(velocities, distances)               
            plt.xlabel("Velocities (ms^-1)")
            plt.ylabel("Minimum distance for each velocity (m)")
                
            plt.show() 
            
        def velocity_modulus_survey (self, theta, velocity_min, velocity_max, v_increment):
            
            # calculates for a fixed angle theta the best velocity to reach the closest distance to Mars
            
            #not necessary for the way how the experiment is performed just felt like a complementary function to have considering the angle survey
            
            velocity_min = velocity_min
            
            velocity_max = velocity_max
            
            v_increment = v_increment 
            
            velocities = []
            
            distances = []
            
            angles = []
            
            for v in range (velocity_min, velocity_max, v_increment):
                
                time_initial = time.time()
                
                for i in range (0,len(self.bodies)):
                    self.bodies[i].initialization(self.bodies[0])
                
                self.bodies[-1].initialization(self.bodies[3])
                
                self.bodies[-1].velocity = np.copy(self.bodies[3].velocity )

                velocities.append(v)
                
                theta = theta
                
                v_distance = self.simulation_no_animation(v, theta)
                
                distances.append(v_distance)
                
                time_final = time.time()
                
                final_time = time_initial - time_final 
                
                total_time = final_time * (velocity_max - velocity_min)/1
                
                print (total_time)
            
            best_distance = min(distances)
            
            best_distance_index = distances.index(best_distance)
            
            best_velocity = velocities[best_distance_index]
            
            print ("The closest distance to Mars is " + str(best_distance) + " meters")
            
            
            
            print ("The velocity of launch is " + str(best_velocity) + " ms^-1")
            
            plt.plot(velocities, distances)               
            plt.xlabel("Velocities (ms^-1)")
            plt.ylabel("Minimum distance for each velocity")
                
            plt.show() 
        
           
   
        def animate (self, frame_idx): 
            
            #updates velocities and positions for a given simulation and returns the necessary data for visual representation
            
            for i in range (0, len(self.bodies)):
                
                for k in range (0, len(self.bodies)):
                    
                    if (i != k):
                        
                           self.bodies[i].update_velocity(self.bodies[k])
                           

            
            for i in range (0, len(self.bodies)):
                
                self.bodies[i].update_position()
                
                self.patches[i].center = self.bodies[i].position
            
            
            #get the distance from Mars at every step
            r =  self.bodies[-1].position - self.bodies[4].position 
            
            r = np.linalg.norm(r)
            
            self.positions.append(r)
            
            #get time in seconds
            
            time = (frame_idx ) * self.timestep
            
            self.times.append(time)
            
            # translate time into Earth Years 
            
            time_earth = time/(60*60*24*365) 
            #get the distance from Earth at eveery step
            r_earth = self.bodies[-1].position - self.bodies[3].position
            
            r_earth = np.linalg.norm(r_earth)
            
            #find if the sattelite is still leaving the earth or has returned (will return the same result difference is time)
            #sattekite will have returned to earth when this command prints and the sattelite has already gone to Mars you need to be seing the animation to interpret this data
            if r_earth < 9e9:
                
                print ("The sattelite returns to Earth after " + "%.2f"%(time_earth) + " after the initial launch")
            
            #time_earth = time 
            
            return self.patches
            
        def printing(self, v, theta ):
            
            #visual representation for a given launch velocity and angle
            
            v = v
            
            theta = theta
            
            theta = theta * (math.pi/180)
            
            
            #calculation of the velocity to add to the inital velocity of the sattelite
            v_x = v * math.cos(theta)
            
            v_y = v * math.sin(theta)
            
            self.bodies[-1].velocity +=  (v_x, v_y)
            
            maximum_distance = np.linalg.norm(self.bodies[-2].position) #jupiter will be the second body counting from the end since we appended the satelitte

            fig, ax = plt.subplots()
                        
            self.patches = []
            
            for i in range (0, len(self.bodies)):
               
                if (i==0):
                   
                    self.patches.append(plt.Circle(self.bodies[i].position, radius = maximum_distance*0.04 , color = self.bodies[i].colour, animated = True ))
           
                else :
               
                    self.patches.append(plt.Circle(self.bodies[i].position, radius = maximum_distance*0.02 , color = self.bodies[i].colour, animated = True ))
            
            
            for i in range (0,len(self.bodies)):
                
                ax.add_patch(self.patches[i])
           
            plt.axis('scaled')
            
            maximum_distance = np.linalg.norm(self.bodies[-2].position)
            plt.xlim(-maximum_distance,maximum_distance)
            plt.ylim(-maximum_distance,maximum_distance)
           
            self.anim = FuncAnimation(fig, self.animate, init_func= self.initialize, frames = 1000000, repeat = True, interval = 1, blit= True)
            
            plt.show()
            
        def satelite_values(self):
            
            #returns the necessary values regarding the simulation using the animation
            
            closest_distance = min(self.positions)
            
            closest_position_index = self.positions.index(closest_distance)
            
            aproach_time = self.times[closest_position_index]
            
            time_earth = aproach_time/(60*60*24*365) 
            
            print ("The distance of closest approach is " + "%.3f"%(closest_distance) + " meters.")
            
            print ("The sattelite will reach Mars after " + "%.3f"%(time_earth) + " years." )
        
        def simulation_no_animation (self, v, theta):
            
            #runs a loop over 2 years (expected maximum time for the sattelite to reach Mars) without the need for animation to identify the closest distance for a given launch velocity and angle 
         
            positions = []

            v = v
            
            theta = theta
            
            theta = theta * (math.pi/180)

            v_x = v * math.cos(theta)
            
            v_y = v * math.sin(theta)
            
            self.bodies[-1].velocity +=  (v_x, v_y)
            
            for i in range (0, (2*365*24*60*60), self.timestep):
                
                time_initial = time.time()
                
                for i in range (0, len(self.bodies)):
                    
                    for k in range (0, len(self.bodies)):
                        
                        if (i != k):
                            
                               self.bodies[i].update_velocity(self.bodies[k])
                               
                #self.satelite.update_velocity(self.bodies(i))
                
                for i in range (0, len(self.bodies)):
                    
                    self.bodies[i].update_position()

            
                r =  self.bodies[-1].position - self.bodies[4].position 
                
                r = np.linalg.norm(r)
                
                positions.append(r)
                
            
            minimum_r = min(positions)
            
            return minimum_r
                
            
        
        
        
        