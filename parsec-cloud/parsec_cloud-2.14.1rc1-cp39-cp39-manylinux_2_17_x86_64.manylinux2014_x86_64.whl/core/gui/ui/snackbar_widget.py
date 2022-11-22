# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/project/parsec/core/gui/forms/snackbar_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SnackbarWidget(object):
    def setupUi(self, SnackbarWidget):
        SnackbarWidget.setObjectName("SnackbarWidget")
        SnackbarWidget.resize(608, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SnackbarWidget.sizePolicy().hasHeightForWidth())
        SnackbarWidget.setSizePolicy(sizePolicy)
        SnackbarWidget.setMinimumSize(QtCore.QSize(0, 75))
        SnackbarWidget.setMaximumSize(QtCore.QSize(16777215, 101))
        SnackbarWidget.setWindowTitle("")
        SnackbarWidget.setStyleSheet("QLabel {\n"
"    font-size: 15px;\n"
"    color: rgb(170, 170, 170);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: none;\n"
"    color: rgb(0, 146, 255);\n"
"    text-align: right;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"")
        self.horizontalLayout = QtWidgets.QHBoxLayout(SnackbarWidget)
        self.horizontalLayout.setContentsMargins(10, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, 5, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_icon = QtWidgets.QLabel(SnackbarWidget)
        self.label_icon.setMinimumSize(QtCore.QSize(56, 56))
        self.label_icon.setMaximumSize(QtCore.QSize(56, 56))
        self.label_icon.setText("")
        self.label_icon.setScaledContents(True)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_2.addWidget(self.label_icon)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.label = QtWidgets.QLabel(SnackbarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 10, -1, 10)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_close = QtWidgets.QPushButton(SnackbarWidget)
        self.button_close.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.button_close.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_close.setFlat(True)
        self.button_close.setObjectName("button_close")
        self.verticalLayout.addWidget(self.button_close)
        self.button_action = QtWidgets.QPushButton(SnackbarWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_action.sizePolicy().hasHeightForWidth())
        self.button_action.setSizePolicy(sizePolicy)
        self.button_action.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.button_action.setText("")
        self.button_action.setFlat(True)
        self.button_action.setObjectName("button_action")
        self.verticalLayout.addWidget(self.button_action)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(SnackbarWidget)
        QtCore.QMetaObject.connectSlotsByName(SnackbarWidget)

    def retranslateUi(self, SnackbarWidget):
        _translate = QtCore.QCoreApplication.translate
        self.button_close.setText(_translate("SnackbarWidget", "ACTION_DISMISS"))
