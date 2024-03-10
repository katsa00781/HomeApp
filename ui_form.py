# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_HomeAppWidget(object):
    def setupUi(self, HomeAppWidget):
        if not HomeAppWidget.objectName():
            HomeAppWidget.setObjectName(u"HomeAppWidget")
        HomeAppWidget.resize(1064, 608)
        HomeAppWidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(121, 149, 159, 145), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"color:#000000\n"
"")
        self.actionFilmek = QAction(HomeAppWidget)
        self.actionFilmek.setObjectName(u"actionFilmek")
        self.actionSorozatok = QAction(HomeAppWidget)
        self.actionSorozatok.setObjectName(u"actionSorozatok")
        self.actionEdz_stervez_s = QAction(HomeAppWidget)
        self.actionEdz_stervez_s.setObjectName(u"actionEdz_stervez_s")
        self.actionEdz_sterv = QAction(HomeAppWidget)
        self.actionEdz_sterv.setObjectName(u"actionEdz_sterv")
        self.actionTestkompozici = QAction(HomeAppWidget)
        self.actionTestkompozici.setObjectName(u"actionTestkompozici")
        self.actionEdz_sadatok_felvitele = QAction(HomeAppWidget)
        self.actionEdz_sadatok_felvitele.setObjectName(u"actionEdz_sadatok_felvitele")
        self.actionB_rkalkul_tor = QAction(HomeAppWidget)
        self.actionB_rkalkul_tor.setObjectName(u"actionB_rkalkul_tor")
        self.actionMegtakar_t_sok = QAction(HomeAppWidget)
        self.actionMegtakar_t_sok.setObjectName(u"actionMegtakar_t_sok")
        self.actionR_szv_nyek = QAction(HomeAppWidget)
        self.actionR_szv_nyek.setObjectName(u"actionR_szv_nyek")
        self.actionK_lts_gvet_s_tervez = QAction(HomeAppWidget)
        self.actionK_lts_gvet_s_tervez.setObjectName(u"actionK_lts_gvet_s_tervez")
        self.actionk_lts_gvet_s_kimutat_sok = QAction(HomeAppWidget)
        self.actionk_lts_gvet_s_kimutat_sok.setObjectName(u"actionk_lts_gvet_s_kimutat_sok")
        self.actionStatisztik_k = QAction(HomeAppWidget)
        self.actionStatisztik_k.setObjectName(u"actionStatisztik_k")
        self.actionHeti_teend_k = QAction(HomeAppWidget)
        self.actionHeti_teend_k.setObjectName(u"actionHeti_teend_k")
        self.actionNapt_r = QAction(HomeAppWidget)
        self.actionNapt_r.setObjectName(u"actionNapt_r")
        self.actionKarbantart_s = QAction(HomeAppWidget)
        self.actionKarbantart_s.setObjectName(u"actionKarbantart_s")
        self.centralwidget = QWidget(HomeAppWidget)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QLabel {\n"
"color:#000000;\n"
"background: none\n"
"\n"
"}\n"
"Qprogressbar {\n"
"color:#000000;\n"
"\n"
"\n"
"\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 10, 1021, 41))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color:#8D3D3D;\n"
"background: none")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: none;\n"
"color: #000000")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background: none;\n"
"color: #000000")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"background: none;\n"
"color: #000000")

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background: none;\n"
"color: #000000")

        self.horizontalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background: none;\n"
