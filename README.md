# Solar-Project-

This project aimed at creating a computational simulation of the Solar System and perform multiple experiments on it 

the experiments performed were, as stated in the project report:  

1. Orbital Periods and Energy Conservation - Determining the Orbital period for 
each planet in the simulation and comparing them with the real values. 
Observing the total of the energy of the system trough a long period of time and confirm if it is conserved over time.
2. Influence of Jupiter on Inner Planets - Creating a system where the planets 
only feel the gravitational force from the Sun and are not affected by each other’s gravitational pull 
and analyse how this affects the orbital periods of the 4 inner planets.
3. Direct Euler’s Integration - Using Euler’s method of integration (instead of 
Beeman’s method) to compute the orbits of the planets and observe its effects on the orbital 
periods and the energy conservation of the system.
4. Satellite to Mars - Simulating the launch of a satellite to Mars from Earth. 
This included finding the velocity for which the satellite gets closer to the planet and the time it takes to get there. 
The results were compared with previous missions to Mars in order to determine their accuracy.


As such this project comprises of multiple files :

project data - file from which the data for the planets, constants and unit conversions are read from

celestial_bodies - creates the class for the bodies that will be run in the simulation(planets and satellite), making sure its velocities, positions and accelerations are updated using the beeman method

celestial_bodies_inheritance - creates the class for the bodies that will be in the simulation (planets), but using the Euler's integration method instead

Project1 - creates the functions that will be used in the tasks for experiments 1, 2 and 3 

project2 - creates the functions used to performed experiment 4 

Experiment_1. Experiment_2, Experiment_3, Experiment_4 - files the perform the tasks necessary for each experiment 


The code in each experiment is made to be explored by the user, allowing for a high degree of experimentation on experiment 4 due to its testing nature
allowing the use to change the time step if they wish so 

The code on project1 and project2 contains extra functions that are not used for this experiments but that were thought to be interesting and potentially useful if the user pretends to develop their own experiments


To start testing each experiment just open the the files  Experiment_1. Experiment_2, Experiment_3, Experiment_4 and click run

