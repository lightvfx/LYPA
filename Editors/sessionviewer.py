# -*- coding: utf-8 -*-

"""A custom widget that edits a task's properties"""

# Import Qt modules
from PyQt4 import QtCore,QtGui

# Import the compiled UI module
from sessionViewerUI import Ui_Form
try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
import sys
from PyQt4 import QtGui, QtCore
import os
#import nukeSS
import atom
import gdata.spreadsheet.text_db
import gdata.calendar.data
import gdata.calendar.client
import gdata.acl.data
try:
  from xml.etree import ElementTree
except ImportError:
  from elementtree import ElementTree
# The backend
#import model

# Misc.

class sessionViewer(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)

        self.ui=Ui_Form()
        self.ui.setupUi(self)
       
    
    def _PrintAllEventsOnDefaultCalendar(self):
        #text_query=
        #calendar.id = atom.data.Id(text='8lglqkn2teder5d3ek4fuku0a0@group.calendar.google.com')
        a = []
        feed = self.cal_client.GetCalendarEventFeed("")
        #print 'Events on Primary Calendar: %s' % (feed.title.text,)
        for i, an_event in zip(xrange(len(feed.entry)), feed.entry):
            a.append(an_event.title.text)
        return a
    
    def refreshCal(self):
        self.cal_client = gdata.calendar.client.CalendarClient(source='')
        self.cal_client.ClientLogin('', '', self.cal_client.source);
        self.ui.SessionSelectTreeWidget.clear()
       #self._InsertCalendar()
        #print a
        #records = self.table.GetRecords(1,10000)
        records = self._PrintAllEventsOnDefaultCalendar()
        # Start with no task item to edit
       
        for record in records:
            rec  = record
            item= QtGui.QTreeWidgetItem()
            item.setText(0, rec)
            self.ui.SessionSelectTreeWidget.addTopLevelItem(item)
        
        for column in range( self.ui.SessionSelectTreeWidget.columnCount()):   
        	 self.ui.SessionSelectTreeWidget.resizeColumnToContents(column)