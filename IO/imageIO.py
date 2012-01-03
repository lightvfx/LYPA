import numpy
import sys, os 
import OpenEXR
import Imath
import multiprocessing
#import GLviewport
import exrnpy
import cv2
#import cv

class openExrSeq(multiprocessing.Process):
    def __init__(self,fn,):
        multiprocessing.Process.__init__(self)
        exrimage = OpenEXR.InputFile(fn)
	dw = exrimage.header()['dataWindow']
	(self.w,self.h) = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
        
        self.Start = 0
        self.End = 5
        self.parent_conn, self.child_conn =  multiprocessing.Pipe(False)
        self.fn = fn.split(".")
        
        
    def run(self):
        instances = numpy.zeros((self.End-self.Start+1,self.w,self.h,3),dtype = numpy.float16) 
        frame =self.Start
        i = 0
        for k in range(self.Start,self.End+1):
            
            fn =  self.fn[0] + "." +'%04d' % frame + "." + self.fn[2]
            img = exrnpy.exr2npy(fn)
            if k == self.start:
                instances = img
            else:
                instances[i,:,:] = img
            frame += 1
            i+=1
        self.child_conn.send(instances)
        img = []
        instances = []
        self.child_conn.close()
         
    def receive(self):
        self.texArr = self.parent_conn.recv()

class exrLoader():
    def __init__(self,fn):
        exrimage = OpenEXR.InputFile(fn)
        dw = exrimage.header()['dataWindow']
        meta = exrimage.header()
        #print "hello"
        (self.height,self.width) = (dw.max.x - dw.min.x + 1, dw.max.y - dw.min.y + 1)
        pt = Imath.PixelType(Imath.PixelType.FLOAT)
        #self.fout = fout
        #print "hey"
          #get individual channels
        (r, g, b) = [numpy.fromstring(s,dtype = numpy.float32) for s in exrimage.channels("RGB", pt)]
        #print (width,height)
          #merge image as rgb
        self.img = numpy.zeros((self.width,self.height,3),dtype= numpy.float32)
        #img2 = numpy.zeros((width,height,3),dtype= numpy.float32)
        r.resize(self.width,self.height)
        g.resize(self.width,self.height)
        b.resize(self.width,self.height)
        self.img[:,:,0]= b
        self.img[:,:,1]= g
        self.img[:,:,2]= r
        
    def save2jpg(self,fout):
        img8 = numpy.zeros((self.width,self.height,3),dtype= numpy.uint8)
        img = cv2.pow(self.img,1/2.2)
        cv2.convertScaleAbs(img,img8,256)
        proxy = cv2.resize(img8, (1280, 720), interpolation=cv2.INTER_AREA)
        #cv2.putText(proxy, "HELLO", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255),2)
        print "saving image: " + fout
        cv2.imwrite(fout, proxy)
        return "saving image: " + fout

    
    def save2Thumbnail(self,fout):
        Tb = numpy.zeros((256,256,3),dtype= numpy.uint8)
        img8 = numpy.zeros((self.width,self.height,3),dtype= numpy.uint8)
        img = cv2.pow(self.img,1/2.2)
        cv2.convertScaleAbs(img,img8,256)
        big = max(self.width,self.height)
        small = min(self.width,self.height)
        scale = float(big)/float(small)
        newSize =  int(256 / scale)
        thumbnail = cv2.resize(img8, (256,newSize), interpolation=cv2.INTER_AREA)
        h, w = thumbnail.shape[:2]
        s =  int((256-h)/2.0)
        Tb[s:256-s,:,:] = thumbnail[:,:,:]
        cv2.imwrite(fout, Tb)
    

class jpgLoader():      
        def __init__(self,fn):
            self.img = cv2.imread(fn)
            #self.img = cv2.transpose(img)
            #self.img = cv2.cvtColor(img,cv.CV_BGR2RGB)
          
            #cv2.imshow('img', self.img)
            #cv2.waitKey()
class utils():
    def __init__(self):
        self.fn = ""
        
    def findFirstSeqFrame(self, basenamelist):
        for i in range(0,100000):
          new_file = '%s.%04d.%s' % (basenamelist[0], i,basenamelist[2])
          #cur_file = new_file + ".zip"
          if os.path.isfile(new_file):
            frameNumber = i
            return frameNumber
    
    def findLastSeqFrame(self, basenamelist,In):
        for i in range(In+1,100000):
          new_file = '%s.%04d.%s' % (basenamelist[0], i,basenamelist[2])
          #cur_file = new_file + ".zip"
          if not os.path.isfile(new_file):
            frameNumber = i-1
            return frameNumber
    
