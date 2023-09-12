################################################################################
All the code used in this lab is originally written by E. Holm, J. Jansson
and R.G. Graversen. The original package/script is written in matlab.
The code has been translated into python by Tuomas Heiskanen (spring 2019).
For questions email tuomas.i.heiskanen@uit.no
################################################################################

-------------------------------------------------------------------------------------------
2023 Update by Kai-Uwe Eiselt:
------------------------------

I suggest creating and using a new conda environment for this lab and then running
the script "gui_pygt.py". The following conda command creates the environment "lab2"
in which the gui_pyqt.py script should run:

>>> conda create -n lab2 cycler=0.10.0 kiwisolver=1.0.1 matplotlib=3.0.2 numpy=1.16.0 pyparsing=2.3.1 scipy=1.2.0 six=1.12.0 pyqt spyder

Then activate the conda environment via:
>>> conda activate lab2

and run the script via:
>>> python gui_pyqt.py

This should open the GUI (Graphical User Interface) of the model we want to run in this lab.

This has been tested on Windows and Linux systems but should work on Apple systems as well.

For questions on this procedure contact kai-uwe.eiselt@uit.no; a fail-safe method is to run the model
without the GUI. This can be done by directly running the model in the console via
>>> python run_corlab.py

To adjust the parameters open this script (run_corlab.py) in a text editor.


--------------------------------------------------------------------------------------------
Pre-2023 Version:
-----------------

Instructions for the usage of the python3 version of corlab.

SHORT GUIDE (the bare minimum you need know to run the scripts):
-- Install the packages in requirements.txt.
    (e.g. run "pip install -r requirements.txt" in the folder containing
    requirements.txt)
-- run gui_pyqt.py in you favorite python3 interpreter.
    (e.g. run "python3 gui_pyqt.py")

LONG GUIDE:

The code is provided with three user-interfaces. One is based on a GUI
made with tkinter. one on a GUI made with pyqt and the last on is
based on changing parameter values in "run_corlab.py".

The recommended way is to use the GUI based on PyQt.

Method 1 -- GUI tkinter:

To run the simulations through the GUI you have to run the script
"gui_tkinter.py" (e.g. python3 gui_tkinter.py ). This requires that your python3
installation has tkinter installed. Most python3 distributions have this module
as a default component of the installation. If yours does not have this you
have to install it, search the web for a guide on how to do it on your preferred
OS. In addition to the tkinter module you need the modules specified in
"requirements.txt". If you have installed the modules for lab1 in FYS-2018
(given spring 2019) you should have all the required modules installed.

Specifying parameters:
-- Fill in the values in the text-boxes of the GUI.
-- Check the wished option boxes. If checked the option is set to ON, if not
   it is OFF.

Running the simulation:
-- Press "Run simulation" to run the simulation. Parameters are read from
   the text boxes after the "Run simulation" button is pressed.
-- Running a second simulation will write over the previous run.

Resetting parameters:
-- Press "Reset parameters" to reset all parameters except the check-boxes,
   these you have to reset manually (due to the laziness of the developer).
   The default value of the check-boxes is unchecked.

Exit:
-- Press Exit to quit the program. This will close all windows and
   reset all parameters.

Remarks:
-- Checking Geostrophic winds will override your specified initial velocity.
   The winds will be calculated based on the initial position and pressure
   field.
-- Checking "Save figure to png" will save the figure to a .png file in the
   current working directory. The name of the file will be set by
   the figure title parameter.
-- The blue cross in the plots marks the initial position of the air parcel.
   The green cross marks the final position of the air parcel.

Method 2 -- GUI PyQt:

To run the simulations from the PyQt gui you have to run the script
"gui_pyqt.py" . The functionality of the gui is similar to the tkinter
based gui. The PyQt gui will always close the existing plots before
generating new plots. It will also close plots as you quit the program.
The pyqt gui is based on a more modern gui package, and should work
better than the tkinter gui on most systems. This is especially true
if you are running an anaconda-python distribution, as these will not
necessarily have access to the fonts determined by the OS.

Method 3 -- Parameter values in script:

The parameters that are to be changed are specified in "run_corlab.py". To run
the simulation you have to run "run_corlab.py" (e.g. python3 run_corlab.py).
The default values are commented close to the parameters in "run_corlab.py"

All remarks in Method 1 are valid for method 2.


######
Code structure:
The simulation is based on solving the equations of motion on a rotating
sphere. The equations of motion are simplified to the first order, and then
solved by applying an IVP solver from the scipy package. All of this is done
in run_corlab.py/run_gui_tkinter.py. This is also where the plotting routines are
called.

The visualizations are plotted on a cartesian grid, and thus the results of the
simulation has to be translated into cartesian coordinates. This is done by
invoking the method in "sph2cart_lc.py". The coast lines are read from
the file "coast_lines.mat". Both coastlines for the northern and southern
hemisphere are included in the file, but we plot only the northern hemisphere.
The visualizations follow the buildup of the original package closely.
For visualizations of geodata, like we are using here, on the earth there
exists several packages in python. The plots could have been generated easier,
and made more stylish, by applying the Cartopy or Basemap packages.
It was chosen not to do this since the the installation of these packages
can be somewhat challenging. If you want to change the visualizations of the
results you are free to do so. You can either edit the "gen_plot" method
specified in "make_plots.py", or make your own "gen_plot" method and change it
with the original.

The geostrophic winds are calculated for given initial conditions in the
method provided in "calc_geo.py". This is called if we specify that the
winds should be geostrophic initially.

The file "struct_array.py" contains a Class specified to hold the required
variables for this simulation.

The GUIs are defined by the code in "gui_tkinter.py" and "gui_pyqt.py".
This is based on the tkinter and PyQt5 modules. The developer of this python
code has limited experience in the programming of GUIs, and this is shown in
the structure of the code. It is not expected that you should be able to read
the code in these files.
