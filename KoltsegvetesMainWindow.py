# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic koltsegvetes.ui -o ui_koltsegvetes.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_koltsegvetes import Ui_Koltsegvetes
from berkalkulatorwindow import Berkalkulator
from classes.databases import CreateDatabase


class KoltsegvetesMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Koltsegvetes()
        self.ui.setupUi(self)
        
        CreateDatabase("koltsegvetes.db", "főkategoria")
        
        #Ablakok meggyitása
        self.ui.berkalkulatorButton.clicked.connect(self.berkalkulator)
        
        
        
        
        
    def berkalkulator(self):
        self.window =  Berkalkulator()
        self.window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = KoltsegvetesMainWindow()
    widget.show()
    sys.exit(app.exec())

