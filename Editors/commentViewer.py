# -*- coding: utf-8 -*-
import time
import numpy
import sys

import gdata.spreadsheet.text_db
#import GLviewport


# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from commentViewerUI import Ui_Form

# The backend
import model

#Misc.

class commentViewer(QtGui.QWidget):
    def __init__(self):
        model.setup_all()
        QtGui.QWidget.__init__(self)

        self.ui=Ui_Form()
        self.ui.setupUi(self)
        #self.curSeq = model.Sequence.get_by(Name=u'LDEV')
    
    def sendComment(self):
        #print "yeaaah"
        session = "test"
        newcomment = str(self.ui.textEdit.toPlainText())
        client = gdata.spreadsheet.text_db.DatabaseClient(username='',password='')
        db = client.GetDatabases(name = 'commentsDB')
        table = db[0].GetTables(name='comments')[0]
        comment = table.AddRecord({'comment':newcomment,'session':session,'shot':'tl211_0020','user':'anm'})
        self.ui.textEdit.clear()

if __name__ == "__main__":
    import sys
    model.setup_all()
    app = QtGui.QApplication(sys.argv)
    window=commentViewer()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())