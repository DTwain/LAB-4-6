from Aplicatie import *
from Infrastructura import *
from Afis_verifica.output_verify_opp import output

tranzactii = []
tranzactii_anterioare = []
def prelucrare_comanda(sir: str):
    global tranzactii, tranzactii_anterioare
    sir = sir.split(" ")
    idx = 0
    while not idx == len(sir):
        if sir[idx] == "ADD":
            tranzactii_anterioare = getter_setter_creaza_tranz.set_tranzactii(tranzactii_anterioare, undo.tranzactii_prelucrate(tranzactii))
            rezultat_operatie = add_and_mod_tranzactii.add_tranzaction(sir[idx + 1], sir[idx + 2], sir[idx + 3], tranzactii)
            if rezultat_operatie != False: 
                tranzactii = rezultat_operatie
            idx += 4
        
        elif sir[idx] == "DEL":
            tranzactii_anterioare = getter_setter_creaza_tranz.set_tranzactii(tranzactii_anterioare, undo.tranzactii_prelucrate(tranzactii))
            rezultat_operatie = 0
            if sir[idx + 1] == "DATA":
                rezultat_operatie = stergere_tranzactii.stergere_tranzactii_dupa_data(sir[idx + 2], tranzactii)
            if sir[idx + 1] == "PERIOADA":
                rezultat_operatie = stergere_tranzactii.stergere_tranzactii_dupa_perioada(sir[idx + 2], sir[idx + 3], tranzactii)
                idx += 4
            if sir[idx + 1] == "TIP":
                rezultat_operatie = stergere_tranzactii.stergere_tranzactii_dupa_tip(sir[idx + 2], tranzactii)
                idx += 3
            if rezultat_operatie != False: 
                tranzactii = rezultat_operatie
            output(tranzactii)
        
        elif sir[idx] == "UNDO":
            tranzactii = tranzactii_anterioare.pop()
            idx += 1
            output(tranzactii)

        elif sir[idx] == "UPDATE":
            output(tranzactii)
            tranzactii_anterioare = getter_setter_creaza_tranz.set_tranzactii(tranzactii_anterioare, undo.tranzactii_prelucrate(tranzactii))
            rezultat_operatie = add_and_mod_tranzactii.update_tranzaction(sir[idx + 1], sir[idx + 2], sir[idx + 3], sir[idx + 4], tranzactii) 
            if rezultat_operatie != False:
                tranzactii = rezultat_operatie
            idx += 5
            print("\n\n")
            output(tranzactii)

        elif sir[idx] == "RAPORT":
            output(tranzactii)
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
                print(f"{sir[idx + 1]} : {rezultat_operatie}\n")
            idx += 3

def run_batch():
    global tranzactii, tranzactii_anterioare
    print("Introdu comenzile dorite:")
    sir = [0]
    while not len(sir) == 0:
        sir = input()
        prelucrare_comanda(sir)
         
    """
    el = [ADD data suma tip]
    el = [DEL data]
    el = [UNDO]
    el = [FILTRARE tip]
    el = [UPDATE data suma tip index_tranzactie]
    """
    




