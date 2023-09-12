import numpy as np
import matplotlib.pyplot as plt
import scipy.io
from sph2cart_lc import sph2cart_lc
from math import pi
from numpy.matlib import repmat

"""
################################################################################
All the code used in this lab is originally written by E. Holm, J. Jansson
and R.G. Graversen. The original package/script is written in matlab.
The code has been translated into python by Tuomas Heiskanen (spring 2019).
For questions email tuomas.i.heiskanen@uit.no
################################################################################

For user instructions see README.txt
"""


def gen_plot(u,v,lon,lat,ax,dconst,plotcoast = True, plotpfield = True, plotlatlong = True, Nlevs = 10):
    """
    Method for generating similar plots as produced by the matlab code.
    Plots on given axis.
    """
    #Plot coastlines
    ax.clear()
    if plotcoast:
        coast_lines = scipy.io.loadmat('coast_lines.mat')
        coastline_x = coast_lines['coastline_x']
        coastline_y = coast_lines['coastline_y']
        x_co,y_co,z_co = sph2cart_lc(coastline_y*pi/180,coastline_x*pi/180)
        mask = z_co >= 0
        ax.plot(x_co[mask],y_co[mask],color ='darkgreen',marker = '.',linewidth = 0,markersize = 4)

        # Adding information
        xmax = np.nanmax(x_co)
        ymax = np.nanmax(y_co)
        offset = -1.5e6
        if dconst.geostrophic:
            tx = '(geostrophic winds)'
        else:
            tx = '(non-geostrophic winds)'
        txt = 'Initial values:\n u0 = ' + str(np.round(dconst.u0,2)) +' m/s \n v0 = ' + str(np.round(dconst.v0,2)) + ' m/s \n '+tx +'\n lat0 = ' +\
                str(dconst.lat0) + r"$^\circ$N" +" \n lon0 = " +  str(dconst.lon0) + r"$^\circ$E"
        ax.text(xmax + offset, 9*ymax/10,txt)
        if dconst.curv:
            tx = 'on'
        else:
            tx = 'off'
        txt = ' p01 = ' + str(dconst.p01/100) + ' hPa \n p11 = ' + str(dconst.p11/100) + ' hPa \n Friction = ' + str(dconst.fk) + r' s$^{-1}$' + '\n Curvature = ' +tx
        ax.text(-xmax + offset, 9*ymax/10,txt)
        ax.plot(-xmax + 250000 , 6*ymax/10,marker = 'X',color = 'blue')
        ax.text(-xmax + offset , 5.9*ymax/10,'Starting point: ')
    # Plotting lat lon grid
    if plotlatlong:
        plat = [0,20,40,60,80]
        plon = [0,45,90,135,180,-45,-90,-135]
        for pl in range(len(plat)):
            lo = np.linspace(0,360,361)[::6]*pi/180
            la = (plat[pl]*pi/180)*np.ones(len(lo))
            x_pl,y_pl,z_pl = sph2cart_lc(la,lo)
            ax.plot(x_pl,y_pl,'gray',linestyle = '--')

            if plat[pl] != 0:
                i = np.argmin(np.abs(z_pl))
                ax.text(x_pl[i],y_pl[i], str((plat[pl])) + r"$^\circ$N", horizontalalignment = 'center',fontsize = 10)
        for pl in range(len(plon)):
            la = np.array(plat)[::int((max(plat) - min(plat))/50)]*pi/180
            lo = plon[pl]*np.ones(len(la))*pi/180
            x_pl,y_pl,z_pl = sph2cart_lc(la,lo)
            ax.plot(x_pl,y_pl,'gray',linestyle = '--')
            if pl != 360:
                i = np.argmin(np.abs(z_pl))
                ax.text(x_pl[i],y_pl[i], str((plon[pl])) + r"$^\circ$", horizontalalignment = 'center',fontsize = 10)

    # Calculate p-field
    if plotpfield:
        lon_p = np.linspace(0,360,361)[::5]*pi/180
        lat_p = np.linspace(0,90,91)[::5]*pi/180
        lon_p = repmat(lon_p,len(lat_p),1)
        lat_p = repmat(lat_p,lon_p.shape[1],1).T
        x_p,y_p,z_p = sph2cart_lc(lat_p,lon_p)

        p00 = 960e2
        t=0
        alfa = 0
        pfield = p00 + dconst.p01*np.cos(lat_p) - dconst.p11*np.cos(lat_p)*(np.sin(lat_p)**2)*np.sin(dconst.k*lon_p - dconst.angvel*t + alfa)
        #print(pfield)
        CS = plt.contour(x_p,y_p,pfield*1e-2,levels = Nlevs,colors = 'mediumturquoise')
        ax.clabel(CS, np.round(CS.levels,0), inline=True, fmt = '%r hPa', fontsize=10)
    # Calculate cartesian trajetory for air-parcel
    x_c,y_c,z_c = sph2cart_lc(lat,lon)
    mask1 = z_c >0
    mask2 = z_c <=0
    ax.plot(x_c[mask1],y_c[mask1],color = 'red',linestyle = '--',marker = '.',linewidth = 0)
    ax.plot(x_c[mask2],y_c[mask2],color = 'magenta',linestyle = '--',marker = '.',linewidth = 0)
    ax.plot(x_c[0],y_c[0],marker = 'X',color = 'blue')
    ax.plot(x_c[-1],y_c[-1],marker = 'X',color = 'limegreen')



if __name__ == '__main__':
    lon_p = np.linspace(0,360,361)[::5]*pi/180
    lat_p = np.linspace(0,90,91)[::5]*pi/180
    lon_p = repmat(lon_p,len(lat_p),1)
    lat_p = repmat(lat_p,lon_p.shape[1],1).T
    x_p,y_p,z_p = sph2cart_lc(lat_p,lon_p)
