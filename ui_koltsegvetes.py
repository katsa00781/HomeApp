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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_Koltsegvetes(object):
    def setupUi(self, Koltsegvetes):
        if not Koltsegvetes.objectName():
            Koltsegvetes.setObjectName(u"Koltsegvetes")
        Koltsegvetes.resize(1099, 697)
        Koltsegvetes.setStyleSheet(u"\n"
"\n"
"QFrame {\n"
"border-radius: 20px;\n"
"background-color: rgba(202, 238,247, 0.15)\n"
"};\n"
"\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);")
        self.frame_2 = QFrame(Koltsegvetes)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 891, 51))
        self.frame_2.setStyleSheet(u"\n"
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
"                    background-color: #2251AA;\n"
"                    \n"
"                \n"
"}\n"
"\n"
"QFrame {\n"
"border-radius: 20px;\n"
"background-color: rgba(202, 238,247, 0.15)\n"
"};\n"
"\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,\n"
"                                      stop: 0 #FFE381, stop: 1 #A1B0BA);\n"
"\n"
"\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color:#8D3D3D;\n"
"background: none")

        self.horizontalLayout.addWidget(self.label)

        self.reszvenyekButton = QPushButton(self.frame_2)
        self.reszvenyekButton.setObjectName(u"reszvenyekButton")
        self.reszvenyekButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.reszvenyekButton)

        self.berkalkulatorButton = QPushButton(self.frame_2)
        self.berkalkulatorButton.setObjectName(u"berkalkulatorButton")
        self.berkalkulatorButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.berkalkulatorButton)

        self.bevasarlolistaButton = QPushButton(self.frame_2)
        self.bevasarlolistaButton.setObjectName(u"bevasarlolistaButton")
        self.bevasarlolistaButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.bevasarlolistaButton)

        self.visszaButton = QPushButton(self.frame_2)
        self.visszaButton.setObjectName(u"visszaButton")
        self.visszaButton.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.visszaButton)

        self.frame = QFrame(Koltsegvetes)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(290, 70, 265, 341))
        self.frame.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.AutoinputFrame = QFrame(self.frame)
        self.AutoinputFrame.setObjectName(u"AutoinputFrame")
        self.AutoinputFrame.setStyleSheet(u"")
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

        self.szorakozasLineEdit = QLineEdit(self.szorakozasinputFrame)
        self.szorakozasLineEdit.setObjectName(u"szorakozasLineEdit")

        self.horizontalLayout_3.addWidget(self.szorakozasLineEdit)


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

        self.haztartasLineEdit = QLineEdit(self.haztartasInputFrame)
        self.haztartasLineEdit.setObjectName(u"haztartasLineEdit")

        self.horizontalLayout_4.addWidget(self.haztartasLineEdit)


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

        self.hitelLineEdit = QLineEdit(self.hitelInputFrame)
        self.hitelLineEdit.setObjectName(u"hitelLineEdit")

        self.horizontalLayout_5.addWidget(self.hitelLineEdit)


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

        self.egeszsegugyLineEdit = QLineEdit(self.frame_7)
        self.egeszsegugyLineEdit.setObjectName(u"egeszsegugyLineEdit")

        self.horizontalLayout_6.addWidget(self.egeszsegugyLineEdit)


        self.verticalLayout_2.addWidget(self.frame_7)

        self.frame_9 = QFrame(Koltsegvetes)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(750, 70, 331, 611))
        self.frame_9.setStyleSheet(u"QPushButton {\n"
"border-radius: 3px;\n"
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
"                    }\n"
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
        self.KltsegvetesSubTablewiev = QTableWidget(self.frame_9)
        if (self.KltsegvetesSubTablewiev.columnCount() < 3):
            self.KltsegvetesSubTablewiev.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.KltsegvetesSubTablewiev.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.KltsegvetesSubTablewiev.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.KltsegvetesSubTablewiev.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.KltsegvetesSubTablewiev.setObjectName(u"KltsegvetesSubTablewiev")
        self.KltsegvetesSubTablewiev.setGeometry(QRect(10, 60, 311, 391))
        self.KltsegvetesSubTablewiev.setStyleSheet(u"color: #000000")
        self.lekerdezesButton = QPushButton(self.frame_9)
        self.lekerdezesButton.setObjectName(u"lekerdezesButton")
        self.lekerdezesButton.setGeometry(QRect(20, 560, 121, 36))
        self.sorTorleseButton = QPushButton(self.frame_9)
        self.sorTorleseButton.setObjectName(u"sorTorleseButton")
        self.sorTorleseButton.setGeometry(QRect(220, 560, 100, 36))
        self.resetButton = QPushButton(self.frame_9)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(220, 460, 100, 36))
        self.resetButton.setStyleSheet(u"background-color: #ff6b6b")
        self.delete_allButton = QPushButton(self.frame_9)
        self.delete_allButton.setObjectName(u"delete_allButton")
        self.delete_allButton.setGeometry(QRect(180, 510, 141, 36))
        self.delete_allButton.setStyleSheet(u"background-color: #ff6b6b")
        self.sumButton = QPushButton(self.frame_9)
        self.sumButton.setObjectName(u"sumButton")
        self.sumButton.setGeometry(QRect(20, 460, 121, 36))
        self.veglegesitButton = QPushButton(self.frame_9)
        self.veglegesitButton.setObjectName(u"veglegesitButton")
        self.veglegesitButton.setGeometry(QRect(20, 510, 121, 36))
        self.frame_10 = QFrame(Koltsegvetes)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(10, 420, 731, 261))
        self.frame_10.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}\n"
