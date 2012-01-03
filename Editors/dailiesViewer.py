# -*- coding: utf-8 -*-
import time
import numpy
import sys
import OpenEXR
import Imath
import multiprocessing
#import GLviewport
#import exrnpy
from PyQt4 import QtCore,QtGui
from IO.imageIO import openExrSeq

# Import the compiled UI module
from dailiesViewerUI import Ui_Form
import atom
import gdata.spreadsheet.text_db
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
# The backend
import model
import os
import sip


class dailiesViewer(QtGui.QWidget):
    def __init__(self):
        #model.setup_all()
        QtGui.QWidget.__init__(self)
        self.ui=Ui_Form()
        self.ui.setupUi(self)
        self.timer = QtCore.QTimer(self)
        self.currentDaily = []
        self.list = DailiesList()
        self.ui.gridLayout_2.addWidget(self.list)
        self.ui.gridLayout_2.setAlignment(QtCore.Qt.AlignTop)
        self.ui.scrollArea.setStyleSheet("background-color: rgb(80,80,80);\n")
        self.currentId = -1
        self.timer.timeout.connect(self.refreshMe)
        self.timer.start(8000)
        self.connect(self.ui.thumbScale, QtCore.SIGNAL('valueChanged(int)'),self.changeThumbnailScale)
        self.ui.thumbScale.setRange(64,256 )
        self.ui.thumbScale.setValue(128)
        self.refreshMe()
   
    def refreshMe(self):
        #self.ui.list.clear()
        #self.mainGui.curProject.Dailies
        #if self.mainGui.curProject == "none": return
        #self.curProject = model.Project.get_by(Name=str(self.mainGui.curProject))
        #for dailie in self.curProject.Dailies:
            #print render.ShotName
            #tags=','.join([t.name for t in task.tags])
         #   try:
          #    item=QtGui.QTreeWidgetItem([dailie.Renders.Name])
          #    item.dailie=dailie
           #   self.ui.list.addTopLevelItem(item)
           # except:
            #  pass
        #for column in range(self.ui.list.columnCount()):   
        #    self.ui.list.resizeColumnToContents(column)
        #self.connect(self.ui.sessionSelComboBox, QtCore.SIGNAL('activated(QString)'), self.onSessionSelComboBoxActivated)
        model.setup_all()
        for wlabel in self.list.labels:      
          self.list.gridLayout.removeWidget(wlabel)
          sip.delete(wlabel)
          wlabel = None
        self.list.labels = []
        id = 0
        for daily in model.Dailie.query.all():
            label = CustomWidget2(self)
            label.currentDailyItemChanged.connect(self.curDailyItemChanged)
            label.setCheckable(True)
            if id == self.currentId:
              label.setChecked(True)
            label.Id = id
            label.Daily = daily
            label.setup_label()
            self.list.labels.append(label)
            id +=1
        self.list.Redraw()
        
    def curDailyItemChanged(self,id):
        if id == self.currentId :
          for label in self.list.labels:
            label.setChecked(False)
          self.currentDaily = []
          self.currentId = -1
        else:
          for label in self.list.labels:
            label.setChecked(False)
          self.currentId = id
          self.currentDaily = self.list.labels[id].Daily
          self.list.labels[id].setChecked(True)
          
    def DeleteDaily(self):
	'''
        curUserName = os.getenv('USERNAME')
	item=self.ui.list.currentItem()
	if item.render.User == curUserName:
	    fn = item.render.Path
	    path = os.path.dirname(fn)
	    self.deleteDir(path,curUserName)
	    curjob = model.Job.get_by(Name=unicode(item.render.Job))
	    for task in curjob.Tasks:
		print "delete task: " + task.Name
		task.delete()
	    print "deleting job: " + curjob.Name
	    curjob.delete()
	    print "deleting render: " + item.render.Name
	'''
        self.currentDaily.delete()
	model.saveData()
        self.refreshMe()
        
            
    def changeThumbnailScale(self,value):
        self.list.Res = float(value)
        self.list.redrawThb()
     
    def Load(self):
           #t0 = time.clock()
        #self.GL.__del__()
        
        fn = ("d:\\JOBS\\modoPipeline\\OUT\\tl211_0010.0000.exr")
        exrimage = OpenEXR.InputFile(fn)
        dw = exrimage.header()['dataWindow']
        (width,height) = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
        #multiprocessing.cpu_count()
        multiprocessing.freeze_support()
    # this shows up 2 for my core2duo e9300
        parent_conn1, child_conn1 =  multiprocessing.Pipe(False)
        parent_conn2, child_conn2 =  multiprocessing.Pipe(False)
        parent_conn3, child_conn3 =  multiprocessing.Pipe(False)
        parent_conn4, child_conn4 =  multiprocessing.Pipe(False)
        #texArr = numpy.empty((150,1920,1080,3),dtype=float)   
    
    #so now if we iterate this like that
        start = 1     
        end = 50
        self.GL.clearTexBuffer(start,end)
        texArr = []
        self.mainGui.ui.firstFrameLineEdit.setText(str(start))
        self.mainGui.ui.lastFramelineEdit.setText(str(end))
        self.mainGui.ui.TimeLineSlider.setRange(start, end)
        chunk = (end-start+1)/4
        s0 =""
        e0 =""
        imglist = numpy.arange(end-start+1) + start
        #print imglist
        startFrames = imglist[::chunk]
       
        data = "mich"
        frameRange = (end-start)/multiprocessing.cpu_count()
  
   
        t0 = time.clock()
        multiprocessing.freeze_support()
        #print "arf"
        #p1 = run("mich" ,str(start),str(startFrames[0]+chunk-1))
        p1 = openExrSeq("mich" ,str(start),str(startFrames[0]+chunk-1), child_conn1,width,height)
        p2 = openExrSeq("mich2",str(startFrames[1]),str(startFrames[1]+chunk-1), child_conn2,width,height)
        p3 = openExrSeq("mich3",str(startFrames[2]),str(startFrames[2]+chunk-1), child_conn3,width,height)
        p4 = openExrSeq("mich4",str(startFrames[3]),str(end), child_conn4,width,height)
        #p3 = openExrSeq("mich4")
        #p4 = openExrSeq("mich3")
        p1.start()
        p2.start()
        p3.start()
        p4.start()
        #print p1.instances.shape
        texArr1 = parent_conn1.recv()
        texArr2 = parent_conn2.recv()
        texArr3 = parent_conn3.recv()
        texArr4 = parent_conn4.recv()
        
        #q.get()
        p1.join()
        p2.join()
        p3.join()
        p4.join()
        #p1.instances[1]
        texArr = numpy.concatenate((texArr1,texArr2))
        texArr1 = []
        texArr2 = []
        texArr = numpy.concatenate((texArr,texArr3))
        texArr3 = []
        texArr = numpy.concatenate((texArr,texArr4))
        texArr4 = []
        #self.GL.instances = []
        self.loadTextures(texArr,start,end)
        self.GL.update()
        texArr = []
        #print time.clock()
        
    def setGL(self,GL):
        self.GL = GL
       
    def setMainGUI(self,mainGui):
        self.mainGui = mainGui
    
    def loadTextures(self,arrInstances, start,  end):
        self.GL.instances = []
        self.GL.end = end - start
        frame = start
        for i in range(start, end):    
           
            self.GL.instances.append(self.GL.mktex(arrInstances[i-start]))
            frame += 1
            #self.GL.setCurrentFrame(i-start)
            #self.GL.update()
           # self.updateGL()
        self.GL.curFrame =  self.GL.instances[0].texture
        self.GL.width =   self.GL.instances[0].width
       # print self.width
        self.GL.height =  self.GL.instances[0].height
        #self.GL.arrInstances = []
       
        #GLviewport.GLWidget.play()
    def onSessionSelComboBoxActivated(self,text):
        print "addtoSession"
       
    def _PrintAllEventsOnDefaultCalendar(self):
        #text_query=
        #calendar.id = atom.data.Id(text='8lglqkn2teder5d3ek4fuku0a0@group.calendar.google.com')
        a = []
        feed = self.cal_client.GetCalendarEventFeed("")
        #print 'Events on Primary Calendar: %s' % (feed.title.text,)
        for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
            a.append(an_event.title.text)
        return a
    
    def refreshCal(self):
        self.cal_client = gdata.calendar.client.CalendarClient(source='Google-Calendar_Python_Sample-1.0')
        self.cal_client.ClientLogin('', '', self.cal_client.source);
        self.ui.sessionSelComboBox.clear()
       #self._InsertCalendar()
        #print a
        #records = self.table.GetRecords(1,10000)
        records = self._PrintAllEventsOnDefaultCalendar()
        # Start with no task item to edit
       
        for record in records:
            rec  = record
            #item= QtGui.QTreeWidgetItem()
            #item.setText(0, rec)
            self.ui.sessionSelComboBox.addItem(rec)

