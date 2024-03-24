import sqlite3
import berkalkulatorwindow
from ui_berkalkulator import Ui_Berkalkulator

class Berkalkulator:
    def __init__(self, path, parent:None) -> None:
        super().__init__(parent)
        self.ui = Ui_Berkalkulator()
        self.ui.setupUi(self)
        
        self.path = path
        
        
        
        
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
        havi_oraszam = int(self.ui.ledolgozottNapokLineEdit.text()) * 8.17
        napiber_osszege = int(self.ui.alabberLineEdit.text()) / havi_oraszam
        
    
        return int(napiber_osszege)
        
        
    
    def havi_beres_idober(self) -> int:
        ledolgozott_ido = 0
        if self.ui.SzabadsagLineEdit == 0:
            ledolgozott_ido = ledolgozott_ido + int(self.ui.ledolgozottNapokLineEdit.text())
        else:    
            ledolgozott_ido = int(self.ui.ledolgozottNapokLineEdit.text()) - int(self.ui.SzabadsagLineEdit.text())
            self.ui.ledolgozottNapokLineEdit.clear()
            self.ui.ledolgozottNapokLineEdit.insert(str(ledolgozott_ido))
        try:
            haviberes_idober = (int(self.ui.ledolgozottNapokLineEdit.text()) / int(self.ui.ledolgozottNapokLineEdit.text())) * ledolgozott_ido 
            self.ui.haiberesidoberLineEdit.clear()
            self.ui.haiberesidoberLineEdit.insert(str(haviberes_idober))
            return int(haviberes_idober)
        except:
            return 0
           
    def tulora_alap(self) -> int:
        alapber = int(self.ui.alabberLineEdit.text())
        
        if int(self.ui.tuloraLineEdit_2.text()) >= 0:
            ido = int(self.ui.tuloraLineEdit_2.text()) 
            t_ora = ido * 8.17
            m_rend_ido = int(self.ui.ledolgozottNapokLineEdit.text()) * 8.17
            tulóra_osszeg = ((alapber / m_rend_ido) * t_ora ) * 0.94  
        else:
            return 0
        
        self.ui.tuloraAlapLineEdit.clear()
        self.ui.tuloraAlapLineEdit.insert(str(tulóra_osszeg))
        return int(tulóra_osszeg) 
            
            
        
    def fizetett_szabadsag(self) -> int:
        
        if int(self.ui.SzabadsagLineEdit.text()) >= 0:
            napok = int(self.ui.SzabadsagLineEdit.text()) * 8.17
            fizetett_szabadsag = napok * 7038
        else:
            fizetett_szabadsag = 0  
        
        
        self.ui.fizetettSzLineEdit.clear()
        self.ui.fizetettSzLineEdit.insert(str(fizetett_szabadsag))
        return int(fizetett_szabadsag)       
            
        
    def munkaszuneti_munkavegzes(self) -> int:
        napiber = self.napiber()
        munkaszuneti_ora = int(self.ui.munkaszuntimvLineEdit.text()) * 8.17
        szumma_munkaszuneti = (napiber * munkaszuneti_ora) * 1.45
           
        self.ui.munkaszunetiLineEdit.clear()
        self.ui.munkaszunetiLineEdit.insert(str(szumma_munkaszuneti))
        
        
        return int(szumma_munkaszuneti)   
        
    def muszakpotlek(self) -> int:
        haviber = self.havi_beres_idober()
        m_potlek = haviber * 0.45
        
        self.ui.mpotlekLineEdit.clear()
        self.ui.mpotlekLineEdit.insert(str(m_potlek))
        
        
        return int(m_potlek)
        
    def brutto_ber(self)-> int:
        values = [self.havi_beres_idober(), self.tulora_alap(), self.fizetett_szabadsag(), self.munkaszuneti_munkavegzes(), self.muszakpotlek(), 26736 , self.p_tulora(), self.t_muszakpotlek()]
        # values_int = list(map(int, values))
        if int(self.ui.jutalomLineEdit.text()) >= 0:
            values.append(int(self.ui.jutalomLineEdit.text()))
        else:
            values.append(0)    
        total = sum(values)
        self.ui.bruttoberLineEdit.clear()
        self.ui.bruttoberLineEdit.insert(str(total))
        return total

        # Itt tartok a QT integrálással // !!! Át kell nézni az input fieldeket, hogy minden függvénynek megvan e a mezője

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