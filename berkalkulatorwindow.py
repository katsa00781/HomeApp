# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets

import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic berkalkulator.ui -o ui_berkalkulator.py
from ui_berkalkulator import Ui_Berkalkulator

class Berkalkulator(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.ui = Ui_Berkalkulator()
        self.ui.setupUi(self)
        
        

if __name__ == "__main__":
    app = QApplication()
    widget = Berkalkulator()
    widget.show()
    sys.exit(app.exec())
            