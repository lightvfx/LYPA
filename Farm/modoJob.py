#!/usr/bin/env python
import os
import sys

from PyQt4 import QtCore, QtGui, QtNetwork
import subprocess

import model

class modo501Job():
    def __init__(self,modoTaskfile,task):
        #super(modo501Job,self).__init__()
        modo = "\"C:/Program Files/Luxology/modo/501sp4/modo_cl.exe\""
        self.command = modo + " < " + modoTaskfile
        self.progress = 600
        self.task = task
        self.log = modoTaskfile.split(".")

    def run(self):
        log = self.log[0] + "_log.txt"
        logPath = log.split("/")
        #fpid = open("c:/Apps/test.txt", 'w')
        print log
        f = open(log, 'w')
        self.process = subprocess.Popen(self.command,shell = True,stdout=subprocess.PIPE)
        self.task.Pid = self.process.pid
        model.saveData()
        time = ""
        for i in range(100000):
            arf = self.process.stdout.readline()
            #self.task.Log = arf
            #model.saveData()
            f.write(arf)
            print arf
         
                
            if arf.find("@exit")!= -1:
                #self.wait()
                #self.usedBytes.release()
                self.process.terminate()
                self.progress = 100
                #print "hello"
                f.close()
                return
            if arf.find("Frame") != -1 and arf.find("Frame:") == -1:
                frame = arf
                #model.saveData()
            
            if arf.find("Time:") != -1:
                time = arf
                self.task.Log = unicode(frame + " " + time)
                model.saveData()
              
            
                
                #self.process.wait()
                #return
       


#a = main()
#print a
