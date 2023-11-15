from Aplicatie.FUNCTIONALITATI.ADD_MOD_VALIDARE_TRANZ.add_and_mod_tranzactii import add_tranzaction, update_tranzaction
from Aplicatie.FUNCTIONALITATI.rapoarte import suma_tranzactiilor_de_un_anumit_tip, soldul_contului_la_o_data_specificata, tranzactiile_IN_or_OUT_ordonate_dupa_suma
from Aplicatie.FUNCTIONALITATI.stergere_tranzactii import stergere_tranzactii_dupa_data, stergere_tranzactii_dupa_perioada, stergere_tranzactii_dupa_tip
from Aplicatie.FUNCTIONALITATI.undo import tranzactie_anterioara, tranzactii_prelucrate
from Aplicatie.GETTER_SETTER_validari.getter_setter_creaza_tranz import set_tranzactii
from Afis_verifica.output_verify_opp import output 

def prelucrare_comanda(sir: str, tranzactii: list, tranzactii_anterioare: list):
    sir = sir.split(" ")
    idx = 0
    while not idx == len(sir):
        try:
            if sir[idx] == "ADD":
                add_tranzaction(sir[idx + 1], sir[idx + 2], sir[idx + 3], tranzactii)
                set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
                idx = len(sir)
            
            elif sir[idx] == "DEL":
                if sir[idx + 1] == "DATA":
                    stergere_tranzactii_dupa_data(sir[idx + 2], tranzactii)
        
                elif sir[idx + 1] == "PERIOADA":
                    stergere_tranzactii_dupa_perioada(sir[idx + 2], sir[idx + 3], tranzactii)
                    
                elif sir[idx + 1] == "TIP":
                    stergere_tranzactii_dupa_tip(sir[idx + 2], tranzactii)
                idx = len(sir)
                set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
                
                output(tranzactii)
            
            elif sir[idx] == "UNDO":
                tranzactie_anterioara(tranzactii, tranzactii_anterioare)
                idx = len(sir)
                output(tranzactii)

            elif sir[idx] == "UPDATE":
                update_tranzaction(sir[idx + 1], sir[idx + 2], sir[idx + 3], int(sir[idx + 4]) - 1, tranzactii) 
                set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
                idx = len(sir)  

            elif sir[idx] == "RAPORT":
                rezultat_operatie = 0
                if sir[idx + 1] == "TIP":
                    rezultat_operatie = suma_tranzactiilor_de_un_anumit_tip(sir[idx + 2], tranzactii)
                elif sir[idx + 1] == "DATA":
                    rezultat_operatie = soldul_contului_la_o_data_specificata(sir[idx + 2], tranzactii)
                elif sir[idx + 1] == "SORTARE":
                    rezultat_operatie = tranzactiile_IN_or_OUT_ordonate_dupa_suma(sir[idx + 2], tranzactii)
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
    




