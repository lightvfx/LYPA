from Farm import LYPA_renderNodeUI
import os,sys
import model
from PyQt4 import QtCore , QtGui
import subprocess



class RN_window(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #print "yeehhaa"
        #self.computerName = computerName
        #self.Node = Node
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.start)
        self.timer.start(8000)
        self.labelText = "waiting...."
        #self.app = app
        self.ui=LYPA_renderNodeUI.Ui_MainWindow()
        self.ui.setupUi(self)
        model.setup_all()
        comp = os.getenv('COMPUTERNAME')
        self.newNode = model.Node.get_by(Name= unicode(comp))
        if self.newNode == None:
            self.newNode = model.Node(Name= unicode(comp))
            model.saveData()
        self.start()
 

    def start(self):

        model.saveData()
        for task in self.newNode.Tasks:
            print self.newNode.Name    
            if task.Status == 666:
                print "killing:" + str(task.Pid)
                subprocess.Popen(["taskkill.exe", "/PID", str(task.Pid) , "/t", "/f"])

            elif task.Status <100:
                self.newNode.Status = 1
                
            else:
                pass
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window= RN_window()
    window.show()
      # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())