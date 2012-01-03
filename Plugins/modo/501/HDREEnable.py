#!/usr/bin/env python

################################################################################
#
# HDREEnable.py
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
# Last Update 16:49 08/12/10 
#
################################################################################

# part of a hack for later on so we can identify if a second HDRE assembly has been applied
camnames = {'HDRECam (2)':' (2)',
        'HDRECam(2)':'(2)',
        'HDRECam 2':' 2',
        'HDRECam_2':'_2',
        'HDRECam2':'2'}

HDREEnvs = ['HDRERefl', 'HDREBackplate', 'HDREEnv']

def itemexists(name):
        lx.eval('select.item {%s} set' % name)
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
    lx.eval('item.channel lock on item:HDRECam_Grp')

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
    lx.eval('item.channel lock on item:HDRECamAnimate_Grp')
        

def hastag(item):
    lx.eval('select.drop item')
    lx.eval('select.item {%s} set' % item)
    if lx.eval('item.tag HDRE ?') == 'set':
        return true

def clearold():
    try:
        numenvs = lx.eval('query sceneservice environment.N ? all')
        envs = []
        oldclips = []
        for x in xrange(numenvs):
            envs.append(lx.eval('query sceneservice environment.ID ? %s' % x))
        # need a hack here to work round what appears to be a bug. We need to collect a
        # list of clips to delete after deleting the env items. For some reason we have
        # to collect the list in one loop, then delete the env items in a second loop
        # otherwise querying the env refl image returns None. I think this is because the
        # env image layer is originally an instance
        for env in envs:
            lx.eval('select.item %s set' % env)
            if lx.eval('item.tag string HDRE ?') == 'set':
                layer, process = lx.eval('query sceneservice mask.children ? {%s}' % env)
                lx.eval('select.item {%s} set' % layer)
                oldclips.append(lx.eval('texture.setIMap ?'))
        # now delete the env items
        for env in envs:
            lx.eval('select.item %s set' % env)
            if lx.eval('item.tag string HDRE ?') == 'set':
                lx.eval('!!item.delete')
        numgrplocs = lx.eval('query sceneservice groupLocator.N ? all')
        grplocs = []
        for x in xrange(numgrplocs):
            grplocs.append(lx.eval('query sceneservice groupLocator.ID ? %s' % x))
        for loc in grplocs:
            lx.eval('select.item %s set' % loc)
            if lx.eval('item.tag string HDRE ?') == 'set':
                lx.eval('!!item.delete')
                break
        
        # clear old ground and water material groups
        lx.eval('select.itemPattern HDREGroup')
        id = lx.eval1('query sceneservice selection ? mask')
        parent = lx.eval('query sceneservice mask.parent ? %s' % id)
        lx.eval('select.item %s set' % parent)
        lx.eval('texture.delete')
        
        # clear old clips
        for clip in oldclips:
            lx.eval('select.drop item')
            lx.eval('select.item {%s} set' % clip)
            lx.eval('clip.delete')
    except:
        lx.out('Exception "%s" on line: %d' % (sys.exc_value, sys.exc_traceback.tb_lineno))

def renamenew(incr):
    try:
        lx.eval('item.name HDRECam item:{HDRECam%s}' % incr)
        lx.eval('item.name HDRECamAnimate item:{HDRECamAnimate%s}' % incr)
        lx.eval('item.name HDRESun item:{HDRESun%s}' % incr)
        lx.eval('item.name HDRERefl item:{HDRERefl%s}' % incr)
        lx.eval('item.name HDREBackplate item:{HDREBackplate%s}' % incr)
        lx.eval('item.name HDREEnv item:{HDREEnv%s}' % incr)
        lx.eval('item.name {HDREActivate} item:{HDREActivate%s}' % incr)
        lx.eval('item.name {HDREWater} item:{HDREWater%s}' % incr)
        lx.eval('item.name {HDREShadowGround} item:{HDREShadowGround%s}' % incr)
        lx.eval('item.name {HDREControls} item:{HDREControls%s}' % incr)
        lx.eval('item.name {BackdropBrowser} item:{BackdropBrowser%s}' % incr)
        lx.eval('item.name {Texture Group} item:{Texture Group%s}' % incr)
        lx.eval('item.name {HDREGroup} item:{HDREGroup%s}' % incr)
        # rename the parent group
        root = lx.eval('query sceneservice item.parent ? HDRECam')
        rootname = lx.eval('query sceneservice item.name ? %s' % root)
        newname = rootname.split(incr)[0]
        lx.eval('item.name {%s} item:{%s}' % (newname, rootname))

    except:
        lx.out('Exception "%s" on line: %d' % (sys.exc_value, sys.exc_traceback.tb_lineno))

