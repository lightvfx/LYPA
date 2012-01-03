
"""A custom widget that edits a task's properties"""

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from testUI import Ui_Form

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




if __name__ == "__main__":
    import sys
    model.setup_all()
    app = QtGui.QApplication(sys.argv)
    window=editor()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())