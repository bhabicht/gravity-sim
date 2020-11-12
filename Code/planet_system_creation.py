import numpy as np


class Massiveobject(object):
    """
    Representation of a physical object

    This class should represent the sun or a planet or a rocket.
    It has 4 attributes, name, mass, position x, starting velocity v.
    The last 3 parameters are necessary to solve the differential equation
    which governs the motion of the planets.
    """
    def __init__(self, name, mass, x, v, F):
        """Set values for name, mass, place, velocity and force."""
        self.name = name
        self.mass = mass
        self.x = x
        self.v = v
        self.F = F

# create objects
# for the masses and positions and velocites I used the website
# https://ssd.jpl.nasa.gov/horizons.cgi#top , this is data provided by the NASA
sun = Massiveobject("sun", 1.9885E30,
    np.array([-5.682653841092885E8,1.112997165528592E9,3.445256675517594E6]),
    np.array([-1.446153643855376E+1,-3.447507130430867,3.988611997595555E-1]),
    np.zeros(3))
mercury = Massiveobject("mercury", 3.302E23, np.array([-1.004302793346122E+10,
    -6.782848247285485E+10,-4.760889633162629E+9]),
    np.array([3.847265155592926E+04,-4.158689546981208E+03,
    -3.869763647804497E+03]),np.zeros(3))
venus = Massiveobject("venus", 4.8685E24, np.array([1.076209595805564E11,
    8.974122818036491E9,-6.131976661929069E9]),
    np.array([-2.693485084259549E3,3.476650462014290E4,6.320912271467272E2]),
    np.zeros(3) )
earth = Massiveobject("earth", 5.97219E24,
    np.array([-2.54532370827383E10,1.460913442868109E11,-2.726527903765440E6]),
    np.array([-2.98633820023531E4,-5.165822246700293E3,1.135526860257752]),
    np.zeros(3))
mars = Massiveobject("mars", 6.4171E23,
    np.array([-1.98053552217007E11,-1.313944334060654E11,2.072245594990239E9]),
    np.array([1.439273929359666E4,-1.805004074289640E4,-7.312485979614864E2]),
    np.zeros(3))
jupiter = Massiveobject("jupiter", 1.898E27,  np.array([7.814223897437210E10,
    -7.769490008639349E11,1.474097288004637E+09]),
    np.array([1.284045160909457E4,1.930274035308634E3,-2.952516344902680E2]),
    np.zeros(3))
saturn = Massiveobject("saturn", 5.683E26,  np.array([5.674911817149432E11,
    -1.388366420433696E12,1.549271510988116E+09]),
    np.array([8.406314420691997E3,3.626623210585119E+3,-3.977556551929139E2]),
    np.zeros(3) )
uranus = Massiveobject("uranus", 8.681E25,  np.array([2.426731547813749E12,
    1.703392498245675E12,-2.511216806054187E+10]),
    np.array([-3.962513235696925E3,5.256545196047542E3,7.085805936919209E1]),
    np.zeros(3) )
neptune = Massiveobject("neptune", 1.024E26, ([4.374093815579369E12,
    -9.514047170929278E+11,-8.121298441744870E+10]),
    np.array([1.119134726474025E3,5.343389292709274E3,-1.358275265078215E2]),
    np.zeros(3) )
pluto = Massiveobject("pluto", 1.303E22,  np.array([1.940721406752713E12,
    -4.691796350742417E12,-5.932120230334544E10]),
    np.array([5.145967963274994E3,9.206861918697988E2,-1.587049289756031E3]),
    np.zeros(3) )
masses = np.array([1.9885E30,3.302E23,4.8685E24,5.97219E24,6.4171E23,1.898E27,
                   5.683E26,8.681E25,1.024E26,1.303E22])