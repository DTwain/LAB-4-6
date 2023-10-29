from Aplicatie import * # dau import la toate fisierele pe care le-am declarat in __init__.py
from Intrastructura.corectitudine_data import data_valida

def linker(operatie, dict_of_tranzaction_data : dict, tranzactii : list) :
    """
    Functia va apela celelalte functii din modulul Aplicatie
    in functie de alegerea utilizatorului
    """
    if operatie == 1.1:
        tranzactii.append(dict_of_tranzaction_data)

    return tranzactii

def output(tranzactii: list):
    dimensiune = len(tranzactii)
    if dimensiune == 0:
        print("Nu exista tranzactii!\n")
    else:
        for poz in range(dimensiune):
            print("Tranzactia ", poz + 1, ":")
            print("     Data: ", tranzactii[poz]["data"])
            print("     Suma: ", tranzactii[poz]["suma"])
            print("     Tip: ", tranzactii[poz]["tip"] + "\n")
    
def operatie_de_forma_A_B(operatie):
    #operatia: A.B cu A si B numere naturale
    for i in range(len(operatie)):
        if operatie[i] != '.':
            if operatie[i] < '0' or operatie[i] > '9':
                return False
    return True

