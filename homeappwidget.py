# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_HomeAppWidget
from KoltsegvetesMainWindow import KoltsegvetesMainWindow

class HomeAppWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_HomeAppWidget()
        self.ui.setupUi(self)

        self.ui.koltsegvetesButton.clicked.connect(self.koltsegvetes)
        
    def koltsegvetes(self):
        self.window =  KoltsegvetesMainWindow()
        self.window.show()  

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = HomeAppWidget()
    widget.show()
    sys.exit(app.exec())
