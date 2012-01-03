#!/usr/bin/env python

################################################################################
#
# HDREBackplate.py
#
# Version: 1.000
#
# Author: Gwynne Reddick
#
# Description:
# 
#
# Usage: 
#
# Last Update: time date
#
################################################################################

import sys
from os.path import basename, dirname, join, splitext

class PrefsParser(object):
    """ Encapsulates a windows style .ini file for both creation and reading.
    
    """
    def __init__(self):
        self.sections = {}

    def get_sections(self):
        """ returns the collection of section names found in the file
        
        """
        return self.sections.keys()

    def get_params(self, section):
        """ returns the parameters found for a particular section
        
        """
        return self.sections[section]

    def get_parameter(self, section, param):
        """ returns the named parameter from the named section
        
        """
        return self.sections[section][param]

    def has_section(self, section):
        """ True if the named section exists in the .ibl file
        
        """
        return section in self.sections

    def has_parameter(self, section, param):
        """ returns True if the named parameter exists in the named section
        
        """
        return param in self.sections[section]

    def add_section(self, label):
        """ add a new empty section
        
        """
        self.sections[label] = {}

    def add_parameter(self, section, param, value):
        """ add a new parameter/value pair to a section
        
        """
        self.sections[section][param] = value

    def add_parameters(self, section, params):
        """ add a dictionary of parameters to a section. If the section is empty
            (new) the params will be added, if it already contains parameters
            then the contents of params will be appended. The value of any
            parameters in the section that have the same name as parameters in
            params will be updated (replaced) with the value from params
            
        """
        self.sections[section].update(params)

    def read(self, filename):
        """ parse the provided file and build a collection of sections and their
            parameters
            
        """
        contents = []
        try:
            f_in = open(filename, 'r')
        except:
            exc_log()

        for line in f_in:
            if line.startswith('['):
                currsection = line.strip('[]\n\r')
                self.sections[currsection] = {}
            elif line.startswith('--') or line.startswith('SDR') or line.strip('\n\r') == '':
                continue
            else:
                values = line.rstrip().split(' = ')
                if len(values) == 1:
                    self.sections[currsection][values[0]] = None
                elif len(values) == 2:
                    self.sections[currsection][values[0]] = values[1].strip('"')
        f_in.close()

    def write(self, filename, sorted=False):
        """ write the current config object to disk. If sorted is true, the file
            sections will be written in alphabetical order
            
        """
        try:
            f_out = open(filename, 'w')
        except:
            exc_log()
        if sorted:
            keys = self.sections.keys()
            keys.sort()
            try:
                for key in keys:
                    f_out.write('[%s]\n' %  key)
                    for item in self.sections[key].items():
                        f_out.write('%s = %s\n' % (item[0], item[1]))
                    f_out.write(linesep)
            except:
                exc_log()
        else:
            try:
                for section in self.sections:
                    f_out.write('[%s]\n' %  section)
                    for item in self.sections[section].items():
                        f_out.write('%s = %s\n' % (item[0], item[1]))
                    f_out.write('\n')
            except:
                exc_log()
        f_out.close()


def exc_log(script='SetbackplateImage.py'):
    """ Utility function to print out usefull debug info to the event log from
        a try/except clause

        script - name of the script we're being called from, defaults to this module's name

    """
    lx.out('Exception "%s" on line: %d in: %s' % (sys.exc_value, sys.exc_traceback.tb_lineno, script))


def itemexists(name):
        lx.eval('select.item %s set' % name)
        selected = lx.evalN('item.name ?')
        return name in selected


def lockcamera():
    if not itemexists('HDRECam_Grp'):
        lx.eval('select.drop item')
        lx.eval('group.create')
        lx.eval('item.name HDRECam_Grp')
        lx.eval('select.subItem HDRECam set camera')
        lx.eval('!!group.edit add item')
    lx.eval('select.item HDRECam_Grp set')
    lx.eval('!!item.channel lock on item:HDRECam_Grp')


def lockanimcamera():
    if not itemexists('HDRECamAnimate_Grp'):
        lx.eval('select.drop item')
        lx.eval('group.create')
        lx.eval('item.name HDRECamAnimate_Grp')
    xfrmitem = lx.eval('query sceneservice item.xfrmPos ? HDRECamAnimate')
    lx.eval('select.channel {%s:pos.X} set' % xfrmitem)
    lx.eval('select.channel {%s:pos.Y} add' % xfrmitem)
    lx.eval('select.channel {%s:pos.Z} add' % xfrmitem)
    lx.eval('!!group.edit add chan')
    lx.eval('!!item.channel lock on item:HDRECamAnimate_Grp')


def unlockcamera(group):
    if itemexists(group):
        lx.eval('select.item %s set' % group)
        lx.eval('item.channel lock off item:%s' % group)


