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

def calc_geo(p11,p01,lat0,lon0,k):
    """
    Method for calculating the geostrophic winds for a given
    pressurefield.
    """
    # Setting physical Constants

    a = 6371e3
    om = 7.292e-5
    ro = 1.29

    # lat/lon to rad
    latx = lat0*pi/180
    lonx = lon0*pi/180

    # Calculating the geostrophic wind components
    dpdx = -(k*p11/a)*(np.sin(latx)**2)*np.cos(k*lonx)
    dpdy = (p01/a)*np.sin(latx) - (p11/a)*np.sin(latx)*(2-3*(np.sin(latx)**2))*np.sin(k*lonx)
    u0g = dpdy/(ro*2*om*np.sin(latx))
    v0g = dpdx/(ro*2*om*np.sin(latx))

    return np.array([u0g,v0g])
