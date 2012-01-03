#!/usr/bin/env python

#import model
#from PyQt4 import QtCore,QtGui
import lx    # for lx.out
import subprocess


info = subprocess.Popen([r"C:/Users/antoinem/Dropbox/LYPA_001_beta/dev/LYPA_shotManager.py"],shell = True,  stdout=subprocess.PIPE).communicate()[0]
#job = "modoPipeline"
infoSort = info.split('---')
shotSort = infoSort[0].split('shot: ')
seqSort = infoSort[1].split('sequ: ')
inSort = infoSort[2].split('in: ')
outSort = infoSort[3].split('out: ')
projectSort = infoSort[4].split('project: ')
widthSort = infoSort[5].split('width: ')
heightSort = infoSort[6].split('height: ')
framerateSort = infoSort[7].split('framerate: ')
LUTSort = infoSort[8].split('LUT: ') 
seq = seqSort[len(seqSort)-1]
shot =  shotSort[len(shotSort)-1]
first = int(inSort[len(inSort)-1])
last =  int(outSort[len(outSort)-1])
job = projectSort[len(projectSort)-1]
width = int(widthSort[len(widthSort)-1])
height = int(heightSort[len(heightSort)-1])
chunk = "5"
timeIn = float(first) / 24.0
timeOut =  float(last)/ 24.0
layer = "L01"
version = "5"
projectScenePath = "J:/" + job + "/film/" + shot +"/CG/lighting/modo/scenes/build.lxo"

#projectPath = "J:/modoPipeline/film/TL/tl211_0020/CG/lighting/modo"

lx.eval('select.item  Render set')
lx.eval( "!item.tag string PROJ {%s} " % job)
lx.eval( "!item.tag string SEQU {%s} " % seq)
lx.eval( "!item.tag string SHOT {%s}" % shot)
lx.eval( "!item.tag string LAYE  {%s}" % layer )
lx.eval( "!item.tag string VERS {%s}" % version )
lx.eval( "!item.tag string CHNK {%s}" % chunk )
lx.eval( "!item.channel last {%d}" % last)
lx.eval( "!item.channel first {%d}" % first)
lx.eval( "!render.res 0 {%d}" % width)
lx.eval( "!render.res 1 {%d}" % height)
lx.eval( "!pref.value animation.fps film")
lx.eval( "!time.range scene {%f}" % timeIn )
lx.eval( "!time.range scene out:{%f}" % timeOut) 
#lx.eval( "!projdir.chooseProject {%s}" % projectPath)
lx.out(info)
lx.eval("scene.saveAs \"%s\" $LXOB false" %projectScenePath)