"color: #000000")

        self.horizontalLayout.addWidget(self.pushButton_5)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(10, 60, 321, 221))
        self.frame_3.setStyleSheet(u"border-radius: 20px\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gyakorlat_1_LineEdit = QLineEdit(self.frame_3)
        self.gyakorlat_1_LineEdit.setObjectName(u"gyakorlat_1_LineEdit")

        self.verticalLayout.addWidget(self.gyakorlat_1_LineEdit)

        self.gyakorlat_2_lineEdit = QLineEdit(self.frame_3)
        self.gyakorlat_2_lineEdit.setObjectName(u"gyakorlat_2_lineEdit")

        self.verticalLayout.addWidget(self.gyakorlat_2_lineEdit)

        self.lineEdit_3 = QLineEdit(self.frame_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout.addWidget(self.lineEdit_3)

        self.lineEdit_4 = QLineEdit(self.frame_3)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout.addWidget(self.lineEdit_4)

        self.lineEdit_6 = QLineEdit(self.frame_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout.addWidget(self.lineEdit_6)

        self.lineEdit_5 = QLineEdit(self.frame_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout.addWidget(self.lineEdit_5)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(10, 290, 321, 271))
        self.frame_4.setStyleSheet(u"border-radius: 20px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(10, 10, 291, 16))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_6)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 0, 58, 16))
        self.label_2.setStyleSheet(u"color:#000000;\n"
"background: none\n"
"")
        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(10, 30, 301, 172))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_7)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkBox = QCheckBox(self.frame_7)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout_2.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.frame_7)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout_2.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(self.frame_7)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout_2.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.frame_7)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout_2.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.frame_7)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout_2.addWidget(self.checkBox_5)

        self.checkBox_6 = QCheckBox(self.frame_7)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout_2.addWidget(self.checkBox_6)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(340, 60, 691, 571))
        self.frame_5.setStyleSheet(u"border-radius: 20px")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(20, 10, 661, 40))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 10, 117, 20))
        self.label_3.setStyleSheet(u"background: none;\n"
"color:#000000\n"
"")
        self.koltsegvetes_kimutatas = QFrame(self.frame_5)
        self.koltsegvetes_kimutatas.setObjectName(u"koltsegvetes_kimutatas")
        self.koltsegvetes_kimutatas.setGeometry(QRect(20, 60, 661, 401))
        self.koltsegvetes_kimutatas.setStyleSheet(u"Qframe.TextLabel {\n"
"color:#000000;\n"
"background: none\n"
"}")
        self.koltsegvetes_kimutatas.setFrameShape(QFrame.StyledPanel)
        self.koltsegvetes_kimutatas.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.koltsegvetes_kimutatas)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.right_koltsegvetes_frame = QFrame(self.koltsegvetes_kimutatas)
        self.right_koltsegvetes_frame.setObjectName(u"right_koltsegvetes_frame")
        self.right_koltsegvetes_frame.setFrameShape(QFrame.StyledPanel)
        self.right_koltsegvetes_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.right_koltsegvetes_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.auto_frame = QFrame(self.right_koltsegvetes_frame)
        self.auto_frame.setObjectName(u"auto_frame")
        self.auto_frame.setStyleSheet(u"padding: 2px")
        self.auto_frame.setFrameShape(QFrame.StyledPanel)
        self.auto_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.auto_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_4 = QLabel(self.auto_frame)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.progressBar = QProgressBar(self.auto_frame)
        self.progressBar.setObjectName(u"progressBar")
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(121, 149, 159, 145))
        gradient.setColorAt(1, QColor(255, 255, 255, 255))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(121, 149, 159, 145))
        gradient1.setColorAt(1, QColor(255, 255, 255, 255))
        brush2 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(121, 149, 159, 145))
        gradient2.setColorAt(1, QColor(255, 255, 255, 255))
        brush3 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 128))
        brush4.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(121, 149, 159, 145))
        gradient3.setColorAt(1, QColor(255, 255, 255, 255))
        brush5 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(121, 149, 159, 145))
        gradient4.setColorAt(1, QColor(255, 255, 255, 255))
        brush6 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush6)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(121, 149, 159, 145))
        gradient5.setColorAt(1, QColor(255, 255, 255, 255))
        brush7 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush7)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush4)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(121, 149, 159, 145))
        gradient6.setColorAt(1, QColor(255, 255, 255, 255))
        brush8 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(121, 149, 159, 145))
        gradient7.setColorAt(1, QColor(255, 255, 255, 255))
        brush9 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(121, 149, 159, 145))
        gradient8.setColorAt(1, QColor(255, 255, 255, 255))
        brush10 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush10)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush4)
