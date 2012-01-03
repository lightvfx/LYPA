# -*- coding: utf-8 -*-

from model import *
#create_all()
setup_all(True)
defaultProject = Project(Name=u"SITE",Widh=1024,Height=1024,Framerate = 24,LUT= "1.6")
defaultShot = Shot(Name=u"LDEV_default",In=u"20",Out=u"100",CutIn= 20,CutOut=100,Scan=u"",Description=u"",Grade=u"",Lut=u"",Thumbnail=u"",Status=0)
defaultAsset = Asset(Name=u"defaultEnv",PathLXL=u"",PathOBJ=u"",PathBGEO=u"",Description=u"",version=1,type=u"environnement")
defaultTexture = Texture(Name=u"defaultTex",Widh=1024,Height=1024,Format="jpg",Path=u"d:/jobs/defaultText.jpg",version=1)
defaultDailie = Dailie(Name=u"defaultDailie",Comments=u"",status=0)
defaultRender = Render(Name=u"defaultRender",In=0,Out=100,Path=u"j:\\modoPipeline\\OUT\\tl211_0010.0000.exr",version=1,ScenePath="",Type=u"TEST",Width=1280,Height=720,Format=u"EXR",Job=u"defaultJob",User = u"defaultUser")
defaultSequence = Sequence(Name=u"LDEV")
defaultUser = User(Name=u"User")
defaultJob = Job(Name=u"defaultJob",Type=u"TEST")
defaultTask = Task(Name=u"defaultTask")


session.commit()

print defaultShot
print defaultAsset
print defaultTexture
print defaultDailie
print defaultRender
print defaultSequence
print defaultUser
print defaultJob
print defaultProject

defaultShot.Assets.append(defaultAsset)
defaultShot.Renders.append(defaultRender)
defaultSequence.Shots.append(defaultShot)
defaultSequence.Renders.append(defaultRender)
defaultTexture.Assets.append(defaultAsset)
defaultRender.Dailie.append(defaultDailie)
#defaultUser.Renders.append(defaultRender)
#defaultUser.projects.append(defaultProject)
defaultProject.Seqs.append(defaultSequence)
defaultProject.Renders.append(defaultRender)
session.commit()

print defaultShot.Assets
print defaultShot.Renders
print defaultSequence.Shots
print defaultTexture.Assets
print defaultRender.Dailie
#print defaultUser.Renders
print defaultSequence.Renders
print defaultProject.Seqs
#print defaultProject.Users