# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoViewer.ui'
#
# Created: Fri Dec 09 20:30:03 2011
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
        Form.resize(616, 715)
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
        self.tabWidget = QtGui.QTabWidget(self.widget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.InfoTab = QtGui.QWidget()
        self.InfoTab.setObjectName(_fromUtf8("InfoTab"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.InfoTab)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.scrollArea = QtGui.QScrollArea(self.InfoTab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 604, 683))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setMargin(2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.groupBox_5 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_5.setMaximumSize(QtCore.QSize(270, 16777215))
        self.groupBox_5.setTitle(QtGui.QApplication.translate("Form", "thumbnail", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_5)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setMargin(2)
        self.formLayout_2.setSpacing(2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.thumbnailLabel = QtGui.QLabel(self.groupBox_5)
        self.thumbnailLabel.setMinimumSize(QtCore.QSize(256, 256))
        self.thumbnailLabel.setMaximumSize(QtCore.QSize(256, 256))
        self.thumbnailLabel.setText(_fromUtf8(""))
        self.thumbnailLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.thumbnailLabel.setObjectName(_fromUtf8("thumbnailLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.thumbnailLabel)
        self.horizontalLayout.addWidget(self.groupBox_5)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setMargin(2)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.InfoTab, _fromUtf8(""))
        self.PaletteTab = QtGui.QWidget()
        self.PaletteTab.setObjectName(_fromUtf8("PaletteTab"))
        self.tabWidget.addTab(self.PaletteTab, _fromUtf8(""))
        self.Histogram = QtGui.QWidget()
        self.Histogram.setObjectName(_fromUtf8("Histogram"))
        self.tabWidget.addTab(self.Histogram, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.verticalLayout.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.InfoTab), QtGui.QApplication.translate("Form", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.PaletteTab), QtGui.QApplication.translate("Form", "Color palette", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Histogram), QtGui.QApplication.translate("Form", "Histogram", None, QtGui.QApplication.UnicodeUTF8))