"\n"
"QComboBox{\n"
"color: #000000\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.fokategoria_comboBox = QComboBox(self.frame_10)
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.addItem("")
        self.fokategoria_comboBox.setObjectName(u"fokategoria_comboBox")
        self.fokategoria_comboBox.setGeometry(QRect(300, 10, 151, 32))
        self.label_13 = QLabel(self.frame_10)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(210, 20, 81, 16))
        self.label_14 = QLabel(self.frame_10)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(460, 20, 81, 16))
        self.alkategoria_comboBox = QComboBox(self.frame_10)
        self.alkategoria_comboBox.setObjectName(u"alkategoria_comboBox")
        self.alkategoria_comboBox.setGeometry(QRect(540, 10, 171, 32))
        self.textEdit = QTextEdit(self.frame_10)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 120, 511, 131))
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(40, 70, 58, 16))
        self.add_subcategory_cash_LineEdit = QLineEdit(self.frame_10)
        self.add_subcategory_cash_LineEdit.setObjectName(u"add_subcategory_cash_LineEdit")
        self.add_subcategory_cash_LineEdit.setGeometry(QRect(130, 70, 151, 21))
        self.add_subcategory_cash_LineEdit.setStyleSheet(u"color: #000000")
        self.felvitelButton = QPushButton(self.frame_10)
        self.felvitelButton.setObjectName(u"felvitelButton")
        self.felvitelButton.setGeometry(QRect(480, 60, 100, 36))
        self.felvitelButton.setStyleSheet(u"   border-radius: 3px;\n"
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
"                    ")
        self.createTableButton = QPushButton(self.frame_10)
        self.createTableButton.setObjectName(u"createTableButton")
        self.createTableButton.setGeometry(QRect(590, 60, 121, 36))
        self.createTableButton.setStyleSheet(u"   border-radius: 3px;\n"
"                    font-size: 14px;\n"
"                    font-weight: 500;\n"
"                    line-height: 16px;\n"
"                    padding: 2px 16px;\n"
"                    height: 32px;\n"
"                    min-width: 60px;\n"
"                    min-height: 32px;\n"
"                    border: none;\n"
"                    color: #fff;\n"
"                    background-color: #2251AA;")
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 20, 51, 16))
        self.honap_comboBox = QComboBox(self.frame_10)
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.addItem("")
        self.honap_comboBox.setObjectName(u"honap_comboBox")
        self.honap_comboBox.setGeometry(QRect(90, 10, 103, 32))
        self.frame_3 = QFrame(Koltsegvetes)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(20, 70, 265, 341))
        self.frame_3.setStyleSheet(u"QLineEdit{\n"
"\n"
"background-color: rgba(206, 194, 136, 0.5);\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgba(202,238,247, 0.5);\n"
"color: #000000;\n"
"border-radius:20px;}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.AutoinputFrame_2 = QFrame(self.frame_3)
        self.AutoinputFrame_2.setObjectName(u"AutoinputFrame_2")
        self.AutoinputFrame_2.setStyleSheet(u"")
        self.AutoinputFrame_2.setFrameShape(QFrame.StyledPanel)
        self.AutoinputFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.AutoinputFrame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_7 = QLabel(self.AutoinputFrame_2)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_7.addWidget(self.label_7)

        self.rezsiLineEdit = QLineEdit(self.AutoinputFrame_2)
        self.rezsiLineEdit.setObjectName(u"rezsiLineEdit")

        self.horizontalLayout_7.addWidget(self.rezsiLineEdit)


        self.verticalLayout_5.addWidget(self.AutoinputFrame_2)

        self.szorakozasinputFrame_2 = QFrame(self.frame_3)
        self.szorakozasinputFrame_2.setObjectName(u"szorakozasinputFrame_2")
        self.szorakozasinputFrame_2.setFrameShape(QFrame.StyledPanel)
        self.szorakozasinputFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.szorakozasinputFrame_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_8 = QLabel(self.szorakozasinputFrame_2)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_8.addWidget(self.label_8)

        self.digitrezsLineEdit = QLineEdit(self.szorakozasinputFrame_2)
        self.digitrezsLineEdit.setObjectName(u"digitrezsLineEdit")

        self.horizontalLayout_8.addWidget(self.digitrezsLineEdit)


        self.verticalLayout_5.addWidget(self.szorakozasinputFrame_2)

        self.haztartasInputFrame_2 = QFrame(self.frame_3)
        self.haztartasInputFrame_2.setObjectName(u"haztartasInputFrame_2")
        self.haztartasInputFrame_2.setFrameShape(QFrame.StyledPanel)
        self.haztartasInputFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.haztartasInputFrame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_9 = QLabel(self.haztartasInputFrame_2)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_9.addWidget(self.label_9)

        self.mamaLineEdit = QLineEdit(self.haztartasInputFrame_2)
        self.mamaLineEdit.setObjectName(u"mamaLineEdit")

        self.horizontalLayout_9.addWidget(self.mamaLineEdit)


        self.verticalLayout_5.addWidget(self.haztartasInputFrame_2)

        self.hitelInputFrame_2 = QFrame(self.frame_3)
        self.hitelInputFrame_2.setObjectName(u"hitelInputFrame_2")
        self.hitelInputFrame_2.setFrameShape(QFrame.StyledPanel)
        self.hitelInputFrame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.hitelInputFrame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_10 = QLabel(self.hitelInputFrame_2)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_10.addWidget(self.label_10)

        self.magtakaritasLineEdit = QLineEdit(self.hitelInputFrame_2)
        self.magtakaritasLineEdit.setObjectName(u"magtakaritasLineEdit")

        self.horizontalLayout_10.addWidget(self.magtakaritasLineEdit)


        self.verticalLayout_5.addWidget(self.hitelInputFrame_2)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_11.addWidget(self.label_11)

        self.egyebLineEdit = QLineEdit(self.frame_8)
        self.egyebLineEdit.setObjectName(u"egyebLineEdit")

        self.horizontalLayout_11.addWidget(self.egyebLineEdit)


        self.verticalLayout_5.addWidget(self.frame_8)


        self.retranslateUi(Koltsegvetes)

        QMetaObject.connectSlotsByName(Koltsegvetes)
    # setupUi

    def retranslateUi(self, Koltsegvetes):
        Koltsegvetes.setWindowTitle(QCoreApplication.translate("Koltsegvetes", u"Form", None))
        self.label.setText(QCoreApplication.translate("Koltsegvetes", u"HomeApp", None))
        self.reszvenyekButton.setText(QCoreApplication.translate("Koltsegvetes", u"R\u00e9szv\u00e9nyek", None))
        self.berkalkulatorButton.setText(QCoreApplication.translate("Koltsegvetes", u"B\u00e9rkalkul\u00e1tor", None))
        self.bevasarlolistaButton.setText(QCoreApplication.translate("Koltsegvetes", u"Bev\u00e1s\u00e1rl\u00f3lista", None))
        self.visszaButton.setText(QCoreApplication.translate("Koltsegvetes", u"Vissza", None))
        self.label_2.setText(QCoreApplication.translate("Koltsegvetes", u"Aut\u00f3", None))
        self.label_3.setText(QCoreApplication.translate("Koltsegvetes", u"Sz\u00f3rakoz\u00e1s", None))
        self.label_4.setText(QCoreApplication.translate("Koltsegvetes", u"H\u00e1ztart\u00e1s", None))
        self.label_5.setText(QCoreApplication.translate("Koltsegvetes", u"Hitel", None))
        self.label_6.setText(QCoreApplication.translate("Koltsegvetes", u"Eg\u00e9szs\u00e9g\u00fcgy", None))
        self.label_12.setText(QCoreApplication.translate("Koltsegvetes", u"R\u00e9szletes k\u00f6lts\u00e9gvet\u00e9s", None))
        ___qtablewidgetitem = self.KltsegvetesSubTablewiev.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Koltsegvetes", u"D\u00e1tum", None));
        ___qtablewidgetitem1 = self.KltsegvetesSubTablewiev.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Koltsegvetes", u"H\u00f3nap", None));
        ___qtablewidgetitem2 = self.KltsegvetesSubTablewiev.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Koltsegvetes", u"\u00d6sszeg", None));
        self.lekerdezesButton.setText(QCoreApplication.translate("Koltsegvetes", u"Lek\u00e9rdez\u00e9s", None))
        self.sorTorleseButton.setText(QCoreApplication.translate("Koltsegvetes", u"Sor t\u00f6rl\u00e9se", None))
        self.resetButton.setText(QCoreApplication.translate("Koltsegvetes", u"RESET", None))
        self.delete_allButton.setText(QCoreApplication.translate("Koltsegvetes", u"Minden t\u00f6rl\u00e9se", None))
        self.sumButton.setText(QCoreApplication.translate("Koltsegvetes", u"\u00f6sszes\u00edt\u00e9s", None))
        self.veglegesitButton.setText(QCoreApplication.translate("Koltsegvetes", u"V\u00e9gleges\u00edt", None))
        self.fokategoria_comboBox.setItemText(0, QCoreApplication.translate("Koltsegvetes", u"Aut\u00f3", None))
        self.fokategoria_comboBox.setItemText(1, QCoreApplication.translate("Koltsegvetes", u"Sz\u00f3rakoz\u00e1s", None))
        self.fokategoria_comboBox.setItemText(2, QCoreApplication.translate("Koltsegvetes", u"H\u00e1ztart\u00e1s", None))
        self.fokategoria_comboBox.setItemText(3, QCoreApplication.translate("Koltsegvetes", u"Hitel", None))
        self.fokategoria_comboBox.setItemText(4, QCoreApplication.translate("Koltsegvetes", u"Eg\u00e9szs\u00e9g\u00fcgy", None))
        self.fokategoria_comboBox.setItemText(5, QCoreApplication.translate("Koltsegvetes", u"Rezsi", None))
        self.fokategoria_comboBox.setItemText(6, QCoreApplication.translate("Koltsegvetes", u"Digit\u00e1lisRezsi", None))
        self.fokategoria_comboBox.setItemText(7, QCoreApplication.translate("Koltsegvetes", u"Mama", None))
        self.fokategoria_comboBox.setItemText(8, QCoreApplication.translate("Koltsegvetes", u"Megtakar\u00edt\u00e1s", None))
        self.fokategoria_comboBox.setItemText(9, QCoreApplication.translate("Koltsegvetes", u"Egy\u00e9b", None))

        self.label_13.setText(QCoreApplication.translate("Koltsegvetes", u"F\u0151kateg\u00f3ria", None))
        self.label_14.setText(QCoreApplication.translate("Koltsegvetes", u"Alkaterg\u00f3ria", None))
        self.label_15.setText(QCoreApplication.translate("Koltsegvetes", u"\u00d6sszeg", None))
        self.felvitelButton.setText(QCoreApplication.translate("Koltsegvetes", u"Felvitel", None))
        self.createTableButton.setText(QCoreApplication.translate("Koltsegvetes", u"T\u00e1bla", None))
        self.label_16.setText(QCoreApplication.translate("Koltsegvetes", u"H\u00f3nap", None))
        self.honap_comboBox.setItemText(0, QCoreApplication.translate("Koltsegvetes", u"Janu\u00e1r", None))
        self.honap_comboBox.setItemText(1, QCoreApplication.translate("Koltsegvetes", u"Febru\u00e1r", None))
        self.honap_comboBox.setItemText(2, QCoreApplication.translate("Koltsegvetes", u"M\u00e1rcius", None))
        self.honap_comboBox.setItemText(3, QCoreApplication.translate("Koltsegvetes", u"\u00c1prilis", None))
        self.honap_comboBox.setItemText(4, QCoreApplication.translate("Koltsegvetes", u"M\u00e1jus", None))
        self.honap_comboBox.setItemText(5, QCoreApplication.translate("Koltsegvetes", u"J\u00fanius", None))
        self.honap_comboBox.setItemText(6, QCoreApplication.translate("Koltsegvetes", u"J\u00falius", None))
        self.honap_comboBox.setItemText(7, QCoreApplication.translate("Koltsegvetes", u"Augusztus", None))
        self.honap_comboBox.setItemText(8, QCoreApplication.translate("Koltsegvetes", u"Szeptember", None))
        self.honap_comboBox.setItemText(9, QCoreApplication.translate("Koltsegvetes", u"Okt\u00f3ber", None))
        self.honap_comboBox.setItemText(10, QCoreApplication.translate("Koltsegvetes", u"November", None))
        self.honap_comboBox.setItemText(11, QCoreApplication.translate("Koltsegvetes", u"December", None))

        self.label_7.setText(QCoreApplication.translate("Koltsegvetes", u"Rezsi", None))
        self.label_8.setText(QCoreApplication.translate("Koltsegvetes", u"Digit\u00e1lis Rezsi", None))
        self.label_9.setText(QCoreApplication.translate("Koltsegvetes", u"Mama", None))
        self.label_10.setText(QCoreApplication.translate("Koltsegvetes", u"Megtakar\u00edt\u00e1s/oktat\u00e1s", None))
        self.label_11.setText(QCoreApplication.translate("Koltsegvetes", u"Egy\u00e9b", None))
    # retranslateUi

