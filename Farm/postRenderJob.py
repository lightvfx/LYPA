#!/usr/bin/env python
import os
import sys
from IO.imageIO import exrLoader
import subprocess
from PyQt4 import QtCore
#f = open('d:/log.txt', 'w')

class postRender():
    def __init__(self,command):
        self.command =  command
        self.progress = 600
        self.command = command.split(" ")
        
    def run(self,frame):
        if self.command[1] == "-makeProxy":
            self.fn = self.command[0].split(".")
            img = exrLoader(self.fn[0] + "." +'%04d' % frame + "." + self.fn[2])
            a = img.save2jpg(self.command[2] + "/proxy."+ '%04d' % frame + ".jpg")
        self.progress = 100
        if self.command[1] == "-makeThumbnail":
            self.fn = self.command[0].split(".")
            img = exrLoader(self.fn[0] + "." +'%04d' % frame + "." + self.fn[2])
            a = img.save2Thumbnail(self.command[2] + "/thumbnail.jpg")
        self.progress = 100
        return a
       
    def makeThumbnail(self,frame):
        self.fn = self.command[0].split(".")
        img = exrLoader(self.fn[0] + "." +'%04d' % frame + "." + self.fn[2])
        img.save2Thumbnail(self.command[2] + "/thumbnail.jpg")
        self.progress = 100
        return
    def stop(self):
        self.process.terminate()

