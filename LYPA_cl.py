#!/usr/bin/env python
import datetime
import model
import os
import sys
import gdata.spreadsheet.text_db

class accessDB():
    def __init__(self):
        self.contentDirectory = "J:/"
        model.setup_all()

    def login(self,curUserName):
        
        newUser = model.User.get_by(Name= unicode(curUserName))
        if newUser == None:
     
            newUser = model.User(Name= unicode(curUserName))
            model.saveData()
        return newUser

    def getRenderName(self,project,shot,layer,ver):
        curProject = model.Project.get_by(Name =str(project))
        renderName = shot + "_" + layer + "_v" + '%03d' % int(ver)
        renders = model.Render.query.filter_by(Project=curProject)
        while renders.filter_by(Name=unicode(renderName)).all() != []:
            #print renders.filter_by(Name=unicode(renderName)).all() 
            verI = int(ver)
            verI += 1
            #print "hello"
            renderName = shot + "_" + layer + "_v" + '%03d' % verI
            ver = str(verI)
        return renderName, ver

    def addRender(self,project,shot,first,last,ver,path,RenderScenefile,type,w,h,renderOutput,renderName,jobName,jobType,format,curUserName,Schunk,cmd):
        print "go2"
        #jobName = "job_" + renderName + time.strftime('_%d%m%y_%H%M%S')
        chunk = int(Schunk)
        curShot = model.Shot.get_by(Name=unicode(shot))
        curProj = model.Project.get_by(Name=unicode(project))
        now = datetime.datetime.now()
        newRender = model.Render(Name=renderName,In= int(first),Out= int(last),Path=path,Date = now,version= int(ver),ScenePath=RenderScenefile,Type= type,Width=int(w),Height=int(h),Format=format,Job = jobName,User = curUserName)
        model.saveData()
        curShot.Renders.append(newRender)
        curShot.Seq.Renders.append(newRender)
        curProj.Renders.append(newRender)
        model.saveData()
        newJob = model.Job(Name=jobName,Type = jobType,Status = 101)
        model.saveData()
          
        startFrame = int(first)
        curChunk = 0
        taskDir = renderOutput + "/tasks"
        
        for i in range(int(first),int(last),chunk):
            if curChunk == (int(last) - int(first))/chunk -1 :
                shortName = "task" + "_" + "%04d" % i
                taskName = jobName + "_" + "%04d" % i
                taskFile = taskDir + "/" + taskName + ".txt"
                newTask = model.Task(Name=taskName,In=startFrame,Out=last,Type =jobType, ShortName = shortName,Status = 101,Command = unicode(RenderScenefile + " -taskFile " + taskFile))
                newJob.Tasks.append(newTask)
            else:
                shortName = "task" + "_" + "%04d" % i
                taskName = jobName + "_" + "%04d" % i
                taskFile = taskDir + "/" + taskName + ".txt"
                newTask = model.Task(Name=taskName,In=startFrame,Out=startFrame+chunk-1,Type =jobType,ShortName = shortName,Status = 101,Command = unicode(RenderScenefile + " -taskFile " + taskFile))
                newJob.Tasks.append(newTask)
            startFrame += chunk
            curChunk += 1
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
    

    def createProject(self,name,cfg,width,height,ratio,framerate,lut,client):
        project = model.Project(Name=name,ConfigFile=cfg,Width=width,Height=height,Ratio=ratio,FrameRate=framerate,LUT=lut,Client=client)
        model.saveData()
        self.makeProjectdir(name)
        self.makeGDataDB(name)

    def makeProjectdir(self,name):
        os.mkdir(self.contentDirectory + name + "/")
        os.mkdir(self.contentDirectory + name + "/Assets/")
        os.mkdir(self.contentDirectory + name + "/Assets/DB")
        os.mkdir(self.contentDirectory + name + "/Assets/Env")
        os.mkdir(self.contentDirectory + name + "/Assets/Env/HDR")
        os.mkdir(self.contentDirectory + name + "/Assets/Env/REF")
        os.mkdir(self.contentDirectory + name + "/Assets/Env/PAN")
        os.mkdir(self.contentDirectory + name + "/Assets/Props")
        os.mkdir(self.contentDirectory + name + "/Assets/Scripts")
        os.mkdir(self.contentDirectory + name + "/Assets/Characters")
        os.mkdir(self.contentDirectory + name + "/Assets/Set")
        os.mkdir(self.contentDirectory + name + "/Assets/Effects")
        os.mkdir(self.contentDirectory + name + "/Edit/")
        os.mkdir(self.contentDirectory + name + "/Edit/Movie")
        os.mkdir(self.contentDirectory + name + "/Film/")
        os.mkdir(self.contentDirectory + name + "/In/")
        os.mkdir(self.contentDirectory + name + "/Out/")
        os.mkdir(self.contentDirectory + name + "/Previz/")
        os.mkdir(self.contentDirectory + name + "/Previz/CG")
        os.mkdir(self.contentDirectory + name + "/Previz/AFTERFX")
    
    def makeGDataDB(self,name):
        print "creating googleDB"
        client = gdata.spreadsheet.text_db.DatabaseClient(username='',password='')
        db = client.CreateDatabase(name = name + '_commentsDB')
        table = db.CreateTable('comments',['comment','session','shot','user'])


if __name__ == "__main__":
 
    DB = accessDB()
    if sys.argv[1] == "-lr":
        render = DB.getRenderName(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
        print render[0] + "---" + render[1]
    elif sys.argv[1] == "-sr":
        DB = accessDB()
        render = DB.addRender(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9],sys.argv[10],sys.argv[11],sys.argv[12],sys.argv[13],sys.argv[14],sys.argv[15],sys.argv[16],sys.argv[17],sys.argv[18],sys.argv[19])
    elif sys.argv[1] == "-cfg":
        DB = accessDB()
    elif sys.argv[1] == "-addtask":
        DB = accessDB()
        task = DB.addTask(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8])
    elif sys.argv[1] == "-addjob":
        DB = accessDB()
        task = DB.addTask(sys.argv[2],sys.argv[3],sys.argv[4])
    elif sys.argv[1] == "-createproject":
        DB = accessDB()
        task = DB.createProject(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5],sys.argv[6],sys.argv[7],sys.argv[8],sys.argv[9])