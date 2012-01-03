import numpy
import datetime
import multiprocessing
from IO.imageIO import openExrSeq, jpgLoader
import IO.exrnpy
from PyQt4 import QtCore,QtGui
import elixir
from renderViewerUI import Ui_Form
import model
import os,sys,time,shutil
import subprocess
import OpenEXR
#import LYPA_cl

class renderViewer(QtGui.QWidget):
    def __init__(self):
	QtGui.QWidget.__init__(self)
	self.ui=Ui_Form()
	self.ui.setupUi(self)
	self.ProjectFilter = "none"
	#self.DB = LYPA_cl.accessDB()
	#self.userFilter = "all"
	self.SeqFilter = "all"
	self.ShotFilter = "all"
	self.TypeFilter = "all"
	self.ProjectFilter = "none"
	self.SearchFilter  = ""
	#self.curUser = model.User.get_by(Name= os.getenv("USERNAME"))
        self.UserFilter = os.getenv("USERNAME")
        self.pixmap = QtGui.QPixmap("j:/modoPipeline/OUT/tl211_0010.0000_th.jpg")
	self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.refreshMe)
        self.timer.start(3000)
	
	model.setup_all()
	self.refreshCombos()

	self.ui.list.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.connect(self.ui.list, QtCore.SIGNAL('customContextMenuRequested(const QPoint&)'), self.openMenu)
        self.connect(self.ui.UserComboBox, QtCore.SIGNAL('activated(QString)'), self.onUserComboBoxActivated)
	self.connect(self.ui.SequComboBox, QtCore.SIGNAL('activated(QString)'), self.onSequComboBoxActivated)
	self.connect(self.ui.ShotComboBox, QtCore.SIGNAL('activated(QString)'), self.onShotComboBoxActivated)
	self.connect(self.ui.ProjectComboBox, QtCore.SIGNAL('activated(QString)'), self.onProjectComboBoxActivated)
	self.connect(self.ui.thumbScale, QtCore.SIGNAL('valueChanged(int)'),self.changeThumbnailScale)
	self.ui.thumbScale.setRange(16,256 )
	self.ui.thumbScale.setValue(16)
        #for task in model.Shot.query.all():
	self.refreshMe()

        # Start with no task item to edit
	
	
    def updateInfo(self):
	try:
	    item=self.ui.list.currentItem()
	    if item.render.Name != self.Info.Name:
		self.Info.update(item)
	except:
	    return

    def setInfo(self,info):
        self.Info = info
	
    def changeThumbnailScale(self,value):
    	#print "yeay"
    	self.ui.list.setIconSize(QtCore.QSize(value,value))
	for column in range(self.ui.list.columnCount()):   
            self.ui.list.resizeColumnToContents(column)

    def onUserComboBoxActivated(self,text):
        if text == "all": 
	    self.UserFilter = "all"
	    self.SeqFilter = "all"
	    self.ShotFilter = "all"
	    self.TypeFilter = "all"
	    #print self.UserFilter
        else:
	    self.UserFilter = text
	self.refreshMe()
	
    def onProjectComboBoxActivated(self,text):
        if text == "none":
	    self.ProjectFilter = "none"
	    #self.UserFilter = "all"
	    self.SeqFilter = "all"
	    self.ShotFilter = "all"
	    self.TypeFilter = "all"
        else:
            self.ProjectFilter = text
	    self.mainGui.curProject = self.ProjectFilter
	    self.ui.ShotComboBox.clear()
	    self.ui.SequComboBox.clear()
	    self.ui.ShotComboBox.addItem("all")
	    self.ui.SequComboBox.addItem("all")
	    self.curProjectFilter = model.Project.get_by(Name =str(self.ProjectFilter))
	    self.mainGui.curProjectLUT = float(self.curProjectFilter.LUT)
	    for Seq in self.curProjectFilter.Seqs:
		self.ui.SequComboBox.addItem(Seq.Name)
		for Shot in Seq.Shots:
		    self.ui.ShotComboBox.addItem(Shot.Name)
	self.refreshMe()

    def onSequComboBoxActivated(self,text):
	if text == "all":
	    self.ui.ShotComboBox.clear()
	    #self.userFilter = "all"
	    self.SeqFilter = "all"
	    self.ShotFilter = "all"
	    self.TypeFilter = "all"
	    self.ui.ShotComboBox.addItem("all")
	    for Shot in model.Shot.query.all():
		self.ui.ShotComboBox.addItem(Shot.Name)
	    self.refreshMe()
	else:
	    print "go"
	    self.ui.ShotComboBox.clear()
	    self.SeqFilter = text
	    self.curSeqFilter =  model.Sequence.get_by(Name =str(self.SeqFilter))
	    self.ui.ShotComboBox.addItem("all")
	    for Shot in self.curSeqFilter.Shots:
		self.ui.ShotComboBox.addItem(Shot.Name)
	    self.refreshMe()

    def onShotComboBoxActivated(self,text):
	if text == "all":
	    self.ShotFilter = "all"
	    self.refreshMe()
	else:
	    #print "go"
	    self.ShotFilter = text
	    self.curSeqFilter =  model.Sequence.get_by(Name =str(self.SeqFilter))
	    self.curShotFilter =  model.Shot.get_by(Name =str(self.ShotFilter))
	    self.refreshMe()
	    
    def Search(self,text):
	self.SearchFilter  = str(text)
	self.refreshMe()
    
    def refreshMe(self):
	currItem=self.ui.list.currentItem()
	pixmap = self.pixmap 
    	icon = QtGui.QIcon(pixmap)
	currId = self.ui.list.indexOfTopLevelItem(currItem)
	listExp = []
	listcount = 0
	for i in range(self.ui.list.topLevelItemCount()):
	    if self.ui.list.topLevelItem(i).isExpanded () == True:
		itList = []
		itList.append(i)
		listExp.append(itList)
		for j in range(self.ui.list.topLevelItem(i).childCount()):
		    if self.ui.list.topLevelItem(i).child(j).isExpanded ():
			listExp[listcount].append(j)
		listcount += 1

	self.ui.list.clear()
	if self.ProjectFilter == "none":
	    self.ui.list.clear()
	    return
	else:
	    remember = True
	    pass
	
	if self.UserFilter != "all":
	    remember = True
	    renders = model.Render.query.filter_by(Project=self.curProjectFilter)
	    renders = renders.filter_by(User=str(self.UserFilter))

	if self.UserFilter == "all":
	    renders = model.Render.query.filter_by(Project=self.curProjectFilter)

	if self.SeqFilter != "all" and self.ShotFilter == "all":
	    remember = True
	    self.ui.list.clear()
	    #seql = model.Render.query.filter_by(SeqName=self.curSeqFilter)
	    renders = renders.filter_by(SeqName=self.curSeqFilter)

	if self.SeqFilter != "all" and self.ShotFilter != "all":
	    remember = True
	    self.ui.list.clear()
	    #shotl = model.Render.query.filter_by(ShotName=self.curShotFilter)
	    renders = renders.filter_by(ShotName=self.curShotFilter)
	
	if self.SeqFilter == "all" and self.ShotFilter != "all":
	    remember = True
	    self.ui.list.clear()
	    #curSeq =  model.Sequence.get_by(Name =str(self.SeqFilter))
	    renders = renders.filter_by(ShotName=self.curShotFilter)
	
	
	if self.SearchFilter != "":
	    renders = renders.filter(model.Render.Name.contains(self.SearchFilter))
        loc = "server"
        ja = 0
	
        for render in renders.all():
            renderStatus = "Offline"
	    a = str(render.Job)
            fJob  = model.Job.get_by(Name= unicode(a))
	    jobStatus = fJob.Status
	    if jobStatus == 101:
		renderStatus = "Offline"
		jobStatusReport = "not started"
	    elif jobStatus >= 0 and jobStatus < 100:
		renderStatus = "Offline"
		jobStatusReport = str(jobStatus)+"%"
		
	    elif jobStatus == 600:
		renderStatus = "Error"
		jobStatusReport = "Error"
	    elif jobStatus == 100:
		renderStatus = "Online"
		jobStatusReport = "Finished"
	    else:
		renderStatus = "Offline"
		jobStatusReport = "Stopped"
	    renderpath = render.Path
            item=QtGui.QTreeWidgetItem([render.Name,loc,str(render.In),str(render.Out),str(render.version),renderStatus,render.Type,str(render.User),str(render.Date),str(str(render.Width) + "x" + str(render.Height)),renderpath,render.ScenePath])
	    
	    item.setIcon(0,icon)
	    if renderStatus == "Offline":
		item.setBackground(5,QtCore.Qt.yellow)
		item.setForeground(5,QtCore.Qt.black)
	    if renderStatus == "Online":
		item.setForeground(5,QtCore.Qt.green)
		if os.path.exists(renderpath):
		    iconPath = os.path.dirname(renderpath)  + "/proxy/thumbnail.jpg"
		    pixmap = QtGui.QPixmap(iconPath)
		    icon = QtGui.QIcon(pixmap)
		    item.setIcon(0,icon)
		    item.pixmap = pixmap
	    if renderStatus == "Error":
		item.setBackground(5,QtCore.Qt.red)
		item.setForeground(5,QtCore.Qt.black)

            farmJob = QtGui.QTreeWidgetItem([fJob.Name,"","","","",jobStatusReport,fJob.Type])
            farmJob.setForeground(0,QtCore.Qt.darkBlue)
	    for j in range(0,12):
		farmJob.setBackground(j,QtGui.QColor(70, 72, 76))
		farmJob.setForeground(j,QtGui.QColor(160, 165, 170))
            farmJob.Job = fJob
            if jobStatus == 101:
                farmJob.setBackground(5,QtCore.Qt.yellow)
		farmJob.setForeground(5,QtCore.Qt.black)
            elif jobStatus >= 0 and fJob.Status < 100:
                farmJob.setBackground(5,QtCore.Qt.green)
		farmJob.setForeground(5,QtCore.Qt.black)
	    elif jobStatus == 600: 
                farmJob.setBackground(5,QtCore.Qt.red)
		farmJob.setForeground(5,QtCore.Qt.black)
	    
            
            frameBuffers = QtGui.QTreeWidgetItem(["channels",""])
            frameBuffers.setForeground(0,QtCore.Qt.darkBlue)
            item.render=render
             
            self.ui.list.addTopLevelItem(item)
            item.addChild(farmJob)
            item.addChild(frameBuffers)
            Fcount = 0
            Ferror = 0
            line = 0
	    
	    for farmTask in fJob.Tasks:
		taskItem = QtGui.QTreeWidgetItem([farmTask.ShortName,"",str(farmTask.In),str(farmTask.Out),"",str(farmTask.Status),str(farmTask.Type),str(farmTask.Node),"","",str(farmTask.Log)])
                taskItem.Task = farmTask
		#print str(farmTask.Status)
		for i in range(0,12):
		    if line == 0:
			taskItem.setBackground(i,QtGui.QColor(92, 102, 115))
		    if line == 1:
			taskItem.setBackground(i,QtGui.QColor(100, 112, 124))
		    taskItem.setForeground(i,QtGui.QColor(200, 205, 210))
		    
                if farmTask.Status == 101:
                    taskItem.setBackground(5,QtCore.Qt.yellow)
		    taskItem.setForeground(5,QtCore.Qt.black)
                elif farmTask.Status >= 0 and farmTask.Status < 100:
                    taskItem.setBackground(5,QtCore.Qt.green)
		    taskItem.setForeground(5,QtCore.Qt.black)
		elif farmTask.Status == 666:
		    taskItem.setBackground(5,QtCore.Qt.darkRed)
		    taskItem.setForeground(5,QtCore.Qt.black)
                elif farmTask.Status == 600: 
                    taskItem.setBackground(5,QtCore.Qt.red)
		    taskItem.setForeground(5,QtCore.Qt.black)
		
		line = abs(line -1)
                farmJob.addChild(taskItem)
	    
	    if renderStatus == "Online":  
		header =  OpenEXR.InputFile(renderpath).header()
		channels = header['channels']
		for chan in channels.keys():
		    chanItem = QtGui.QTreeWidgetItem([chan])
		    frameBuffers.addChild(chanItem)
		item.header = header
	    else: pass
                
 
        if remember == True:
	    for it in listExp:
		#print listExp[it]
		self.ui.list.topLevelItem(it[0]).setExpanded(True)
		#print len(it)
		if len(it) == 2:
		    self.ui.list.topLevelItem(it[0]).child(it[1]).setExpanded(True)
		elif len(it) == 3:
		    self.ui.list.topLevelItem(it[0]).child(it[1]).setExpanded(True)
		    self.ui.list.topLevelItem(it[0]).child(it[2]).setExpanded(True)
            self.ui.list.setCurrentItem(self.ui.list.topLevelItem(currId))  
        for column in range(self.ui.list.columnCount()):   
        	self.ui.list.resizeColumnToContents(column)
	model.saveData()

            
    #def getFarmJob(self,jobName):
        #import FarmMod
        #print "hello"
        #FarmMod.setup_all()
        #job  = FarmMod.job.get_by(Name=jobName)
        #return job
        
    def refreshCombos(self):
	self.ui.SequComboBox.clear()
	self.ui.ShotComboBox.clear()
	self.ui.UserComboBox.clear()
	self.ui.ProjectComboBox.clear()
	self.ui.UserComboBox.addItem("all")
        self.ui.TypeComboBox.addItem("all")
        self.ui.ShotComboBox.addItem("all")
	self.ui.SequComboBox.addItem("all")
	self.ui.ProjectComboBox.addItem("none")
        self.curUser = model.User.get_by(Name= self.UserFilter)
	for Proj in model.Project.query.all():
	    self.ui.ProjectComboBox.addItem(Proj.Name)	
	for User in model.User.query.all():
	    self.ui.UserComboBox.addItem(User.Name)
	UserComboBoxcurID = self.ui.UserComboBox.findText(self.UserFilter)
	self.ui.UserComboBox.setCurrentIndex(UserComboBoxcurID)
	
    def Load(self):
	self.LoadIt(0)
    
    def LoadProxy(self):
	item=self.ui.list.currentItem()
	start = item.render.In
        end = item.render.Out
        #item.render.Path
        fn = item.render.Path
	self.GL.clearTexBuffer(0,self.GL.end)
	self.GL.instances = []
        self.GL.end = end - start
	self.GL.first = start
	self.GL.last = end
        frame = start
        for i in range(start, end +1 ):
	    proxyPath = os.path.dirname(fn) + "/proxy/proxy."+'%04d' % i + ".jpg"
	    print proxyPath
	    jpgload = jpgLoader(proxyPath)
	    img = jpgload.img
	    self.GL.instances.append(self.GL.mktex(img,2))
	    self.GL.width =   self.GL.instances[0].height
       	    self.GL.height =  self.GL.instances[0].width
	    self.GL.curFrame =  self.GL.instances[i-start].texture
	    self.GL.update()
            frame += 1 
        self.GL.curFrame =  self.GL.instances[0].texture
        self.GL.width =   self.GL.instances[0].height
        self.GL.height =  self.GL.instances[0].width
	self.mainGui.ui.firstFrameLineEdit.setText(str(start))
        self.mainGui.ui.lastFramelineEdit.setText(str(end))
        self.mainGui.ui.TimeLineSlider.setRange(start,end)
	self.mainGui.ui.TimeLineSlider.setValue(start)
	self.mainGui.ui.ProjectLabel.setText("Project: " + str(item.render.Project.Name))
	self.mainGui.ui.ShotLabel.setText("Shot: " + str(item.render.ShotName.Name))
	self.mainGui.ui.UserLabel.setText("User: " + str(item.render.User))
	self.mainGui.ui.LUTLabel.setText("Gamma: " + self.curProjectFilter.LUT)
	
    def makeDiskCache(self):
	print "hello"
    
    def Archive(self):
	print "hello"
	
    def deleteRender(self):
        # First see what task is "current".
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
	    item.render.delete()
	    model.saveData()    
	else:
	    print "This render doesn't belong to you"
        
    def deleteDir(self,src,curUserName):
	dst = "J:/TRASH/" + curUserName + "/" +time.strftime('_%d%m%y_%H%M%S')
	shutil.move(src, dst)
	print "deleting files"
	
    def deleFilesOnly(self):
	print "hello"

    def LoadFP(self):
	self.LoadIt(1)
	
    def LoadIt(self,lod):
        #t0 = time.clock()
        #self.GL.__del__()
	self.GL.stopTimer()
	p = []
        #t0 = time.clock()
        #self.GL.__del__()
	
	
	#print self.GL.timer.isActive()
	self.mainGui.toggleMe = 0
	item=self.ui.list.currentItem()
	start = item.render.In
        end = item.render.Out
        #item.render.Path
        fn = item.render.Path
 
        self.GL.clearTexBuffer(0,self.GL.end)
        texArr = []
	cpuCount = multiprocessing.cpu_count()
	#cpuCount = 4
        print cpuCount
	if (end-start+1)> cpuCount:
	    chunk = (end-start+1)/cpuCount
	    print "cores used: " + str(cpuCount)
	    
	elif (end-start+1)> cpuCount/2:
	    cpuCount = cpuCount/2
	    chunk = (end-start+1)/cpuCount
	    print "cores used: " + str(cpuCount)
	elif (end-start+1)> cpuCount/2:
	    cpuCount = cpuCount/2
	    chunk = (end-start+1)/cpuCount
	    print "cores used: " + str(cpuCount)
	elif (end-start+1)> cpuCount/2:
	    cpuCount = 1
	    chunk = (end-start+1)/cpuCount
	    print "cores used: " + str(cpuCount)
	    
	
        s0 =""
        e0 =""
        imglist = numpy.arange(end-start+1) + start
        #print imglist
        startFrames = imglist[::chunk]
        p = [openExrSeq(fn) for i in range(cpuCount)]   
	for i in range(cpuCount):
	    if i == 0:
		p[i].Start = start
		p[i].End = startFrames[i]+chunk-1
	
	    if i == cpuCount - 1:
		p[i].Start = startFrames[i]
		p[i].End = end
	
	    else:
		p[i].Start = startFrames[i]
		p[i].End =  startFrames[i]+chunk-1
		
	
        for i in range(cpuCount):
	    p[i].start()    
	
        for i in range(cpuCount):
	    p[i].receive()     
        #q.get()
	for i in range(cpuCount):
	    p[i].join()
  
	for i in range(cpuCount):
	    if i == 0:
		texArr = numpy.concatenate((p[i].texArr,p[i+1].texArr))
	    if i > 1:
		texArr = numpy.concatenate((texArr,p[i].texArr))

	p = []
	#print time.clock() - t0, "seconds process time"
	#print start
	#print end
        self.loadTextures(texArr,start,end,lod)
	self.GL.update()
        self.mainGui.ui.firstFrameLineEdit.setText(str(start))
        self.mainGui.ui.lastFramelineEdit.setText(str(end))
        self.mainGui.ui.TimeLineSlider.setRange(start,end)
	self.mainGui.ui.TimeLineSlider.setValue(start)
	self.mainGui.ui.ProjectLabel.setText("Project: " + str(item.render.Project.Name))
	self.mainGui.ui.ShotLabel.setText("Shot: " + str(item.render.ShotName.Name))
	self.mainGui.ui.UserLabel.setText("User: " + str(item.render.User))
	self.mainGui.ui.LUTLabel.setText("Gamma: " + self.curProjectFilter.LUT)
	
	self.GL.frame = start
	texArr = []
        #print time.clock()
   
    def setGL(self,GL):
        self.GL = GL
      
    def setMainGUI(self,mainGui):
        self.mainGui = mainGui
    
    def loadTextures(self,arrInstances, start,  end,lod):
        self.GL.instances = []
        self.GL.end = end - start
	self.GL.first = start
	self.GL.last = end
        frame = start
	self.GL.plane = self.GL.makePlane()
        for i in range(start, end +1 ):    
            self.GL.instances.append(self.GL.mktex(arrInstances[i-start],lod))
	    self.GL.width =   self.GL.instances[0].width
       	    self.GL.height =  self.GL.instances[0].height
	    self.GL.curFrame =  self.GL.instances[i-start].texture
	    #self.GL.plane = self.GL.makePlane()
	    self.GL.update()
            frame += 1
        
        self.GL.curFrame =  self.GL.instances[0].texture
	self.GL.width =   self.GL.instances[0].width
       # print self.width
        self.GL.height =  self.GL.instances[0].height
	
    def submitDailie(self):
        #print "hello"
        item=self.ui.list.currentItem()
	if len(item.render.Dailie) != 0:
	    print "already was submitted"
	    return
	
	now = datetime.datetime.now()
	nowstr = str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "_" + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        newDailie = model.Dailie(Name= "D_" + item.render.Name,Comments=u"",status=0)
        #newDailie.Renders.append(item.render)
        item.render.Dailie.append(newDailie)
	self.curProjectFilter.Dailies.append(newDailie)
	self.mainGui.curProject = self.ProjectFilter
        model.saveData()
    
    def addJob(self,name,type,status):
        newJob = model.Job(Name=jobName,Type = jobType,Status = 101)
        model.saveData()
    
    def addTask(self,name,shortName,job,In,Out,cmd,Type):
        print "adding task to " + job
        curJob = model.Job.get_by(Name=unicode(job))
        newTask = model.Task(Name=name,In=In,Out=Out,Type =Type,ShortName = shortName,Status = 101,Command = cmd)
        curJob.Tasks.append(newTask)
        model.saveData()
    
    def openMenu(self, position):
        self.timer.stop()
        indexes =  self.ui.list.selectedIndexes()
        if len(indexes) > 0:
        
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level += 1
         
        menu = QtGui.QMenu()
        if level == 0:
            menu.addAction(self.tr("Preview"))
        elif level == 1:
            menu.addAction(self.tr("Pause Job"))
            menu.addAction(self.tr("Stop Job"))
            menu.addAction(self.tr("Restart Job"))
            menu.addAction(self.tr("Higher priority"))
        elif level == 2:
	    self.log = menu.addAction(self.tr("View Log"))
            self.Skip = menu.addAction(self.tr("Skip Task"))
            self.Stop = menu.addAction(self.tr("Stop Task"))
            self.reStart = menu.addAction(self.tr("Restart Task"))
	    self.connect(self.log, QtCore.SIGNAL('triggered()'), self.on_Log_triggered)
            self.connect(self.Skip, QtCore.SIGNAL('triggered()'), self.on_Skip_triggered)
	    self.connect(self.reStart, QtCore.SIGNAL('triggered()'), self.on_reStart_triggered)
	    self.connect(self.Stop, QtCore.SIGNAL('triggered()'), self.on_Stop_triggered)
            #menu.addAction(self.tr("Higher priority"))        
        menu.exec_(self.ui.list.viewport().mapToGlobal(position))
        self.timer.start(3000)
    
    def on_Log_triggered(self):
        #if argMe == "Restart Task":
            #print "hey !"
            item=self.ui.list.currentItem()
            print str(item.Task.Task)
	    #subprocess.Popen(["Notepad.exe",item.Task.Log])

    
    def on_Skip_triggered(self):
        #if argMe == "Restart Task":
            #print "hey !"
            item=self.ui.list.currentItem()
            item.Task.Status = 100
            print "skiping:  " + str(item.Task)
            model.saveData()
	    #model.setup_all()
	    self.refreshMe()
    def on_Stop_triggered(self):
        #if argMe == "Restart Task":
            #print "hey !"
            item=self.ui.list.currentItem()
            if item.Task.Status == 0 or item.Task.Status == 101 :
		item.Task.Status = 666
		print "stopping:  " + str(item.Task)
		model.saveData()
		self.refreshMe()
	    else:
		print "task not runing so can't be stopped"
        #else:
        #    print "noooooo"
    def on_reStart_triggered(self):
        #if argMe == "Restart Task":
            #sprint "hey !"
            item=self.ui.list.currentItem()
	    if item.Task.Status == 600 or item.Task.Status == 100 :
		item.Task.Status = 101
		print "restarting:  " + str(item.Task)
		model.saveData()
		#model.setup_all()
		self.refreshMe()
    

if __name__ == "__main__":
    import sys
    model.setup_all()
    app = QtGui.QApplication(sys.argv)
    window=renderViewer()
    window.show()
    # It's exec_ because exec is a reserved word in Python
    sys.exit(app.exec_())