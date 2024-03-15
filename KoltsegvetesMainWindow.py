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
from classes.databases import CreateDatabase, CreateSubDatabase,  SubCategoryValueToDatabase, Query_Database, Query_Value_from_dasboard_in_Database, DeleteRow, DeleteAll, CalculateSum, AddSumValueToDatabase



class KoltsegvetesMainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Koltsegvetes()
        self.ui.setupUi(self)
        self.path = "koltsegvetes.db"
        
        
        
        
        #Ablakok meggyitása
        self.ui.berkalkulatorButton.clicked.connect(self.berkalkulator)
        self.ui.createTableButton.clicked.connect(self.create_table)
        
        # Alkategóriák megjelenítése
        self.ui.fokategoria_comboBox.currentTextChanged.connect(self.alkategoria)
        
        #Adatok hozzáadása
        self.ui.felvitelButton.clicked.connect(self.felvitel)
        self.ui.sorTorleseButton.clicked.connect(self.sor_torlese)
        
        #Költségvetés Adattábla kitötlése
        self.ui.lekerdezesButton.clicked.connect(self.lekerdezes)
        
        #Költségvetés tábla törlése
        self.ui.resetButton.clicked.connect(self.tabla_torlese)
        self.ui.delete_allButton.clicked.connect(self.osszes_adat_torlese) 
        
        #QlineEditek feltöltése
        self.ui.sumButton.clicked.connect(self.add_values_edit)
    
    def add_values_edit(self):
        self.path = "koltsegvetes.db"
        self.table = self.ui.fokategoria_comboBox.currentText()  
        sum = CalculateSum(path=self.path, table=self.table)
        
        if self.table == "Autó":
            self.ui.lineEdit.setText(str(sum.get_szum()))
        elif self.table == "Szórakozás":
            self.ui.szorakozasLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Háztartás":
            self.ui.haztartasLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Hitel":
            self.ui.hitelLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Egészségügy":
            self.ui.egeszsegugyLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Rezsi":
            self.ui.rezsiLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Digitális Rezsi":
            self.ui.digitallisRezsiLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Mama":
            self.ui.mamaLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Megtakarítás":
            self.ui.magtakaritasLineEdit.setText(str(sum.get_szum()))
        elif self.table == "Egyéb":
            self.ui.egyebLineEdit.setText(str(sum.get_szum()))
            
           
    def add_values(self):
        self.path = "koltsegvetes.db"
        self.table = self.ui.fokategoria_comboBox.currentText()
        
        self.query = CalculateSum(path=self.path, table=self.table).get_szum()
        cash = int(self.query)
        print(cash)
        
        try:
            AddSumValueToDatabase(path=self.path, table="Költségvetés", values=cash, category=self.table)
            self.ui.textEdit.setText("Sikeres hozzáadás!")
            self.ui.textEdit.setTextColor("green")
        except:
            self.ui.textEdit.setText(f"Hiba! {ValueError}")
            self.ui.textEdit.setTextColor("red")
        
    def create_table(self):
        path = "koltsegvetes.db"
        table = self.ui.fokategoria_comboBox.currentText()
        
        
        
        try:
            CreateSubDatabase(path, table)
            self.ui.textEdit.setText("Sikeres hozzáadás!")
        except:
            self.ui.textEdit.setText(f"Hiba! {ValueError}")       
        
            
        
        
        
    def felvitel(self):
        self.fokategoria = self.ui.fokategoria_comboBox.currentText()
        self.subcategory = self.ui.alkategoria_comboBox.currentText()
        self.month = self.ui.honap_comboBox.currentText()
       
        cash = int(self.ui.add_subcategory_cash_LineEdit.text())
        print(self.subcategory)
        
        
        try:
            SubCategoryValueToDatabase(path="koltsegvetes.db", table=self.fokategoria, subcategory=self.subcategory, month=self.month, values=cash)
            self.ui.textEdit.setText(f"Sikeres hozzáadva a(z) {self.subcategory} alkategóriához {cash}Ft összeg!" )
            self.ui.textEdit.setTextColor("green")
        except:
            ValueError(f"Hiba! {ValueError}")
            self.ui.textEdit.setText(f"Hiba! {ValueError}")
            self.ui.textEdit.setTextColor("red")
    
    def osszes_adat_torlese(self):
        path = "koltsegvetes.db"
        table = self.ui.fokategoria_comboBox.currentText()
        DeleteAll(path=path, table=table)
    def tabla_torlese(self):
        self.ui.KltsegvetesSubTablewiev.model().removeRows(0, self.ui.KltsegvetesSubTablewiev.model().rowCount())    
        
    def lekerdezes(self):
        self.tabla_torlese()
        self.table = self.ui.fokategoria_comboBox.currentText()
        self.query = Query_Value_from_dasboard_in_Database(path="koltsegvetes.db", table=self.table)
        
        
        self.rowdata_import = self.query.get_value()
        
        for row in self.rowdata_import:
            self.ui.KltsegvetesSubTablewiev.insertRow(0)
            for i in range(len(row)):
                self.ui.KltsegvetesSubTablewiev.setItem(0, i, QtWidgets.QTableWidgetItem(str(row[i])))
        
            
            
        self.ui.KltsegvetesSubTablewiev.show()    
        
    
    def set_lineedit(self):
        self.query = Query_Value_from_dasboard_in_Database(path="koltsegvetes.db", table="Költségvetés")      
        
        self.value = self.query.get_value()
        print(self.value) 
        
      
    def alkategoria(self):
        self.ui.alkategoria_comboBox.clear()
        if self.ui.fokategoria_comboBox.currentText() == "Autó":
            self.ui.alkategoria_comboBox.addItems(["Üzemanyag", "Szervíz", "Töltés", "Biztosítás"])
        elif self.ui.fokategoria_comboBox.currentText() == "Szórakozás":
            self.ui.alkategoria_comboBox.addItems(["Mozi", "Nyaralás", "Utazás"])  
        elif self.ui.fokategoria_comboBox.currentText() == "Háztartás":
            self.ui.alkategoria_comboBox.addItems(["Babacuccok", "Család/személyes", "Élelmiszer", "Otthon", "Tápszer"]) 
        elif self.ui.fokategoria_comboBox.currentText() == "Hitel":
            self.ui.alkategoria_comboBox.addItems(["Fundamenta", "Babaváró", "Hitelkártya", "Folyószámlahitel"])  
        elif self.ui.fokategoria_comboBox.currentText() == "Egészségügy":
            self.ui.alkategoria_comboBox.addItems(["Orvos", "Gyógyszer" ]) 
        elif self.ui.fokategoria_comboBox.currentText() == "Rezsi":
            self.ui.alkategoria_comboBox.addItems(["Víz", "Gáz", "Telefon", "Szemét", "TV/internet"])
        elif self.ui.fokategoria_comboBox.currentText() == "Digitális Rezsi":
            self.ui.alkategoria_comboBox.addItems(["HBO Max", "AppleOne", "Netflix","Disney+", "Skyshowtime", "YoutubePrémium"]) 
        elif self.ui.fokategoria_comboBox.currentText() == "Mama":
            self.ui.alkategoria_comboBox.addItems(["Mama"])  
        elif self.ui.fokategoria_comboBox.currentText() == "Megtakarítás":
            self.ui.alkategoria_comboBox.addItems(["Állampapír", "TBSZ", "Oktatás"]) 
        elif self.ui.fokategoria_comboBox.currentText() == "Egyéb":
            self.ui.alkategoria_comboBox.addItems(["Egyéb"])                     
                
    
    def berkalkulator(self):
        self.window =  Berkalkulator()
        self.window.show()
    
    def createTable(self):
        self.database = "koltsegvetes.db"
        try:
            if self.ui.alkategoria_comboBox.currentText() == "":
                self.ui.textEdit.setText("Add meg az alkategóriát is!")
            else:
                table = self.ui.fokategoria_comboBox.currentText()
                category = self.ui.alkategoria_comboBox.currentText()
                CreateDatabase(self.database, table, category) 
                self.ui.textEdit.setText("Sikeres hozzáadás!")
        except:
            self.ui.textEdit.setText("Hiba!")   
    
    def create_sub_database(self):
        self.database = "koltsegvetes.db"
        try:
            if self.ui.alkategoria_comboBox.currentText() == "":
                self.ui.textEdit.setText("Add meg az alkategóriát is!")
            else:
                table = self.ui.fokategoria_comboBox.currentText()
                category = self.ui.alkategoria_comboBox.currentText()
                CreateSubDatabase(self.database, table, category) 
                self.ui.textEdit.setText("Sikeres hozzáadás!")
        except:
            self.ui.textEdit.setText("Hiba!")          
              
                
    def sor_torlese(self):
        row = self.ui.KltsegvetesSubTablewiev.currentIndex().row() + 1
        print(row)
        DeleteRow(path=self.path, table=self.fokategoria, row=row)
        
          
        
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = KoltsegvetesMainWindow()
    widget.show()
    sys.exit(app.exec())