#endif
        self.progressBar.setPalette(palette)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setStyleSheet(u"color:#000000")
        self.progressBar.setValue(24)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_2.addWidget(self.progressBar)


        self.verticalLayout_4.addWidget(self.auto_frame)

        self.egeszsegugy_frame = QFrame(self.right_koltsegvetes_frame)
        self.egeszsegugy_frame.setObjectName(u"egeszsegugy_frame")
        self.egeszsegugy_frame.setStyleSheet(u"padding: 2px")
        self.egeszsegugy_frame.setFrameShape(QFrame.StyledPanel)
        self.egeszsegugy_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.egeszsegugy_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.egeszsegugy_frame)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.progressBar_2 = QProgressBar(self.egeszsegugy_frame)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(0)
        self.progressBar_2.setInvertedAppearance(False)
        self.progressBar_2.setTextDirection(QProgressBar.TopToBottom)

        self.horizontalLayout_3.addWidget(self.progressBar_2)


        self.verticalLayout_4.addWidget(self.egeszsegugy_frame)

        self.szorakozas_frame = QFrame(self.right_koltsegvetes_frame)
        self.szorakozas_frame.setObjectName(u"szorakozas_frame")
        self.szorakozas_frame.setFrameShape(QFrame.StyledPanel)
        self.szorakozas_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.szorakozas_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_6 = QLabel(self.szorakozas_frame)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.haztartas_progressbar = QProgressBar(self.szorakozas_frame)
        self.haztartas_progressbar.setObjectName(u"haztartas_progressbar")
        self.haztartas_progressbar.setValue(24)

        self.horizontalLayout_4.addWidget(self.haztartas_progressbar)


        self.verticalLayout_4.addWidget(self.szorakozas_frame)

        self.haztartas_frame = QFrame(self.right_koltsegvetes_frame)
        self.haztartas_frame.setObjectName(u"haztartas_frame")
        self.haztartas_frame.setFrameShape(QFrame.StyledPanel)
        self.haztartas_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.haztartas_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.haztartas_frame)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.progressBar_4 = QProgressBar(self.haztartas_frame)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(24)

        self.horizontalLayout_5.addWidget(self.progressBar_4)


        self.verticalLayout_4.addWidget(self.haztartas_frame)

        self.rezsi_frame = QFrame(self.right_koltsegvetes_frame)
        self.rezsi_frame.setObjectName(u"rezsi_frame")
        self.rezsi_frame.setFrameShape(QFrame.StyledPanel)
        self.rezsi_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.rezsi_frame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_12 = QLabel(self.rezsi_frame)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_10.addWidget(self.label_12)

        self.progressBar_9 = QProgressBar(self.rezsi_frame)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setValue(24)

        self.horizontalLayout_10.addWidget(self.progressBar_9)


        self.verticalLayout_4.addWidget(self.rezsi_frame)


        self.horizontalLayout_11.addWidget(self.right_koltsegvetes_frame)

        self.left_koltsegvetes_frame = QFrame(self.koltsegvetes_kimutatas)
        self.left_koltsegvetes_frame.setObjectName(u"left_koltsegvetes_frame")
        self.left_koltsegvetes_frame.setFrameShape(QFrame.StyledPanel)
        self.left_koltsegvetes_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.left_koltsegvetes_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.mama_frame = QFrame(self.left_koltsegvetes_frame)
        self.mama_frame.setObjectName(u"mama_frame")
        self.mama_frame.setFrameShape(QFrame.StyledPanel)
        self.mama_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.mama_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.mama_frame)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_7.addWidget(self.label_9)

        self.progressBar_6 = QProgressBar(self.mama_frame)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setValue(0)

        self.horizontalLayout_7.addWidget(self.progressBar_6)


        self.verticalLayout_5.addWidget(self.mama_frame)

        self.egyeb_frame = QFrame(self.left_koltsegvetes_frame)
        self.egyeb_frame.setObjectName(u"egyeb_frame")
        self.egyeb_frame.setFrameShape(QFrame.StyledPanel)
        self.egyeb_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.egyeb_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.egyeb_frame)
        self.label_10.setObjectName(u"label_10")

        self.horizontalLayout_8.addWidget(self.label_10)

        self.progressBar_7 = QProgressBar(self.egyeb_frame)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setStyleSheet(u"")
        self.progressBar_7.setValue(0)
        self.progressBar_7.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.progressBar_7)


        self.verticalLayout_5.addWidget(self.egyeb_frame)

        self.hitel_frame = QFrame(self.left_koltsegvetes_frame)
        self.hitel_frame.setObjectName(u"hitel_frame")
        self.hitel_frame.setFrameShape(QFrame.StyledPanel)
        self.hitel_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.hitel_frame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_11 = QLabel(self.hitel_frame)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)

        self.progressBar_8 = QProgressBar(self.hitel_frame)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setValue(24)

        self.horizontalLayout_9.addWidget(self.progressBar_8)


        self.verticalLayout_5.addWidget(self.hitel_frame)

        self.digitalis_rezsi_frame = QFrame(self.left_koltsegvetes_frame)
        self.digitalis_rezsi_frame.setObjectName(u"digitalis_rezsi_frame")
        self.digitalis_rezsi_frame.setFrameShape(QFrame.StyledPanel)
        self.digitalis_rezsi_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.digitalis_rezsi_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.digitalis_rezsi_frame)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.progressBar_5 = QProgressBar(self.digitalis_rezsi_frame)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setValue(24)

        self.horizontalLayout_6.addWidget(self.progressBar_5)


        self.verticalLayout_5.addWidget(self.digitalis_rezsi_frame)


        self.horizontalLayout_11.addWidget(self.left_koltsegvetes_frame)


        self.verticalLayout_3.addWidget(self.frame)

        HomeAppWidget.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HomeAppWidget)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1064, 24))
        self.menuSzorakoz_s = QMenu(self.menubar)
        self.menuSzorakoz_s.setObjectName(u"menuSzorakoz_s")
        self.menuEdz_s = QMenu(self.menubar)
        self.menuEdz_s.setObjectName(u"menuEdz_s")
        self.menuP_nz_gyek = QMenu(self.menubar)
        self.menuP_nz_gyek.setObjectName(u"menuP_nz_gyek")
        self.menuK_lts_gvet_s = QMenu(self.menuP_nz_gyek)
        self.menuK_lts_gvet_s.setObjectName(u"menuK_lts_gvet_s")
        self.menuOtthon = QMenu(self.menubar)
        self.menuOtthon.setObjectName(u"menuOtthon")
        HomeAppWidget.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HomeAppWidget)
        self.statusbar.setObjectName(u"statusbar")
        HomeAppWidget.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuSzorakoz_s.menuAction())
        self.menubar.addAction(self.menuEdz_s.menuAction())
        self.menubar.addAction(self.menuP_nz_gyek.menuAction())
        self.menubar.addAction(self.menuOtthon.menuAction())
        self.menuSzorakoz_s.addAction(self.actionFilmek)
        self.menuSzorakoz_s.addAction(self.actionSorozatok)
        self.menuEdz_s.addAction(self.actionEdz_stervez_s)
        self.menuEdz_s.addAction(self.actionEdz_sterv)
        self.menuEdz_s.addAction(self.actionTestkompozici)
        self.menuEdz_s.addAction(self.actionEdz_sadatok_felvitele)
        self.menuP_nz_gyek.addAction(self.menuK_lts_gvet_s.menuAction())
        self.menuP_nz_gyek.addAction(self.actionB_rkalkul_tor)
        self.menuP_nz_gyek.addAction(self.actionMegtakar_t_sok)
        self.menuP_nz_gyek.addAction(self.actionR_szv_nyek)
        self.menuK_lts_gvet_s.addAction(self.actionK_lts_gvet_s_tervez)
        self.menuK_lts_gvet_s.addAction(self.actionk_lts_gvet_s_kimutat_sok)
        self.menuK_lts_gvet_s.addAction(self.actionStatisztik_k)
        self.menuOtthon.addAction(self.actionHeti_teend_k)
        self.menuOtthon.addAction(self.actionNapt_r)
        self.menuOtthon.addAction(self.actionKarbantart_s)

        self.retranslateUi(HomeAppWidget)

        QMetaObject.connectSlotsByName(HomeAppWidget)
    # setupUi

    def retranslateUi(self, HomeAppWidget):
        HomeAppWidget.setWindowTitle(QCoreApplication.translate("HomeAppWidget", u"HomeAppWidget", None))
        self.actionFilmek.setText(QCoreApplication.translate("HomeAppWidget", u"Filmek", None))
        self.actionSorozatok.setText(QCoreApplication.translate("HomeAppWidget", u"Sorozatok", None))
        self.actionEdz_stervez_s.setText(QCoreApplication.translate("HomeAppWidget", u"Edz\u00e9stervez\u00e9s", None))
        self.actionEdz_sterv.setText(QCoreApplication.translate("HomeAppWidget", u"Edz\u00e9sterv", None))
        self.actionTestkompozici.setText(QCoreApplication.translate("HomeAppWidget", u"Testkompozici\u00f3", None))
        self.actionEdz_sadatok_felvitele.setText(QCoreApplication.translate("HomeAppWidget", u"Edz\u00e9sadatok felvitele", None))
        self.actionB_rkalkul_tor.setText(QCoreApplication.translate("HomeAppWidget", u"B\u00e9rkalkul\u00e1tor", None))
        self.actionMegtakar_t_sok.setText(QCoreApplication.translate("HomeAppWidget", u"Megtakar\u00edt\u00e1sok", None))
        self.actionR_szv_nyek.setText(QCoreApplication.translate("HomeAppWidget", u"R\u00e9szv\u00e9nyek", None))
        self.actionK_lts_gvet_s_tervez.setText(QCoreApplication.translate("HomeAppWidget", u"K\u00f6lts\u00e9gvet\u00e9s tervez\u0151", None))
        self.actionk_lts_gvet_s_kimutat_sok.setText(QCoreApplication.translate("HomeAppWidget", u"k\u00f6lts\u00e9gvet\u00e9s kimutat\u00e1sok", None))
        self.actionStatisztik_k.setText(QCoreApplication.translate("HomeAppWidget", u"Statisztik\u00e1k", None))
        self.actionHeti_teend_k.setText(QCoreApplication.translate("HomeAppWidget", u"Heti teend\u0151k", None))
        self.actionNapt_r.setText(QCoreApplication.translate("HomeAppWidget", u"Napt\u00e1r", None))
        self.actionKarbantart_s.setText(QCoreApplication.translate("HomeAppWidget", u"Karbantart\u00e1s", None))
        self.label.setText(QCoreApplication.translate("HomeAppWidget", u"HomeApp", None))
        self.pushButton.setText(QCoreApplication.translate("HomeAppWidget", u"Sz\u00f3rakoz\u00e1s", None))
        self.pushButton_2.setText(QCoreApplication.translate("HomeAppWidget", u"Edz\u00e9stervez\u00e9s", None))
        self.pushButton_3.setText(QCoreApplication.translate("HomeAppWidget", u"R\u00e9szv\u00e9nyek", None))
        self.pushButton_4.setText(QCoreApplication.translate("HomeAppWidget", u"K\u00f6lts\u00e9gvet\u00e9s", None))
        self.pushButton_5.setText(QCoreApplication.translate("HomeAppWidget", u"Bev\u00e1s\u00e1rl\u00f3lista", None))
        self.label_2.setText(QCoreApplication.translate("HomeAppWidget", u"Teend\u0151k", None))
        self.checkBox.setText("")
        self.checkBox_2.setText("")
        self.checkBox_3.setText("")
        self.checkBox_4.setText("")
        self.checkBox_5.setText("")
        self.checkBox_6.setText("")
        self.label_3.setText(QCoreApplication.translate("HomeAppWidget", u"K\u00f6lts\u00e9gvet\u00e9s \u00c1ll\u00e1sa", None))
        self.label_4.setText(QCoreApplication.translate("HomeAppWidget", u"Aut\u00f3:", None))
        self.progressBar.setFormat(QCoreApplication.translate("HomeAppWidget", u"%vFt", None))
        self.label_5.setText(QCoreApplication.translate("HomeAppWidget", u"Sz\u00f3rakoz\u00e1s:", None))
        self.progressBar_2.setFormat(QCoreApplication.translate("HomeAppWidget", u"%vFt", None))
        self.label_6.setText(QCoreApplication.translate("HomeAppWidget", u"H\u00e1ztart\u00e1s:", None))
        self.label_7.setText(QCoreApplication.translate("HomeAppWidget", u"Mama:", None))
        self.label_12.setText(QCoreApplication.translate("HomeAppWidget", u"Egy\u00e9b:", None))
        self.label_9.setText(QCoreApplication.translate("HomeAppWidget", u"Rezsi:", None))
        self.progressBar_6.setFormat("")
        self.label_10.setText(QCoreApplication.translate("HomeAppWidget", u"Eg\u00e9szs\u00e9g\u00fcgy", None))
        self.progressBar_7.setFormat(QCoreApplication.translate("HomeAppWidget", u"%vFt", None))
        self.label_11.setText(QCoreApplication.translate("HomeAppWidget", u"digit\u00e1lis rezsi:", None))
        self.label_8.setText(QCoreApplication.translate("HomeAppWidget", u"Hitel:", None))
        self.menuSzorakoz_s.setTitle(QCoreApplication.translate("HomeAppWidget", u"Szorakoz\u00e1s", None))
        self.menuEdz_s.setTitle(QCoreApplication.translate("HomeAppWidget", u"Edz\u00e9s", None))
        self.menuP_nz_gyek.setTitle(QCoreApplication.translate("HomeAppWidget", u"P\u00e9nz\u00fcgyek", None))
        self.menuK_lts_gvet_s.setTitle(QCoreApplication.translate("HomeAppWidget", u"K\u00f6lts\u00e9gvet\u00e9s", None))
        self.menuOtthon.setTitle(QCoreApplication.translate("HomeAppWidget", u"Otthon", None))
    # retranslateUi

