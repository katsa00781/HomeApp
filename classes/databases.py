import sqlite3
import pandas as pd



class CreateDatabase:
    def __init__ (self, path, table):
        self.path = path
        self.table = table
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table}  (
            ID INTEGER PRIMARY KEY,
            Autó INTEGER, 
            Szórakozás INTEGER, 
            Háztartás INTEGER, 
            Hitel INTEGER, 
            Egészségügy INTEGER, 
            Rezsi INTEGER, 
            DigitálisRezsi INTEGER, 
            Mama INTEGER, 
            Megtakarítás INTEGER, 
            Egyeb INTEGER
            )""")
        
            
        
        self.connection.commit()   
        self.connection.close()


class CreateSubDatabase:
    def __init__(self, path, table, category):
        self.path = path
        self.table = table
        self.catecgory = category
        
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()
        
        self.c.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table}  (
            ID INTEGER PRIMARY KEY,
            {self.catecgory} INTEGER
            )"""
        )  

# Subkategoria hozzáadása ----------------------------------------------------------------------------------------------------        

class AddCategoryToSubDatabase:  
    def __init__(self, path, table, category) -> None:
        self.table = table
        self.path = path
        self.category = category
        
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()
        
        self.c.execute(f"""INSERT INTO {self.table} ({self.category}) VALUES (?)""")     
        
        self.conn.commit()
        self.conn.close()       
        
# Adatok lekérdezése az alkategóriából ------------------------------------------------------------------------------------------
# Az összes adat lékerdezése a főkategóriában, vagy az alkategóriában
class QueryDatabase:
    def __init__(self, path, table, rowid) -> None:
        self.path = path
        self.table = table
        self.rowid = rowid
        
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()
        
        self.c.execute(f"""SELECT * FROM {self.table} WHERE ID = {self.rowid}""")
        self.data = self.c.fetchall()
        
        self.conn.commit()
        self.conn.close()
                

# Főkategória összeg hozzáadása ---------------------------------------------------------------------------------------------------

class AddCashToDatabase:
    def __init__ (self, path, table, values): 
        self.path = path
        self.table = table
        self.values = values
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"""INSERT INTO {self.table} (Autó, Szörakozás, Háztartás, Hitel, 
            Egészségügy, Rezsi, DigitálisRezsi, Mama, Megtakarítás,
            Egyeb) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            self.values
        )     
        
        self.connection.commit()
        self.connection.close()