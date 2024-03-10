# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'koltsegvetes.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Koltsegvetes(object):
    def setupUi(self, Koltsegvetes):
        if not Koltsegvetes.objectName():
            Koltsegvetes.setObjectName(u"Koltsegvetes")
        Koltsegvetes.resize(912, 633)
        Koltsegvetes.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(121, 149, 159, 145), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"QPushButton {\n"
"                    \n"
"                    border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 16px;\n"
"                    padding: 2px 16px;\n"
"                    height: 32px;\n"
"                    min-width: 60px;\n"
"                    min-height: 32px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                    \n"
"                \n"
"};\n"
"\n"
"QFrame {\n"
"border-radius: 20px;\n"
"background-color: rgba(202, 238,247, 0.15)\n"
"}")
        self.InputFrame = QFrame(Koltsegvetes)
        self.InputFrame.setObjectName(u"InputFrame")
        self.InputFrame.setGeometry(QRect(10, 70, 265, 325))
        self.InputFrame.setStyleSheet(u"\n"
"\n"
"QLabel {\n"
"background: none;\n"
"color: #000000\n"
"};\n"
"\n"
"background-color:rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.InputFrame.setFrameShape(QFrame.StyledPanel)
        self.InputFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.InputFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_8 = QFrame(self.InputFrame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_8)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_7.addWidget(self.lineEdit_6)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_3 = QFrame(self.InputFrame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.frame_3)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_8.addWidget(self.lineEdit_7)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.InputFrame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_9.addWidget(self.lineEdit_8)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.InputFrame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.frame_5)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_10.addWidget(self.lineEdit_9)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.InputFrame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.frame_6)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_11.addWidget(self.lineEdit_10)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_2 = QFrame(Koltsegvetes)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 891, 51))
        self.frame_2.setStyleSheet(u"background-color:rgba(202,238,247, 0.5);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:#8D3D3D;\n"
"background: none")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.horizontalLayout.addWidget(self.pushButton)

        self.frame = QFrame(Koltsegvetes)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(290, 70, 265, 325))
        self.frame.setStyleSheet(u"\n"
"\n"
"QLabel {\n"
"background: none;\n"
"color: #000000\n"
"};\n"
"\n"
"background-color:rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AutoinputFrame = QFrame(self.frame)
        self.AutoinputFrame.setObjectName(u"AutoinputFrame")
        self.AutoinputFrame.setFrameShape(QFrame.StyledPanel)
        self.AutoinputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.AutoinputFrame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.AutoinputFrame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.AutoinputFrame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.verticalLayout_2.addWidget(self.AutoinputFrame)

        self.szorakozasinputFrame = QFrame(self.frame)
        self.szorakozasinputFrame.setObjectName(u"szorakozasinputFrame")
        self.szorakozasinputFrame.setFrameShape(QFrame.StyledPanel)
        self.szorakozasinputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.szorakozasinputFrame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.szorakozasinputFrame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.szorakozasinputFrame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.szorakozasinputFrame)

        self.haztartasInputFrame = QFrame(self.frame)
        self.haztartasInputFrame.setObjectName(u"haztartasInputFrame")
        self.haztartasInputFrame.setFrameShape(QFrame.StyledPanel)
        self.haztartasInputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.haztartasInputFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.haztartasInputFrame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_3 = QLineEdit(self.haztartasInputFrame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_4.addWidget(self.lineEdit_3)


        self.verticalLayout_2.addWidget(self.haztartasInputFrame)

        self.hitelInputFrame = QFrame(self.frame)
        self.hitelInputFrame.setObjectName(u"hitelInputFrame")
        self.hitelInputFrame.setFrameShape(QFrame.StyledPanel)
        self.hitelInputFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.hitelInputFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.hitelInputFrame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.hitelInputFrame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_5.addWidget(self.lineEdit_4)


        self.verticalLayout_2.addWidget(self.hitelInputFrame)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.frame_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_6.addWidget(self.lineEdit_5)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_9 = QFrame(Koltsegvetes)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(570, 70, 331, 551))
        self.frame_9.setStyleSheet(u"\n"
"\n"
"QLabel {\n"
"background: none;\n"
"color: #000000\n"
"};\n"
"\n"
"background-color:rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 20, 191, 20))
        self.label_12.setStyleSheet(u"font-size: 18px")
        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(10, 50, 151, 491))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_6 = QPushButton(self.frame_11)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"\n"
