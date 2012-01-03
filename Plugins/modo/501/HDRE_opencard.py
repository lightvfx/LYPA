#!/usr/bin/env python

################################################################################
#
# scriptname.py
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

try:
    cookie, layout, title, width, height = lx.args()
    if not lx.eval('query scriptsysservice userValue.isDefined ? HDRE_Card'):
        lx.eval('user.defNew HDRE_Card string temporary')
    lx.eval('user.value HDRE_Card {%s}' % cookie)
    lx.eval('layout.createOrClose {%s} {%s} true {%s} width:{%s} height:{%s} persistent:true style:palette' % (cookie, layout, title, width, height))
except:
    lx.out('Exception "%s" on line: %d' % (sys.exc_value, sys.exc_traceback.tb_lineno))