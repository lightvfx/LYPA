# -*- coding: utf-8 -*-
#import time
import numpy
import sys
#import threading
import gdata.spreadsheet.text_db
#import GLviewport


# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from commentBrowserUI import Ui_Form

# The backend
#import model

#Misc.

class commentBrowser(QtGui.QWidget):
    def __init__(self):
        #model.setup_all()
        QtGui.QWidget.__init__(self)
       
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #timer = QtCore.QTimer(self)
        #self.frame = 0
       
        #timer.timeout.connect(self.refresh)
        #timer.start(3000.0)
        #self.curSeq = model.Sequence.get_by(Name=u'LDEV')
        #self.refresh()
    def refresh(self):
        self.ui.list.clear()
        client = gdata.spreadsheet.text_db.DatabaseClient(username='',password='')
        db = client.GetDatabases(name = 'commentsDB')
        table = db[0].GetTables(name='comments')[0]
        #a = len[db]
        #print a
        records = table.GetRecords(1,10000)
        
        for record in records:
            rec  = record.content
            item= QtGui.QTreeWidgetItem()
            item.setText(0, str(rec["comment"]))
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