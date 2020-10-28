import numpy as np
import leap_frog_algorithm


delta_t = 60*60*24 #a day in seconds

nsteps=1000
'''
initialize the vectors that will store position and velocities of the objects
the first index stores the values as function of the time, the second as a
function of the object and the third stores the x,y and z component
'''
x=np.zeros((nsteps,len(leap_frog_algorithm.massive_objects),3))
v=np.zeros((nsteps,len(leap_frog_algorithm.massive_objects),3))

# now do all the calculation and plotting
leap_frog_algorithm.leapfrog_nsteps(nsteps, delta_t, x, v)
plot(x,y)