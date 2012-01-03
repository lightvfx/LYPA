# -*- coding: utf-8 -*-
#   Lypa 001 beta main entry point by Antoine Moulineau
#  
#setups the whole interface and the connections between all the modules. Needs a seperate entry point
#QT is used for the Interface 
################################################################################

import os,sys,string
sys.path += ['.']
from PyQt4 import QtCore,QtGui
from Editors.FlipUI import Ui_MainWindow
import Editors.nukeSS as nukeSS
from Editors.GLviewport import *
from LYPA_Import import *

import model
import multiprocessing

#import sys


# Create a class for our main window


class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #super(Main, self).__init__()
        self.windowList = []
        ####### login##############################
        curUserName = os.getenv('USERNAME')
        model.setup_all()
        newUser = model.User.get_by(Name= unicode(curUserName))
        if newUser == None:
            newUser = model.User(Name= unicode(curUserName))
            model.saveData()
            
        ##################################################
        self.curProject = "none"
        self.full = 0
        self.toggleMe = 0
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('LYPA beta 101 :  ' + curUserName)
        self.GLviewer = GLWidget()
        self.ui.Dailies.setMainGUI(self)
        self.ui.Renders.setMainGUI(self)
        self.ui.Grade.setGL(self.GLviewer)
        self.ui.Renders.setGL(self.GLviewer)
        
        self.ui.GLLayout.addWidget(self.GLviewer)
        
        self.ui.tabWidget.setCurrentIndex(0)
        nukeSS.setStyleSheet(self)
        screen = QtGui.QDesktopWidget().screenGeometry()
        #self.ui.InfoWidget.styleSheet("background-color: rgb(60,60,60)")
        self.resize(screen.width(),screen.height() )
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
        #self.ui.TimeLineSlider.setRange(0, 20)
        self.ui.TimeLineSlider.setSingleStep(1)
        #self.ui.TimeLineSlider.setPageStep(15 * 16)
        self.ui.TimeLineSlider.setTickInterval(1)
        self.ui.TimeLineSlider.setTickPosition(1)
        self.curProjectLUT = 2.2
        self.connect(self.ui.LUTcomboBox, QtCore.SIGNAL('activated(QString)'), self.onLUTcomboBoxActivated)
        self.ui.TimeLineSlider.valueChanged.connect(self.GLviewer.setCurrentFrame)
        self.ui.TimeLineSlider.valueChanged.connect(self.ui.lcdNumber.display)
        self.GLviewer.currentFrameChanged.connect(self.ui.TimeLineSlider.setValue)
        self.GLviewer.currentFrameChanged.connect(self.ui.lcdNumber.display)
        self.GLviewer.ExpChanged.connect(self.set_infobarExp)
        self.GLviewer.colorSampleChanged.connect(self.set_infobarColor)
        self.ui.actionImport.triggered.connect(self.importFile)
        self.ui.ExpLabel.setText("Exp: 1.0")
        self.ui.Renders.setInfo(self.ui.Info)
        
        
    def set_infobarColor(self,color):
        self.ui.RLabel.setText("R: " + color['R'])
        self.ui.GLabel.setText("G: " + color['G'])
        self.ui.BLabel.setText("B: " + color['B'])
        
    def set_infobarExp(self,exp):
        self.ui.ExpLabel.setText("Exp: " + str(exp))
        
    def on_actionFull_Screen_toggled(self):
        if self.full == 0:
            self.showFullScreen()
            self.ui.ColorCorrect.hide()
            self.ui.ImageHub.hide()
            self.ui.InfoViewer.hide()
            self.ui.commenetBrowserDoc.hide()
            #self.ui.menubar.showMinimized()
            self.full = abs(self.full -1)
            return
        
        elif self.full == 1:
            self.showNormal()
            self.ui.ColorCorrect.show()
            self.ui.ImageHub.show()
            self.ui.InfoViewer.show()
            self.ui.commenetBrowserDoc.show()
            #self.ui.menubar.showNormal()
            self.full = abs(self.full -1)
            return
    
    def on_actionActual_Pixels_triggered(self):
            self.GLviewer.zCam = 2000.0
            self.GLviewer.xCam = 0.0
            self.GLviewer.yCam = 0.0
            self.GLviewer.update()
    
    def on_actionPlay_toggled(self):
        self.playGL()
    
    def on_actionNext_Frame_toggled(self):
        if self.GLviewer.frame == self.GLviewer.last:
            self.GLviewer.frame = self.GLviewer.first
            self.GLviewer.setCurrentFrame(self.GLviewer.frame)
            self.ui.TimeLineSlider.setValue(self.GLviewer.frame)
            self.ui.lcdNumber.display(self.GLviewer.frame)
        else :
            self.GLviewer.frame = self.GLviewer.frame + 1
            self.GLviewer.setCurrentFrame(self.GLviewer.frame)
            self.ui.TimeLineSlider.setValue(self.GLviewer.frame)
            self.ui.lcdNumber.display(self.GLviewer.frame)
    
    def on_actionPrevious_Frame_toggled(self):
        if self.GLviewer.frame == self.GLviewer.first:
            self.GLviewer.frame = self.GLviewer.last
        else:
            self.GLviewer.frame = self.GLviewer.frame - 1
            self.GLviewer.setCurrentFrame(self.GLviewer.frame)
            self.ui.TimeLineSlider.setValue(self.GLviewer.frame)
            self.ui.lcdNumber.display(self.GLviewer.frame)
    
    def importFile(self):
        if self.ui.Renders.SeqFilter != "all" and self.ui.Renders.ShotFilter != "all":
            self.importDialog = importDialog()
            self.importDialog.show()
            #sys.exit(self.importDialog.exec_())
            
    def onLUTcomboBoxActivated(self,text):
        if text == "Linear":
            print "Lut is:" + text
            self.GLviewer.setLUT(1.0)
        if text == "sRGB":
            print "Lut is:" + text
            self.GLviewer.setLUT(2.2)
        if text == "rec709":
            print "Lut is:" + text
            self.GLviewer.setLUT(1.8)
        if text == "Film":
            print "Lut is:" + text
            self.GLviewer.setLUT(1.9)
        if text == "Custom":
            print "Lut is:" + text
            self.GLviewer.setLUT(1.6)
        if text == "Project":
            print "Lut is:" + text
            self.GLviewer.setLUT(self.curProjectLUT)
            
    def playGL(self):
        
        if self.toggleMe == 0:
            print "Playing"
            self.ui.PlaypushButton.setText("Stop")
            self.ui.Renders.ui.refreshCombosPB.setStyleSheet("background-color: rgb(210,10,10);\n")
            self.ui.Renders.timer.stop()
            self.ui.Dailies.timer.stop()
            self.ui.Queue.timer.stop()
            self.GLviewer.startTimer()
            self.toggleMe = abs(self.toggleMe -1)
            return
        
        if self.toggleMe == 1:
            print "Stopped playback"
            self.ui.PlaypushButton.setText("Play")
            self.ui.Renders.ui.refreshCombosPB.setStyleSheet("background-color: rgb(85,85,85);\n")
            self.GLviewer.stopTimer()
            self.toggleMe = abs(self.toggleMe -1)
            self.ui.Renders.timer.start(3000)
            self.ui.Dailies.timer.start(8000)
            self.ui.Queue.timer.start(15000)
            return

        
if __name__ == "__main__":
    print "Starting LYPA beta. Version 001 by Antoine Moulineau."
    print "******************************************************"
    print ""
    multiprocessing.freeze_support()
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    sys.exit(app.exec_())
    