def tagitems():
    try:
        lx.eval('select.drop item')
        for item in HDREEnvs:
            lx.eval('select.item {%s} set' % item)
            lx.eval('item.tag string {HDRE} {set}')
        lx.eval('select.item {%s} set' % rootID)
        lx.eval('item.tag string {HDRE} {set}')
    except:
        lx.out('Exception "%s" on line: %d' % (sys.exc_value, sys.exc_traceback.tb_lineno))
    

def setframesize():
    try:
        backplate = None
        # find the backplate
        envchildren = lx.eval('query sceneservice item.children ? HDREBackplate')
        for child in envchildren:
            if lx.eval('query sceneservice item.type ? {%s}' % child) == 'imageMap':
                lx.eval('select.item %s set' % child)
                backplate = lx.eval('texture.setIMap ?')
                break
        if backplate:
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
    except:
        lx.out('Exception "%s" on line: %d' % (sys.exc_value, sys.exc_traceback.tb_lineno))

try:
    # close previously open backdrop browser if there is one
    if lx.eval('query scriptsysservice userValue.isDefined ? HDRE_Card'):
        cookie = lx.eval('user.value HDRE_Card ?')
        lx.eval('layout.createOrClose {%s} open:0' % cookie)
        
    selectedItem = lx.eval1('query sceneservice selection ? locator')
    rootID = lx.eval('query sceneservice item.parent ? %s' % selectedItem)
    
    # check to see if an HDRE environment already exists and clear it out if it does.
    # this is a bit of a hack, we have to test to see if one of our known items exists
    # with an incremented name. If it does we delete all HDRE items with names that
    # are not incremented and then rename all the ones that are - YUK!!!!
    
    numcams = lx.eval('query sceneservice camera.N ? all')
    for x in xrange(numcams):
        camname = lx.eval('query sceneservice camera.name ? %s' % x)
        if camname in camnames.keys():
            incr = camnames[camname]
            clearold()
            renamenew(incr)
            break
    
    if itemexists('HDRECam'):
        # set animate camera focal length
        if itemexists('HDRECamAnimate'):
            flength = round(lx.eval('item.channel focalLen ? item:HDRECam'), 3) * 1000
            if flength >= 101 and flength <= 200:
                flength = flength + 100
            elif flength >= 51 and flength <= 100:
                flength = flength + 50
            elif flength >= 18 and flength <= 50:
                flength = flength + 10
            lx.eval('item.channel focalLen [%s mm] item:HDRECamAnimate' % flength)
            lx.eval('render.camera HDRECamAnimate')
            lockanimcamera()
        lx.eval('render.camera HDRECam')
        # group and lock the camera
        lockcamera()
        
    renID = lx.eval('query sceneservice polyRender.ID ? 0')
    lx.eval('item.channel globEnable true item:%s' % renID)
    lx.eval('item.channel dispRate 3 item:%s' % renID)
    lx.eval('item.channel dispRatio 8 item:%s' % renID)
    # set the scene gamma
    numouts = lx.eval('query sceneservice renderOutput.N ? all')
    for x in xrange(numouts):
        id = lx.eval('query sceneservice renderOutput.ID ? %s' % x)
        lx.eval('select.item %s set' % id)
        if lx.eval('shader.setEffect ?') == 'shade.color':
            lx.eval('item.channel gamma 2.2 item:%s' % id)
    
    num_envs = lx.eval('query sceneservice environment.N ? all')
    environments = []
    for x in xrange(num_envs):
        environments.append(lx.eval('query sceneservice environment.name ? %s' % x))
    for env in environments:
        if env not in HDREEnvs:
            lx.eval('item.channel visCam false item:{%s}' % env)
            lx.eval('item.channel visInd false item:{%s}' % env)
            lx.eval('item.channel visRefl false item:{%s}' % env)
            lx.eval('item.channel visRefr false item:{%s}' % env)
    
    numlights = lx.eval('query sceneservice light.N ? all')
    for x in xrange(numlights):
        if lx.eval('query sceneservice light.name ? %s' % x) != 'HDRESun':
            id = lx.eval('query sceneservice light.ID ? %s' % x)
            lx.eval('layer.setVisibility {%s} 0' % id)
    
    if itemexists('HDREActivate'):
        lx.eval('layer.setVisibility {HDREActivate} 0')
    
    controlsID =  lx.eval('query sceneservice item.ID ? HDREControls')
    if controlsID:
        lx.eval('layer.setVisibility {%s} 1' % controlsID)
    
    # set render frame size
    setframesize()
    tagitems()
    
except:
    lx.out('Exception "%s" on line: %d' % (sys.exc_value, sys.exc_traceback.tb_lineno))
