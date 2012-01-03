# -*- coding: utf-8 -*-

"""A custom widget that edits a task's properties"""

# Import Qt modules
from PyQt4 import QtCore,QtGui
from Farm import LYPA_renderNodeUI, modo601Job

#import modoJob
import os,sys
import model
#global app
# Misc.

class RN_window(QtGui.QMainWindow):
    def __init__(self,computerName,Node):
        QtGui.QMainWindow.__init__(self)
   
        self.computerName = computerName
        self.Node = Node
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.startNode)
        self.timer.start(5000)
        self.labelText = "waiting...."
        #self.app = app
        self.ui=LYPA_renderNodeUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LYPA_renderNode alpha 101   " + self.computerName, None, QtGui.QApplication.UnicodeUTF8))
      
        
    def startNode(self):
        # Init the database before doing anything else
        n = self.Node
        model.setup_all()
        #print "hey"
        for task in model.Task.query.all():
            #print task.done
            if task.Status == 101:
                self.labelText = "rendering: " + task.Name
                self.refreshMe()
                
            if task.Status == 101:
                task.Status = 0
                
                #print n
                n.Tasks.append(task)
                model.saveData()
                
                taskFile = task.Command.split(" -taskFile ")
                newProcess = modo601Job(taskFile[1])
                #newProcess.modoTaskfile = 
                newProcess.run()
                #self.logIt()
                task.Status = newProcess.progress
                
                if task.Status == 100:
                    task.job.Status += 1
                if task.Status == 600:
                    task.job.Status = 600
       
                model.saveData()
            else:
                self.labelText = "waiting....."
                self.refreshMe()
    
    

      
                
    def refreshMe(self):
        self.ui.label.setText(self.labelText)
        
def main():
    
    model.setup_all()
    comp = os.getenv('COMPUTERNAME')
    print comp
   
    
    newNode = model.Node.get_by(Name= unicode(comp))
    if newNode == None:
        print "hello"
        newNode = model.Node(Name= unicode(comp))
        model.saveData()
        print newNode
    app = QtGui.QApplication(sys.argv)
    window=RN_window(comp,newNode)
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()