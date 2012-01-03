# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'commentBrowser.ui'
#
# Created: Sat Sep 10 16:38:47 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(1249, 425)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_3.setMargin(2)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.frame = QtGui.QFrame(self.widget)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setLineWidth(1)
        self.frame.setMidLineWidth(1)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setMargin(0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setMaximumSize(QtCore.QSize(60, 16777215))
        self.label.setText(QtGui.QApplication.translate("Form", "session", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.ProjectComboBox = QtGui.QComboBox(self.frame)
        self.ProjectComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ProjectComboBox.setEditable(False)
        self.ProjectComboBox.setFrame(False)
        self.ProjectComboBox.setObjectName(_fromUtf8("ProjectComboBox"))
        self.gridLayout.addWidget(self.ProjectComboBox, 1, 1, 1, 1)
        self.refreshPushButton = QtGui.QPushButton(self.frame)
        self.refreshPushButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.refreshPushButton.setText(QtGui.QApplication.translate("Form", "refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.refreshPushButton.setObjectName(_fromUtf8("refreshPushButton"))
        self.gridLayout.addWidget(self.refreshPushButton, 1, 2, 1, 1)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setMinimumSize(QtCore.QSize(50, 0))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout.addWidget(self.frame_2, 1, 3, 1, 1)
        self.verticalLayout_3.addWidget(self.frame)
        self.list = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setMinimumSize(QtCore.QSize(0, 0))
        self.list.setFrameShape(QtGui.QFrame.StyledPanel)
        self.list.setFrameShadow(QtGui.QFrame.Plain)
        self.list.setLineWidth(0)
        self.list.setAutoScroll(False)
        self.list.setTabKeyNavigation(False)
        self.list.setAlternatingRowColors(True)
        self.list.setRootIsDecorated(True)
        self.list.setUniformRowHeights(True)
        self.list.setAnimated(True)
        self.list.setAllColumnsShowFocus(False)
        self.list.setWordWrap(True)
        self.list.setExpandsOnDoubleClick(False)
        self.list.setObjectName(_fromUtf8("list"))
        self.list.headerItem().setText(0, QtGui.QApplication.translate("Form", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(1, QtGui.QApplication.translate("Form", "shot", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(2, QtGui.QApplication.translate("Form", "user", None, QtGui.QApplication.UnicodeUTF8))
        self.list.header().setCascadingSectionResizes(False)
        self.list.header().setDefaultSectionSize(50)
        self.list.header().setHighlightSections(True)
        self.list.header().setMinimumSectionSize(40)
        self.list.header().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.list)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.refreshPushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Form.refresh)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.list.setSortingEnabled(True)

