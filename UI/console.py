"""
Interfata aplicatiei in terminal 
"""
from Aplicatie import *
from Afis_verifica.output_verify_opp import operatie_de_forma_A_B
from Afis_verifica.output_verify_opp import output 
def meniu():
    print("Bine ati venit!")
    print("1. Adaugare de noi tranzactii:")
    print("     1.1 Adaugare tranzactie")
    print("     1.2 Actualizare tranzactie\n")
    print("2. Stergere de tranzactii:")
    print("     2.1 Sterge toate tranzactiiele dintr-o data specificata")
    print("     2.2 Sterge toate tranzactiile dintr-o perioada specificata")
    print("     2.3 Sterge toate tranzactiile de un anumit tip\n")
    print("3. Cautari:")
    print("     3.1 Tipărește tranzacțiile cu sume mai mari decât o sumă dată")
    print("     3.2 Tipărește toate tranzacțiile efectuate înainte de o zi și mai mari decât o sumă")
    print("     3.3 Tipărește tranzacțiile de un anumit tip\n")
    print("4. Rapoarte:")
    print("     4.1 Suma totală a tranzacțiilor de un anumit tip")
    print("     4.2 Soldul contului la o data specificata")
    print("     4.3 Tipărește toate tranzacțiile de un anumit tip ordonate după sumă\n")
    print("5. Filtrari:")
    print("     5.1 Elimină toate tranzacțiile de un anumit tip")
    print("     5.2 Elimină toate tranzacțiile mai mici decât o sumă dată care au tipul specificat\n")
    print("6. UNDO\n")

