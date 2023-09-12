from tkinter import *
from run_corlab_gui import run_corlab
from calc_geo import calc_geo
import matplotlib.pyplot as plt
plt.style.use('seaborn')
"""
################################################################################
All the code used in this lab is originally written by E. Holm, J. Jansson
and R.G. Graversen. The original package/script is written in matlab.
The code has been translated into python by Tuomas Heiskanen (spring 2019).
For questions email tuomas.i.heiskanen@uit.no
################################################################################

For user instructions see README.txt
"""

class Application(Frame):
    def say_hi(self):
        print( "hi there, everyone!")
    def corlab(self):
        self.set_inputs()
        run_corlab(p01 = self.p01,\
                        p11 = self.p11,\
                        c = self.c,\
                        k = self.k,\
                        lat0 = self.lat0,\
                        lon0 = self.lon0,\
                        u0 = self.u0,\
                        v0 = self.v0,\
                        usegeo = self.usegeo,\
                        curv = self.curv,\
                        fric = self.fric,\
                        nD = self.nD,\
                        nt =self.nt,\
                        figname = self.figname,\
                        grpname = self.grpname,\
                        fig = 'self.fig',\
                        ax = 'self.ax',\
                        save = self.save)
    def reset_var(self):
        self.p01 = 100   # hPa DEF = 100
        self.p11 = 0     # hPa DEF = 0
        self.c = 0       # m/s DEF = 0
        self.k = 3       # Wavenumber DEF = 3

        # Initial coordinates of air parcel

        self.lat0 = 50   # Latitude in degrees DEF = 50
        self.lon0 = 40   # Longitude in degrees DEF = 40

        # Initial wind velocities
        self.u0 = -8.3431    # Zonal wind component [m s^-1] DEF = -8.3431
        self.v0 = 0          # Meridional wind component [m s^-1]  DEF = 0

        # Specify geostrophic winds or not. This overrides u0 and v0 if set to True.
        self.usegeo = False  # Whether to use geostrophic winds or not. DEF = False

        # Whether or not to include curvature and friction
        self.curv = False # Curvature [BOOL] DEF = False
        self.fric = False # Friction [BOOL] DEF = False

        # Forecast length and number of steps
        self.nD = 3      # Forecast length in days
        self.nt = 100    # Number of iterations to perform

        # Figtitle
        self.figname = 'Figure 1'
        # Optional text on figure
        self.grpname = 'text on figure'

        self.save = False
        # self.fig = plt.figure(1,figsize = [10,10])
        # self.ax = self.fig.add_subplot(111)

        self.v0_entry.delete(0,END)
        self.u0_entry.delete(0,END)
        self.p01_entry.delete(0,END)
        self.p11_entry.delete(0,END)
        self.c_entry.delete(0,END)
        self.k_entry.delete(0,END)
        self.lat0_entry.delete(0,END)
        self.lon0_entry.delete(0,END)
        self.nD_entry.delete(0,END)
        self.nt_entry.delete(0,END)
        self.figname_entry.delete(0,END)
        self.grpname_entry.delete(0,END)

        self.v0_entry.insert(0,str(self.v0))
        self.u0_entry.insert(0,str(self.u0))
        self.p01_entry.insert(0,str(self.p01))
        self.p11_entry.insert(0,str(self.p11))
        self.c_entry.insert(0,str(self.c))
        self.k_entry.insert(0,str(self.k))
        self.lat0_entry.insert(0,str(self.lat0))
        self.lon0_entry.insert(0,str(self.lon0))
        self.nD_entry.insert(0,str(self.nD))
        self.nt_entry.insert(0,str(self.nt))
        self.figname_entry.insert(0,str(self.figname))
        self.grpname_entry.insert(0,str(self.grpname))

    def set_inputs(self):
        inputValue=self.v0_entry.get()
        self.v0 = float(inputValue)
        inputValue=self.u0_entry.get()
        self.u0 = float(inputValue)
        inputValue=self.p01_entry.get()
        self.p01 = float(inputValue)
        inputValue=self.p11_entry.get()
        self.p11 = float(inputValue)
        inputValue=self.c_entry.get()
        self.c = float(inputValue)
        inputValue=self.c_entry.get()
        self.c = float(inputValue)
        inputValue=self.k_entry.get()
        self.k = float(inputValue)
        inputValue=self.lat0_entry.get()
        self.lat0 = float(inputValue)
        inputValue=self.lon0_entry.get()
        self.lon0 = float(inputValue)
        inputValue=self.nD_entry.get()
        self.nD = float(inputValue)
        inputValue=self.nt_entry.get()
        self.nt = float(inputValue)

        inputValue=self.figname_entry.get()
        self.figname = inputValue
        inputValue=self.grpname_entry.get()
        self.grpname = inputValue


        inputValue = self.geovar.get()

        if inputValue == 1:
            self.usegeo = True

        else:
            self.usegeo = False


        inputValue = self.fricvar.get()

        if inputValue == 1:
            self.fric = True

        else:
            self.fric = False

        inputValue = self.curvar.get()

        if inputValue == 1:
            self.curv = True

        else:
            self.curv = False

        inputValue = self.savevar.get()

        if inputValue == 1:
            self.save = True

        else:
            self.save = False

    def createWidgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        # self.QUIT.pack({"side": "left"})
        self.QUIT.grid(row = 1)

        self.hi_there = Button(self)
        self.hi_there["text"] = "Run simulation"
        self.hi_there['fg'] = "blue"
        self.hi_there["command"] = self.corlab

        # self.hi_there.pack({"side": "left"})
        self.hi_there.grid(row = 1,column = 5)

        self.reset = Button(self)
        self.reset["text"] = "Reset parameters"
        self.reset["command"] = self.reset_var

        # self.reset.pack({"side": "left"})
        self.reset.grid(row = 1,column = 3)

        self.frametitle = Label(self)
        # self.frametitle['width'] = 50
        # self.frametitle['height'] = 20
        self.frametitle['font'] = ('Times',30)
        self.frametitle["text"] = "Motion on a Sphere"
        # self.frametitle['relief'] = "ridge"

        self.frametitle.grid(row = 0, column = 3)
        self.initial_velocity = Label(self)
        self.initial_velocity["text"] = "Initial velocity"
        self.initial_velocity.grid(row = 2,column = 1)

        self.v0_entry = Entry(self)
        self.v0_entry['text'] = 'v0'
        # self.v0_entry.pack({"side": "left"})
        self.v0_entry.grid(row = 3,column = 1)

        self.set_v0 = Label(self)
        self.set_v0["text"] = "v0 [m/s]"
        self.set_v0.grid(row = 3,column = 0)

        self.u0_entry = Entry(self)
        self.u0_entry['text'] = 'u0'
        self.u0_entry.grid(row = 4,column = 1)

        self.set_u0 = Label(self)
        self.set_u0["text"] = "u0 [m/s]"
        # self.set_u0["command"] = self.set_u0_input
        self.set_u0.grid(row = 4,column = 0)

        self.geovar = IntVar()
        self.geostrophic = Checkbutton(self,variable = self.geovar)

        self.geostrophic['text'] = "Geostrophic winds"
        self.geostrophic.grid(row = 3,column = 3)

        self.fricvar = IntVar()
        self.friction = Checkbutton(self,variable = self.fricvar)

        self.friction['text'] = "Friction"
        self.friction.grid(row = 4,column = 3)

        self.curvar = IntVar()
        self.curvature = Checkbutton(self,variable = self.curvar)

        self.curvature['text'] = "Curvature terms"
        self.curvature.grid(row = 5,column = 3)

        self.savevar = IntVar()
        self.savefig = Checkbutton(self,variable = self.savevar)

        self.savefig['text'] = "Save figure to png"
        self.savefig.grid(row = 6,column = 3)

        self.disclaimer = Label(self)
        self.disclaimer["text"] = "By E. Holm, J. Jansson and R.G. Graversen. \n Rewritten in python by T. Heiskanen."
        self.disclaimer['relief'] = "ridge"
        self.disclaimer.grid(row = 11,column = 3)


        self.press_params = Label(self)
        self.press_params["text"] = "Defining the pressurefield"
        self.press_params.grid(row = 5,column = 1)

        self.p01_entry = Entry(self)
        self.p01_entry.grid(row = 6,column = 1)
        self.set_p01 = Label(self)
        self.set_p01["text"] = "p01 [hPa]"
        self.set_p01.grid(row = 6,column = 0)

        self.p11_entry = Entry(self)
        self.p11_entry.grid(row = 7,column = 1)
        self.set_p11 = Label(self)
        self.set_p11["text"] = "p11 [hPa]"
        self.set_p11.grid(row = 7,column = 0)


        self.c_entry = Entry(self)
        self.c_entry.grid(row = 8,column = 1)
        self.set_c = Label(self)
        self.set_c["text"] = "c [m/s]"
        self.set_c.grid(row = 8,column = 0)

        self.k_entry = Entry(self)
        self.k_entry.grid(row = 9,column = 1)
        self.set_k = Label(self)
        self.set_k["text"] = "k [wavenumber]"
        self.set_k.grid(row = 9,column = 0)

        self.initial_pos = Label(self)
        self.initial_pos["text"] = "Initial position:"
        self.initial_pos.grid(row = 2,column = 5)


        self.lat0_entry = Entry(self)
        self.lat0_entry.grid(row = 3,column = 5)
        self.set_lat0 = Label(self)
        self.set_lat0["text"] = "lat0"
        self.set_lat0.grid(row = 3,column = 4)

        self.lon0_entry = Entry(self)
        self.lon0_entry.grid(row = 4,column = 5)
        self.set_lon0 = Label(self)
        self.set_lon0["text"] = "lon0"
        self.set_lon0.grid(row = 4,column = 4)

        self.simlength = Label(self)
        self.simlength["text"] = "Simulation length and iteration steps:"
        self.simlength.grid(row = 5,column = 5)

        self.nD_entry = Entry(self)
        self.nD_entry.grid(row = 6,column = 5)
        self.set_nD = Label(self)
        self.set_nD["text"] = "Days"
        self.set_nD.grid(row = 6,column = 4)

        self.nt_entry = Entry(self)
        self.nt_entry.grid(row = 7,column = 5)
        self.set_nt = Label(self)
        self.set_nt["text"] = "Timesteps"
        self.set_nt.grid(row = 7,column = 4)

        self.fignames = Label(self)
        self.fignames["text"] = "Text to add on figure:"
        self.fignames.grid(row = 8,column = 5)


        self.figname_entry = Entry(self)
        self.figname_entry.grid(row = 9,column = 5)
        self.set_figname = Label(self)
        self.set_figname["text"] = "Figure name"
        self.set_figname.grid(row = 9,column = 4)

        self.grpname_entry = Entry(self)
        self.grpname_entry.grid(row = 10,column = 5)
        self.set_grpname = Label(self)
        self.set_grpname["text"] = "Optional text"
        self.set_grpname.grid(row = 10,column = 4)



        # self.v0_entry["command"] = self.set_v0
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

        self.p01 = 100   # hPa DEF = 100
        self.p11 = 0     # hPa DEF = 0
        self.c = 0       # m/s DEF = 0
        self.k = 3       # Wavenumber DEF = 3

        # Initial coordinates of air parcel

        self.lat0 = 50   # Latitude in degrees DEF = 50
        self.lon0 = 40   # Longitude in degrees DEF = 40

        # Initial wind velocities
        self.u0 = -8.3431    # Zonal wind component [m s^-1] DEF = -8.3431
        self.v0 = 0          # Meridional wind component [m s^-1]  DEF = 0

        # Specify geostrophic winds or not. This overrides u0 and v0 if set to True.
        self.usegeo = False  # Whether to use geostrophic winds or not. DEF = False

        # Whether or not to include curvature and friction
        self.curv = False # Curvature [BOOL] DEF = False
        self.fric = False # Friction [BOOL] DEF = False

        # Forecast length and number of steps
        self.nD = 3      # Forecast length in days
        self.nt = 100    # Number of iterations to perform

        # Figtitle
        self.figname = 'Figure 1'
        # Optional text on figure
        self.grpname = 'text on figure'

        self.save = False
        # self.fig = plt.figure(1,figsize = [10,10])
        # self.ax = self.fig.add_subplot(111)

        self.v0_entry.insert(0,str(self.v0))
        self.u0_entry.insert(0,str(self.u0))
        self.p01_entry.insert(0,str(self.p01))
        self.p11_entry.insert(0,str(self.p11))
        self.c_entry.insert(0,str(self.c))
        self.k_entry.insert(0,str(self.k))
        self.lat0_entry.insert(0,str(self.lat0))
        self.lon0_entry.insert(0,str(self.lon0))
        self.nD_entry.insert(0,str(self.nD))
        self.nt_entry.insert(0,str(self.nt))
        self.figname_entry.insert(0,str(self.figname))
        self.grpname_entry.insert(0,str(self.grpname))


root = Tk()
root.title('Motion on a Sphere')
app = Application(master=root)
# app.configure(background = 'black')
app.mainloop()
root.destroy()
