from Aplicatie import *
from Infrastructura import *
from Afis_verifica.output_verify_opp import output

def prelucrare_comanda(sir: str, tranzactii: list, tranzactii_anterioare: list):
    sir = sir.split(" ")
    idx = 0
    while not idx == len(sir):
        try:
            if sir[idx] == "ADD":
                add_and_mod_tranzactii.add_tranzaction(sir[idx + 1], sir[idx + 2], sir[idx + 3], tranzactii)
                getter_setter_creaza_tranz.set_tranzactii(tranzactii_anterioare, undo.tranzactii_prelucrate(tranzactii))
                idx = len(sir)
            
            elif sir[idx] == "DEL":
                if sir[idx + 1] == "DATA":
                    stergere_tranzactii.stergere_tranzactii_dupa_data(sir[idx + 2], tranzactii)
        
                elif sir[idx + 1] == "PERIOADA":
                    stergere_tranzactii.stergere_tranzactii_dupa_perioada(sir[idx + 2], sir[idx + 3], tranzactii)
                    
                elif sir[idx + 1] == "TIP":
                    stergere_tranzactii.stergere_tranzactii_dupa_tip(sir[idx + 2], tranzactii)
                idx = len(sir)
                getter_setter_creaza_tranz.set_tranzactii(tranzactii_anterioare, undo.tranzactii_prelucrate(tranzactii))
                
                output(tranzactii)
            
            elif sir[idx] == "UNDO":
                undo.tranzactie_anterioara(tranzactii, tranzactii_anterioare)
                idx = len(sir)
                output(tranzactii)

            elif sir[idx] == "UPDATE":
                add_and_mod_tranzactii.update_tranzaction(sir[idx + 1], sir[idx + 2], sir[idx + 3], int(sir[idx + 4]) - 1, tranzactii) 
                getter_setter_creaza_tranz.set_tranzactii(tranzactii_anterioare, undo.tranzactii_prelucrate(tranzactii))
                idx = len(sir)  

            elif sir[idx] == "RAPORT":
                rezultat_operatie = 0
                if sir[idx + 1] == "TIP":
                    rezultat_operatie = rapoarte.suma_tranzactiilor_de_un_anumit_tip(sir[idx + 2], tranzactii)
                elif sir[idx + 1] == "DATA":
                    rezultat_operatie = rapoarte.soldul_contului_la_o_data_specificata(sir[idx + 2], tranzactii)
                elif sir[idx + 1] == "SORTARE":
                    rezultat_operatie = rapoarte.tranzactiile_IN_or_OUT_ordonate_dupa_suma(sir[idx + 2], tranzactii)
                if type(rezultat_operatie) == list:
                    output(rezultat_operatie)
                else:
                    print(rezultat_operatie)
                idx = len(sir)

            else:
                idx = len(sir)

        except ValueError as ex:
            print(ex)
            return

def run_batch():
    tranzactii, tranzactii_anterioare = [], []  
    print("Introdu comenzile dorite:")
    sir = [0]
    while not len(sir) == 0:
        sir = input()
        prelucrare_comanda(sir, tranzactii, tranzactii_anterioare)

    output(tranzactii) 
    """
    el = [ADD data suma tip]
    el = [DEL data]
    el = [UNDO]
    el = [FILTRARE tip]
    el = [UPDATE data suma tip index_tranzactie]
    """
    




