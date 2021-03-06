# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shotmanager.ui'
#
# Created: Sat Nov 26 23:40:33 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(989, 449)
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Shot Manager", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/todo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setMargin(3)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.splitter.setLineWidth(4)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setOpaqueResize(False)
        self.splitter.setHandleWidth(10)
        self.splitter.setChildrenCollapsible(True)
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
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setMargin(1)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setVerticalSpacing(5)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.ProjectComboBox = QtGui.QComboBox(self.frame)
        self.ProjectComboBox.setEditable(False)
        self.ProjectComboBox.setFrame(False)
        self.ProjectComboBox.setObjectName(_fromUtf8("ProjectComboBox"))
        self.gridLayout.addWidget(self.ProjectComboBox, 0, 1, 1, 1)
        self.SequComboBox = QtGui.QComboBox(self.frame)
        self.SequComboBox.setMaximumSize(QtCore.QSize(748, 16777215))
        self.SequComboBox.setObjectName(_fromUtf8("SequComboBox"))
        self.gridLayout.addWidget(self.SequComboBox, 0, 4, 1, 1)
        self.label = QtGui.QLabel(self.frame)
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Select Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Select Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout.addWidget(self.frame_2, 0, 5, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout.setColumnMinimumWidth(1, 50)
        self.gridLayout.setColumnMinimumWidth(4, 50)
        self.gridLayout.setColumnMinimumWidth(5, 300)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_3.addWidget(self.frame)
        self.list = QtGui.QTreeWidget(self.widget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.list.sizePolicy().hasHeightForWidth())
        self.list.setSizePolicy(sizePolicy)
        self.list.setMinimumSize(QtCore.QSize(400, 0))
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
        self.list.headerItem().setText(0, QtGui.QApplication.translate("MainWindow", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(1, QtGui.QApplication.translate("MainWindow", "In", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(2, QtGui.QApplication.translate("MainWindow", "Out", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(3, QtGui.QApplication.translate("MainWindow", "CutIn", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(4, QtGui.QApplication.translate("MainWindow", "CutOut", None, QtGui.QApplication.UnicodeUTF8))
        self.list.headerItem().setText(5, QtGui.QApplication.translate("MainWindow", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.list.header().setCascadingSectionResizes(False)
        self.list.header().setDefaultSectionSize(50)
        self.list.header().setHighlightSections(True)
        self.list.header().setMinimumSectionSize(40)
        self.list.header().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.list)
        self.editor = editor(self.splitter)
        self.editor.setEnabled(False)
        self.editor.setMaximumSize(QtCore.QSize(500, 16777215))
        self.editor.setObjectName(_fromUtf8("editor"))
        self.verticalLayout_2.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 30))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionDelete_Task = QtGui.QAction(MainWindow)
        self.actionDelete_Task.setEnabled(False)
        self.actionDelete_Task.setText(QtGui.QApplication.translate("MainWindow", "Delete Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Task.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDelete_Task.setObjectName(_fromUtf8("actionDelete_Task"))
        self.actionNew_Task = QtGui.QAction(MainWindow)
        self.actionNew_Task.setEnabled(False)
        self.actionNew_Task.setText(QtGui.QApplication.translate("MainWindow", "New Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Task.setObjectName(_fromUtf8("actionNew_Task"))
        self.actionUpdate_database = QtGui.QAction(MainWindow)
        self.actionUpdate_database.setEnabled(False)
        self.actionUpdate_database.setText(QtGui.QApplication.translate("MainWindow", "Update Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_database.setObjectName(_fromUtf8("actionUpdate_database"))
        self.actionEdit = QtGui.QAction(MainWindow)
        self.actionEdit.setCheckable(True)
        self.actionEdit.setText(QtGui.QApplication.translate("MainWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionNew_Sequence = QtGui.QAction(MainWindow)
        self.actionNew_Sequence.setEnabled(False)
        self.actionNew_Sequence.setText(QtGui.QApplication.translate("MainWindow", "New Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew_Sequence.setObjectName(_fromUtf8("actionNew_Sequence"))
        self.actionSet_project = QtGui.QAction(MainWindow)
        self.actionSet_project.setText(QtGui.QApplication.translate("MainWindow", "set Environment", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSet_project.setObjectName(_fromUtf8("actionSet_project"))
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSet_project)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionNew_Sequence)
        self.toolBar.addAction(self.actionNew_Task)
        self.toolBar.addAction(self.actionUpdate_database)
        self.toolBar.addAction(self.actionDelete_Task)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.list.setSortingEnabled(True)

from editor import editor
