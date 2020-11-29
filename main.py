import numpy as np

from Code.plotting import plot3D
from Code.leap_frog_algorithm import leapfrog_nsteps
from Code.planet_system_creation import sun, mercury, venus, earth, mars


delta_t = 60*60*24  # a day in seconds
selected_objects = [sun, mercury, venus, earth, mars]

nsteps = 100  # simulated time interval: nsteps*delta_t = 100 days
'''
initialize the vectors that will store position and velocities of the objects
the first index stores the values as function of the time, the second as a
function of the object and the third stores the x,y and z component
'''
x = np.zeros((nsteps, len(selected_objects), 3))
v = np.zeros((nsteps, len(selected_objects), 3))

# now do all the calculation and plotting
leapfrog_nsteps(nsteps, delta_t, selected_objects, x, v)
plot3D(x)
