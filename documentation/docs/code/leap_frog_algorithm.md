Module code.leap_frog_algorithm
===============================

Functions
---------

    
`calculate_all_forces(selected_objects)`
:   Calculate sum of all forces.
    
    This function updates the forces as a function of the new positions.
    We need the second loop to sum up all the forces that act upon the object
    given by the first loop. We need the if statement to prohibit that we
    calculate the gravitational force of the object acting on itself.
    You could store the results and calculate only half of the terms, using
    F_12 = -F_21 (newton's 3rd law)

    
`leapfrog_nsteps(nsteps, delta_t, selected_objects, x, v)`
:   Execute n steps of the leapfrog algorithm.
    
    Put all 4 steps into a function, that also stores the position and
    velocities vectors of all objects and for every time step

    
`update_all_positions(delta_t, selected_objects)`
:   Update the coordinates.
    
    This function updates all the positions, with a euler step using half of
    the step size

    
`update_all_velocities(delta_t, selected_objects)`
:   Update all the velocities.