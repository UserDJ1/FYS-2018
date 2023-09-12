"""
################################################################################
All the code used in this lab is originally written by E. Holm, J. Jansson
and R.G. Graversen. The original package/script is written in matlab.
The code has been translated into python by Tuomas Heiskanen (spring 2019).
For questions email tuomas.i.heiskanen@uit.no
################################################################################

For user instructions see README.txt
"""

class S_array():
    """Structured array used in cor_lab"""
    def __init__(self):
        self.ipm = 0
        self.ifwe0 = 0
        self.a = 0
        self.p01 = 0
        self.p11 = 0
        self.angvel = 0
        self.k1 = 0
        self.k2 = 0
        self.om = 0
        self.ro = 0
        self.fk = 0
        self.k = 0
        self.u0 =0
        self.v0 = 0
        self.lat0 = 0
        self.lon0 = 0
        self.geostrophic = 0
        self.curv = 0
