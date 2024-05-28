from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from PyQt5 import QtGui, QtCore
 

import sys

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from functions import*

#  import the gui :
gui_py = True

if gui_py == True :
    from gui import Ui_Form  as ui
else:
    ui, _ = loadUiType('gui.ui')

class MainWindow(QWidget, ui):

    def __init__(self):
        QWidget.__init__(self)
        #self.setWindowIcon(QtGui.QIcon('logo.jpg')) choose logo from the designer
        self.setupUi(self)
        # desactivate buttons
        #self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        #self.setWindowFlag(QtCore.Qt.WindowMinimizeButtonHint, False)
        self.setWindowFlag(QtCore.Qt.WindowMaximizeButtonHint, False)
        # First empty plot
        self.plot_layout()
        # function to setup buttons
        self.HandleButtons()
        
        
    def HandleButtons(self):
        self.clickHere_pushButton.clicked.connect(self.essential_values)
        self.clickHere_pushButton.clicked.connect(self.plot)

    def plot_layout(self):
        self.fig = plt.figure(facecolor='#a5a6a5')
        self.canvas = FigureCanvas(self.fig)
        toolbar = NavigationToolbar(self.canvas, self)
        self.plottingSpace_verticalLayout.addWidget(toolbar)
        self.plottingSpace_verticalLayout.addWidget(self.canvas)

    def plot(self):
        self.fig.clear()
        ax = self.fig.add_subplot(111, facecolor='white')
        ax.set_aspect('equal')

        hexagon = RegularPolygon((0,0), numVertices=6, radius=self.GK,ls='-', alpha=.7, edgecolor='k')
        t2 = mpl.transforms.Affine2D().rotate_deg(30) + ax.transData
        t3 = mpl.transforms.Affine2D().rotate_deg(45) + ax.transData
        hexagon.set_transform(t2)     

        w = self.kx_slit
        l = self.ky_tilt + self.theta_slit_integration

        

        Rectangle1 = plt.Rectangle((self.slit_offset,self.tilt_offset), w, l, angle=self.phi,ls='--', facecolor = 'yellow', alpha=0.4, edgecolor='k')
        Rectangle2 = plt.Rectangle((self.slit_offset,self.tilt_offset), w, -l, angle=self.phi,ls='--', facecolor = 'yellow', alpha=0.4, edgecolor='k')
        Rectangle3 = plt.Rectangle((self.slit_offset,self.tilt_offset), -w, l, angle=self.phi,ls='--', facecolor = 'yellow', alpha=0.4, edgecolor='k')
        Rectangle4 = plt.Rectangle((self.slit_offset,self.tilt_offset), -w, -l, angle=self.phi,ls='--', facecolor = 'yellow', alpha=0.4, edgecolor='k')

        # line1 = plt.Line2D((0,0),(self.GK,0),ls='--',lw=1,color = 'blue')
        # line2 = plt.Line2D((0,0),(0,self.GM),ls='--',lw=1,color = 'blue')

        ax.add_patch(hexagon)
        ax.add_patch(Rectangle1)
        ax.add_patch(Rectangle2)
        ax.add_patch(Rectangle3)
        ax.add_patch(Rectangle4)

        ax.hlines(0, 0, self.GK, colors='b', lw = 3, linestyles='--')
        ax.vlines(0, 0, self.GM, colors='b', lw = 3,linestyles='--')
       
        # ax.add_line(line1)
        # ax.add_line(line2)

        ax.set_xlim(0,10)
        ax.set_ylim(0,3)

        ax.set_xlabel("$k_{x}$ ($\AA^{-1}$)")
        ax.set_ylabel("$k_{y}$ ($\AA^{-1}$)")

        #plt.axis('scaled')
        plt.autoscale(enable = True)
        #plt.axis("off")
        

        self.fig.tight_layout()
        self.canvas.draw()
       

                

    
    def essential_values(self):
        # Global Varilables
        self.a0 = 0 ; self.E = 0 ; self.theta_slit = 0 ; self.theta_tilt = 0 ;  self.slit_offset = 0 ; self.tilt_offset = 0 ; self.theta_slit_integration = 0 ; self.kx_slit = 0 ; self.ky_tilt = 0 ; self.phi = 0; self.GK = 0 ; self.GM = 0 ; self.KM = 0 ; self.theta_GK = 0 ; self.theta_GM = 0

        self.a0 = float(self.get_a0())
        self.E = float(self.get_E())
        self.theta_slit = float(self.get_theta_slit())
        self.theta_tilt = float(self.get_theta_tilt())
        self.slit_offset = float(self.get_slit_offset())
        self.tilt_offset = float(self.get_tilt_offset())
        self.theta_slit_integration = float(self.get_theta_slit_integration())
        self.slit_offset = theta2k(self.E,self.slit_offset)
        self.tilt_offset = theta2k(self.E,self.tilt_offset)
        self.theta_slit_integration = theta2k(self.E,self.theta_slit_integration)
        self.phi = float(self.get_phi())
        
        self.kx_slit = theta2k(self.E,self.theta_slit)
        self.ky_tilt = theta2k(self.E,self.theta_tilt)
        self.GK =  (4/3)*(np.pi/self.a0)   
        self.GM = (2*np.pi)/(np.sqrt(3)*self.a0)
        self.KM = (2*np.pi)/(np.sqrt(3)*self.a0)*1E10
        Ejoule = self.E*1.6E-19
        # self.theta_GK = np.arcsin((self.KM/np.sqrt(Ejoule))*(self.hbar/np.sqrt(2*self.m)))
        # self.theta_GM = np.arcsin((self.KM/np.sqrt(Ejoule))*(self.hbar/np.sqrt(2*self.m)))
        self.theta_GK = k2theta(self.E,self.GK)
        self.theta_GM = k2theta(self.E,self.GM)
        #self.theta_GK = np.rad2deg(self.theta_GK)
        #self.theta_GM = np.rad2deg(self.theta_GM)
        print('a0 = '+ str(self.a0) +'\n' + 'E = '+ str(self.E) +'\n' + 'GK = '+ str(self.GK) +'\n' + 'GM = '+ str(self.GM) +'\n' +  
         'KM = '+ str(self.KM) +'\n' + 'theta_GK = '+ str(self.theta_GK) +'°'+'\n' + 'theta_GM = ' + str(self.theta_GM)+'°')
        print('k slit : ',self.kx_slit)
        print('ky tilt :', self.ky_tilt)
        

    def get_a0(self):
        a0 = self.a0_lineEdit.text()
        return a0

    def get_E(self):
        E = self.E_lineEdit.text()
        return E
    
    def get_theta_slit(self):
        theta_slit = self.theta_slit_lineEdit.text()
        return theta_slit

    def get_theta_tilt(self):
        theta_tilt = self.theta_tilt_lineEdit.text()
        return theta_tilt

    def get_phi(self):
        phi = self.E_lineEdit_Phi.text()
        return phi

    def get_slit_offset(self):
        slit_offset = self.theta_slit_offset_lineEdit.text()
        return slit_offset

    def get_tilt_offset(self):
        tilt_offset = self.theta_tilt_offset_lineEdit.text()
        return tilt_offset

    def get_theta_slit_integration(self):
        theta_slit_integration = self.theta_slit_integration_lineEdit.text()
        return theta_slit_integration



        

