# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colorCorrect.ui'
#
# Created: Fri Dec 09 19:58:31 2011
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
        Form.resize(851, 718)
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(Form)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.scrollArea = QtGui.QScrollArea(Form)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 845, 712))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setMargin(2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.formLayout_7 = QtGui.QFormLayout()
        self.formLayout_7.setObjectName(_fromUtf8("formLayout_7"))
        self.pushButton = QtGui.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Save shot grade", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.LabelRole, self.pushButton)
        self.comboBox = QtGui.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.formLayout_7.setWidget(0, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.verticalLayout_3.addLayout(self.formLayout_7)
        self.groupBox = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 300))
        self.groupBox.setTitle(QtGui.QApplication.translate("Form", "Exposure", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout = QtGui.QFormLayout(self.groupBox)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(2)
        self.formLayout.setSpacing(2)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.ExpSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.ExpSB.setProperty("value", 1.0)
        self.ExpSB.setObjectName(_fromUtf8("ExpSB"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.ExpSB)
        self.ExpSL = QtGui.QSlider(self.groupBox)
        self.ExpSL.setProperty("value", 1)
        self.ExpSL.setOrientation(QtCore.Qt.Horizontal)
        self.ExpSL.setTickPosition(QtGui.QSlider.TicksBelow)
        self.ExpSL.setObjectName(_fromUtf8("ExpSL"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.ExpSL)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        self.rExpSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.rExpSB.setProperty("value", 1.0)
        self.rExpSB.setObjectName(_fromUtf8("rExpSB"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.rExpSB)
        self.rExpSL = QtGui.QSlider(self.groupBox)
        self.rExpSL.setProperty("value", 1)
        self.rExpSL.setOrientation(QtCore.Qt.Horizontal)
        self.rExpSL.setObjectName(_fromUtf8("rExpSL"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.rExpSL)
        self.gExpSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.gExpSB.setObjectName(_fromUtf8("gExpSB"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.gExpSB)
        self.gExpSL = QtGui.QSlider(self.groupBox)
        self.gExpSL.setOrientation(QtCore.Qt.Horizontal)
        self.gExpSL.setObjectName(_fromUtf8("gExpSL"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.gExpSL)
        self.bExpSB = QtGui.QDoubleSpinBox(self.groupBox)
        self.bExpSB.setObjectName(_fromUtf8("bExpSB"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.bExpSB)
        self.bExpSL = QtGui.QSlider(self.groupBox)
        self.bExpSL.setOrientation(QtCore.Qt.Horizontal)
        self.bExpSL.setObjectName(_fromUtf8("bExpSL"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.bExpSL)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.groupBox_3 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("Form", "lift", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox_3)
        self.formLayout_2.setMargin(2)
        self.formLayout_2.setSpacing(2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.doubleSpinBox_8)
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.doubleSpinBox_7)
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.doubleSpinBox_6)
        self.rLvlBSL = QtGui.QSlider(self.groupBox_3)
        self.rLvlBSL.setOrientation(QtCore.Qt.Horizontal)
        self.rLvlBSL.setObjectName(_fromUtf8("rLvlBSL"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.rLvlBSL)
        self.gLvlBSL = QtGui.QSlider(self.groupBox_3)
        self.gLvlBSL.setOrientation(QtCore.Qt.Horizontal)
        self.gLvlBSL.setObjectName(_fromUtf8("gLvlBSL"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.gLvlBSL)
        self.bLvlBSL = QtGui.QSlider(self.groupBox_3)
        self.bLvlBSL.setOrientation(QtCore.Qt.Horizontal)
        self.bLvlBSL.setObjectName(_fromUtf8("bLvlBSL"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.bLvlBSL)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.groupBox_2 = QtGui.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Form", "Gamma", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.formLayout_5 = QtGui.QFormLayout(self.groupBox_2)
        self.formLayout_5.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_5.setMargin(2)
        self.formLayout_5.setSpacing(2)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.doubleSpinBox_3)
        self.gammaSL = QtGui.QSlider(self.groupBox_2)
        self.gammaSL.setOrientation(QtCore.Qt.Horizontal)
        self.gammaSL.setObjectName(_fromUtf8("gammaSL"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.FieldRole, self.gammaSL)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_5.setItem(2, QtGui.QFormLayout.FieldRole, spacerItem1)
        self.label_14 = QtGui.QLabel(self.groupBox_2)
        self.label_14.setText(QtGui.QApplication.translate("Form", "Contrast", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.formLayout_5.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_14)
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.LabelRole, self.doubleSpinBox_4)
        self.horizontalSlider_15 = QtGui.QSlider(self.groupBox_2)
        self.horizontalSlider_15.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_15.setObjectName(_fromUtf8("horizontalSlider_15"))
        self.formLayout_5.setWidget(4, QtGui.QFormLayout.FieldRole, self.horizontalSlider_15)
        self.label_17 = QtGui.QLabel(self.groupBox_2)
        self.label_17.setText(QtGui.QApplication.translate("Form", "pivot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.formLayout_5.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_17)
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.LabelRole, self.doubleSpinBox_2)
        self.pivotSL = QtGui.QSlider(self.groupBox_2)
        self.pivotSL.setOrientation(QtCore.Qt.Horizontal)
        self.pivotSL.setObjectName(_fromUtf8("pivotSL"))
        self.formLayout_5.setWidget(6, QtGui.QFormLayout.FieldRole, self.pivotSL)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.formLayout_5.setItem(8, QtGui.QFormLayout.FieldRole, spacerItem2)
        self.label_16 = QtGui.QLabel(self.groupBox_2)
        self.label_16.setText(QtGui.QApplication.translate("Form", "Saturation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.formLayout_5.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_16)
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.LabelRole, self.doubleSpinBox)
        self.satSL = QtGui.QSlider(self.groupBox_2)
        self.satSL.setOrientation(QtCore.Qt.Horizontal)
        self.satSL.setObjectName(_fromUtf8("satSL"))
        self.formLayout_5.setWidget(10, QtGui.QFormLayout.FieldRole, self.satSL)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        pass
