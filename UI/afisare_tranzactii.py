def output(tranzactii: list):
    dimensiune = len(tranzactii)
    if dimensiune == 0:
        print("\nNu exista tranzactii!\n")
    else:
        for poz in range(dimensiune):
            print("Tranzactia ", poz + 1, ":")
            print("     Data: ", tranzactii[poz]["data"])
            print("     Suma: ", tranzactii[poz]["suma"])
            print("     Tip:  ", tranzactii[poz]["tip"] + "\n")
    