import sqlite3
import pandas as pd



class CreateDatabase:
    def __init__ (self, path, table):
        self.path = path
        self.table = table
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        try:
        
            self.cursor.execute(
                f"""CREATE TABLE IF NOT EXISTS {self.table}  (
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
        except:
            print("Hiba!")
            
        
        self.connection.commit()   
        self.connection.close()


class CreateSubDatabase:
    def __init__(self, path, table):
        self.path = path
        self.table = table
        
        
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()
        
        self.c.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.table}  (
            Hónap TEXT,
            Alkategória INTEGER,
            összeg INTEGER
            )"""
        )  
        
        self.conn.commit()
        self.conn.close()
        
        print(f"Hozzáadva! {self.table}")

# Subkategoria hozzáadása ----------------------------------------------------------------------------------------------------        

class AddOneValueToSubDatabase:  
    def __init__(self, path, maincategory, month,  category, cash, ) -> None:
        self.table = maincategory
        self.path = path
        self.month = month
        self.category = category
        self.cash = cash
        
        self.conn = sqlite3.connect(self.path)
        self.c = self.conn.cursor()
        
        self.c.execute(f"""INSERT INTO {self.table} ({self.category}, ) VALUES (?)""")     
        
        self.conn.commit()
        self.conn.close()       
        
# Adatok lekérdezése az alkategóriából ------------------------------------------------------------------------------------------
# Az összes adat lékerdezése a főkategóriában, vagy az alkategóriában
class Query_Database():
    def __init__(self, path, table):
        self.path = path
        self.table = table
       
        #Create or connet database 
        self.conn = sqlite3.connect(path)
        # Create cursor
        self.c = self.conn.cursor()
        self.sql = pd.read_sql_query(f" SELECT * FROM {self.table} ", self.conn)
        self.df_keszenlet = pd.DataFrame(self.sql)
        self.coldata = []
        self.rowdata = []
        
        
        for col in self.df_keszenlet:
            self.coldata.append(col)
        self.df_rows = self.df_keszenlet.to_numpy().tolist()
        for row in self.df_rows:
            self.rowdata.append(row)
        
    
        print(self.rowdata)
        
    def return_coldata(self):
        return self.coldata
        
    def return_rowdata(self):
        return self.rowdata
        
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
            f"""INSERT INTO {self.table} (Autó, Szórakozás, Háztartás, Hitel, 
            Egészségügy, Rezsi, DigitálisRezsi, Mama, Megtakarítás,
            Egyeb) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            self.values
        )     
        
        self.connection.commit()
        self.connection.close()
 
    # Alkategória Hozzáadása -----------------------------------------------------------------------------------------------
    
class SubCategoryValueToDatabase:
    def __init__(self, path, table, subcategory, month, values):
        self.path = path
        self.table = table
        self.month = month
        self.subcategory = subcategory
        self.values = values
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"""INSERT INTO {self.table} VALUES (
            :Hónap,
            :Alkategória,
            :összeg)""",
            {
                "Hónap": self.month,
                "Alkategória": self.subcategory,
                "összeg": self.values
            }
        )      
        
        self.connection.commit()
        self.connection.close()

class DeleteColumn:
    def __init__(self, path, table, column):
        self.path = path
        self.table = table
        self.column = column
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"ALTER TABLE {self.table} DROP COLUMN {self.column}"
        )     
        
        self.connection.commit()
        self.connection.close()        



class Query_Value_from_dasboard_in_Database:
    def __init__(self, path : str, table : str) -> None:
        self.path = path
        self.table = table
        #Create or connet database 
        self.conn = sqlite3.connect(self.path)
        # Create cursor
        self.c = self.conn.cursor()
        self.df = pd.read_sql_query(f" SELECT * from {self.table} ", self.conn)
        
        self.rowdata = []
        self.coldata = []
        
        self.df_cols = self.df.columns.tolist()
        

        self.df_rows = self.df.to_numpy().tolist()
        for row in self.df_rows:
                self.rowdata.append(row)
        
           
            
        
        self.conn.commit()
        self.conn.close()
        
       
        
    def get_value(self):
        return self.rowdata
        
    def get_coldata(self):
        return self.coldata  


#CreateSubDatabase(path="koltsegvetes.db" , table="Egészségügy", category="Alkategória")   

class DeleteRow:
    def __init__(self, path, table, row):
        self.path = path
        self.table = table
        self.row = row
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"DELETE FROM {self.table} WHERE ROWID = {self.row}"
        )     
        
        self.connection.commit()
        self.connection.close()

class DeleteAll:
    def __init__(self, path, table):
        self.path = path
        self.table = table
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"DELETE FROM {self.table}"
        )     
        
        self.connection.commit()
        self.connection.close()

class CalculateSum:
    def __init__(self, path, table):
        self.path = path
        self.table = table
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"SELECT SUM(összeg) FROM {self.table}"
        )   
        
    def get_szum(self):
        return self.cursor.fetchone()[0]
        
        self.connection.commit()
        self.connection.close()        

 

class AddSumValueToDatabase:
    def __init__ (self, path, table, values, category): 
        self.path = path
        self.table = table
        self.values = values
        self.category = category
        
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        
        self.cursor.execute(
            f"INSERT INTO {self.table} ({self.category} ) VALUES (?)",
            (self.values,)
        )     
        
        self.connection.commit()
        self.connection.close()

CreateDatabase(path="koltsegvetes.db" , table="Költségvetés")  
AddSumValueToDatabase(path="koltsegvetes.db", table="Költségvetés", values=5000, category="Autó")     
