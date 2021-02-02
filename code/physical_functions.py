import numpy as np
import scipy.constants as const


def gravforce(x1, x2, m1, m2):
    """
    Calculate the gravitational force.

    This function returns the value of the gravitational force, in SI units,
    acting on the first object and caused by the second object, using
    newton's law of gravitation and newton's 2nd law of motion. I.e. we ignore
    relativistic effects (relevant for the apsidal precession of e.g. mercury).
    Input values are the positions of the 2 object in cartesian coordinates and
    the masses of the objects
    """
    if np.array_equal(x1, x2):
        raise ValueError("Division by 0 Error")
    return -const.G*m1*m2/np.linalg.norm(x1-x2)**3*(x1-x2)


def generalized_gravforce(kappa):
    """
    Calculate a generalized gravitational force

    The same as gravforce, but gravforce_kappa returns a function that takes as
    argument a parameter kappa, which determines how strong the gravitational
    attraction will be.
    """
    def gravforce_kappa(x1, x2, m1, m2):
        return -const.G*m1*m2/np.linalg.norm(x1-x2)**(kappa+1)*(x1-x2)
    return gravforce_kappa


def gravpot(x1, x2, m1, m2):
    """
    Calculate the gravitational potential.

    Return the value of the gravitational potential, in SI units,
    for both particles at positions x1 and x2, caused be the presence of the
    other mass. Input values are the positions of the 2 object in cartesian
    coordinates and the masses of the objects
    """
    if np.array_equal(x1, x2):
        raise ValueError("Division by 0 Error")
    return -const.G*m1*m2/np.linalg.norm(x1-x2)
