import numpy as np
from math import pi
from calc_geo import calc_geo
from struct_array import S_array as sarray
from scipy.integrate import solve_ivp
from make_plots import gen_plot
import matplotlib.pyplot as plt
"""
################################################################################
All the code used in this lab is originally written by E. Holm, J. Jansson
and R.G. Graversen. The original package/script is written in matlab.
The code has been translated into python by Tuomas Heiskanen (spring 2019).
For questions email tuomas.i.heiskanen@uit.no
################################################################################

For user instructions see README.txt
"""



# Define values here:

# Parameters for initial pressurefield

p01 = 100   # hPa DEF = 100
p11 = 0     # hPa DEF = 0
c = 0       # m/s DEF = 0
k = 3       # Wavenumber DEF = 3

# Initial coordinates of air parcel

lat0 = 50   # Latitude in degrees DEF = 50
lon0 = 40   # Longitude in degrees DEF = 40

# Initial wind velocities
u0 = -8.3431    # Zonal wind component [m s^-1] DEF = -8.3431
v0 = 0          # Meridional wind component [m s^-1]  DEF = 0
# Specify geostrophic winds or not. This overrides u0 and v0 if set to True.
usegeo = False  # Whether to use geostrophic winds or not. DEF = False

# Whether or not to include curvature and friction
curv = False # Curvature [BOOL] DEF = False
fric = False # Friction [BOOL] DEF = False

# Forecast length and number of steps
nD = 3      # Forecast length in days
nt = 100    # Number of iterations to perform

# Figtitle
figname = 'Figure 1'
# Optional text on figure
grpname = 'text on figure'


##### ALL PARAMETERS ARE SPECIFIED BEFORE THIS LINE ######
def run_corlab(p01 = 100,\
                p11 = 0,\
                c = 0,\
                k = 3,\
                lat0 = 50,\
                lon0 = 40,\
                u0 = -8.3431,\
                v0 = 0,\
                usegeo = False,\
                curv = False,\
                fric = False,\
                nD = 3,\
                nt =100,\
                figname = figname,\
                grpname = grpname,\
                fig = None,\
                ax = None,\
                save = False):
    # Setting physical constants

    a = 6371e3          #Earth radius [m]
    om = 7.292e-5       #Earths rotation Omega [s^-1]
    ro = 1.29           #Density of air [kg m^-3]


    # Converting to hPa
    p01 *= 100
    p11 *= 100

    # iteration step
    # dt *= 3600*24/(nt-1)

    angvel = c/(a*np.cos(lat0*pi/180))*k

    # Checking which parameters to include
    if not curv and not fric:
        ipm = 1
        k1 = 0
        k2 = 0
        fk = 0
        ifwe0 = True
    elif not curv and fric:
        ipm = 2
        k1 = 0
        k2 = 0
        fk = 1e-6
        ifwe0 = True
    elif curv and not fric:
        ipm = 3
        k1 = 1
        k2 = 0
        fk = 0
        ifwe0 = True
    elif curv and fric:
        ipm = 4
        k1 = 1
        k2 = 0
        fk = 1e-6
        ifwe0 = True

    u0g,v0g = calc_geo(p11,p01,lat0,lon0,k)
    if usegeo:
        u0 = u0g
        v0 = v0g
    #Setting the timespan for the simulation
    tstart = 0
    #From days to seconds
    nS = 3600*24*nD
    tspan = np.linspace(0,nS,nt)
    # Initializing structured arrays
    dsetup = sarray()
    dconst = sarray()

    dsetup.ipm = ipm
    dsetup.ifwe0 = ifwe0

    dconst.a = a
    dconst.p01 = p01
    dconst.p11 = p11
    dconst.angvel = angvel
    dconst.k1 = k1
    dconst.k2 = k2
    dconst.om = om
    dconst.ro = ro
    dconst.fk = fk
    dconst.k = k
    dconst.lon0 = lon0
    dconst.lat0 = lat0
    dconst.u0 = u0
    dconst.v0 = v0
    dconst.geostrophic = usegeo
    dconst.curv = curv

    def eqs_of_motion(t,y):
        """
        RHS of the first order momentum equations on a sphere.
        Use this is combination with an ODE solver to solve the motions
        of air-parcels on a sphere.
        dsetup,dconst are structured arrays containing setup information and
        constants.
        """
        ipm = dsetup.ipm
        ifwe0 = dsetup.ifwe0

        #------------------------------------------------------------------
        # TRANSFER ACTUAL VALUES TO THE PROGNOSTIC VALUES THEMSELVES
        #------------------------------------------------------------------
        u = y[0]
        v = y[1]
        lon = y[2]
        lat = y[3]

        sf = np.sin(lat)
        cf = np.cos(lat)
        tf = np.tan(lat)

        #------------------------------------------------------------------
        # CALCULATE THE PRESSURE GRADIENT
        #------------------------------------------------------------------

        a = dconst.a
        p01 = dconst.p01
        p11 = dconst.p11
        angvel = dconst.angvel
        k = dconst.k

        dpdx = -(k*p11/a) * (np.sin(lat)**2) * np.cos(k*lon - angvel*t)
        # The sine at the end of the next line is commented out due to numerical inaccuracies
        # arising when we are close to the pole. When this term is exluded we get more physical
        # results than with the inclusion of the term.
        dpdy = -(p01/a)*np.sin(lat) - (p11/a)*(2*np.sin(lat)*(np.cos(lat)**2) - np.sin(lat)**3)#*np.sin(k*lon - angvel*t)

        # Alternate forms of the same expression as above. 
        # dpdy = -(p01/a)*np.sin(lat) - (p11/a)*np.sin(lat)*(2-3*(np.sin(lat)**2))*np.sin(k*lon - angvel*t)
        # dpdy = -(p01/a)*np.sin(lat) - (p11/a)*(np.sin(lat)*(3*(np.cos(lat)**2) -1))#*np.sin(k*lon - angvel*t)
        #------------------------------------------------------------------
        # CALCULATE THE RHS OF THE DIFFERENTIAL EQN
        #------------------------------------------------------------------

        k1 = dconst.k1
        k2 = dconst.k2
        om = dconst.om
        ro = dconst.ro
        fk = dconst.fk

        yp1 = k1*u*v*tf/a + 2*om*v*sf -dpdx/ro -fk*u
        yp2 = -k1*u*u*tf/a -2*om*u*sf - dpdy/ro - fk*v
        yp3 = u/(a*cf +1)
        #print(yp3)
        yp4 = v/a


        return np.array([yp1,yp2,yp3,yp4]).T



    ## Solving

    y = np.array([u0,v0,lon0*pi/180,lat0*pi/180]).T
    sol = solve_ivp(eqs_of_motion,[0,nS],y,t_eval = tspan,method = 'BDF')

    u = sol.y[0,:]
    v = sol.y[1,:]
    lon = sol.y[2,:]
    lat = sol.y[3,:]
    fig = plt.figure(1,figsize = [10,10])
    fig.canvas.set_window_title('Motion on a sphere: Plotresult')
    ax = fig.add_subplot(111)
    fig.suptitle(figname)
    fig.patch.set_visible(False)
    gen_plot(u,v,lon,lat,ax,dconst,plotpfield = True)
    ax.set_title(grpname,pad = 20)
    ax.axis('off')
    # plt.tight_layout()
    if save:
        fig.savefig(figname + '.png',transparent= False,facecolor = 'w',edgecolor = 'w')
    plt.show()
