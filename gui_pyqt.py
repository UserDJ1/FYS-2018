from run_corlab_gui import run_corlab
import matplotlib.pyplot as plt
from PyQt5.QtCore import QDateTime, Qt,QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        ##DEF VALUES
        self.p01 = 100   # hPa DEF = 100
        self.p11 = 0     # hPa DEF = 0
        self.c = 0       # m/s DEF = 0
        self.k = 3       # Wavenumber DEF = 3

        # Initial coordinates of air parcel

        self.lat0 = 50   # Latitude in degrees DEF = 50
        self.lon0 = 40   # Longitude in degrees DEF = 40

        # Initial wind velocities
        self.u0 = 8.3431    # Zonal wind component [m s^-1] DEF = -8.3431
        self.v0 = 0          # Meridional wind component [m s^-1]  DEF = 0

        # Specify geostrophic winds or not. This overrides u0 and v0 if set to True.
        self.geos = True  # Whether to use geostrophic winds or not. DEF = False

        # Whether or not to include curvature and friction
        self.curv = False # Curvature [BOOL] DEF = False
        self.fric = False # Friction [BOOL] DEF = False

        # Forecast length and number of steps
        self.nD = 3      # Forecast length in days
        self.nt = 100    # Number of iterations to perform

        # Figtitle
        self.figtitle = 'Figure 1'
        # Optional text on figure
        self.grptxt = ' '

        self.save = False

        self.originalPalette = QApplication.palette()

        styleComboBox = QComboBox()
        styleComboBox.addItems(QStyleFactory.keys())

        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createBottomLeftGroupBox()
        self.createBottomRightGroupBox()
        topLayout = QVBoxLayout()
        toptoplayout = QHBoxLayout()
        toptoplayout.addWidget(QLabel(''))

        txt = "Motion on a Sphere"
        ewfont = QFont("Times", 20, QFont.Bold)
        title = QLabel('Motion on a Sphere')
        title.setFont(ewfont)
        toptoplayout.addWidget(title)

        toptoplayout.addWidget(QLabel(''))


        topLayout_part = QHBoxLayout()
        run_lab = QPushButton('Run simulation')
        run_lab.setStyleSheet('color: blue')
        run_lab.clicked.connect(self.GO)

        reset_lab = QPushButton('Reset parameters')
        reset_lab.clicked.connect(self.reset_params)
        reset_lab.setStyleSheet('color: red')


        topLayout_part.addWidget(run_lab)
        topLayout.addLayout(toptoplayout)
        topLayout.addLayout(topLayout_part)
        txt = "Motion on a Sphere"
        ewfont = QFont("Times", 8, QFont.Bold)
        title = QLabel('')
        title.setFont(ewfont)
        topLayout_part.addWidget(title)
        topLayout_part.addWidget(reset_lab)
        #
        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 2)
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.bottomLeftGroupBox, 2, 0)
        mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
        dsc = 'By E. Holm, J. Jansson and R.G. Graversen. \nRewritten in python by T. Heiskanen (2019).'
        disclaimer = QLabel(dsc)
        dfont  = QFont("Times", 10, italic = True)
        disclaimer.setFont(dfont)
        mainLayout.addWidget(disclaimer, 3, 0, 1, 2)
        self.setLayout(mainLayout)

        self.setWindowTitle("Motion on a Sphere")
        self.changeStyle('Fusion')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()
    def changePalette(self):
        QApplication.setPalette(self.originalPalette)
    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Initial velocity and position")
        labelu0 = QLabel('u0 [m/s]')
        self.u0_te = QLineEdit(str(self.u0))
        labelv0 = QLabel('v0 [m/s]')
        self.v0_te = QLineEdit(str(self.v0))
        labellon0 = QLabel('lon0')
        self.lon0_te = QLineEdit(str(self.lon0))
        labellat0 = QLabel('lat0')
        self.lat0_te = QLineEdit(str(self.lat0))


        layout = QVBoxLayout()

        hl1 = QHBoxLayout()
        hl1.addWidget(labelu0)
        hl1.addWidget(self.u0_te)

        hl2 = QHBoxLayout()
        hl2.addWidget(labelv0)
        hl2.addWidget(self.v0_te)

        hl3 = QHBoxLayout()
        hl3.addWidget(labellon0)
        hl3.addWidget(self.lon0_te)

        hl4 = QHBoxLayout()
        hl4.addWidget(labellat0)
        hl4.addWidget(self.lat0_te)


        layout.addLayout(hl1)
        layout.addLayout(hl2)
        layout.addLayout(hl3)
        layout.addLayout(hl4)

        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Defining pressurefield")
        labelp01 = QLabel('p01 [hPa]')
        self.p01_te = QLineEdit(str(self.p01))
        labelp11 = QLabel('p11 [hPa]')
        self.p11_te = QLineEdit(str(self.p11))
        labelc = QLabel('c [m/s]')
        self.c_te = QLineEdit(str(self.c))
        labelk = QLabel('k [Wavenumber]')
        self.k_te = QLineEdit(str(self.k))

        button = QPushButton('GO!')
        button.clicked.connect(self.GO)
        layout = QVBoxLayout()

        hl1 = QHBoxLayout()
        hl1.addWidget(labelp01)
        hl1.addWidget(self.p01_te)

        hl2 = QHBoxLayout()
        hl2.addWidget(labelp11)
        hl2.addWidget(self.p11_te)

        hl3 = QHBoxLayout()
        hl3.addWidget(labelc)
        hl3.addWidget(self.c_te)

        hl4 = QHBoxLayout()
        hl4.addWidget(labelk)
        hl4.addWidget(self.k_te)


        layout.addLayout(hl1)
        layout.addLayout(hl2)
        layout.addLayout(hl3)
        layout.addLayout(hl4)

        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    def createBottomLeftGroupBox(self):
        self.bottomLeftGroupBox = QGroupBox("Checkboxes")

        self.geo_box = QCheckBox("Use geostrophic winds")
        self.geo_box.setChecked(self.geos)
        self.curv_box = QCheckBox("Include curvature terms")
        self.fric_box = QCheckBox("Include friction")


        layout = QVBoxLayout()
        layout.addWidget(self.geo_box)
        layout.addWidget(self.curv_box)
        layout.addWidget(self.fric_box)
        layout.addStretch(1)
        self.bottomLeftGroupBox.setLayout(layout)

    def createBottomRightGroupBox(self):
        self.bottomRightGroupBox = QGroupBox("Figure parameters and simulation length")
        labelnD = QLabel("Integration time in days")
        self.nD_te = QLineEdit(str(self.nD))

        labelnt = QLabel('Number of timesteps')
        self.nt_te = QLineEdit(str(self.nt))


        labelfigtitle = QLabel('Figure title')
        self.figtitle_te = QLineEdit(str(self.figtitle))
        labelgrptxt = QLabel('Optional text on figure')
        self.grptxt_te = QLineEdit(str(self.grptxt))
        # self.geo_box = QCheckBox("Use geostrophic winds")
        # self.curv_box = QCheckBox("Include curvature terms")
        self.save_box = QCheckBox("Save to png")


        # checkBox = QCheckBox("Tri-state check box")
        # checkBox.setTristate(True)
        # checkBox.setCheckState(Qt.PartiallyChecked)
        layout = QVBoxLayout()

        hl1 = QHBoxLayout()
        hl1.addWidget(labelfigtitle)
        hl1.addWidget(self.figtitle_te)

        hl2 = QHBoxLayout()
        hl2.addWidget(labelgrptxt)
        hl2.addWidget(self.grptxt_te)

        hl3 = QHBoxLayout()
        hl3.addWidget(labelnD)
        hl3.addWidget(self.nD_te)

        hl4 = QHBoxLayout()
        hl4.addWidget(labelnt)
        hl4.addWidget(self.nt_te)

        layout.addLayout(hl1)
        layout.addLayout(hl2)
        layout.addWidget(self.save_box)
        layout.addLayout(hl3)
        layout.addLayout(hl4)

        layout.addStretch(1)
        self.bottomRightGroupBox.setLayout(layout)

    def reset_params(self):
        self.p01 = 100   # hPa DEF = 100
        self.p11 = 0     # hPa DEF = 0
        self.c = 0       # m/s DEF = 0
        self.k = 3       # Wavenumber DEF = 3

        # Initial coordinates of air parcel

        self.lat0 = 50   # Latitude in degrees DEF = 50
        self.lon0 = 40   # Longitude in degrees DEF = 40

        # Initial wind velocities
        self.u0 = 8.3431    # Zonal wind component [m s^-1] DEF = -8.3431
        self.v0 = 0          # Meridional wind component [m s^-1]  DEF = 0

        # Specify geostrophic winds or not. This overrides u0 and v0 if set to True.
        self.geos = True  # Whether to use geostrophic winds or not. DEF = False

        # Whether or not to include curvature and friction
        self.curv = False # Curvature [BOOL] DEF = False
        self.fric = False # Friction [BOOL] DEF = False

        # Forecast length and number of steps
        self.nD = 3      # Forecast length in days
        self.nt = 100    # Number of iterations to perform

        # Figtitle
        self.figtitle = 'Figure 1'
        # Optional text on figure
        self.grptxt = ' '
        self.save = False

        self.u0_te.setText(str(self.u0))
        self.v0_te.setText(str(self.v0))
        self.lon0_te.setText(str(self.lon0))
        self.lat0_te.setText(str(self.lat0))

        self.p01_te.setText(str(self.p01))
        self.p11_te.setText(str(self.p11))
        self.c_te.setText(str(self.c))
        self.k_te.setText(str(self.k))

        self.nD_te.setText(str(self.nD))
        self.nt_te.setText(str(self.nt))

        self.figtitle_te.setText(self.figtitle)
        self.grptxt_te.setText(self.grptxt)

        self.fric_box.setChecked(self.fric)
        self.curv_box.setChecked(self.curv)
        self.save_box.setChecked(self.save)
        self.geo_box.setChecked(self.geos)

    def GO(self):
        self.set_params()
        plt.close()
        run_corlab(p01 = self.p01,\
                        p11 = self.p11,\
                        c = self.c,\
                        k = self.k,\
                        lat0 = self.lat0,\
                        lon0 = self.lon0,\
                        u0 = self.u0,\
                        v0 = self.v0,\
                        usegeo = self.geos,\
                        curv = self.curv,\
                        fric = self.fric,\
                        nD = self.nD,\
                        nt =self.nt,\
                        figname = self.figtitle,\
                        grpname = self.grptxt,\
                        fig = 'self.fig',\
                        ax = 'self.ax',\
                        save = self.save)

    def set_params(self):
        self.u0 = float(self.u0_te.text())
        self.v0 = float(self.v0_te.text())
        self.lon0 = float(self.lon0_te.text())
        self.lat0 = float(self.lat0_te.text())

        self.p01 = float(self.p01_te.text())
        self.p11 = float(self.p11_te.text())
        self.c = float(self.c_te.text())
        self.k = float(self.k_te.text())

        self.nD = float(self.nD_te.text())
        self.nt = float(self.nt_te.text())

        self.figtitle = self.figtitle_te.text()
        self.grptxt = self.grptxt_te.text()

        self.fric = bool(self.fric_box.checkState())
        self.curv = bool(self.curv_box.checkState())
        self.save = bool(self.save_box.checkState())
        self.geos = bool(self.geo_box.checkState())

    # def closeEvent(self, event):
    #     ret = QMessageBox.question(None, 'Close request', 'Are you sure you want to quit?',
    #                                      QMessageBox.Yes | QMessageBox.No,
    #                                      QMessageBox.Yes)
    #     if ret == QMessageBox.Yes:
    #         plt.close()
    #         QMainWindow.closeEvent(self, event)
    #     else:
    #         event.ignore()
    def closeEvent(self, event):
        plt.close()
        QMainWindow.closeEvent(self, event)
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    gallery = WidgetGallery()
    gallery.show()
    sys.exit(app.exec_())