def check_xfrms(item):
    try:
        lx.eval('!!item.channel pos.X ? item:%s' % item)
    except:
        lx.eval('transform.add pos item:%s' % item)
    try:
       lx.eval('!!item.channel rot.X ? item:%s' % item)
    except:
        lx.eval('transform.add rot item:%s' % item)
    try:
       lx.eval('!!item.channel scl.X ? item:%s' % item)
    except:
        try:
            lx.eval('!!transform.add scl item:%s' % item)
        except:
            pass




# Script -----------------------------------------------------------------------

try:
    args = lx.args()
    if len(args) != 2:
        raise Exception('Wrong number of arguments given')
    
    config_path = args[0]
    backplate = args[1]
    assets = lx.eval('query platformservice path.path ? Asset')
    config_path = join(assets, config_path)
    
    # unlock the camera
    unlockcamera('HDRECam_Grp')
    unlockcamera('HDRECamAnimate_Grp')
    # lets get a list of scene item names so we can check if our HDRE items exist or not
    types = ['sunLight', 'camera', 'environment', 'mesh']
    scene_items = set()
    num_sceneitems = lx.eval('query sceneservice item.N ? all')
    for x in xrange(num_sceneitems):
        if lx.eval('query sceneservice item.type ? %s' % x) in types:
            scene_items.add(lx.eval('query sceneservice item.name ? %s' % x))
    
    # read the config file
    cfg = PrefsParser()
    cfg.read(config_path)
    
    if backplate not in cfg.get_sections():
        raise Exception('Backplate definition not found in configuration file')
    
    # get scene attributes
    scene_gamma = None
    image_gamma = None
    if 'scene' in cfg.get_sections():
        scene_gamma = cfg.get_parameter('scene', 'Scene Gamma')
        image_gamma = cfg.get_parameter('scene', 'Image Gamma')
        bg_image_dir = join(assets, 'Images', cfg.get_parameter('scene', 'Kit'), cfg.get_parameter('scene', 'Location'), 'BG-Images')
    
    # load the backplate image
    bg_image = backplate + '.png'
    lx.eval('clip.addStill {%s}' % join(bg_image_dir, bg_image))
    
    # set up the backplate image
    try:
        lx.eval('query sceneservice item.ID ? HDREBackplate')
    except:
        lx.eval('item.create environment')
        lx.eval('item.name HDREBackplate')

    #layers = lx.eval1('query sceneservice item.children ? HDREBackplate')
    #for layer in layers:
        #if lx.eval('query sceneservice item.type ? %s' % layer) == 'imageMap':
    layer = lx.eval1('query sceneservice item.children ? HDREBackplate')
    lx.eval('select.item {%s} set' % layer)
    lx.eval('item.name {Backplate_Img}') 
    lx.eval('select.item %s set' % layer)
    lx.eval('item.setType imageMap textureLayer')
    lx.eval('item.channel gamma 0.454 item:{Backplate_Img}')
    lx.eval('item.channel alpha ignore item:{Backplate_Img}')
    lx.eval('item.channel aa false item:{Backplate_Img}')
    oldimage = lx.eval1('texture.setIMap ?')
    lx.eval('texture.setIMap {%s}' % backplate)
    locID = lx.eval('texture.setLocator Backplate_Img ?')
    lx.eval('select.item {%s} set' % locID)
    lx.eval('texture.setProj fr')
    lx.eval('texture.setCamera {HDRECam}')
    
    clip_width = None
    clip_height = None
    # set render frame size and film back aspect aspect
    clips = lx.evalN('query layerservice clips ? all')
    for clip in clips:
        if lx.eval('query layerservice clip.name ? {%s}' % clip) == backplate:
            info = lx.eval('query layerservice clip.info ? {%s}' % clip).split()
            clip_width = float(info[1].split(':')[1])
            clip_height = float(info[2].split(':')[1])
    
            if clip_width != None and clip_height != None:
                if clip_width > clip_height:
                    frame_width = 1024
                    frame_height = int((clip_height/clip_width) * 1024)
                else:
                    frame_height = 1024
                    frame_width = int((clip_width/clip_height) * 1024)
                lx.eval('render.res 0 %s' % frame_width)
                lx.eval('render.res 1 %s' % frame_height)
                filmback = cfg.get_parameter(backplate, 'filmback')
                film_width, film_height  = filmback.split(',')
                lx.eval('item.channel apertureY [%s mm] item:{HDRECam}' % film_height)
                lx.eval('item.channel apertureX [%s mm] item:{HDRECam}' % film_width)
                lx.eval('item.channel apertureY [%s mm] item:{HDRECamAnimate}' % film_height)
                lx.eval('item.channel apertureX [%s mm] item:{HDRECamAnimate}' % film_width)
    
    # delete the old backplate
    if oldimage != '(none)' and oldimage != backplate:
        lx.eval('select.drop item')
        lx.eval('select.item {%s} set' % oldimage)
        lx.eval('clip.delete')
    
    # turn off visible to camera for other environment layers
    num_env_items = lx.eval('query sceneservice environment.N ? all')
    for x in xrange(num_env_items):
        env = lx.eval('query sceneservice environment.name ? %s' % x)
        if env != 'HDREBackplate':
            lx.eval('item.channel visCam false item:{%s}' % env)
            
    # set up Sun
    if 'HDRESun' in scene_items:
        sunparams = cfg.get_parameter(backplate, 'HDRESun')
        if sunparams != '':
            suntime, sunday, noffset = sunparams.split(',')
            if lx.eval('item.channel sunPos ? item:HDRESun') == 0:
                lx.eval('item.channel sunPos true item:HDRESun')
            lx.eval('item.channel north %s item:HDRESun' % noffset)
            lx.eval('item.channel time {%s} item:HDRESun' % suntime)
            lx.eval('item.channel day {%s} item:HDRESun' % sunday)
    
    # set up environment
    if 'HDREEnv' in scene_items:
        envparams = cfg.get_parameter(backplate, 'HDREEnv')
        if envparams != '':
            posX, posY, posZ, rotX, rotY, rotZ, sclX, sclY, sclZ = envparams.split(',')
            children = lx.eval('query sceneservice environment.children ? HDREEnv')
            for child in children:
                if lx.eval('query sceneservice item.type ? %s' % child) == 'imageMap':
                    envimage = child
                    break
            lx.eval('select.item %s set' % envimage)
            loc = lx.eval('texture.setLocator %s ?' % envimage)
            lx.eval('select.item {%s} set' % loc)
            lx.eval('item.channel rot.Y {%s}' % rotY)

    # set up reflection image if specified
    if cfg.has_parameter(backplate, 'reflimg'):
        reflimg = cfg.get_parameter(backplate, 'reflimg')
        if reflimg != '':
            children = lx.evalN('query sceneservice environment.children ? HDRERefl')
            for child in children:
                if lx.eval('query sceneservice item.type ? %s' % child) == 'imageMap':
                    imglayer = child
                    break
            lx.eval('select.item {%s} set' % imglayer)
            oldimage = lx.eval1('texture.setIMap ?')
            # delete the old reflection image
            if oldimage != '(none)':
                lx.eval('select.drop item')
                lx.eval('select.item {%s} set' % oldimage)
                lx.eval('clip.delete')
            lx.eval('clip.addStill {%s}' % join(bg_image_dir, reflimg))
            lx.eval('select.item {%s} set' % imglayer)
            lx.eval('item.name {Reflection_Img}') 
            lx.eval('texture.setIMap {%s}' % splitext(reflimg)[0])
    
    # set up camera
    if 'HDRECam' in scene_items:
        camparams = cfg.get_parameter(backplate, 'HDRECam')
        if camparams != '':
            posX, posY, posZ, rotX, rotY, rotZ, flength, fdist, fstop = camparams.split(',')
            check_xfrms('HDRECam')
            lx.eval('item.channel pos.X {%s} item:HDRECam' % posX)
            lx.eval('item.channel pos.Y {%s} item:HDRECam' % posY)
            lx.eval('item.channel pos.Z {%s} item:HDRECam' % posZ)
            lx.eval('item.channel rot.X {%s} item:HDRECam' % rotX)
            lx.eval('item.channel rot.Y {%s} item:HDRECam' % rotY)
            lx.eval('item.channel rot.Z {%s} item:HDRECam' % rotZ)
            lx.eval('item.channel focalLen [%s mm] item:HDRECam' % flength)
            lx.eval('item.channel dof true item:Render')
            lx.eval('item.channel focusDist %s item:HDRECam' % fdist)
            lx.eval('item.channel fStop %s item:HDRECam' % fstop)
            lx.eval('item.channel dof false item:Render')

    # set up animation camera
    if 'HDRECamAnimate' in scene_items:
        camparams = cfg.get_parameter(backplate, 'HDRECam')
        if camparams != '':
            check_xfrms('HDRECamAnimate')
            posX, posY, posZ, rotX, rotY, rotZ, flength, fdist, fstop = camparams.split(',')
            lx.eval('item.channel pos.X {%s} item:HDRECamAnimate' % posX)
            lx.eval('item.channel pos.Y {%s} item:HDRECamAnimate' % posY)
            lx.eval('item.channel pos.Z {%s} item:HDRECamAnimate' % posZ)
            lx.eval('item.channel rot.X {%s} item:HDRECamAnimate' % rotX)
            lx.eval('item.channel rot.Y {%s} item:HDRECamAnimate' % rotY)
            lx.eval('item.channel rot.Z {%s} item:HDRECamAnimate' % rotZ)
            flength = float(flength)
            if flength >= 101 and flength <= 200:
                flength = flength + 100
            elif flength >= 51 and flength <= 100:
                flength = flength + 50
            elif flength >= 18 and flength <= 50:
                flength = flength + 10
            lx.eval('item.channel focalLen [%s mm] item:HDRECamAnimate' % flength)
            lx.eval('item.channel dof true item:Render')
            lx.eval('item.channel focusDist %s item:HDRECamAnimate' % fdist)
            lx.eval('item.channel fStop %s item:HDRECamAnimate' % fstop)
            lx.eval('item.channel dof false item:Render')
    
    # set up shadow ground
    if 'HDREShadowGround' in scene_items:
        shadowparams = cfg.get_parameter(backplate, 'HDREShadowGround')
        if shadowparams != '':
            posX, posY, posZ, rotX, rotY, rotZ, sclX, sclY, sclZ = shadowparams.split(',')
            check_xfrms('HDREShadowGround')
            lx.eval('item.channel pos.X {%s} item:HDREShadowGround' % posX)
            lx.eval('item.channel pos.Y {%s} item:HDREShadowGround' % posY)
            lx.eval('item.channel pos.Z {%s} item:HDREShadowGround' % posZ)
            lx.eval('item.channel rot.X {%s} item:HDREShadowGround' % rotX)
            lx.eval('item.channel rot.Y {%s} item:HDREShadowGround' % rotY)
            lx.eval('item.channel rot.Z {%s} item:HDREShadowGround' % rotZ)
            lx.eval('item.channel scl.X [%s %%] item:HDREShadowGround' % sclX)
            lx.eval('item.channel scl.Y [%s %%] item:HDREShadowGround' % sclY)
            lx.eval('item.channel scl.Z [%s %%] item:HDREShadowGround' % sclZ)
    
    # set up water object
    if 'HDREWater' in scene_items:
        waterparams = cfg.get_parameter(backplate, 'HDREWater')
        if waterparams != '':
            check_xfrms('HDREWater')
            posX, posY, posZ, rotX, rotY, rotZ, sclX, sclY, sclZ = waterparams.split(',')
            lx.eval('item.channel pos.X {%s} item:HDREWater' % posX)
            lx.eval('item.channel pos.Y {%s} item:HDREWater' % posY)
            lx.eval('item.channel pos.Z {%s} item:HDREWater' % posZ)
            lx.eval('item.channel rot.X {%s} item:HDREWater' % rotX)
            lx.eval('item.channel rot.Y {%s} item:HDREWater' % rotY)
            lx.eval('item.channel rot.Z {%s} item:HDREWater' % rotZ)
            lx.eval('item.channel scl.X [%s %%] item:HDREWater' % sclX)
            lx.eval('item.channel scl.Y [%s %%] item:HDREWater' % sclY)
            lx.eval('item.channel scl.Z [%s %%] item:HDREWater' % sclZ)
    
    # set up shadow object if there is one
    if 'HDREShadowObject' in scene_items:
        shadowparams = cfg.get_parameter(backplate, 'HDREShadowObject')
        if shadowparams != '':
            check_xfrms('HDREShadowObject')
            posX, posY, posZ, rotX, rotY, rotZ, sclX, sclY, sclZ = shadowparams.split(',')
            lx.eval('item.channel pos.X %s item:HDREShadowObject' % posX)
            lx.eval('item.channel pos.Y %s item:HDREShadowObject' % posY)
            lx.eval('item.channel pos.Z %s item:HDREShadowObject' % posZ)
            lx.eval('item.channel rot.X %s item:HDREShadowObject' % rotX)
            lx.eval('item.channel rot.Y %s item:HDREShadowObject' % rotY)
            lx.eval('item.channel rot.Z %s item:HDREShadowObject' % rotZ)
            lx.eval('item.channel scl.X [%s %%] item:HDREShadowObject' % sclX)
            lx.eval('item.channel scl.Y [%s %%] item:HDREShadowObject' % sclY)
            lx.eval('item.channel scl.Z [%s %%] item:HDREShadowObject' % sclZ)
            
    
    # set the scene gamma
    if scene_gamma != None:
        numouts = lx.eval('query sceneservice renderOutput.N ? all')
        for x in xrange(numouts):
            id = lx.eval('query sceneservice renderOutput.ID ? %s' % x)
            lx.eval('select.item %s set' % id)
            if lx.eval('shader.setEffect ?') == 'shade.color':
                lx.eval('item.channel gamma %s item:%s' % (scene_gamma, id))
    
    # lock the camera again
    lockcamera()
    lockanimcamera()
except:
    exc_log()



