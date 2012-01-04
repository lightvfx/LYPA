############################################################################################
# LYPA alpha version 001 by Antoine Moulineau.
#-------------------------------------------------------------------------------------
# very simple mudule to read and write with JSON global and user variables in every modules.
# 
# Not used yet, needs integration.
# some variables are still hardcoded.
############################################################################################

import sys
import json
import os
class config():
    def __init__(self):
        #print murf
        self.cfgFile = os.getcwd() + "\\LYPA.cfg"
        self.userCfgFile = os.getenv('USERPROFILE') + "\\LYPA.cfg"
        self.DBtype = "sqlite"
        self.DB     = "c:/DB/LYPA.sqlite"
        self.user   = ""
        self.passw   = ""
        self.DBbind = self.DBtype + ":///" + self.DB
        self.contentDirectory = "j:/"
        self.filmSt = "@contentDirectory/film/"
        self.CGprojectFileSt = ""
        self.googleLogin = ""
        self.googlePWD = ""
        self.cfg = {'DBtype': self.DBtype, 'DB': self.DB, 'user' : self.user, 'passw' : self.passw,
        'contentDirectory' :self.contentDirectory,'googleLogin': self.googleLogin,
        'googlePWD': self.googlePWD}
        ######################################################
        ##User cfg
        ####################################################
        self.currentProject = "none"
        self.UserCfg = {'currentProject': self.currentProject}
        
    def write_cfg(self):
        f = open(self.cfgFile,'w')
        json.dump(self.cfg,f,sort_keys=True)
        f.close
               
    def read_cfg(self):
        f = open(self.cfgFile,r)
        json.dump(f)
        f.close()
    
    def write_UserCfg(self):
        f = open(self.userCfgFile,'w')
        json.dump(self.UserCfg,f,sort_keys=True)
        f.close
               
    def read_UserCfg(self):
        f = open(self.userCfgFile,r)
        json.dump(f)
        f.close()
        


if __name__ == '__main__':
    
    #print file
    cfg = config()
    print cfg.DBbind
    cfg.write_cfg()
    cfg.write_UserCfg()
    