Module code.physical_functions
==============================

Functions
---------

    
`gravforce(x1, x2, m1, m2)`
:   Calculate the gravitational force.
    
    This function returns the value of the gravitational force, in SI units,
    acting on the first object and caused by the second object, using
    newton's law of gravitation and newton's 2nd law of motion. I.e. we ignore
    relativistic effects (relevant for the apsidal precession of e.g. mercury).
    Input values are the positions of the 2 object in cartesian coordinates and
    the masses of the objects

    
`gravpot(x1, x2, m1, m2)`
:   Calculate the gravitational potential.
    
    Return the value of the gravitational potential, in SI units,
    for both particles at positions x1 and x2, caused be the presence of the
    other mass. Input values are the positions of the 2 object in cartesian
    coordinates and the masses of the objects