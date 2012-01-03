#!/usr/bin/env python
from multiprocessing import Process
import sys

import math
import numpy
#import nukeSS
#import cv
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GL.shaders import *
from OpenGL.GLUT import *
from PyQt4 import  QtCore, QtGui, QtOpenGL


from ctypes import util
try:
    from OpenGL.platform import win32
except AttributeError:
    pass

import timer

#global falloffValue


class GLWidget(QtOpenGL.QGLWidget):
    xRotationChanged = QtCore.pyqtSignal(int)
    yRotationChanged = QtCore.pyqtSignal(int)
    zRotationChanged = QtCore.pyqtSignal(int)
    currentFrameChanged = QtCore.pyqtSignal(int)
    ExpChanged = QtCore.pyqtSignal(float)
    colorSampleChanged = QtCore.pyqtSignal(dict)
    glutInit(sys.argv)
    #scaleChanged     = QtCore.pyqtSignal(int)
    #


    def __init__(self,parent=None):
        super(GLWidget, self).__init__(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers), parent)
        self.arrInstances =  numpy.ones((1,720,576,3),dtype = numpy.float16) 
        
        self.instances = []
        #cv2.imshow("hello",a[0])
        #cv2.waitKey() 
        self.setMouseTracking(True)
        self.xRot = 0
        self.yRot = 0
        self.zRot = 0
        self.gear1Rot = 2
        self.zCam = 2000.0
        self.xCam = 0.0
        self.yCam = 0.0
        ###############################
        self.frame = 0
        #self.timer = QtCore.QTimer(self)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.play)
        self.curFrameNumber = 0
        #global falloffValue
        self.expValue = 1.0
        self.gamma = 2.2
        self.first =  0
        self.last =  1
        self.lastPos = QtCore.QPoint()
        
    def __del__(self):
        self.makeCurrent()
        print "deleting textures"
        for i in self.instances:
            glDeleteTextures(self.instances[i].texture)

    
    def setXRotation(self, angle):
        #print("murf")
        self.normalizeAngle(angle)

        if angle != self.xRot:
            self.xRot = angle
            self.xRotationChanged.emit(angle)
            self.updateGL()

    def setYRotation(self, angle):
        self.normalizeAngle(angle)
        if angle != self.yRot:
            self.yRot = angle
            self.yRotationChanged.emit(angle)
            self.updateGL()
           
    def setZRotation(self, angle):
        self.normalizeAngle(angle)

        if angle != self.zRot:
            self.zRot = angle
            self.zRotationChanged.emit(angle)
            self.updateGL()
            
    def setAngle(self, angle):
        self.normalizeAngle(angle)

        if angle != self.zRot:
            self.zRot = angle
   
    def setZcam(self, move):
        if move != self.zCam:
            self.zCam = math.fabs(move)

        self.updateGL()
    def setXcam(self, move):
        if move != self.xCam:
            self.xCam = move

        self.updateGL()
    def setYcam(self, move):
        #self.normalizeAngle(angle)
        if move != self.yCam:
            self.yCam = move
            #self.zRotationChanged.emit(angle)
        self.updateGL()
    
    def setCurrentFrame(self,f):
        #print f
        self.curFrameNumber = f
        self.curFrame = self.instances[f-self.first].texture
        self.updateGL()
    
    def clearTexBuffer(self,start,end):
        self.makeCurrent()
        self.instances = []
      
        for i in range(start,end +1 ):
            print "clearing cached texture: " + str(i)
            glDeleteTextures(i)
        #glFlush()
        self.updateGL()
        
    def update(self):
        #self.makeCurrent()
        self.updateGL()
        
    def mktex(self,arr,lod):
        a = GLtexture(arr,lod)
        return a
    
    def loadTextures(self,arrInstances, start,  end):
        
        self.first = start
        self.last = end
        print self.first
        print self.last
        self.instances = []
        frame = start
        for i in range(start, end +1 ):    
            print "creating texture: " + str(i)
            self.instances.append(GLtexture(arrInstances[i-start],1))
            frame += 1
 
        self.curFrame = self.instances[0].texture
        self.width =  self.instances[0].width
        self.height = self.instances[0].height
        self.arrInstances = []
        self.end = end - start
        
        
    def initializeGL(self):
        
        #filename =  "/media/DATA/JOBS/modoPipeline/OUT/tl211_0010.0038.exr"
        start = 0
        end = 0
        #p1 = Process(target=self.loadTextures, args =(0,10))
        self.loadTextures(self.arrInstances,start, end)
     
        glShadeModel (GL_FLAT)
        #glShadeModel(GL_SMOOTH) 
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_NORMALIZE)        
        glClearColor(0.0, 0.0, 0.0, 1.0)
        #self.plane = self.makePlane()
        glLoadIdentity()
        if not glUseProgram:
            print 'Missing Shader Objects!'
            sys.exit(1)
     
        global program
        program = compileProgram(
            compileShader('''
                // Application to vertex shader
                varying vec3 P;
                varying vec3 N;
                varying vec3 I;
               
     
                void main()
                {
                    //Transform vertex by modelview and projection matrices
                    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
     
                    // Position in clip space
                    P = vec3(gl_ModelViewMatrix * gl_Vertex);
                    
                    // Normal transform (transposed model-view inverse)
                    N = gl_NormalMatrix * gl_Normal;
     
                    // Incident vector
                    I = P;
     
                    // Forward current color and texture coordinates after applying texture matrix
                    gl_FrontColor = gl_Color;
                    gl_TexCoord[0] = gl_TextureMatrix[0] * gl_MultiTexCoord0;
                }
     
            ''',GL_VERTEX_SHADER),
            compileShader('''
                varying vec3 P;
                varying vec3 N;
                varying vec3 I;
                uniform sampler2D TextureMapper;
     
                uniform float rExp = 1.0;
                uniform float gExp = 1.0;
                uniform float bExp = 1.0;
                uniform float Exp = 1.0;
                uniform float ExpGLB = 1.0;
                //vec3 grayXfer = vec3(0.3, 0.59, 0.11);
                //vec3 gray = vec3(dot(grayXfer, color));
                //return vec4(mix(color, gray, Desaturation), 1.0);
                uniform float gamma = 0.454;
     
                void main()
                {
                    //float opacity = dot(normalize(N), normalize(-I));
                    //pacity = abs(opacity);
                    vec4 exposure = vec4(1.0,1.0,1.0,1.0); 
                    exposure = vec4(exposure[0]*rExp,exposure[1]*gExp,exposure[2]*bExp,exposure[3])* Exp * ExpGLB;
                    vec4 color = texture2D(TextureMapper, gl_TexCoord[0].st);
                    color = exposure * color;
                    gl_FragColor = pow(color,gamma) ;
                }
        ''',GL_FRAGMENT_SHADER),
        )
        glUseProgram(program)
        #self.setLUT(1.0)

    def makePlane(self):
        imgX = float(self.width / 100)
        imgY = float(self.height / 100)
        genList = glGenLists(1)
        glNewList(genList, GL_COMPILE)
        #glPushMatrix()
        #program.bind()
        glBegin(GL_QUADS)
        glTexCoord2f(0 , 1)
        glVertex2f(-imgX / 2 , -imgY / 2)
        glTexCoord2f(1, 1)
        glVertex2f(imgX /2, -imgY /2)
        glTexCoord2f(1, 0)
        glVertex2f(imgX /2, imgY / 2)
        glTexCoord2f(0, 0)
        glVertex2f(-imgX / 2, imgY  / 2)
        #glEnd()
        #glPopMatrix()
        #glFlush()
        #glBegin(GL.GL_QUADS)
        glEnd()
        glEndList()

        return genList


    def paintGL(self):
        
        imgX = self.width / 100
        imgY = self.height / 100
    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslated(0.0, 0.0,-20.0)
        #self.qglColor(QtCore.Qt.yellow)
        #glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, (0.8, 0.1, 0.0, 1.0))
        glScalef(self.zCam/2000.0 ,self.zCam/2000,0)
        glTranslated(self.xCam / 500.0 , self.yCam / 500.0 * -1, 0)        
        glBindTexture(GL_TEXTURE_2D, self.curFrame)
        #glCallList(self.plane)
        glPushMatrix()
        #program.bind()
        glBegin(GL_QUADS)
        glTexCoord2f(0 , 1)
        glVertex2f(-imgX / 2 , -imgY / 2)
        glTexCoord2f(1, 1)
        glVertex2f(imgX /2, -imgY /2)
        glTexCoord2f(1, 0)
        glVertex2f(imgX /2, imgY / 2)
        glTexCoord2f(0, 0)
        glVertex2f(-imgX / 2, imgY  / 2)
        glEnd()
        glPopMatrix()   
        
    def resizeGL(self, width, height):
        glViewport(0, 0, width, height)
        #print str(width) + " " + str(height)
        side = min(width, height)
        if side < 0:
            return
        glMatrixMode(GL_PROJECTION)
        #glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        #self.makeCurrent()
        glOrtho(-float(width) /200.0 , +float(width) /200.0 , -float(height) /200.0 , +float(height) /200.0 , 19, 23.0)
        self.updateGL()
        
    def setExp(self, val):
        #print self.expValue
        if program:
            edgefalloff = glGetUniformLocation(program, "ExpGLB")
            if not edgefalloff in (None,-1):
                self.expValue = self.expValue + val
               #print self.expValue
                glUniform1f(edgefalloff,self.expValue)
                self.updateGL()
                self.ExpChanged.emit(self.expValue)
    
    def setExpSl(self, value):
        #print value
        if program:
            edgefalloff = glGetUniformLocation(program, "Exp")
            if not edgefalloff in (None,-1):
                expValue =  value /10.0
                #print "exp: " + str(expValue)
                glUniform1f(edgefalloff,expValue)
            self.updateGL()
    
    def setrExpSl(self, value):
        if program:
            edgefalloff = glGetUniformLocation(program, "rExp")
            if not edgefalloff in (None,-1):
                expValue =  value /10.0
                glUniform1f(edgefalloff,expValue)
            self.updateGL()
    
    def setgExpSl(self, value):
        if program:
            edgefalloff = glGetUniformLocation(program, "gExp")
            if not edgefalloff in (None,-1):
                expValue =  value /10.0
                glUniform1f(edgefalloff,expValue)
            self.updateGL()
  
    def setbExpSl(self, value):
        if program:
            edgefalloff = glGetUniformLocation(program, "bExp")
            if not edgefalloff in (None,-1):
                expValue =  value /10.0
                glUniform1f(edgefalloff,expValue)
            self.updateGL()
    
    def setLUT(self, val):
        if program:
            gamma = glGetUniformLocation(program, "gamma")
            self.gamma = 1.0/val
            glUniform1f(gamma,self.gamma)
            self.updateGL()
        
    def mousePressEvent(self, event):
        self.lastPos = event.pos()
    
    #def keyPressEvent(self, event):
    #    self.lastPos = event.pos()
  
    def mouseDoubleClickEvent(self,event):
        #self.expValue = 1.0
        if program:
            edgefalloff = glGetUniformLocation(program, "ExpGLB")
            if not edgefalloff in (None,-1):
                self.expValue =  1.0
                print "exp: " + str(self.expValue)
                glUniform1f(edgefalloff,self.expValue)
        self.updateGL()
        self.ExpChanged.emit(self.expValue)
        

    def mouseMoveEvent(self, event):
        dx = event.x() - self.lastPos.x()
        dy = event.y() - self.lastPos.y()
        self.mousePosX = self.mapFromGlobal(QtGui.QCursor.pos()).x()
	self.mousePosY = self.mapFromGlobal(QtGui.QCursor.pos()).y()
        adjustedY = glGetIntegerv(GL_VIEWPORT)[3] - self.mousePosY - 1
        a = glReadPixels(self.mousePosX ,adjustedY,1,1,GL_RGB,GL_FLOAT)
        colorsample = []
        r = float(a[:,:,0])
        g = float(a[:,:,1])
        b = float(a[:,:,2])
        RGB = {'R': str(r), 'G': str(g),'B': str(b)}
        self.colorSampleChanged.emit(RGB)
        
        if event.buttons() & QtCore.Qt.LeftButton:
            self.setExp((dx +  dx / 10000.0)/50) 
  
        elif event.buttons() & QtCore.Qt.RightButton:
            self.setZcam(self.zCam + 10* float(dx))
        elif event.buttons() & QtCore.Qt.MidButton:
            self.setXcam(self.xCam + 10* float(dx))
            self.setYcam(self.yCam + 10* float(dy))

        self.lastPos = event.pos()

    def startTimer(self):
        #print "yihaa"
  
        self.timer.start(1000/24)
    
    def stopTimer(self):
        #print "stop"
        self.timer.stop()
      
        #self.setWindowTitle("Number of vertices")
    def play(self):
        self.frame += 1
        if self.frame == self.last + 1 :
            self.frame = self.first
        self.currentFrameChanged.emit(self.frame)

    def xRotation(self):
        return self.xRot
    
    def yRotation(self):
        return self.yRot

    def zRotation(self):
        return self.zRot

    def currentFrame(self):
        print self.frame
        #return self.frame

    def zCamera(self):
        return self.zCam
    def xCamera(self):
        return self.xCam
    def yCamera(self):
        return self.yCam 


    def normalizeAngle(self, angle):
        while (angle < 0):
            angle += 360 * 16

        while (angle > 360 * 16):
            angle -= 360 * 16
            
class GLtexture(object):
    
    def __init__(self,img,lod):
        self.texture = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        self.height = 512
        self.width = 512
        self.makeTex(img,lod)
        img = []

    
    def makeTex(self,img,lod):
        self.height = img.shape[1]
        self.width = img.shape[0]
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        if lod == 0:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.width, self.height, 0, GL_RGB,GL_FLOAT, img)
        elif lod == 1:
            glTexImage2D(GL_TEXTURE_2D, 0,GL_RGB16F_ARB, self.width, self.height, 0, GL_RGB,GL_FLOAT, img)
        elif lod == 2:
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, self.height, self.width, 0, GL_BGR,GL_UNSIGNED_BYTE, img)
        img = []

