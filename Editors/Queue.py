# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore,QtGui
from QueueUI import Ui_Form
import model

class Queue(QtGui.QWidget):
    def __init__(self):
        #model.setup_all()
        QtGui.QWidget.__init__(self)
       
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer(self)
        #self.frame = 0
        self.timer.timeout.connect(self.refreshMe)
        self.timer.start(15000.0)
        #self.curSeq = model.Sequence.get_by(Name=u'LDEV')
        self.refreshMe()
        
    def refreshMe(self):
        model.setup_all()
        self.ui.list.clear()

        
        for task in model.Task.query.all():
            item = QtGui.QTreeWidgetItem([str(task.Name),str(task.Type),str(task.Status),str(task.Node),str(task.Pid)])

            
            item.setForeground(1,QtGui.QColor(160, 165, 170))
            if task.Status < 100:
                item.setForeground(0,QtGui.QColor(160, 250, 160))
                item.setForeground(2,QtGui.QColor(160, 250, 160))
            elif task.Status == 101:
                item.setForeground(0,QtGui.QColor(250, 220, 160))
                item.setForeground(2,QtGui.QColor(250, 220, 160))
            else:
                item.setForeground(0,QtGui.QColor(160, 165, 170))
                item.setForeground(2,QtGui.QColor(160, 165, 170))
            item.setForeground(3,QtGui.QColor(160, 165, 170))
            #item.setText(0, str(rec["comment"]))
            self.ui.list.addTopLevelItem(item)
        
        for column in range(self.ui.list.columnCount()):   
            self.ui.list.resizeColumnToContents(column)

if __name__ == "__main__":
    import sys
    #model.setup_all()
    app = QtGui.QApplication(sys.argv)
    window=commentBrowser()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())