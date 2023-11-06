from Aplicatie import *
from Intrastructura import *
from Afis_verifica.output_verify_opp import output
def run_batch():
    el = input("Introdu comenzile dorite: ").split()
    """
    el = [ADD, data, suma, tip]
    el = [DEL, data]
    el = [UNDO]
    el = [FILTRARE, tip]
    """
    tranzactii = []
    tranzactii_anterioare = []
    opperatie_anterioara = 0
    idx = 0
    while not idx == len(el):
        if el[idx] == "ADD":
            tranzactii_anterioare.append(undo.tranzactii_prelucrate(tranzactii))
            rezultat_operatie = add_and_mod_tranzactii.add_tranzaction(el[idx + 1], el[idx + 2], el[idx + 3], tranzactii)
            if rezultat_operatie != False: 
                tranzactii = rezultat_operatie
            idx += 4
            output(tranzactii)
        
        elif el[idx] == "DEL":
            tranzactii_anterioare.append(undo.tranzactii_prelucrate(tranzactii))
            rezultat_operatie = stergere_tranzactii.stergere_tranzactii_dupa_tip(el[idx + 1], tranzactii)
            if rezultat_operatie != False: 
                tranzactii = rezultat_operatie
            idx += 2
            output(tranzactii)
        
        elif el[idx] == "UNDO":
            tranzactii = tranzactii_anterioare.pop()
            idx += 1
            output(tranzactii)

        elif el[idx] == "FILTRARE":
            tranzactii_anterioare.append(undo.tranzactii_prelucrate(tranzactii))
            rezultat_operatie = filtrare.filtrare_tranzactii_dupa_tip(el[idx + 1], tranzactii)
            if rezultat_operatie != False: 
                tranzactii = rezultat_operatie
            idx += 2
            output(tranzactii)