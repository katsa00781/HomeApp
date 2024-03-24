from tkinter import *
from tkinter import ttk
import sqlite3
from tkinter import messagebox
import ttkbootstrap as tb
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *
import object.classes as object
import object.database_class as db


class Berkalkulator(tb.Frame):
    def __init__(self, master ):
        super().__init__()
        self.master = master
        self.window = Toplevel(master)
        self.window.title("Bevételek")
        self.colors = self.master.style.colors
        self.m_rend_ido_entry = tb.StringVar()
        self.ledolgozott_idoadat_entry = tb.StringVar(value="")
        self.szabadsag_entry = tb.StringVar(value="")
        self.munkaszuneti_mv_entry = tb.StringVar(value="")
        self.tulora_p_entry = tb.StringVar(value="")
        self.alapber_entry = tb.StringVar(value="")
        
        
        
    
        self.beviteli_mezo("juttatások")
        self.levonasok("Levonások")
        self.kifizetendo("Kifizetendő")
        self.idoadatok("Időadatok")
        self.tablewiev_mezo()
        self.query()
        
        
        
    def szamol(self):
        self.havi_beres_idober()
        self.tulora_alap()
        self.fizetett_szabadsag()
        self.munkaszuneti_munkavegzes()
        self.muszakpotlek()
        self.brutto_ber()
        self.p_tulora()
        self.t_muszakpotlek()
        self.mesz()
        self.szja()
        self.tb_jarulek()
        self.onkentes_nyugdij()
        self.osszes_levonas()
        self.netto()
    
    # Brutto bérhez szükséges számítások
    def napiber(self) -> int:
        havi_oraszam = int(self.m_rend_ido_entry.get()) * 8.17
        napiber_osszege = int(self.alapber_entry.get()) / havi_oraszam
        
    
        return int(napiber_osszege)
        
        
    
    def havi_beres_idober(self) -> int:
        ledolgozott_ido = 0
        if self.szabadsag_entry == 0:
            ledolgozott_ido = ledolgozott_ido + int(self.ledolgozott_idoadat_entry.get())
        else:    
            ledolgozott_ido = int(self.m_rend_ido_entry.get()) - int(self.szabadsag_entry.get())
            self.ledolgozott_idoadat_entry.delete(0, END)
            self.ledolgozott_idoadat_entry.insert(0, ledolgozott_ido)
        try:
            haviberes_idober = (int(self.alapber_entry.get()) / int(self.m_rend_ido_entry.get())) * ledolgozott_ido 
            self.haviberes_idober_entry.delete(0, END)
            self.haviberes_idober_entry.insert(0, int(haviberes_idober))
            return int(haviberes_idober)
        except:
            return 0
           
    def tulora_alap(self) -> int:
        alapber = int(self.alapber_entry.get())
        
        if int(self.tulora_p_entry.get()) >= 0:
            ido = int(self.tulora_p_entry.get()) 
            t_ora = ido * 8.17
            m_rend_ido = int(self.m_rend_ido_entry.get()) * 8.17
            tulóra_osszeg = ((alapber / m_rend_ido) * t_ora ) * 0.94  
        else:
            return 0
        
        self.tuloralap_entry.delete(0, END)
        self.tuloralap_entry.insert(0, int(tulóra_osszeg))
        return int(tulóra_osszeg) 
            
            
        
    def fizetett_szabadsag(self) -> int:
        
        if int(self.szabadsag_entry.get()) >= 0:
            napok = int(self.szabadsag_entry.get()) * 8.17
            fizetett_szabadsag = napok * 7038
        else:
            fizetett_szabadsag = 0  
        
        
        self.fizetett_szabadsag_entry.delete(0, END)
        self.fizetett_szabadsag_entry.insert(0, int(fizetett_szabadsag))
        return int(fizetett_szabadsag)       
            
        
    def munkaszuneti_munkavegzes(self) -> int:
        napiber = self.napiber()
        munkaszuneti_ora = int(self.munkaszuneti_mv_entry.get()) * 8.17
        szumma_munkaszuneti = (napiber * munkaszuneti_ora) * 1.45
           
        self.munkaszuneti_entry.delete(0, END)
        self.munkaszuneti_entry.insert(0, int(szumma_munkaszuneti))
        
        
        return int(szumma_munkaszuneti)   
        
    def muszakpotlek(self) -> int:
        haviber = self.havi_beres_idober()
        m_potlek = haviber * 0.45
        
        self.muszakpotlek_entry.delete(0, END)
        self.muszakpotlek_entry.insert(0, int(m_potlek))
        
        
        return int(m_potlek)
        
    def brutto_ber(self)-> int:
        values = [self.havi_beres_idober(), self.tulora_alap(), self.fizetett_szabadsag(), self.munkaszuneti_munkavegzes(), self.muszakpotlek(), 26736 , self.p_tulora(), self.t_muszakpotlek()]
        # values_int = list(map(int, values))
        if int(self.jutalom_entry.get()) >= 0:
            values.append(int(self.jutalom_entry.get()))
        else:
            values.append(0)    
        total = sum(values)
        self.bruttober_entry.delete(0, END)
        self.bruttober_entry.insert(0, int(total))
        return total
    def p_tulora(self) -> int:
        napiber = self.napiber()
        tuloralap = int(self.tulora_p_entry.get()) * 8.22
        pihenonapos_tulora = (napiber * tuloralap) * 1.4
        
        self.to_pihenonapos_entry.delete(0, END)
        self.to_pihenonapos_entry.insert(0, int(pihenonapos_tulora))
        return int(pihenonapos_tulora)
    
    
    
    def t_muszakpotlek(self) -> int:
        tulóra_alap = self.tulora_alap()
        m_potlek = tulóra_alap * 0.45
        
        self.to_muszakpotlek_entry.delete(0, END)
        self.to_muszakpotlek_entry.insert(0, int(m_potlek))
        
        return int(m_potlek)
        
    # levonások függvények
    def mesz(self):
        brutto = self.brutto_ber()
        mesz = brutto * 0.007
        
        self.mesz_entry.delete(0, END)
        self.mesz_entry.insert(0, int(mesz))
        return int(mesz)
    
    def szja(self):
        brutto = self.brutto_ber()
        mesz = self.mesz()
        
        adoeloleg = (brutto - mesz - 333000) * 0.15
        
        self.adoeloleg_entry.delete(0, END)
        self.adoeloleg_entry.insert(0, int(adoeloleg))
        return int(adoeloleg)
    
    def tb_jarulek(self):
        brutto = self.brutto_ber()
        tb_jarulek = brutto * 0.185
        
        self.tb_jarulek_entry.delete(0, END)
        self.tb_jarulek_entry.insert(0, int(tb_jarulek))
        
        return tb_jarulek
    
    def onkentes_nyugdij(self):
        brutto = self.brutto_ber()
        onkentes_dolgozoi = brutto * 0.0015
        
        self.onkentes_entry.delete(0, END)
        self.onkentes_entry.insert(0, int(onkentes_dolgozoi))
        
        return onkentes_dolgozoi
        
    
    def osszes_levonas(self):
        levonasok = [self.mesz(), self.szja(), self.tb_jarulek(), self.onkentes_nyugdij()]
        osszes_levonas = sum(levonasok)
        
        self.osszes_entry.delete(0, END)
        self.osszes_entry.insert(0, int(osszes_levonas))
        
        return osszes_levonas
    
    def netto(self):   
        brutto = self.brutto_ber()
        osszes_levonas = self.osszes_levonas()
        kifizetendo = brutto - osszes_levonas
        
        self.kifizetendo_entry.delete(0, END) 
        self.kifizetendo_entry.insert(0, int(kifizetendo))
        
    def rogzites(self):
        db.CreateDatabase(path="database/bevetel.db", table="berkalkulator")  
        db.Add_Data_Berkalkulator(path="database/bevetel.db", table="berkalkulator", 
                                  szabadság=self.szabadsag_entry.get(),
                                  munkaszüneti_munkavégzés=self.munkaszuneti_mv_entry.get(),
                                  Túlóra=self.tulora_p_entry.get(),
                                  Bruttóbér=self.bruttober_entry.get(),
                                  Kifizetendő=self.kifizetendo_entry.get())
        db.Query_Database(path="database/bevetel.db", table="berkalkulator", tablewiev= self.table)
    
    
    def delete_data(self):
        messagebox.askyesno(title="Törlés", message="Biztosan törli az adatokat?", parent=self.window)
        db.Delete_All_Record(path="database/bevetel.db", table="berkalkulator")
        db.Query_Database(path="database/bevetel.db", table="berkalkulator", tablewiev= self.table)
    def query(self):
        db.Query_Database(path="database/bevetel.db", table="berkalkulator", tablewiev= self.table)
    def tablewiev_mezo(self):
        self.table = Tableview(self.window, paginated=False, searchable=False)
        self.table.pack( expand=False, fill="both", padx=10, pady=10)
    
    def beviteli_mezo(self, label):
        
        self.bevitelimezo = LabelFrame(self.window, text="Bevételi mező")
        self.bevitelimezo.pack(side=LEFT, fill=Y, pady=40, padx=5)
        
        self.alapber_label = Label(self.bevitelimezo, text="Alapbér")
        self.alapber_label.grid(row=0, column=0, padx=10, pady=5)
        self.alapber_entry = Entry(self.bevitelimezo)
        self.alapber_entry.insert(0, "754300")
        self.alapber_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.haviberes_idober_label = Label(self.bevitelimezo, text="havibéres időbér")
        self.haviberes_idober_label.grid(row=1, column=0, padx=10, pady=5)
        self.haviberes_idober_entry = Entry(self.bevitelimezo)
        self.haviberes_idober_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.tuloraalap_label = Label(self.bevitelimezo, text="Túlóraalap")
        self.tuloraalap_label.grid(row=2, column=0, padx=10, pady=5)
        self.tuloralap_entry = Entry(self.bevitelimezo)
        self.tuloralap_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.fizetett_szabadsag_label = Label(self.bevitelimezo, text="Fizetett szabadság")
        self.fizetett_szabadsag_label.grid(row=3, column=0, padx=10, pady=5)
        self.fizetett_szabadsag_entry = Entry(self.bevitelimezo)
        self.fizetett_szabadsag_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.munkaszuneti_label = Label(self.bevitelimezo, text="Munkaszüneti munkavégzés")
        self.munkaszuneti_label.grid(row=4, column=0, padx=10, pady=5)
        self.munkaszuneti_entry = Entry(self.bevitelimezo)
        self.munkaszuneti_entry.grid(row=4, column=1, padx=10, pady=5)
        
        self.muszakpotlek_label = Label(self.bevitelimezo, text="Műszakpótlék")
        self.muszakpotlek_label.grid(row=5, column=0, padx=10, pady=5)
        self.muszakpotlek_entry = Entry(self.bevitelimezo)
        self.muszakpotlek_entry.grid(row=5, column=1, padx=10, pady=5)
        
        self.ter_label = Label(self.bevitelimezo, text="TÉR kiegészítő bér")
        self.ter_label.grid(row=6, column=0, padx=10, pady=5)
        self.ter_entry = Entry(self.bevitelimezo)
        self.ter_entry.insert(0, "26736")
        self.ter_entry.grid(row=6, column=1, padx=10, pady=5)
        
        self.to_pihenonapos_label = Label(self.bevitelimezo, text="Pihenőnapos túlóra")
        self.to_pihenonapos_label.grid(row=8, column=0, padx=10, pady=5)
        self.to_pihenonapos_entry = Entry(self.bevitelimezo)
        self.to_pihenonapos_entry.grid(row=8, column=1, padx=10, pady=5)
        
        self.to_muszakpotlek_label = Label(self.bevitelimezo, text="Túlóra műszakpótlék")
        self.to_muszakpotlek_label.grid(row=9, column=0, padx=10, pady=5)
        self.to_muszakpotlek_entry = Entry(self.bevitelimezo)
        self.to_muszakpotlek_entry.grid(row=9, column=1, padx=10, pady=5)
        
        self.jutalom_label = Label(self.bevitelimezo, text="Jutalom")
        self.jutalom_label.grid(row=10, column=0, padx=10, pady=5)
        self.jutalom_entry = Entry(self.bevitelimezo)
        self.jutalom_entry.insert(0, "0")
        self.jutalom_entry.grid(row=10, column=1, padx=10, pady=5)
        
        self.bruttober_label = Label(self.bevitelimezo, text="Bruttober")
        self.bruttober_label.grid(row=11, column=0, padx=10, pady=5)
        self.bruttober_entry = Entry(self.bevitelimezo)
        self.bruttober_entry.grid(row=11, column=1, padx=10, pady=5)
        
    def levonasok(self, label):
        self.levonasok_label = LabelFrame(self.window, text="Levonások")
        self.levonasok_label.pack(side=RIGHT, fill=Y, pady=40, padx=5)
        
        self.adoeloleg = Label(self.levonasok_label, text="Adóelőleg")
        self.adoeloleg.grid(row=0, column=3, padx=10, pady=5) 
        self.adoeloleg_entry = Entry(self.levonasok_label)
        self.adoeloleg_entry.grid(row=0, column=4, padx=10, pady=5)
        
        self.tb_jarulek_label = Label(self.levonasok_label, text="TB járulék")
        self.tb_jarulek_label.grid(row=1, column=3, padx=10, pady=5)
        self.tb_jarulek_entry = Entry(self.levonasok_label)
        self.tb_jarulek_entry.grid(row=1, column=4, padx=10, pady=5)
        
        self.onkentes_label = Label(self.levonasok_label, text="Önkéntes dolgozói hozzájárulás")
        self.onkentes_label.grid(row=2, column=3, padx=10, pady=5)
        self.onkentes_entry = Entry(self.levonasok_label)
        self.onkentes_entry.grid(row=2, column=4, padx=10, pady=5)
        
        self.mesz_label = Label(self.levonasok_label, text="Mész")
        self.mesz_label.grid(row=3, column=3, padx=10, pady=5)
        self.mesz_entry = Entry(self.levonasok_label)
        self.mesz_entry.grid(row=3, column=4, padx=10, pady=5)   
        
        self.egyeb_label = Label(self.levonasok_label, text="Egyéb")
        self.egyeb_label.grid(row=4, column=3, padx=10, pady=5)
        self.egyeb_entry = Entry(self.levonasok_label)
        self.egyeb_entry.grid(row=4, column=4, padx=10, pady=5)
        
        self.osszes_label = Label(self.levonasok_label, text="Összes levonás")
        self.osszes_label.grid(row=5, column=3, padx=10, pady=5)
        self.osszes_entry = Entry(self.levonasok_label)
        self.osszes_entry.grid(row=5, column=4, padx=10, pady=5)
        
    def kifizetendo(self, label):
        self.kifizetendo_label_frame = LabelFrame(self.window) 
        self.kifizetendo_label_frame.pack(side=BOTTOM, fill=Y, padx=20, pady=20)
        
        self.kifizetendo_label = Label(self.kifizetendo_label_frame, text="Kifizetendő")
        self.kifizetendo_label.grid(row=0, column=0, padx=10, pady=5)
        self.kifizetendo_entry = Entry(self.kifizetendo_label_frame)
        self.kifizetendo_entry.grid(row=0, column=1, padx=10, pady=5)  
    
    def idoadatok(self, label):
        self.idoadatok_label_frame = LabelFrame(self.window)   
        self.idoadatok_label_frame.pack(side=BOTTOM, fill=Y, padx=20, pady=5) 
        
        self.m_rend_ido_label = Label(self.idoadatok_label_frame, text="Munkarend szerinti idő")
        self.m_rend_ido_label.grid(row=0, column=0, padx=10, pady=5)
        self.m_rend_ido_entry = Entry(self.idoadatok_label_frame)
        self.m_rend_ido_entry.insert(0, "20")
        self.m_rend_ido_entry.grid(row=0, column=1, padx=10, pady=5)
        
        self.ledolgozott_idoadat_label = Label(self.idoadatok_label_frame, text="Ledolgozott idő")
        self.ledolgozott_idoadat_label.grid(row=1, column=0, padx=10, pady=5)
        self.ledolgozott_idoadat_entry = Entry(self.idoadatok_label_frame, state="readonly")
        self.ledolgozott_idoadat_entry.grid(row=1, column=1, padx=10, pady=5)
        
        self.szabadsag_label = Label(self.idoadatok_label_frame, text="Szabadság")
        self.szabadsag_label.grid(row=2, column=0, padx=10, pady=5)
        self.szabadsag_entry = Entry(self.idoadatok_label_frame)
        self.szabadsag_entry.insert(0, "0")
        self.szabadsag_entry.grid(row=2, column=1, padx=10, pady=5)
        
        self.munkaszuneti_mv_label = Label(self.idoadatok_label_frame, text="Munkaszüneti munkavégzés")
        self.munkaszuneti_mv_label.grid(row=3, column=0, padx=10, pady=5)
        self.munkaszuneti_mv_entry = Entry(self.idoadatok_label_frame)
        self.munkaszuneti_mv_entry.insert(0, "0")
        self.munkaszuneti_mv_entry.grid(row=3, column=1, padx=10, pady=5)
        
        self.tulora_p = Label(self.idoadatok_label_frame, text="Túlóra P")
        self.tulora_p.grid(row=4, column=0, padx=10, pady=5)
        self.tulora_p_entry = Entry(self.idoadatok_label_frame)
        self.tulora_p_entry.insert(0, "0")
        self.tulora_p_entry.grid(row=4, column=1, padx=10, pady=5)
        
        
        
        # Buttons
        self.button_label_frame = LabelFrame(self.window)
        self.button_label_frame.pack(side=BOTTOM, fill=Y, padx=20, pady=5)
        
        self.szamol_button = tb.Button(self.button_label_frame, text="Számol", command=self.szamol)
        self.szamol_button.grid(row=0, column=0, padx=10, pady=10)
        
        self.vissza_button = tb.Button(self.button_label_frame, text="Vissza", command=self.window.destroy)
        self.vissza_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.fizetes_rogzites = tb.Button(self.button_label_frame, text="Fizetés rögzítés", bootstyle = SUCCESS, command=self.rogzites)
        self.fizetes_rogzites.grid(row=0, column=2, padx=10, pady=10)
        
        self.delete_button = tb.Button(self.button_label_frame, text="Törlés", bootstyle = DANGER, command=self.delete_data)
        self.delete_button.grid(row=0, column=3, padx=10, pady=10)
        
        
        
    
    
        
if __name__ == "__main__":
    app = tb.Window(themename="morph", title="Bérkalkulator")
    berkalkulator =Berkalkulator(app)
    berkalkulator.pack(fill="both", expand=True)
    app.mainloop()       
                
           