import scipy.constants as const
import numpy as np

def gravpot(x1,x2,m1,m2):
    return -const.G*m1*m2/np.linalg.norm(x1-x2)