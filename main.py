import numpy as np

from code.plotting import plot3D
from code.leap_frog_algorithm import leapfrog_nsteps, massive_objects


delta_t = 60*60*24 #a day in seconds

nsteps=100
'''
initialize the vectors that will store position and velocities of the objects
the first index stores the values as function of the time, the second as a
function of the object and the third stores the x,y and z component
'''
x=np.zeros((nsteps,len(massive_objects),3))
v=np.zeros((nsteps,len(massive_objects),3))

# now do all the calculation and plotting
leapfrog_nsteps(nsteps, delta_t, x, v)
plot3D(x)