import sys,os
from PyQt4 import QtGui,QtCore
from Editors.importDialogUI import *
import Editors.nukeSS as nukeSS
import model
import OpenEXR
import elixir
import LYPA_cl
from IO.imageIO import utils, exrLoader
import sip
#import pickle

class importDialog(QtGui.QDialog):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    model.setup_all()
    self.DB = LYPA_cl.accessDB()
    self.ui = Ui_importDialog()
    self.ui.setupUi(self)
    nukeSS.setStyleSheet(self)
    self.connect(self.ui.SequComboBox, QtCore.SIGNAL('activated(QString)'), self.onSequComboBoxActivated)
    self.connect(self.ui.ShotComboBox, QtCore.SIGNAL('activated(QString)'), self.onShotComboBoxActivated)
    self.connect(self.ui.ProjectComboBox, QtCore.SIGNAL('activated(QString)'), self.onProjectComboBoxActivated)
    self.elemName = ""
    self.SeqFilter = ""
    self.shotFilter = ""
    self.ProjectFilter = ""
    self.In = 0
    self.Out = 0
    self.DBIn = 0
    self.DBOut = 0
    self.Offset = 0
    self.ver = 0
    self.labels = []
    self.ui.OffsetlineEdit.setText(str(self.Offset))
    self.ui.OffsetlineEdit.setInputMask("0000")
    self.refreshCombos()
    
    
  def rejected(self):
    print "reject"
    self.close()

  def accepted(self):
    print "accept"
    self.DB.addRender(self.ProjectFilter,self.shotFilter,self.DBIn,self.DBOut,self.ver,path,"",type,w,h,renderOutput,renderName,jobName,jobType,format,curUserName,Schunk,cmd)
    self.close()
  
  def fileBrowser(self):
    #labels = []
    if self.ui.ProjectComboBox.currentText() == "none":
      print "Need to set project first"
      return
    fileName = QtGui.QFileDialog.getOpenFileName(self,
                   "Import Image sequence",
                    "c:/",
                    "openExr file (*.exr)")
    if fileName:
      labels = []
      fnlist = fileName.split(".")
      fn =  fnlist[0] + "." +'$F4' + "." + fnlist[2]
      self.ui.InputPathLineEdit.setText(fn)
      header =  OpenEXR.InputFile(str(fileName)).header()
      self.clearLabels()
      for key in header.keys():
        newLabel = QtGui.QLabel(self)
        newLabel.setText(key + ": " + str(header[key]))
        self.ui.verticalLayout.addWidget(newLabel)
        self.labels.append(newLabel)
        #print key 
      IOutils = utils()
      self.In = IOutils.findFirstSeqFrame(fnlist)
      #print str(In)
      self.ui.InlineEdit.setText(str(self.In))
      self.Out = IOutils.findLastSeqFrame(fnlist,self.In)
      self.ui.OutlineEdit.setText(str(self.Out))
      self.refreshMe()
      self.setFrameRange()
      fout = os.getenv('USERPROFILE')
      img = exrLoader(str(fileName))
      thmb = img.save2Thumbnail(fout + "/thb.jpg")
         
      pixmap = QtGui.QPixmap(fout + "/thb.jpg")
      self.ui.ThumbPixmap.setPixmap(pixmap)
     
      #self.setLayout(hbox)
              
      #print str(Out)
      #self.ui.Metadata_TextEdit.setDocumetTitle("metadatas")
  def clearLabels(self):
      for wlabel in self.labels:      
        self.ui.verticalLayout.removeWidget(wlabel)
        sip.delete(wlabel)
        wlabel = None
      labels = []
      
  def onProjectComboBoxActivated(self,text):
    self.ProjectFilter = text
    self.curProject = self.ProjectFilter
    self.ui.ShotComboBox.clear()
    self.ui.SequComboBox.clear()
    #self.ui.ShotComboBox.addItem("all")
    self.ui.SequComboBox.addItem("all")
    self.curProjectFilter = model.Project.get_by(Name =str(self.ProjectFilter))
    
    for Seq in self.curProjectFilter.Seqs:
      self.ui.SequComboBox.addItem(Seq.Name)

    #self.refreshMe()
        #curUser = model.User.get_by(Name=str(text))

  def onSequComboBoxActivated(self,text):
      if text == "all":
        self.ui.ShotComboBox.clear()
        self.SeqFilter = ""
        self.shotFilter = ""
        return
      self.ui.ShotComboBox.clear()
      self.SeqFilter = text
      self.curSeqFilter =  model.Sequence.get_by(Name =str(self.SeqFilter))
      #self.ui.ShotComboBox.addItem("all")
      for Shot in self.curSeqFilter.Shots:
          self.ui.ShotComboBox.addItem(Shot.Name)
      self.shotFilter = self.curSeqFilter.Shots[0].Name
      self.refreshMe()
  
  def onShotComboBoxActivated(self,text):
      self.shotFilter = text
      self.curShotFilter =  model.Shot.get_by(Name =str(self.shotFilter))
      self.refreshMe()
      
  def refreshCombos(self):
    self.ui.ProjectComboBox.addItem("none")
    #self.ui.ProjectComboBox.addItem("none")
    #self.curUser = model.User.get_by(Name= self.UserFilter)
    for Proj in model.Project.query.all():
        self.ui.ProjectComboBox.addItem(Proj.Name)	
  
  def setElemName(self):
    self.elemName = self.ui.ElemNamelineEdit.displayText()
    #print "wadasd"
    self.refreshMe()
  
  def setFrameRange(self):
    #print self.ui.OffsetlineEdit.displayText()
    try:   
      self.Offset = int(self.ui.OffsetlineEdit.displayText())
      self.DBIn = self.In + self.Offset
      self.DBOut = self.Out + self.Offset
      self.ui.DBInlineEdit.setText(str(self.DBIn))
      self.ui.DBOutlineEdit.setText(str(self.DBOut))
    except:
      return
  def refreshMe(self):
    
    verI = 1
    renderName = self.DB.getRenderName(self.curProjectFilter.Name,self.shotFilter, self.elemName,verI)
    rootfolder = "j:/" + self.curProjectFilter.Name + "/Film/"
    self.ui.VerlineEdit.setText(str(renderName[1]))
    self.ver = renderName[1]
    renderOutput = rootfolder + self.shotFilter + "/CG/lighting/modo/renders/" +self.shotFilter + "_" + self.elemName  + "/v" + '%03d' % int(renderName[1]) + "/" + renderName[0] + ".$F4.exr"
    self.ui.OutputPathlineEdit.setText(renderOutput)
    #adaprint renderOutput
  
      
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  MainWindow = importDialog()
  MainWindow.show()
  sys.exit(app.exec_())