"            border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_8 = QPushButton(self.frame_11)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"\n"
"            border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_3.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_11)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"\n"
"            border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.pushButton_9 = QPushButton(self.frame_11)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"\n"
"            border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_3.addWidget(self.pushButton_9)

        self.pushButton_2 = QPushButton(self.frame_11)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"\n"
"            border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(170, 50, 151, 491))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_10 = QPushButton(self.frame_12)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_4.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.frame_12)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_4.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.frame_12)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_4.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_12)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_4.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.frame_12)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u" border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 15px;\n"
"                    padding: 2px 5px;\n"
"                    height: 20px;\n"
"                    min-width: 60px;\n"
"                    min-height: 20px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #4f545c;\n"
"                  \n"
"                ")

        self.verticalLayout_4.addWidget(self.pushButton_14)

        self.frame_10 = QFrame(Koltsegvetes)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 400, 551, 221))
        self.frame_10.setStyleSheet(u"\n"
"\n"
"QLabel {\n"
"background: none;\n"
"color: #000000\n"
"};\n"
"\n"
"background-color:rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Koltsegvetes)

        QMetaObject.connectSlotsByName(Koltsegvetes)
    # setupUi

    def retranslateUi(self, Koltsegvetes):
        Koltsegvetes.setWindowTitle(QCoreApplication.translate("Koltsegvetes", u"Form", None))
        self.label_7.setText(QCoreApplication.translate("Koltsegvetes", u"Digit\u00e1lis rezsi", None))
        self.label_8.setText(QCoreApplication.translate("Koltsegvetes", u"Megtakar\u00edt\u00e1s", None))
        self.label_9.setText(QCoreApplication.translate("Koltsegvetes", u"Rezsi", None))
        self.label_10.setText(QCoreApplication.translate("Koltsegvetes", u"Egy\u00e9b", None))
        self.label_11.setText(QCoreApplication.translate("Koltsegvetes", u"Mama", None))
        self.label.setText(QCoreApplication.translate("Koltsegvetes", u"HomeApp", None))
        self.pushButton_3.setText(QCoreApplication.translate("Koltsegvetes", u"R\u00e9szv\u00e9nyek", None))
        self.pushButton_4.setText(QCoreApplication.translate("Koltsegvetes", u"B\u00e9rkalkul\u00e1tor", None))
        self.pushButton_5.setText(QCoreApplication.translate("Koltsegvetes", u"Bev\u00e1s\u00e1rl\u00f3lista", None))
        self.pushButton.setText(QCoreApplication.translate("Koltsegvetes", u"Vissza", None))
        self.label_2.setText(QCoreApplication.translate("Koltsegvetes", u"Aut\u00f3", None))
        self.label_3.setText(QCoreApplication.translate("Koltsegvetes", u"Sz\u00f3rakoz\u00e1s", None))
        self.label_4.setText(QCoreApplication.translate("Koltsegvetes", u"H\u00e1ztart\u00e1s", None))
        self.label_5.setText(QCoreApplication.translate("Koltsegvetes", u"Hitel", None))
        self.label_6.setText(QCoreApplication.translate("Koltsegvetes", u"Eg\u00e9szs\u00e9g\u00fcgy", None))
        self.label_12.setText(QCoreApplication.translate("Koltsegvetes", u"R\u00e9szletes k\u00f6lts\u00e9gvet\u00e9s", None))
        self.pushButton_6.setText(QCoreApplication.translate("Koltsegvetes", u"Aut\u00f3", None))
        self.pushButton_8.setText(QCoreApplication.translate("Koltsegvetes", u"Sz\u00f3rakoz\u00e1s", None))
        self.pushButton_7.setText(QCoreApplication.translate("Koltsegvetes", u"H\u00e1ztart\u00e1s", None))
        self.pushButton_9.setText(QCoreApplication.translate("Koltsegvetes", u"Hitel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Koltsegvetes", u"Eg\u00e9szs\u00e9g\u00fcgy", None))
        self.pushButton_10.setText(QCoreApplication.translate("Koltsegvetes", u"Digit\u00e1lis Rezsi", None))
        self.pushButton_11.setText(QCoreApplication.translate("Koltsegvetes", u"Megtakar\u00edt\u00e1s", None))
        self.pushButton_12.setText(QCoreApplication.translate("Koltsegvetes", u"Rezsi", None))
        self.pushButton_13.setText(QCoreApplication.translate("Koltsegvetes", u"Mama", None))
        self.pushButton_14.setText(QCoreApplication.translate("Koltsegvetes", u"Egy\u00e9b", None))
    # retranslateUi

