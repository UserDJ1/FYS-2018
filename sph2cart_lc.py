import numpy as np
from math import pi
"""
################################################################################
All the code used in this lab is originally written by E. Holm, J. Jansson
and R.G. Graversen. The original package/script is written in matlab.
The code has been translated into python by Tuomas Heiskanen (spring 2019).
For questions email tuomas.i.heiskanen@uit.no
################################################################################

For user instructions see README.txt
"""


def sph2cart_lc(lat,lon,z = 0,flag = 'a'):
    """
    Converts spherical coordinates to catesian coordinates with height a
    (or a = 6371e3 if not specified). IF flag 'z' is specified, height
    is z otherwise height is a + z.

    """
    a = 6371e3
    if flag == 'z':
        r = z
    else:
        r = z+a
    x = r*np.sin(pi/2 - lat) *np.cos(lon-pi/2)
    y = r*np.sin(pi/2 - lat)*np.sin(lon-pi/2)
    z = r*np.cos(pi/2 - lat)
    return x,y,z
