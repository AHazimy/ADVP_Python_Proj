# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUi4.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1214, 825)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(440, 200, 371, 491))
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.widget.setStyleSheet("QPushButton{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_fb, #pushButton_twitt, #pushButton_yt, #pushButton_in{    \n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_fb:hover, #pushButton_twitt:hover, #pushButton_yt:hover, #pushButton_in:hover{    \n"
"    color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_fb:pressed, #pushButton_twitt:pressed, #pushButton_yt:pressed, #pushButton_in:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(115, 128, 142, 255);\n"
"}")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 69, 300, 361))
        self.label.setStyleSheet("background-image: url(:/newPrefix/bianry_eye.png);\n"
"\n"
"border-radius:20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(94, 340, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 79, 301, 351))
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.488318, y1:0.733, x2:0.488636, y2:1, stop:0 rgba(126, 126, 126, 0), stop:1 rgba(36, 36, 36, 198));\n"
"border-radius:20px;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/images/bianry_eye.jpg"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(159, 85, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(255, 255, 255, 210);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(94, 221, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(94, 290, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(94, 156, 251, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255, 255, 255, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 390, 141, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_fb = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_fb.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_fb.setFont(font)
        self.pushButton_fb.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_fb.setObjectName("pushButton_fb")
        self.horizontalLayout.addWidget(self.pushButton_fb)
        self.pushButton_twitt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_twitt.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_twitt.setFont(font)
        self.pushButton_twitt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_twitt.setObjectName("pushButton_twitt")
        self.horizontalLayout.addWidget(self.pushButton_twitt)
        self.pushButton_yt = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yt.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_yt.setFont(font)
        self.pushButton_yt.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_yt.setObjectName("pushButton_yt")
        self.horizontalLayout.addWidget(self.pushButton_yt)
        self.pushButton_in = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_in.setMaximumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.pushButton_in.setFont(font)
        self.pushButton_in.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_in.setObjectName("pushButton_in")
        self.horizontalLayout.addWidget(self.pushButton_in)
        self.label.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.pushButton.raise_()
        self.pushButton_6.raise_()
        self.horizontalLayoutWidget.raise_()
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(270, 89, 791, 551))
        self.label_6.setStyleSheet("background-image: url(:/Cam/Cam_pic.jpg);\n"
"background-color: qlineargradient(spread:pad, x1:0.449318, y1:0.466, x2:0.449, y2:1, stop:0 rgba(0, 0, 0, 194), stop:1 rgba(115, 115, 115, 223));\n"
"border-radius:20px;\n"
"")
        self.label_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_6.setText("")
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(False)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(270, 89, 791, 551))
        self.label_7.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.449318, y1:0.466, x2:0.449, y2:1, stop:0 rgba(0, 0, 0, 171), stop:1 rgba(115, 115, 115, 191));\n"
"border-radius:20px;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(430, 90, 461, 91))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(173, 177, 180);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(540, 170, 261, 91))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(48)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(173, 177, 180);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(280, 610, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Stencil")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(173, 177, 180);")
        self.label_10.setObjectName("label_10")
        self.label_6.raise_()
        self.label_7.raise_()
        self.widget.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_6.setText(_translate("Form", "EXIT"))
        self.label_4.setText(_translate("Form", "Log In"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  Password"))
        self.pushButton.setText(_translate("Form", "L o g  I n"))
        self.lineEdit.setPlaceholderText(_translate("Form", "  User Name"))
        self.pushButton_fb.setText(_translate("Form", "E"))
        self.pushButton_twitt.setText(_translate("Form", "D"))
        self.pushButton_yt.setText(_translate("Form", "M"))
        self.pushButton_in.setText(_translate("Form", "C"))
        self.label_8.setText(_translate("Form", "Surveillence "))
        self.label_9.setText(_translate("Form", "System"))
        self.label_10.setText(_translate("Form", "Client"))

import res_cam
import res

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

