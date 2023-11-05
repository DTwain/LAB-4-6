def output(tranzactii: list):
    dimensiune = len(tranzactii)
    if dimensiune == 0:
        print("\nNu exista tranzactii!\n")
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
