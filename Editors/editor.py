# -*- coding: utf-8 -*-

"""A custom widget that edits a task's properties"""

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from editorUi import Ui_Form

# The backend
import model

# Misc.

class editor(QtGui.QWidget):
    def __init__(self,parent,task=None):
        QtGui.QWidget.__init__(self,parent)

        self.ui=Ui_Form()
        self.ui.setupUi(self)
        
        # Start with no task item to edit
        self.item=None

    def edit(self,item):
        """Takes an item, loads the widget with the item's
        task contents, shows the widget"""
        self.item=item
        self.ui.Shot_LineEdit.setText(self.item.task.Name)
        self.ui.CompInLineEdit.setText(self.item.task.In)
        self.ui.CompOutLineEdit.setText(self.item.task.Out)
        #self.ui.ShotLabel.setText(self.item.task.Name)
        
        
        self.show()
        #model.saveData()
        
    def save(self):
        if self.item==None: return
        
         
        #print(self.ui.task.text())
        # Display the data in the item
        self.item.setText(0,self.ui.Shot_LineEdit.text())
        self.item.setText(1,self.ui.CompInLineEdit.text())
        self.item.setText(2,self.ui.CompOutLineEdit.text())
        self.item.task.Name = str(self.ui.Shot_LineEdit.text())
        self.item.task.In = str(self.ui.CompInLineEdit.text())
        self.item.task.Out = str(self.ui.CompOutLineEdit.text())
        #self.item.task.In = str(self.ui.CutInLineEdit.text())
        #self.item.task.In = str(self.ui.CutOutLineEdit.text())
        #print self.ui.Shot_LineEdit.text()
        #model.saveData()
    def showInfo(self,trigger):
        print "trig:" + str(trigger)
        #self.ui.info.setEnabled(trigger)
        #self.ui=Ui_Form()
        #self.ui.setupUi(self)
        
        