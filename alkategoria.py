import sys

from PySide6.QtWidgets import QApplication, QMainWindow


from ui_koltsegvetes import Ui_Koltsegvetes

class addAlkategoria():
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Koltsegvetes()
        self.ui.setupUi(self)
        
        if self.ui.fokategoria_comboBox.currentText() == "Autó":
            self.ui.alkategoria_comboBox.addItems(["Üzemanyag", "Szervíz", "Töltés", "Biztosítás"])
        if self.ui.fokategoria_comboBox.currentText() == "Szórakozás":
            self.ui.alkategoria_comboBox.addItems(["Mozi", "Nyaralás", "Utazás"])
            
              
        
        