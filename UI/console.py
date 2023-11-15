"""
Interfata aplicatiei in terminal 
"""
from Aplicatie.FUNCTIONALITATI.ADD_MOD_VALIDARE_TRANZ.add_and_mod_tranzactii import add_tranzaction, update_tranzaction
from Aplicatie.FUNCTIONALITATI.cautare_printre_tranzactii import cautare_tranzactii_mai_mari_decat_suma, cautare_tranzactii_dupa_data_si_suma, cautare_tranzactii_dupa_tip
from Aplicatie.FUNCTIONALITATI.filtrare import filtrare_tranzactii_dupa_tip, filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit
from Aplicatie.FUNCTIONALITATI.rapoarte import suma_tranzactiilor_de_un_anumit_tip, soldul_contului_la_o_data_specificata, tranzactiile_IN_or_OUT_ordonate_dupa_suma
from Aplicatie.FUNCTIONALITATI.stergere_tranzactii import stergere_tranzactii_dupa_data, stergere_tranzactii_dupa_perioada, stergere_tranzactii_dupa_tip
from Aplicatie.FUNCTIONALITATI.undo import tranzactie_anterioara, tranzactii_prelucrate
from Aplicatie.GETTER_SETTER_validari.getter_setter_creaza_tranz import set_tranzactii
from Afis_verifica.output_verify_opp import operatie_de_forma_A_B, output 
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
    print("6. UNDO:")
    print("     6.0 UNDO")

def opp(operatie, tranzactii, tranzactii_anterioare):
    
    if operatie == 1.1:
        print("Adaugare tranzactie:\n")
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        suma = input("Introduceti suma: ")
        tip = input("Introduceti tipul: IN/OUT: ")
        try:
            add_tranzaction(data, suma, tip, tranzactii)
            set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
        except ValueError as ve:
            print("\n" + ve + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 1.2:
        print("Alege tranzactia pe care vrei sa o modifici: \n")
        output(tranzactii)
        nr_tranzactie = input("Introduceti numarul tranzactiei: ")
        nr_tranzactie = int(nr_tranzactie) - 1 
        data = input("Introduceti noua data sub forma DD/MM/YYYY: ")
        suma = input("Introduceti noua suma: ")
        tip = input("Introduceti noul tip: IN/OUT: ")
        try:
            update_tranzaction(data, suma, tip, nr_tranzactie, tranzactii)
            set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
        except ValueError as ve:
            print("\n" + ve + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)
    
    elif operatie == 2.1:
        print("Alege data din care vrei sa stergi tranzactiile: \n")
        output(tranzactii)
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        try:
            stergere_tranzactii_dupa_data(data, tranzactii)
            set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
        except ValueError as ve:
            print("\n" + ve + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 2.2:
        print("Alege perioada din care vrei sa stergi tranzactiile: \n")
        output(tranzactii)
        data_start = input("Introduceti data de inceput sub forma DD/MM/YYYY: ")
        data_end = input("Introduceti data de sfarsit sub forma DD/MM/YYYY: ")
        try:
            stergere_tranzactii_dupa_perioada(data_start, data_end, tranzactii)
            set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
        except ValueError as ve:
            print("\n" + ve + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 2.3:
        print("Alege tipul tranzactiilor pe care vrei sa le stergi: \n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        try:
            stergere_tranzactii_dupa_tip(tip, tranzactii)
            set_tranzactii(tranzactii_anterioare, tranzactii_prelucrate(tranzactii))
        except ValueError as ve:
            print("\n" + ve + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)
        
        
    elif operatie == 3.1:
        print("Alege suma dupa care vrei sa cauti tranzactiile: \n")
        output(tranzactii)
        suma = input("Introduceti suma: ")
        try:
            rezultat_operatie = cautare_tranzactii_mai_mari_decat_suma(suma, tranzactii)
            output(rezultat_operatie)
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)
    
    elif operatie == 3.2:
        print("Alege data si suma dupa care vrei sa cauti tranzactiile: \n")
        output(tranzactii)
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        suma = input("Introduceti suma: ")
        try:
            rezultat_operatie = cautare_tranzactii_dupa_data_si_suma(data, suma, tranzactii)
            output(rezultat_operatie)
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 3.3:
        print("Alege tipul tranzactiilor pe care vrei sa le cauti: \n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        try:
            rezultat_operatie = cautare_tranzactii_dupa_tip(tip, tranzactii)
            output(rezultat_operatie)
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 4.1:
        print("Alege tipul de tranzactie la care doresti sa afli suma tuturor tranzactiilor:\n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        try:
            rezultat_operatie = suma_tranzactiilor_de_un_anumit_tip(tip, tranzactii)
            print(f"Suma tranzactiilor de tipul {tip} este: {rezultat_operatie}")
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 4.2:
        print("Alegeti data la care doriti sa aflati soldul contului: ")
        output(tranzactii)
        data = input("Introduceti data sub forma DD/MM/YYYY: ")
        try:
            rezultat_operatie = soldul_contului_la_o_data_specificata(tip, tranzactii)
            print(f"Soldul contului la data de {data} este: {rezultat_operatie}")
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 4.3:
        print("Alegeti tipul tranzactiilor pe care doriti sa le vedeti sortate dupa suma:")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        try:
            rezultat_operatie = tranzactiile_IN_or_OUT_ordonate_dupa_suma(tip, tranzactii)
            output(rezultat_operatie)
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)
            
    elif operatie == 5.1:
        print("Alege tipul tranzactiilor pe care doresti sa nu le ai in lista de tranzactii: \n")
        output(tranzactii)
        tip = input("Introduceti tipul: IN/OUT: ")
        try:
            rezultat_operatie = filtrare_tranzactii_dupa_tip(tip, tranzactii)
            output(rezultat_operatie)
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)

    elif operatie == 5.2:
        print("Alegeti suma si tipul dupa care sa se filtreze tranzactiile:")
        output(tranzactii)
        suma = input("Introduceti suma: ")
        tipul = input("Introduceti tipul: IN/OUT: ")
        try:
            rezultat_operatie = filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit(suma, tipul, tranzactii)
            output(rezultat_operatie)
        except ValueError as VE:
            print("\n" + VE + "\n")
            opp(operatie, tranzactii, tranzactii_anterioare)
            
    elif operatie == 6.0:
        tranzactie_anterioara(tranzactii, tranzactii_anterioare)


def run_console(nr_crt = 1):
    tranzactii = []
    tranzactii_anterioare = [] 
    rep = "da"
    meniu()
    while rep == "da":
        try:
            operatie = input(f"\n{nr_crt}.Introduceti operatia dorita SUB FORMA   A.B  : ")
            operatie_de_forma_A_B(operatie)
            operatie = float(operatie)

            while not operatie in [1.1, 1.2, 2.1, 2.2, 2.3, 3.1, 3.2, 3.3, 4.1, 4.2, 4.3, 5.1, 5.2, 6.0] :
                operatie = input(f"\n{nr_crt}.Introduceti operatia dorita SUB FORMA   A.B  : ")
                operatie_de_forma_A_B(operatie)
                operatie = float(operatie)

            opp(operatie, tranzactii, tranzactii_anterioare)
            
            rep = input("\nDoriti sa mai efectuati o operatie? da/nu: ")
            rep = rep.lower()
            if rep == "NU":
                print("La revedere!")
                break
            else:
                nr_crt += 1
                continue
        except ValueError as VE:
            assert str(VE) == "Operatia nu este valida"
            print("OPERATIE INVALIDA!")
        
    


