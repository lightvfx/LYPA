#!/usr/bin/env python
import time
#import lx    # for lx.out
import os
import datetime
import subprocess


def createModoTask(taskFile,scene,rOutputPath,start,end):
        #print "hey !"
        #scene = "J:/modoPipeline/film/tl/tl211_0020/CG/lighting/modo/scenes/testmodo5.lxo"
        #self.start = 10
        #self.end = 15
    f = open(taskFile, 'w')
    f.write("log.toConsole true\n")
    f.write("scene.open \"%s\" normal\n" %scene)
    f.write("pref.value render.threads 2\n")
    f.write("select.item Render set\n")
    f.write("item.channel first %d\n" %start) 
    f.write("item.channel last %d\n" %end)
    f.write("render.animation \"%s\" format:openexrlayers\n" %rOutputPath)
    f.write("app.quit\n")
    f.close()

#############################
### query modo
############################
rootfolder = "j:/modoPipeline/film/"
lx.eval('select.item  Render set')
seq = lx.eval( "item.tag string SEQU ? ")
proj = lx.eval( "item.tag string PROJ ? ")
shot = lx.eval( "item.tag string SHOT ?")
layer = lx.eval( "item.tag string LAYE  ?" )
ver = lx.eval( "item.tag string VERS ?" )
chnk = lx.eval( "item.tag string CHNK ?" )
first = lx.eval( "item.channel first ?")
last = lx.eval( "item.channel last ?")
w = lx.eval( "render.res 0 ?")
h = lx.eval( "render.res 1 ?")
type = "CG"
jobType = "modo501"
chunk = int(chnk)
rootfolder = "j:/" + proj + "/Film/"
lenTasks = last - first + 1
format = "EXR"


curUserName = os.getenv('USERNAME')
#lx.eval("dialog.msg version: {%s}" % cmd)


##################################
## generate Name and get version
##################################
info = subprocess.Popen([u"C:/Users/antoinem/Dropbox/LYPA_001_beta/dev/LYPA_cl.py","-lr",proj,shot,layer,ver],shell = True,  stdout=subprocess.PIPE).communicate()[0]
infoSort = info.split('---')
lx.eval("dialog.msg {%s}" % infoSort)
version =  infoSort[1]
renderName = infoSort[0]
#lx.eval( "!item.tag string VERS {%s}" % version )
verI = int(version)
lx.eval( "!item.tag string VERS {%s}" % verI )
#shot,first,last,ver,path,RenderScenefile,type,w,h,renderName,format


lx.eval("user.value ImageIO.EXR.compression.index comp2")
jobName = "job_" + renderName + time.strftime('_%d%m%y_%H%M%S')
RenderScenefile = rootfolder + shot + "/CG/lighting/modo/renderScenes/" + jobName + ".lxo"
renderOutput = rootfolder + shot + "/CG/lighting/modo/renders/" +shot + "_" + layer  + "/v" + '%03d' % verI + "/"
path = renderOutput + renderName + "." +'%04d' % int(first) + ".exr"

startFrame = int(first)
curChunk = 0
taskDir = renderOutput + "/tasks"

a = lx.eval( "query sceneservice renderOutput.N ?")
    
for i in range(a):
    modoROutput = lx.eval( "query sceneservice renderOutput.id ? {%d}" % i)
    lx.command("select.item",  item = modoROutput, mode = "set")
    rOutputType = lx.eval("shader.setEffect ?")
    if rOutputType == "shade.color":
        #lx.eval("item.channel renderOutput$filename {%s}" % rOutputPath)
        lx.eval("item.channel renderOutput$format {%s}" % "openexr")
        lx.eval("item.channel renderOutput$gamma 1.0")
        
       
lx.eval("dialog.msg {%s}" % jobName)

#rOutputType = "_BEAUTY."
rOutputPath = renderOutput   + renderName + "."
lx.eval("scene.saveAs \"%s\" $LXOB true" %RenderScenefile)
os.makedirs(taskDir)

##############################
##make Task files
############################

for i in range(int(first),int(last),chunk):
    if curChunk == (int(last) - int(first))/chunk-1:
        shortName = "task" + "_" + "%04d" % i
        taskName = jobName + "_" + "%04d" % i
        taskFile = taskDir + "/" + taskName + ".txt"
        createModoTask(taskFile,RenderScenefile,rOutputPath,startFrame,last)
    else:
        shortName = "task" + "_" + "%04d" % i
        taskName = jobName + "_" + "%04d" % i
        taskFile = taskDir + "/" + taskName + ".txt"
        createModoTask(taskFile,RenderScenefile,rOutputPath,startFrame,startFrame+chunk - 1)
        startFrame += chunk
    curChunk += 1

##############################
##register render and submit to farm
############################

info2 = subprocess.Popen([u"C:/Users/antoinem/Dropbox/LYPA_001_beta/dev/LYPA_cl.py","-sr",proj,shot,str(first),str(last),str(verI),path,RenderScenefile,type,str(w),str(h),renderOutput,renderName,jobName,jobType,format,curUserName,str(chunk),unicode(RenderScenefile + " -taskFile " + taskFile)],shell = True,  stdout=subprocess.PIPE).communicate()[0]
#print info2
lx.eval("dialog.msg {%s}" % info)
proxyDir = renderOutput + "proxy"
cmd = path + " -makeProxy " + proxyDir
os.makedirs(proxyDir)
info3 = subprocess.Popen([u"C:/Users/antoinem/Dropbox/LYPA_001_beta/dev/LYPA_cl.py","-addtask",renderName + "_proxy","Proxy",jobName,str(first),str(last),cmd,"postRender"],shell = True,  stdout=subprocess.PIPE).communicate()[0]
#print info2
lx.eval("dialog.msg {%s}" % info3)








