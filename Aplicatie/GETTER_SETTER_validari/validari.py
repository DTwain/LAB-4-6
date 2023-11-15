from Infrastructura.corectitudine_suma import suma_valida
from Infrastructura.corectitudine_data import data_valida
from Infrastructura.data_apartine_perioada import verificare_data_1_mai_mica_decat_data_2
def validare_suma(suma):
    if not (suma_valida(suma) or suma == "0"):  
        raise ValueError("Suma invalida")

def validare_data(data):
    if not data_valida(data):
        raise ValueError("Data invalida")
    
def validare_tip(tip):
    if not (tip.upper() == "IN" or tip.upper() == "OUT"):
        raise ValueError("Tip invalid")
    
def validare_data_start_mai_mica_decat_data_end(data_start, data_end):
    if not verificare_data_1_mai_mica_decat_data_2(data_start, data_end) and not data_start == data_end:
        raise ValueError("data_start > data_end")

def validare_lungime_lista(tranzactii_precedente: list):
    if len(tranzactii_precedente) == 0: 
        raise ValueError("NU SE POATE DA UNDO")

