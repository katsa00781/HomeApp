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
        Berkalkulator.resize(964, 825)
        Berkalkulator.setStyleSheet(u"\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);\n"
"\n"
"color: #000000;\n"
"\n"
"\n"
"font: 400 13pt \"Arial\";\n"
"\n"
"")
        self.frame = QFrame(Berkalkulator)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 1021, 801))
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
        self.dataFrame.setGeometry(QRect(20, 10, 931, 71))
        self.dataFrame.setStyleSheet(u"color:#8D3D3D;\n"
"background: none")
        self.dataFrame.setFrameShape(QFrame.StyledPanel)
        self.dataFrame.setFrameShadow(QFrame.Raised)
        self.tableWidget = QTableWidget(self.dataFrame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 911, 61))
        self.tableWidget.setStyleSheet(u"QFrame{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);\n"
"color: #fff\n"
"}\n"
"")
        self.munkaidodataFrame = QFrame(self.frame)
        self.munkaidodataFrame.setObjectName(u"munkaidodataFrame")
        self.munkaidodataFrame.setGeometry(QRect(650, 100, 288, 313))
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
        self.verticalLayout_3 = QVBoxLayout(self.munkaidodataFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_18 = QFrame(self.munkaidodataFrame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_15 = QLabel(self.frame_18)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_15.addWidget(self.label_15)

        self.ledolgozottNapokLineEdit = QLineEdit(self.frame_18)
        self.ledolgozottNapokLineEdit.setObjectName(u"ledolgozottNapokLineEdit")

        self.horizontalLayout_15.addWidget(self.ledolgozottNapokLineEdit)


        self.verticalLayout_3.addWidget(self.frame_18)

        self.frame_26 = QFrame(self.munkaidodataFrame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_22 = QLabel(self.frame_26)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_23.addWidget(self.label_22)

        self.tuloraLineEdit_3 = QLineEdit(self.frame_26)
        self.tuloraLineEdit_3.setObjectName(u"tuloraLineEdit_3")

        self.horizontalLayout_23.addWidget(self.tuloraLineEdit_3)


        self.verticalLayout_3.addWidget(self.frame_26)

        self.frame_20 = QFrame(self.munkaidodataFrame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_17 = QLabel(self.frame_20)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.SzabadsagLineEdit = QLineEdit(self.frame_20)
        self.SzabadsagLineEdit.setObjectName(u"SzabadsagLineEdit")

        self.horizontalLayout_17.addWidget(self.SzabadsagLineEdit)


        self.verticalLayout_3.addWidget(self.frame_20)

        self.frame_19 = QFrame(self.munkaidodataFrame)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_16 = QLabel(self.frame_19)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_16.addWidget(self.label_16)

        self.munkaszunetiLineEdit = QLineEdit(self.frame_19)
        self.munkaszunetiLineEdit.setObjectName(u"munkaszunetiLineEdit")

        self.horizontalLayout_16.addWidget(self.munkaszunetiLineEdit)


        self.verticalLayout_3.addWidget(self.frame_19)

        self.frame_21 = QFrame(self.munkaidodataFrame)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_18.addWidget(self.label_18)

        self.mrendIdoLineEdit = QLineEdit(self.frame_21)
        self.mrendIdoLineEdit.setObjectName(u"mrendIdoLineEdit")

        self.horizontalLayout_18.addWidget(self.mrendIdoLineEdit)


        self.verticalLayout_3.addWidget(self.frame_21)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(20, 90, 311, 701))
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
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.alabberLineEdit = QLineEdit(self.frame_3)
        self.alabberLineEdit.setObjectName(u"alabberLineEdit")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        self.alabberLineEdit.setFont(font)

        self.horizontalLayout.addWidget(self.alabberLineEdit)


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

        self.haiberesidoberLineEdit = QLineEdit(self.frame_4)
        self.haiberesidoberLineEdit.setObjectName(u"haiberesidoberLineEdit")

        self.horizontalLayout_2.addWidget(self.haiberesidoberLineEdit)


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

        self.tuloraAlapLineEdit = QLineEdit(self.frame_5)
        self.tuloraAlapLineEdit.setObjectName(u"tuloraAlapLineEdit")

        self.horizontalLayout_3.addWidget(self.tuloraAlapLineEdit)


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

        self.fizetettSzLineEdit = QLineEdit(self.frame_6)
        self.fizetettSzLineEdit.setObjectName(u"fizetettSzLineEdit")

        self.horizontalLayout_4.addWidget(self.fizetettSzLineEdit)


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

        self.munkaszuntimvLineEdit = QLineEdit(self.frame_7)
        self.munkaszuntimvLineEdit.setObjectName(u"munkaszuntimvLineEdit")

        self.horizontalLayout_5.addWidget(self.munkaszuntimvLineEdit)


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

        self.mpotlekLineEdit = QLineEdit(self.frame_8)
        self.mpotlekLineEdit.setObjectName(u"mpotlekLineEdit")

        self.horizontalLayout_6.addWidget(self.mpotlekLineEdit)


        self.verticalLayout.addWidget(self.frame_8)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setStyleSheet(u"")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_14)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.TuloraLineEdit = QLineEdit(self.frame_14)
        self.TuloraLineEdit.setObjectName(u"TuloraLineEdit")

        self.horizontalLayout_11.addWidget(self.TuloraLineEdit)


        self.verticalLayout.addWidget(self.frame_14)

        self.frame_16 = QFrame(self.frame_2)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_13 = QLabel(self.frame_16)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_13.addWidget(self.label_13)

        self.jutalomLineEdit = QLineEdit(self.frame_16)
        self.jutalomLineEdit.setObjectName(u"jutalomLineEdit")

        self.horizontalLayout_13.addWidget(self.jutalomLineEdit)


        self.verticalLayout.addWidget(self.frame_16)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.frame_15)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_12.addWidget(self.label_12)

        self.tuloraMuszakpotlekLineEdit = QLineEdit(self.frame_15)
        self.tuloraMuszakpotlekLineEdit.setObjectName(u"tuloraMuszakpotlekLineEdit")

        self.horizontalLayout_12.addWidget(self.tuloraMuszakpotlekLineEdit)


        self.verticalLayout.addWidget(self.frame_15)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.terLineEdit = QLineEdit(self.frame_9)
        self.terLineEdit.setObjectName(u"terLineEdit")

        self.horizontalLayout_7.addWidget(self.terLineEdit)


        self.verticalLayout.addWidget(self.frame_9)

        self.frame_17 = QFrame(self.frame_2)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_14 = QLabel(self.frame_17)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_14.addWidget(self.label_14)

        self.bruttoberLineEdit = QLineEdit(self.frame_17)
        self.bruttoberLineEdit.setObjectName(u"bruttoberLineEdit")

        self.horizontalLayout_14.addWidget(self.bruttoberLineEdit)


        self.verticalLayout.addWidget(self.frame_17)

        self.LevonasokFrame = QFrame(self.frame)
        self.LevonasokFrame.setObjectName(u"LevonasokFrame")
        self.LevonasokFrame.setGeometry(QRect(342, 100, 291, 291))
        self.LevonasokFrame.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}")
        self.LevonasokFrame.setFrameShape(QFrame.StyledPanel)
        self.LevonasokFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.LevonasokFrame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_10 = QFrame(self.LevonasokFrame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.meszLineEdit = QLineEdit(self.frame_10)
        self.meszLineEdit.setObjectName(u"meszLineEdit")
        self.meszLineEdit.setFont(font)

        self.horizontalLayout_8.addWidget(self.meszLineEdit)


        self.verticalLayout_2.addWidget(self.frame_10)

        self.frame_12 = QFrame(self.LevonasokFrame)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.frame_12)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.szjaLineEdit = QLineEdit(self.frame_12)
        self.szjaLineEdit.setObjectName(u"szjaLineEdit")

        self.horizontalLayout_10.addWidget(self.szjaLineEdit)


        self.verticalLayout_2.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.LevonasokFrame)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_20 = QLabel(self.frame_13)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_21.addWidget(self.label_20)

        self.tbLineEdit = QLineEdit(self.frame_13)
        self.tbLineEdit.setObjectName(u"tbLineEdit")

        self.horizontalLayout_21.addWidget(self.tbLineEdit)


        self.verticalLayout_2.addWidget(self.frame_13)

        self.frame_25 = QFrame(self.LevonasokFrame)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_21 = QLabel(self.frame_25)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_22.addWidget(self.label_21)

        self.onkentesLineEdit = QLineEdit(self.frame_25)
        self.onkentesLineEdit.setObjectName(u"onkentesLineEdit")

        self.horizontalLayout_22.addWidget(self.onkentesLineEdit)


        self.verticalLayout_2.addWidget(self.frame_25)

        self.frame_11 = QFrame(self.LevonasokFrame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.osszeLevonasLineEdit = QLineEdit(self.frame_11)
        self.osszeLevonasLineEdit.setObjectName(u"osszeLevonasLineEdit")

        self.horizontalLayout_9.addWidget(self.osszeLevonasLineEdit)


        self.verticalLayout_2.addWidget(self.frame_11)

        self.frame_23 = QFrame(self.frame)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(350, 570, 521, 81))
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
        self.horizontalLayout_20 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.szamolButton = QPushButton(self.frame_23)
        self.szamolButton.setObjectName(u"szamolButton")

        self.horizontalLayout_20.addWidget(self.szamolButton)

        self.visszaButton = QPushButton(self.frame_23)
        self.visszaButton.setObjectName(u"visszaButton")
        self.visszaButton.setStyleSheet(u"background-color: lightgreen\n"
"")

        self.horizontalLayout_20.addWidget(self.visszaButton)

        self.RogziteButton = QPushButton(self.frame_23)
        self.RogziteButton.setObjectName(u"RogziteButton")

        self.horizontalLayout_20.addWidget(self.RogziteButton)

        self.torlesButton = QPushButton(self.frame_23)
        self.torlesButton.setObjectName(u"torlesButton")
        self.torlesButton.setStyleSheet(u"background-color: red")

        self.horizontalLayout_20.addWidget(self.torlesButton)

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

        self.kifizetendoLineEdit = QLineEdit(self.frame_22)
        self.kifizetendoLineEdit.setObjectName(u"kifizetendoLineEdit")

        self.horizontalLayout_19.addWidget(self.kifizetendoLineEdit)


        self.retranslateUi(Berkalkulator)

        QMetaObject.connectSlotsByName(Berkalkulator)
    # setupUi

    def retranslateUi(self, Berkalkulator):
        Berkalkulator.setWindowTitle(QCoreApplication.translate("Berkalkulator", u"Form", None))
        self.label_15.setText(QCoreApplication.translate("Berkalkulator", u"Ledolgozott napok", None))
        self.label_22.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra", None))
        self.label_17.setText(QCoreApplication.translate("Berkalkulator", u"Szabads\u00e1g", None))
        self.label_16.setText(QCoreApplication.translate("Berkalkulator", u"Munkasz\u00fcneti mv", None))
        self.label_18.setText(QCoreApplication.translate("Berkalkulator", u"Munkarend szerinti id\u0151", None))
        self.mrendIdoLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"20", None))
        self.label.setText(QCoreApplication.translate("Berkalkulator", u"Alapb\u00e9r:", None))
        self.alabberLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"764300", None))
        self.alabberLineEdit.setPlaceholderText(QCoreApplication.translate("Berkalkulator", u"764300", None))
        self.label_2.setText(QCoreApplication.translate("Berkalkulator", u"Havib\u00e9res id\u0151b\u00e9r", None))
        self.haiberesidoberLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_3.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3raalap", None))
        self.tuloraAlapLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_4.setText(QCoreApplication.translate("Berkalkulator", u"Fizetett szabads\u00e1g", None))
        self.fizetettSzLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_5.setText(QCoreApplication.translate("Berkalkulator", u"Munkasz\u00fcneti mv.", None))
        self.munkaszuntimvLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_6.setText(QCoreApplication.translate("Berkalkulator", u"M\u0171szakp\u00f3tl\u00e9k", None))
        self.mpotlekLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_11.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra", None))
        self.TuloraLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_13.setText(QCoreApplication.translate("Berkalkulator", u"Jutalom", None))
        self.jutalomLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_12.setText(QCoreApplication.translate("Berkalkulator", u"T\u00fal\u00f3ra M\u0171szakp\u00f3tl\u00e9k", None))
        self.tuloraMuszakpotlekLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Berkalkulator", u"T\u00c9R", None))
        self.terLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"26300", None))
        self.label_14.setText(QCoreApplication.translate("Berkalkulator", u"Brutt\u00f3 b\u00e9r", None))
        self.bruttoberLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_8.setText(QCoreApplication.translate("Berkalkulator", u"M\u00c9SZ", None))
        self.meszLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.meszLineEdit.setPlaceholderText(QCoreApplication.translate("Berkalkulator", u"764300", None))
        self.label_10.setText(QCoreApplication.translate("Berkalkulator", u"SZJA", None))
        self.szjaLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_20.setText(QCoreApplication.translate("Berkalkulator", u"TB j\u00e1rul\u00e9k", None))
        self.tbLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_21.setText(QCoreApplication.translate("Berkalkulator", u"\u00d6nk\u00e9ntes nyugd\u00edj", None))
        self.onkentesLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.label_9.setText(QCoreApplication.translate("Berkalkulator", u"\u00d6sszes Levon\u00e1s", None))
        self.osszeLevonasLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
        self.szamolButton.setText(QCoreApplication.translate("Berkalkulator", u"Sz\u00e1mol", None))
        self.visszaButton.setText(QCoreApplication.translate("Berkalkulator", u"Vissza", None))
        self.RogziteButton.setText(QCoreApplication.translate("Berkalkulator", u"R\u00f6gz\u00edt\u00e9s", None))
        self.torlesButton.setText(QCoreApplication.translate("Berkalkulator", u"T\u00f6rl\u00e9s", None))
        self.label_19.setText(QCoreApplication.translate("Berkalkulator", u"Kifizetend\u0151", None))
        self.kifizetendoLineEdit.setText(QCoreApplication.translate("Berkalkulator", u"0", None))
    # retranslateUi