'''
    def plotting(self):
        plt.rcParams['figure.figsize'] = [8, 5]
        fig,ax = plt.subplots(1)
        ax.set_aspect('equal')

        hexagon = RegularPolygon((0,0), numVertices=6, radius=self.GK,ls='-', alpha=1, edgecolor='k')
        #hexagon2 = RegularPolygon((0,0), numVertices=4, radius=.2,ls='-', alpha=.3, edgecolor='k')
    
        t2 = mpl.transforms.Affine2D().rotate_deg(30) + ax.transData
        t3 = mpl.transforms.Affine2D().rotate_deg(45) + ax.transData
        hexagon.set_transform(t2)

        k1_cord = (-1,0)
        k2_cord = (1,0)
        M1_cord = (0,-.87)
        M2_cord = (0,.87)       

        l = self.kx_slit
        w = self.kx_slit

        Rectangle1 = plt.Rectangle((0,0), w, l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')
        Rectangle2 = plt.Rectangle((0,0), w, -l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')
        Rectangle3 = plt.Rectangle((0,0), -w, l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')
        Rectangle4 = plt.Rectangle((0,0), -w, -l, angle=0,ls='--', facecolor = 'yellow', alpha=0.2, edgecolor='k')

        line1 = plt.Line2D((k1_cord[0],k2_cord[0]),(k1_cord[1],k2_cord[1]),ls='--',lw=2,color = 'blue')
        line2 = plt.Line2D((M1_cord[0],M2_cord[0]),(M1_cord[1],M2_cord[1]),ls='--',lw=2,color = 'blue')

        ax.add_patch(hexagon)
        ax.add_patch(Rectangle1)
        ax.add_patch(Rectangle2)
        ax.add_patch(Rectangle3)
        ax.add_patch(Rectangle4)
        #ax.add_patch(hexagon2)
        ax.add_line(line1)
        ax.add_line(line2)

        ax.set_xlim(0,10)
        ax.set_ylim(0,3)

        #plt.axis('scaled')
        plt.autoscale(enable = True)
        #plt.axis("off")
        

        fig.tight_layout()
        plt.show()

'''               


            
                
                



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    # hold ui
    app.exec_()

if __name__ == "__main__" :
    main()



