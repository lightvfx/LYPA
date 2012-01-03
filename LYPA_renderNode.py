# -*- coding: utf-8 -*-

"""A custom widget that edits a task's properties"""

# Import Qt modules
from PyQt4 import QtCore,QtGui
from Farm import LYPA_renderNodeUI
import Farm.postRenderJob as postRenderJob
import Farm.modoJob as modoJob
#import modoJob
import os,sys
import model
#global app
# Misc.



class RN_window(QtGui.QMainWindow):
    def __init__(self,computerName,Node):
        QtGui.QMainWindow.__init__(self)
        print "yeehhaa"
        self.computerName = computerName
        self.Node = Node
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.startNode)
        self.timer.start(5000)
        self.labelText = "waiting...."
        #self.app = app
        self.ui=LYPA_renderNodeUI.Ui_MainWindow()
        self.ui.setupUi(self)
        model.setup_all()
        self.setWindowTitle(QtGui.QApplication.translate("MainWindow", "LYPA_renderNode alpha 101   " + self.computerName, None, QtGui.QApplication.UnicodeUTF8))
      
        
    def startNode(self):
        print "checking"
        model.saveData()
        stat = 0
        n = self.Node
        n.Status = 0
        
        #print "hey"
        for task in model.Task.query.all():
            #print task.Name
            #print task.done
            #if n.Status = 
            if task.Status == 101:
                self.labelText = "rendering: " + task.Name
                self.refreshMe()
                
            if task.Status == 101:
                #print task.Type
           
                if task.Type == "modo501":
                    for dependingtasks in  task.job.Tasks:
                        if dependingtasks.Type == "postRender":
                            dependingtasks.Status = 101
                        else:
                            pass
                    task.Status = 0
                    n.Tasks.append(task)
                    model.saveData()
                    self.updateJobStatus(task)
                    reload(modoJob)
                    taskFile = task.Command.split(" -taskFile ")
                    newProcess = modoJob.modo501Job(taskFile[1],task)
                    #newProcess.modoTaskfile = taskFile[1]
                    newProcess.run()
                   
                    #newProcess.process.terminate
                #self.logIt()
                    
                    #newProcess.killme()
                    n.Status = 1
                    #task.Pid = newProcess.process.pid
                   # model.saveData()
                    #print task.Pid
                    #newProcess.wait()
                    task.Status = newProcess.progress
                    model.saveData()
                elif task.Type == "postRender":
                    #print len(task.job.Tasks)
                    for dependingtasks in  task.job.Tasks:
                        if dependingtasks.Type != "postRender" and dependingtasks.Status == 100:
                            stat += 1
                        else:
                            pass
                    
                    if stat == len(task.job.Tasks)-1:
                        reload(postRenderJob)
                        #print task.job.Name
                        task.Status = 0
                        #task.Log = "starting"
                        n.Tasks.append(task)
                        model.saveData()
                        self.updateJobStatus(task)
                        try:
                            print task.Command
                            newProcess = postRenderJob.postRender(task.Command)
                            for frame in range(int(task.In),int(task.Out) + 1):
                                log = newProcess.run(frame)
                                task.Log = log
                                #model.saveData()
                                if newProcess.progress == 100:
                                    task.Status = int((100.0 /(float(task.Out)-float(task.In)))* (float(frame)-float(task.In))) 
                                    model.saveData()
                            thumbnail = postRenderJob.postRender(task.Command)
                            thumbnail.makeThumbnail(int(task.In))
                        except (RuntimeError, TypeError, NameError,AttributeError,IOError) as strerror:
                            task.Status = 600
                            model.saveData()
                            print strerror
                    else:
                        stat =0
            elif task.Status == 100:
                if task.job.Status != 100:
                    self.updateJobStatus(task)                 
                else:
                    pass
            else:
                
                #model.saveData()
                self.labelText = "waiting....."
                self.refreshMe()
    

    def updateJobStatus(self,task):
        jobStat = 0
        for dtask in  task.job.Tasks:
            if dtask.Status == 100:
                jobStat +=1
            elif dtask.Status == 600:
                task.job.Status = 600
                model.saveData()
                return
            else:
                pass
        if jobStat == len(task.job.Tasks):
            task.job.Status = 100
            model.saveData()
        else:
            task.job.Status = int((100.0 / float(len(task.job.Tasks)))* float(jobStat))
            model.saveData()
        jobStat = 0
    def refreshMe(self):
        self.ui.label.setText(self.labelText)
        
    

if __name__ == "__main__":
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