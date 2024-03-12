# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'berkalkulator.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Berkalkulator(object):
    def setupUi(self, Berkalkulator):
        if not Berkalkulator.objectName():
            Berkalkulator.setObjectName(u"Berkalkulator")
        Berkalkulator.resize(1046, 695)
        Berkalkulator.setStyleSheet(u"\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);")
        self.frame = QFrame(Berkalkulator)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1021, 681))
        self.frame.setStyleSheet(u"\n"
"\n"
"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QLabel,  {\n"
"background: none;\n"
"color: #000000;\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);\n"
"\n"
"\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.dataFrame = QFrame(self.frame)
        self.dataFrame.setObjectName(u"dataFrame")
        self.dataFrame.setGeometry(QRect(20, 10, 991, 71))
        self.dataFrame.setStyleSheet(u"color:#8D3D3D;\n"
"background: none")
        self.dataFrame.setFrameShape(QFrame.StyledPanel)
        self.dataFrame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.dataFrame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 0, 971, 61))
        self.tableWidget.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);\n"
"color: #fff\n"
"}\n"
"")
        self.munkaidodataFrame = QFrame(self.frame)
        self.munkaidodataFrame.setObjectName(u"munkaidodataFrame")
        self.munkaidodataFrame.setGeometry(QRect(650, 100, 351, 291))
        self.munkaidodataFrame.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}")
        self.munkaidodataFrame.setFrameShape(QFrame.StyledPanel)
        self.munkaidodataFrame.setFrameShadow(QFrame.Raised)
        self.frame_18 = QFrame(self.munkaidodataFrame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setGeometry(QRect(10, 10, 263, 44))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.lineEdit_15 = QLineEdit(self.frame_18)
        self.lineEdit_15.setObjectName(u"lineEdit_15")

        self.horizontalLayout_15.addWidget(self.lineEdit_15)

        self.frame_20 = QFrame(self.munkaidodataFrame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(20, 70, 263, 44))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.lineEdit_17 = QLineEdit(self.frame_20)
        self.lineEdit_17.setObjectName(u"lineEdit_17")

        self.horizontalLayout_17.addWidget(self.lineEdit_17)

        self.frame_19 = QFrame(self.munkaidodataFrame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(20, 120, 263, 44))
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.lineEdit_16 = QLineEdit(self.frame_19)
        self.lineEdit_16.setObjectName(u"lineEdit_16")

        self.horizontalLayout_16.addWidget(self.lineEdit_16)

        self.frame_21 = QFrame(self.munkaidodataFrame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(20, 170, 263, 44))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_18.addWidget(self.label_18)

        self.lineEdit_18 = QLineEdit(self.frame_21)
        self.lineEdit_18.setObjectName(u"lineEdit_18")

        self.horizontalLayout_18.addWidget(self.lineEdit_18)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 90, 311, 571))
        self.frame_2.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_2)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_5)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_3)


        self.verticalLayout.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame_6)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.frame_6)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.horizontalLayout_4.addWidget(self.lineEdit_4)


        self.verticalLayout.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.frame_7)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.horizontalLayout_5.addWidget(self.lineEdit_5)


        self.verticalLayout.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_6.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.frame_8)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.frame_9)
        self.lineEdit_7.setObjectName(u"lineEdit_7")

        self.horizontalLayout_7.addWidget(self.lineEdit_7)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.frame_11)
        self.lineEdit_9.setObjectName(u"lineEdit_9")

        self.horizontalLayout_9.addWidget(self.lineEdit_9)


        self.verticalLayout.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.frame_10)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_8.addWidget(self.lineEdit_8)


        self.verticalLayout.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.lineEdit_10 = QLineEdit(self.frame_12)
        self.lineEdit_10.setObjectName(u"lineEdit_10")

        self.horizontalLayout_10.addWidget(self.lineEdit_10)


        self.verticalLayout.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(342, 100, 291, 291))
        self.frame_13.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_13)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_14 = QFrame(self.frame_13)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.lineEdit_11 = QLineEdit(self.frame_14)
        self.lineEdit_11.setObjectName(u"lineEdit_11")

        self.horizontalLayout_11.addWidget(self.lineEdit_11)


        self.verticalLayout_2.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_13)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.lineEdit_12 = QLineEdit(self.frame_15)
        self.lineEdit_12.setObjectName(u"lineEdit_12")

        self.horizontalLayout_12.addWidget(self.lineEdit_12)


        self.verticalLayout_2.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_13)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.lineEdit_13 = QLineEdit(self.frame_16)
        self.lineEdit_13.setObjectName(u"lineEdit_13")

        self.horizontalLayout_13.addWidget(self.lineEdit_13)


        self.verticalLayout_2.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.frame_13)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.lineEdit_14 = QLineEdit(self.frame_17)
        self.lineEdit_14.setObjectName(u"lineEdit_14")

        self.horizontalLayout_14.addWidget(self.lineEdit_14)


        self.verticalLayout_2.addWidget(self.frame_17)

        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(340, 540, 581, 121))
        self.frame_23.setStyleSheet(u"QPushButton {\n"
"				 border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 16px;\n"
"                    padding: 2px 16px;\n"
"                    height: 32px;\n"
"                    min-width: 60px;\n"
"                    min-height: 32px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #2251AA;\n"
"                    \n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;\n"
"}\n"
"\n"
"")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame_23)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(60, 50, 100, 36))
        self.pushButton_2 = QPushButton(self.frame_23)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(200, 50, 100, 36))
        self.pushButton_3 = QPushButton(self.frame_23)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(320, 50, 100, 36))
        self.pushButton_4 = QPushButton(self.frame_23)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(430, 50, 100, 36))
        self.frame_24 = QFrame(self.frame)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(450, 430, 361, 80))
        self.frame_24.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.frame_22 = QFrame(self.frame_24)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(40, 20, 263, 44))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_19 = QLabel(self.frame_22)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_19.addWidget(self.label_19)

        self.lineEdit_19 = QLineEdit(self.frame_22)
        self.lineEdit_19.setObjectName(u"lineEdit_19")

        self.horizontalLayout_19.addWidget(self.lineEdit_19)


        self.retranslateUi(Berkalkulator)

        QMetaObject.connectSlotsByName(Berkalkulator)
    # setupUi

    def retranslateUi(self, Berkalkulator):
        Berkalkulator.setWindowTitle(QCoreApplication.translate("Berkalkulator", u"Form", None))
        self.label_15.setText(QCoreApplication.translate("Berkalkulator", u"Ledolgozott napok", None))
        self.label_17.setText(QCoreApplication.translate("Berkalkulator", u"Szabads\u00e1g", None))
        self.label_16.setText(QCoreApplication.translate("Berkalkulator", u"Munkasz\u00fcneti mv", None))
        self.label_18.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra", None))
        self.label.setText(QCoreApplication.translate("Berkalkulator", u"Alapb\u00e9r:", None))
        self.label_2.setText(QCoreApplication.translate("Berkalkulator", u"Havib\u00e9res id\u0151b\u00e9r", None))
        self.label_3.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3raalap", None))
        self.label_4.setText(QCoreApplication.translate("Berkalkulator", u"Fizetett szabads\u00e1g", None))
        self.label_5.setText(QCoreApplication.translate("Berkalkulator", u"Munkasz\u00fcneti mv.", None))
        self.label_6.setText(QCoreApplication.translate("Berkalkulator", u"M\u0171szakp\u00f3tl\u00e9k", None))
        self.label_7.setText(QCoreApplication.translate("Berkalkulator", u"T\u00c9R", None))
        self.label_9.setText(QCoreApplication.translate("Berkalkulator", u"Pihen\u0151napos t\u00fal\u00f3ra", None))
        self.label_8.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra m\u0171szakp\u00f3tl\u00e9k", None))
        self.label_10.setText(QCoreApplication.translate("Berkalkulator", u"Jutalom", None))
        self.label_11.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra", None))
        self.label_12.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra M\u0171szakp\u00f3tl\u00e9k", None))
        self.label_13.setText(QCoreApplication.translate("Berkalkulator", u"Jutalom", None))
        self.label_14.setText(QCoreApplication.translate("Berkalkulator", u"Brutt\u00f3 b\u00e9r", None))
        self.pushButton.setText(QCoreApplication.translate("Berkalkulator", u"Sz\u00e1mol", None))
        self.pushButton_2.setText(QCoreApplication.translate("Berkalkulator", u"Vissza", None))
        self.pushButton_3.setText(QCoreApplication.translate("Berkalkulator", u"R\u00f6gz\u00edt\u00e9s", None))
        self.pushButton_4.setText(QCoreApplication.translate("Berkalkulator", u"Vissza", None))
        self.label_19.setText(QCoreApplication.translate("Berkalkulator", u"Kifizetend\u0151", None))
    # retranslateUi