class DailiesList(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.Hcount = 0
        self.Res = 256
        self.labels = []
        self.pixmaps = []
        #self.size = self.geometry()
        #self.resize(1200, 600)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setContentsMargins(3, 4, 3, 4)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.size = self.geometry()
        
        
    def resizeEvent(self,event):
        self.size = self.geometry()
        self.redrawThb()
    
    def Redraw(self):
        self.resize(self.size.width(),self.size.height())
    
    def redrawThb(self):
        self.Hcount = int(float(self.size.width()) /float(self.Res + 15))
        col = 0
        row = 0
        id = 0
        for label in self.labels:
          label.setMinimumSize(QtCore.QSize(self.Res,self.Res))
          label.setMaximumSize(QtCore.QSize(self.Res,self.Res))
            #label.res = self.res - 50
            #self.gridLayout.removeWidget(label)
          self.gridLayout.addWidget(label,row,col)
          if col < self.Hcount:
            col += 1 
          if col == self.Hcount:
            row +=1
            col = 0
            #print self.Hcount
            #print row
          self.gridLayout.setAlignment(QtCore.Qt.AlignLeft)
        self.Hcount = 0

class CustomWidget2(QtGui.QPushButton):
    currentDailyItemChanged = QtCore.pyqtSignal(int)
    def __init__(self, parent):
        QtGui.QPushButton.__init__(self, parent)
        self.connect(self, QtCore.SIGNAL('clicked()'), self.selectDaily)
        self.Daily = []
        self.Id = 0
        self.label = QtGui.QLabel(self)
        self.ShotLabel = QtGui.QLabel(self)
        self.ShotLabel.setStyleSheet("background-color: rgb(100,160,200);\n color: rgb(50,50,50);\n ;border-radius: 6px;\n")
        self.setStyleSheet("""QPushButton{color: rgb(120,120,120);background-color: qlineargradient(spread:pad, x1:0.0227273, y1:1, x2:0, y2:0, stop:0 rgba(103, 103, 105, 255), stop:1 rgba(143, 143, 145, 255));border: 1px solid;border-color: rgb(100, 100, 105);border-radius: 6px;}
QPushButton:pressed {
background-color: rgb(30, 30, 30);border-color: orange;border: 3px solid orange;}
QPushButton:checked {
 background-color: rgb(30, 30, 30);
 ;border-color: orange;border: 3px solid orange;}
""")
    def setup_label(self):
        renderpath = self.Daily.Renders.Path
        thbPath = os.path.dirname(renderpath)  + "/proxy/thumbnail.jpg"
        pixmap = QtGui.QPixmap(thbPath)
        self.label.setScaledContents(True)
        self.label.setMaximumSize(QtCore.QSize(256,256))
        #self.label.setMinimumSize(QtCore.QSize(256,256))
        self.label.setPixmap(pixmap)
        self.ShotLabel.setText(self.Daily.Name)
        #self.TypeLabel.setText("yeaah")
        self.horizontalLayout = QtGui.QVBoxLayout(self)
        self.horizontalLayout.setContentsMargins(3, 4, 3, 4)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout.addWidget(self.label)
        self.horizontalLayout.addWidget(self.ShotLabel)
        #self.horizontalLayout.addWidget(self.TypeLabel)
        self.ShotLabel.setAlignment(QtCore.Qt.AlignCenter)
        #self.TypeLabel.setAlignment(QtCore.Qt.AlignCenter)
      
    def selectDaily(self):
      self.currentDailyItemChanged.emit(self.Id)
      
     

if __name__ == "__main__":
    import sys
    model.setup_all()
    app = QtGui.QApplication(sys.argv)
    window=dailiesViewer()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())
    
    
  