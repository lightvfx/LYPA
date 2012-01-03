# -*- coding: utf-8 -*-

"""A custom widget that edits a task's properties"""

from PyQt4 import QtCore,QtGui
from colorCorrectUI import Ui_Form


class colorCorrect(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #############
        self.mountExpSL(self.ui.ExpSL,self.ui.ExpSB)
        self.ui.ExpSL.valueChanged.connect(self.setExpSB)
        self.ui.ExpSB.valueChanged.connect(self.setExpSL)
        ###############
        self.mountExpSL(self.ui.rExpSL,self.ui.rExpSB)
        self.ui.rExpSL.valueChanged.connect(self.setrExpSB)
        self.ui.rExpSB.valueChanged.connect(self.setrExpSL)
        ###############
        self.mountExpSL(self.ui.gExpSL,self.ui.gExpSB)
        self.ui.gExpSL.valueChanged.connect(self.setgExpSB)
        self.ui.gExpSB.valueChanged.connect(self.setgExpSL)
        
        ###############
        self.mountExpSL(self.ui.bExpSL,self.ui.bExpSB)
        self.ui.bExpSL.valueChanged.connect(self.setbExpSB)
        self.ui.bExpSB.valueChanged.connect(self.setbExpSL)
     
        #self.mountExpSL(self.ui.ExpSL,self.ui.ExpSB)
        #print "hellob lala"
        #
            
    def setGL(self,GL):
        print "ccGL"
        self.GL = GL
        self.ui.ExpSB.valueChanged.connect(self.GL.setExpSl)
        self.ui.rExpSB.valueChanged.connect(self.GL.setrExpSl)
        self.ui.gExpSB.valueChanged.connect(self.GL.setgExpSl)
        self.ui.bExpSB.valueChanged.connect(self.GL.setbExpSl)
        
    def mountExpSL(self,sl,sb):
        
        sl.setRange(0,10000)
        sl.setTickInterval(25)
        sl.setTickPosition(10)
        sl.setSingleStep(25)
        sb.setRange(0.0,1000.0)
        sb.setSingleStep(0.01)
        sl.setValue(1000)
        sb.setValue(10.0)
     
        
    def setExpSB(self,value):
        self.ui.ExpSB.setValue(value/100.0)
    def setExpSL(self,value):
        self.ui.ExpSL.setValue(value*100)
    def setrExpSB(self,value):
        print value
        self.ui.rExpSB.setValue(value/100.0)
    def setrExpSL(self,value):
        self.ui.rExpSL.setValue(value*100)
    def setgExpSB(self,value):
        self.ui.gExpSB.setValue(value/100.0)
    def setgExpSL(self,value):
        self.ui.gExpSL.setValue(value*100)
    def setbExpSB(self,value):
        self.ui.bExpSB.setValue(value/100.0)
    def setbExpSL(self,value):
        self.ui.bExpSL.setValue(value*100)
   

