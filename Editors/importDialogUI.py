# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImportDialog.ui'
#
# Created: Fri Dec 09 17:18:57 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_importDialog(object):
    def setupUi(self, importDialog):
        importDialog.setObjectName(_fromUtf8("importDialog"))
        importDialog.resize(775, 803)
        importDialog.setWindowTitle(QtGui.QApplication.translate("importDialog", "render details", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout = QtGui.QFormLayout(importDialog)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.groupBox_2 = QtGui.QGroupBox(importDialog)
        self.groupBox_2.setTitle(QtGui.QApplication.translate("importDialog", "Preview", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.ThumbPixmap = QtGui.QLabel(self.groupBox_2)
        self.ThumbPixmap.setMinimumSize(QtCore.QSize(256, 256))
        self.ThumbPixmap.setMaximumSize(QtCore.QSize(256, 256))
        self.ThumbPixmap.setText(_fromUtf8(""))
        self.ThumbPixmap.setObjectName(_fromUtf8("ThumbPixmap"))
        self.horizontalLayout.addWidget(self.ThumbPixmap)
        self.infoGroupBox = QtGui.QGroupBox(self.groupBox_2)
        self.infoGroupBox.setTitle(QtGui.QApplication.translate("importDialog", "Info", None, QtGui.QApplication.UnicodeUTF8))
        self.infoGroupBox.setObjectName(_fromUtf8("infoGroupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.infoGroupBox)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout.addWidget(self.infoGroupBox)
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.groupBox_2)
        self.groupBox_3 = QtGui.QGroupBox(importDialog)
        self.groupBox_3.setTitle(QtGui.QApplication.translate("importDialog", "Infos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_4.setMinimumSize(QtCore.QSize(300, 0))
        self.groupBox_4.setTitle(QtGui.QApplication.translate("importDialog", "Select  Info", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.formLayout_3 = QtGui.QFormLayout(self.groupBox_4)
        self.formLayout_3.setObjectName(_fromUtf8("formLayout_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setText(QtGui.QApplication.translate("importDialog", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_8)
        self.ProjectComboBox = QtGui.QComboBox(self.groupBox_4)
        self.ProjectComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ProjectComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.ProjectComboBox.setObjectName(_fromUtf8("ProjectComboBox"))
        self.formLayout_3.setWidget(0, QtGui.QFormLayout.FieldRole, self.ProjectComboBox)
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setText(QtGui.QApplication.translate("importDialog", "Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_9)
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setText(QtGui.QApplication.translate("importDialog", "Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_10)
        self.SequComboBox = QtGui.QComboBox(self.groupBox_4)
        self.SequComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SequComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.SequComboBox.setObjectName(_fromUtf8("SequComboBox"))
        self.formLayout_3.setWidget(1, QtGui.QFormLayout.FieldRole, self.SequComboBox)
        self.ShotComboBox = QtGui.QComboBox(self.groupBox_4)
        self.ShotComboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.ShotComboBox.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContents)
        self.ShotComboBox.setObjectName(_fromUtf8("ShotComboBox"))
        self.formLayout_3.setWidget(2, QtGui.QFormLayout.FieldRole, self.ShotComboBox)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.groupBox = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox.setTitle(QtGui.QApplication.translate("importDialog", "Render Infos", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.groupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setText(QtGui.QApplication.translate("importDialog", "In", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_2)
        self.InlineEdit = QtGui.QLineEdit(self.groupBox)
        self.InlineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.InlineEdit.setReadOnly(True)
        self.InlineEdit.setObjectName(_fromUtf8("InlineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.InlineEdit)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setText(QtGui.QApplication.translate("importDialog", "Out", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_3)
        self.OutlineEdit = QtGui.QLineEdit(self.groupBox)
        self.OutlineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.OutlineEdit.setReadOnly(True)
        self.OutlineEdit.setObjectName(_fromUtf8("OutlineEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.OutlineEdit)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setText(QtGui.QApplication.translate("importDialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_5)
        self.VerlineEdit = QtGui.QLineEdit(self.groupBox)
        self.VerlineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.VerlineEdit.setReadOnly(True)
        self.VerlineEdit.setObjectName(_fromUtf8("VerlineEdit"))
        self.formLayout_2.setWidget(7, QtGui.QFormLayout.FieldRole, self.VerlineEdit)
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("importDialog", "CG", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("importDialog", "PLATE", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("importDialog", "COMP", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.setItemText(3, QtGui.QApplication.translate("importDialog", "ELEMENT", None, QtGui.QApplication.UnicodeUTF8))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setText(QtGui.QApplication.translate("importDialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_4)
        self.ElemNamelineEdit = QtGui.QLineEdit(self.groupBox)
        self.ElemNamelineEdit.setReadOnly(False)
        self.ElemNamelineEdit.setObjectName(_fromUtf8("ElemNamelineEdit"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.FieldRole, self.ElemNamelineEdit)
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setText(QtGui.QApplication.translate("importDialog", "Element name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout_2.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_6)
        self.OffsetlineEdit = QtGui.QLineEdit(self.groupBox)
        self.OffsetlineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.OffsetlineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.OffsetlineEdit.setInputMask(_fromUtf8(""))
        self.OffsetlineEdit.setObjectName(_fromUtf8("OffsetlineEdit"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.OffsetlineEdit)
        self.label_11 = QtGui.QLabel(self.groupBox)
        self.label_11.setText(QtGui.QApplication.translate("importDialog", "Offset", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_11)
        self.DBInlineEdit = QtGui.QLineEdit(self.groupBox)
        self.DBInlineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.DBInlineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.DBInlineEdit.setReadOnly(True)
        self.DBInlineEdit.setObjectName(_fromUtf8("DBInlineEdit"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.DBInlineEdit)
        self.DBOutlineEdit = QtGui.QLineEdit(self.groupBox)
        self.DBOutlineEdit.setMinimumSize(QtCore.QSize(60, 0))
        self.DBOutlineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.DBOutlineEdit.setReadOnly(True)
        self.DBOutlineEdit.setObjectName(_fromUtf8("DBOutlineEdit"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.DBOutlineEdit)
        self.label_12 = QtGui.QLabel(self.groupBox)
        self.label_12.setText(QtGui.QApplication.translate("importDialog", "DB In", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_12)
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setText(QtGui.QApplication.translate("importDialog", "DB Out", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.formLayout.setWidget(11, QtGui.QFormLayout.FieldRole, self.groupBox_3)
        self.label_7 = QtGui.QLabel(importDialog)
        self.label_7.setText(QtGui.QApplication.translate("importDialog", "Output path", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(12, QtGui.QFormLayout.FieldRole, self.label_7)
        self.OutputPathlineEdit = QtGui.QLineEdit(importDialog)
        self.OutputPathlineEdit.setReadOnly(True)
        self.OutputPathlineEdit.setObjectName(_fromUtf8("OutputPathlineEdit"))
        self.formLayout.setWidget(13, QtGui.QFormLayout.FieldRole, self.OutputPathlineEdit)
        self.checkBox = QtGui.QCheckBox(importDialog)
        self.checkBox.setText(QtGui.QApplication.translate("importDialog", "Auto Generate Proxy", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.formLayout.setWidget(14, QtGui.QFormLayout.FieldRole, self.checkBox)
        self.buttonBox = QtGui.QDialogButtonBox(importDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(15, QtGui.QFormLayout.FieldRole, self.buttonBox)
        self.InputPathLineEdit = QtGui.QLineEdit(importDialog)
        self.InputPathLineEdit.setReadOnly(True)
        self.InputPathLineEdit.setObjectName(_fromUtf8("InputPathLineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.InputPathLineEdit)
        self.BrowserToolButton = QtGui.QToolButton(importDialog)
        self.BrowserToolButton.setMinimumSize(QtCore.QSize(50, 0))
        self.BrowserToolButton.setText(QtGui.QApplication.translate("importDialog", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.BrowserToolButton.setObjectName(_fromUtf8("BrowserToolButton"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.BrowserToolButton)
        self.label = QtGui.QLabel(importDialog)
        self.label.setText(QtGui.QApplication.translate("importDialog", "Input path", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.label)

        self.retranslateUi(importDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), importDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), importDialog.reject)
        QtCore.QObject.connect(self.BrowserToolButton, QtCore.SIGNAL(_fromUtf8("clicked()")), importDialog.fileBrowser)
        QtCore.QObject.connect(self.ElemNamelineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), importDialog.setElemName)
        QtCore.QObject.connect(self.OffsetlineEdit, QtCore.SIGNAL(_fromUtf8("textEdited(QString)")), importDialog.setFrameRange)
        QtCore.QMetaObject.connectSlotsByName(importDialog)

    def retranslateUi(self, importDialog):
        pass

