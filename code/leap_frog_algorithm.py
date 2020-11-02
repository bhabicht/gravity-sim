import numpy as np

from code.planet_system_creation import sun, mercury, venus, earth, mars
from code.physical_functions import gravforce

"""
implementation of leap frog algorithm
start with just 3 objects and calculate the trajectories
1. update all positions
2. calculate force with new positions
3. calculate new velocities
4. update all positions again
5. repeat
6. ...
7. profit!
"""

#massive_objects = [sun, mercury, venus, earth, mars, jupiter, saturn, uranus,
#                   neptune, pluto]
massive_objects = [sun, mercury, venus, earth, mars]
# 1. update all positions
def update_all_positions(delta_t):
    """
    This function updates all the positions, with a euler step using half of
    the step size.
    """
    for m_obj in massive_objects:
        m_obj.x = m_obj.x + m_obj.v * delta_t/2
        
# 2. calculate the force acting on each massive object
def calculate_all_forces(delta_t):
    """
    This function updates the forces as a function of the new positions.
    We need the second loop to sum up all the forces that act upon the object
    given by the first loop. We need the if statement to prohibit that we
    calculate the gravitational force of the object acting on itself.
    You could store the results and calculate only half of the terms, using
    F_12 = -F_21 (newton's 3rd law)
    """
    for m_obj1 in massive_objects:
        m_obj1.F = np.zeros(3)
        for m_obj2 in massive_objects:
            if(m_obj2!=m_obj1):
                m_obj1.F += gravforce(m_obj1.x, m_obj2.x, m_obj1.mass, 
                                      m_obj2.mass)

# 3. calculate new velocities
def update_all_velocities(delta_t):
    """
    This function updates all the velocities.
    """
    for m_obj in massive_objects:
        m_obj.v = m_obj.v + m_obj.F/m_obj.mass * delta_t
        
def leapfrog_nsteps(nsteps, delta_t, x, v):
    """
    Put all 4 steps into a function, that also stores the position and 
    velocities vectors of all objects and for every time step
    """
    for i in range(nsteps):
        j=0
        update_all_positions(delta_t)
        calculate_all_forces(delta_t)
        update_all_velocities(delta_t)
        update_all_positions(delta_t)
        for m_obj in massive_objects:
            x[i,j]=m_obj.x
            v[i,j]=m_obj.v
            j += 1