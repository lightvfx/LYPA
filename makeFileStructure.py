#!/usr/bin/env python
import sys, os
import model

class mkShotFolder():
    def __init__(self,job,shot):
        type = "lighting"
        
        jobPath = "j://" + job 
        sequencePath = jobPath + "//Film//"
        self.ModoProjPath =  sequencePath + shot + "//CG//" + type + "//modo"
        renderOutputPath = sequencePath + shot + "//render//main"
        
        try:
            os.mkdir(sequencePath + shot )
        except:
            print shot + " already exist"
            return
        os.mkdir(sequencePath + shot + "//2D")
        os.mkdir(sequencePath + shot + "//2D//afterfx")
        os.mkdir(sequencePath + shot + "//CG")
        os.mkdir(sequencePath + shot + "//CG//animation")
        os.mkdir(sequencePath + shot + "//CG//animation//modo")
        os.mkdir(sequencePath + shot + "//CG//animation//blender")
        os.mkdir(sequencePath + shot + "//CG//animation//lightwave")
        os.mkdir(sequencePath + shot + "//CG//lighting")
        os.mkdir(sequencePath + shot + "//CG//lighting//modo")
        os.mkdir(sequencePath + shot + "//CG//lighting//houdini")
        os.mkdir(sequencePath + shot + "//CG//lighting//lightwave")
        os.mkdir(sequencePath + shot + "//CG//SFX")
        os.mkdir(sequencePath + shot + "//CG//SFX//blender")
        os.mkdir(sequencePath + shot + "//CG//SFX//houdini")
        os.mkdir(sequencePath + shot + "//CG//SFX//lightwave")
        os.mkdir(sequencePath + shot + "//CG//dev")
        os.mkdir(sequencePath + shot + "//assets")
        os.mkdir(sequencePath + shot + "//assets//anim")
        os.mkdir(sequencePath + shot + "//assets//cameras")
        os.mkdir(sequencePath + shot + "//assets//LUT")
        os.mkdir(sequencePath + shot + "//assets//MDD")
        os.mkdir(sequencePath + shot + "//assets//mattepainting")
        os.mkdir(sequencePath + shot + "//assets//elements")
        os.mkdir(sequencePath + shot + "//2d//comps")
        
        self.createModoProj()
        type = "animation"
        self.ModoProjPath =  sequencePath +  shot + "//CG//" + type + "//modo"
        renderOutputPath = sequencePath +  shot + "//render//anim"
        self.createModoProj()
    
    def createModoProj(self):
        #os.mkdir(mayaProjPath + "" )
    
        os.mkdir(self.ModoProjPath + "//data" )
        os.mkdir(self.ModoProjPath + "//images" )
        os.mkdir(self.ModoProjPath + "//python" )
        os.mkdir(self.ModoProjPath + "//renderData" )
        os.mkdir(self.ModoProjPath + "//renderData//IrradianceCaches" )
        os.mkdir(self.ModoProjPath + "//renderScenes" )
        os.mkdir(self.ModoProjPath + "//scenes" )
        os.mkdir(self.ModoProjPath + "//sourceimages" )
        os.mkdir(self.ModoProjPath + "//textures" )
        os.mkdir(self.ModoProjPath + "//renders" )
        
        file = open(self.ModoProjPath + '//.luxproject', 'w')
        file.write('#LXProject#\n')
        file.write('Associate image Images\n')
        file.write('Associate irrad renderDatas/IrradianceCaches\n')
        file.write('Associate image@render renders\n')
        file.write('Associate movie@render renders\n')
        file.write('Associate scene Scenes\n')
        file.close
    
if __name__ == "__main__":
    project = sys.argv[1]
    model.setup_all()
    proj = model.Project.get_by(Name=unicode(project))
    for Seq in proj.Seqs:
        for shot in Seq.Shots:
            print "making directory for:" + shot.Name
            a = mkShotFolder(proj.Name,shot.Name)

        