tranzactii = []
tranzactii_anterioare = [] 
def opp(operatie):
    global tranzactii
    global tranzactii_anterioare
    if operatie == 1.1:
        print("Adaugare tranzactie:\n")
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        suma = input("Introduceti suma: ")
        tip = input("Introduceti tipul: IN/OUT: ")
        rezultat_operatie = add_and_mod_tranzactii.add_tranzaction(data, suma, tip, tranzactii)
        if rezultat_operatie == False:
            print("DATE INVALIDE!!\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)  

    elif operatie == 1.2:
        print("Alege tranzactia pe care vrei sa o modifici: \n")
        output(tranzactii)
        nr_tranzactie = input("Introduceti numarul tranzactiei: ")
        nr_tranzactie = int(nr_tranzactie) - 1 
        data = input("Introduceti noua data sub forma DD/MM/YYYY: ")
        suma = input("Introduceti noua suma: ")
        tip = input("Introduceti noul tip: IN/OUT: ")
        rezultat_operatie = add_and_mod_tranzactii.update_tranzaction(data, suma, tip, nr_tranzactie, tranzactii)
        if rezultat_operatie == False:
            print("DATE INVALIDE!!\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(tranzactii)
    
    elif operatie == 2.1:
        print("Alege data din care vrei sa stergi tranzactiile: \n")
        output(tranzactii)
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        rezultat_operatie = stergere_tranzactii.filtrare_tranzactii_dupa_data(data, tranzactii)
        if rezultat_operatie == False:
            print("DATA ALEASA NU ESTE VALIDA!!\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(tranzactii)

    elif operatie == 2.2:
        print("Alege perioada din care vrei sa stergi tranzactiile: \n")
        output(tranzactii)
        data_start = input("Introduceti data de inceput sub forma DD/MM/YYYY: ")
        data_end = input("Introduceti data de sfarsit sub forma DD/MM/YYYY: ")
        rezultat_operatie = stergere_tranzactii.filtrare_tranzactii_dupa_perioada(data_start, data_end, tranzactii)
        if rezultat_operatie == False:
            print("PERIOADA ALEASA NU ESTE VALIDA!!\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(tranzactii)

    elif operatie == 2.3:
        print("Alege tipul tranzactiilor pe care vrei sa le stergi: \n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        rezultat_operatie = stergere_tranzactii.filtrare_tranzactii_dupa_tip(tip, tranzactii)
        if rezultat_operatie == False:
            print("TIPUL ALES NU ESTE VALID!!\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(tranzactii)
        
    elif operatie == 3.1:
        print("Alege suma dupa care vrei sa cauti tranzactiile: \n")
        output(tranzactii)
        suma = input("Introduceti suma: ")
        rezultat_operatie = cautare_printre_tranzactii.filtrare_tranzactii_mai_mari_decat_suma(suma, tranzactii)
        if rezultat_operatie == False:
            print("SUMA ALEASA ESTE MAI MARE DECAT SUMA ORICAREI TRANZACTII!!\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(rezultat_operatie)
    
    elif operatie == 3.2:
        print("Alege data si suma dupa care vrei sa cauti tranzactiile: \n")
        output(tranzactii)
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        suma = input("Introduceti suma: ")
        rezultat_operatie = cautare_printre_tranzactii.filtrare_tranzactii_dupa_data_si_suma(data, suma, tranzactii)
        if rezultat_operatie == False:
            print("DATELE INTRODUSE SUNT INVALIDE\n")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(rezultat_operatie)

    elif operatie == 3.3:
        print("Alege tipul tranzactiilor pe care vrei sa le cauti: \n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        rezultat_operatie = cautare_printre_tranzactii.filtrare_tranzactii_dupa_tip(tip, tranzactii)
        if rezultat_operatie == False:
            print("TIPUL INTRODUS ESTE INVALID!!")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(rezultat_operatie)

    elif operatie == 4.1:
        print("Alege tipul de tranzactie la care doresti sa afli suma tuturor tranzactiilor:\n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        rezultat_operatie = rapoarte.suma_tranzactiilor_de_un_anumit_tip(tip, tranzactii)
        if rezultat_operatie == False:
            print("TIPUL INTRODUS ESTE INVALID!!")
            opp(operatie)
        else:
            print(rezultat_operatie) 

    elif operatie == 4.2:
        print("Alegeti data la care doriti sa aflati soldul contului: ")
        output(tranzactii)
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        rezultat_operatie = rapoarte.soldul_contului_la_o_data_specificata(data, tranzactii)
        if rezultat_operatie == False:
            print("Data introdusa este invalida")
            opp(operatie)
        else:
            print(f"Soldul contului pana la data de {data}, inclusiv este: {rezultat_operatie}")

    elif operatie == 4.3:
        print("Alegeti tipul tranzactiilor pe care doriti sa le vedeti sortate dupa suma:")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        rezultat_operatie = rapoarte.tranzactiile_IN_or_OUT_ordonate_dupa_suma(tranzactii)
        if rezultat_operatie == False:
            print("TIPUL INTRODUS ESTE INVALID")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(rezultat_operatie)
    elif operatie == 5.1:
        opp(2.3)
    elif operatie == 5.2:
        ##5.2 Elimină toate tranzacțiile mai mici decât o sumă dată care au tipul specificat
        print("Alegeti suma si tipul dupa care sa se filtreze tranzactiile:")
        output(tranzactii)
        suma = input("Introduceti suma: ")
        tipul = input("Introduceti tipul: IN/OUT: ")
        rezultat_operatie = filtrare.filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat(suma, tipul, tranzactii)
        if rezultat_operatie == False:
            print("DATELE INTRODUSE SUNT INVALIDE")
            opp(operatie)
        else:
            tranzactii = rezultat_operatie
            tranzactii_anterioare.append(tranzactii)
            output(rezultat_operatie)
            
    
    elif operatie == 6:
        if len(tranzactii_anterioare) == 0:
            print("Ai ajuns la inceput!")
        else:
            tranzactii = tranzactii_anterioare[-1]
            tranzactii_anterioare.pop()
        

def run_console(nr_crt = 1):
    if nr_crt == 1:
        meniu()
    operatie = input(f"\n{nr_crt}.Introduceti operatia dorita SUB FORMA   A.B  : ")
    if operatie_de_forma_A_B(operatie):
        operatie = float(operatie)
    while not operatie in [1.1, 1.2, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 6] :
        print("Operatie invalida!")
        operatie = input(f"{nr_crt}Introduceti operatia dorita SUB FORMA   A.B  : ")
        if operatie_de_forma_A_B(operatie):
            operatie = float(operatie)

    opp(operatie)

    rep = input("\nDoriti sa mai efectuati o operatie? da/nu: ")
    rep = rep.lower()
    if rep == "da":
        run_console(nr_crt = nr_crt + 1)
    else:
        print("La revedere!")
    
    


