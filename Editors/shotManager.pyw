# -*- coding: utf-8 -*-

"""The user interface for our app"""

import os,sys,string

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from windowUi import Ui_MainWindow

# Import our backend
import model
import nukeSS

# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        
        # This is always the same
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.EditTrigger = False
        
        # Start with the editor hidden
        #self.ui.editor.hide()

        # Let's do something interesting: load the database contents 
        # into our task list widget
        #for task in model.Shot.query.all():
        self.curSeq = model.Sequence.get_by(Name=u'LDEV')
        self.ui.SequComboBox.addItem("all")
        for task in model.Shot.query.all():
            
            #tags=','.join([t.name for t in task.tags])
            item=QtGui.QTreeWidgetItem([task.Name,task.In,task.Out])
            item.task=task
          
            self.ui.list.addTopLevelItem(item)
        
        print  model.Sequence.query.all()
        for Seq in model.Sequence.query.all():
            #tags=','.join([t.name for t in task.tags])
            #item=QtGui.QTreeWidgetItem([Seq.Name])
            self.ui.SequComboBox.addItem(Seq.Name)
                      
        self.connect(self.ui.actionNew_Sequence, QtCore.SIGNAL('triggered()'), self.makeNewSeq)
        self.connect(self.ui.SequComboBox, QtCore.SIGNAL('activated(QString)'), self.onSequComboBoxActivated)
        #nukeSS.setStyleSheet(self)
        

    def on_list_itemChanged(self,item,column):
        #item.task.Name = str(self.ui.task.text())
        print "update"
        #model.saveData()

    def on_actionDelete_Task_triggered(self,checked=None):
        if checked is None: return
        # First see what task is "current".
        item=self.ui.list.currentItem()
        
        if not item: # None selected, so we don't know what to delete!
            return
        # Actually delete the task
        item.task.delete()
        model.saveData()
        
        # And remove the item. I think that's not pretty. Is it the only way?
        self.ui.list.takeTopLevelItem(self.ui.list.indexOfTopLevelItem(item))

    def on_list_currentItemChanged(self,current=None,previous=None):
        # In Session 5, fixes a bug where an item was current but had no visible
        # changes, so it could be deleted/edited surprisingly.
        #item=self.ui.list.currentItem()
        if current:
            current.setSelected(True)
        if self.EditTrigger == False:
            self.ui.editor.setEnabled(False)    
        # Changed in session 5, because we have more than one action
        # that should only be enabled only if a task is selected
            #for action in  [
             #           self.ui.actionEdit,
              #         ]:
               # if current:
                #    action.setEnabled(True)
                #else:
                 #   action.setEnabled(False)
        self.ui.editor.edit(current)
        
            
        #model.saveData()
    
    def onSequComboBoxActivated(self,text):
        # In Session 5, fixes a bug where an item was current but had no visible
        # changes, so it could be deleted/edited surprisingly.
        #item=self.ui.list.currentItem()
        self.ui.list.clear()
       
        if text == "all": 
            for task in model.Shot.query.all():
                item=QtGui.QTreeWidgetItem([task.Name,task.In,task.Out])
                item.task=task
          
                self.ui.list.addTopLevelItem(item)
        
        else:
            self.curSeq = model.Sequence.get_by(Name=str(text))
            for task in self.curSeq.Shots:
            
            #tags=','.join([t.name for t in task.tags])
                item=QtGui.QTreeWidgetItem([task.Name,task.In,task.Out])
                item.task=task
          
                self.ui.list.addTopLevelItem(item)
        
        #model.saveData()

    def on_actionNew_Task_triggered(self,checked=None):
        if checked is None: return
        # Create a dummy task
        task=model.Shot(Name="TL_211_0020",In = "25", Out = "100")
        self.curSeq.Shots.append(task)
        self.ui.editor.setEnabled(True)
        # Create an item reflecting the task
        item=QtGui.QTreeWidgetItem([task.Name,task.In,task.Out])
        item.task=task
        
        # Put the item in the task list
        self.ui.list.addTopLevelItem(item)
        self.ui.list.setCurrentItem(item)
        # Save it in the DB
        model.saveData()
        # Open it with the editor
        self.ui.editor.edit(item)
        #self.ui.editor.setEnabled(False)
    
    def on_actionUpdate_database_triggered(self,checked=None):
        print "hello"
        model.saveData()
    
    def makeNewSeq(self):
        seq, ok = QtGui.QInputDialog.getText(self, "QInputDialog.getText()",
                "Sequence name:", QtGui.QLineEdit.Normal,"")
        if ok and len(str(seq)) == 2:
            #self.textLabel.setText(text)
            print 
            model.Sequence(Name= string.upper(str(seq)))
            self.ui.SequComboBox.addItem(string.upper(str(seq)))
            model.saveData()
           

    def on_actionEdit_triggered(self,checked=None):
        #print checked
        if checked is None: return
        if checked is True:
            self.ui.editor.setEnabled(True)
            self.EditTrigger = True
        if checked is False:
            self.ui.editor.setEnabled(False)
            self.EditTrigger = False
        for action in  [self.ui.actionDelete_Task,
                        self.ui.actionNew_Task, self.ui.actionUpdate_database, self.ui.actionNew_Sequence
                       ]:
            if checked is True:
                action.setEnabled(True)
            else:
                action.setEnabled(False)
        #self.ui.editor.hide()
        # First see what task is "current".
        #item=self.ui.list.currentItem()
        
        #if not item: # None selected, so we don't know what to edit!
            #return
            
        # Open it with the editor
        #self.updateUi()

def main():
    # Init the database before doing anything else
    model.setup_all()
    
    # Again, this is boilerplate, it's going to be the same on 
    # almost every app you write
    app = QtGui.QApplication(sys.argv)
    window=Main()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    main()
    
