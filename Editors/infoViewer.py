# -*- coding: utf-8 -*-
import time
import numpy
import sys
import sip
from PyQt4 import QtCore,QtGui
from infoViewerUI import Ui_Form
import model

class infoViewer(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.Name = ""
        self.labels = []
        
    def update(self,item): 
        self.ui.thumbnailLabel.setScaledContents(True)
        self.ui.thumbnailLabel.setPixmap(item.pixmap)
        self.Name = str(item.render.Name)
        self.clearLabels()
        nameLabel = QtGui.QLabel(self)
        nameLabel.setText(" Name: " + self.Name)
        nameLabel.setStyleSheet("background-color: rgb(252,87,94);\n color: rgb(10,10,10);\n ;border-radius: 2px;\n")
        self.ui.formLayout.addWidget(nameLabel)
        self.labels.append(nameLabel)
        #self.createLabel("Name",str(self.Name))
        self.createLabel("Shot",str(item.render.ShotName.Name))
        self.createLabel("Sequence",str(item.render.SeqName.Name))
        self.createLabel("Project",str(item.render.Project.Name))
        self.createLabel("User",str(item.render.User))
        self.createLabel("Date",str(item.render.Date))
        self.createLabel("Format",str(item.render.Format))
        self.createLabel("Path",str(item.render.Path))
        self.createLabel("ScenePath",str(item.render.ScenePath))

        for key in item.header.keys():
            newLabel = QtGui.QLabel(self)
            newLabel.setText(" " + key + ": " + str(item.header[key]))
            newLabel.setStyleSheet("background-color: rgb(100,160,200);\n color: rgb(10,10,10);\n ;border-radius: 2px;\n")
            self.ui.formLayout.addWidget(newLabel)
            self.labels.append(newLabel)
        #print key
        
    def createLabel(self,Key,Value):
        newLabel = QtGui.QLabel(self)
        newLabel.setText(" " + Key + ": " + Value)
        newLabel.setStyleSheet("background-color: rgb(195,197,78);\n color: rgb(10,10,10);\n ;border-radius: 2px;\n")
        self.ui.formLayout.addWidget(newLabel)
        self.labels.append(newLabel)
    
    def clearLabels(self):
        for wlabel in self.labels:      
            self.ui.verticalLayout.removeWidget(wlabel)
            sip.delete(wlabel)
            wlabel = None
            self.labels = []

if __name__ == "__main__":
    import sys
    model.setup_all()
    app = QtGui.QApplication(sys.argv)
    window= infoViewer()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())