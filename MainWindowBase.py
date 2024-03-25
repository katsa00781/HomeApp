# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from KoltsegvetesMainWindow import KoltsegvetesMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
# pyside6-uic MainWindow.ui -o ui_MainWindow.py

from ui_form import Ui_HomeAppWidget

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomeAppWidget()
        self.ui.setupUi(self)
        
        self.ui.koltsegvetesButton.clicked.connect(self.koltsegvetes)  
        
    def koltsegvetes(self):
        self.koltsegvetes = KoltsegvetesMainWindow()
        self.koltsegvetes.show()  
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())        
