from Infrastructura import *
from Aplicatie.GETTER_SETTER_validari.getter_setter_creaza_tranz import get_data, get_suma, get_tip, set_tranzactii
from Aplicatie.GETTER_SETTER_validari.validari import validare_suma, validare_data, validare_tip
def cautare_tranzactii_mai_mari_decat_suma(suma, tranzactii: list) -> list:
    """
    functie care returneaza tranzactiile mai mari decat suma data
    preconditii: suma - float nenul
                 tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca suma nu este valida
    """
    validare_suma(suma)
    tranzactii_mai_mari_decat_suma = []
    for tranzactie in tranzactii:
        if float(get_suma(tranzactie)) > float(suma):
            set_tranzactii(tranzactii_mai_mari_decat_suma, tranzactie)
    return tranzactii_mai_mari_decat_suma

def cautare_tranzactii_dupa_data_si_suma(data, suma, tranzactii: list) -> list:
    """
    functie care returneaza tranzactiile mai mari decat "suma", dar efectuate in inainte de "data"
    preconditii: suma - float nenul
                 data - string de forma dd/mm/yyyy
                 tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "suma" / "data" nu sunt valide
    """
    validare_suma(suma)
    validare_data(data)
    data = data_default.get_data_with_default_format(data)
    tranzactii_mai_mari_decat_suma_mai_mici_decat_data = []
    for tranzactie in tranzactii:
        if float(get_suma(tranzactie)) > float(suma) and data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(get_data(tranzactie), data):
            set_tranzactii(tranzactii_mai_mari_decat_suma_mai_mici_decat_data, tranzactie)
    return tranzactii_mai_mari_decat_suma_mai_mici_decat_data

def cautare_tranzactii_dupa_tip(tip_ales:str, tranzactii: list) -> list:
    """
    functie care returneaza tranzactiile care au tipul "tip"
    preconditii : tip_ales - string egal cu "IN" sau "OUT"
                  tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "tip_ales" nu este valid
    """
    validare_tip(tip_ales)
    tranzactii_cu_tipul_dorit = []
    dimensiune = len(tranzactii)
    for tranzactie in tranzactii:
        if get_tip(tranzactie) == tip_ales.upper():
            set_tranzactii(tranzactii_cu_tipul_dorit, tranzactie)
    return tranzactii_cu_tipul_dorit

def test_cautare_tranzactii_mai_mari_decat_suma():
    assert cautare_tranzactii_mai_mari_decat_suma("200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == []
    assert cautare_tranzactii_mai_mari_decat_suma("200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]) == [{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    assert cautare_tranzactii_mai_mari_decat_suma("200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]) == [{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    
    try:
        cautare_tranzactii_mai_mari_decat_suma("-200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "-1740", 'tip': "OUT"}])
        assert False
    except ValueError:
        assert True
    
    try:
        cautare_tranzactii_mai_mari_decat_suma("1000d", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "-1740", 'tip': "OUT"}])
        assert False
    except ValueError:
        assert True

def test_cautare_tranzactii_dupa_data_si_suma():
    assert cautare_tranzactii_dupa_data_si_suma("12/3/2019", "200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == []
    assert cautare_tranzactii_dupa_data_si_suma("12/3/2019", "200", [{'data': "11/2/2019",'suma': "1500", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]) == [{'data': "11/2/2019",'suma': "1500", 'tip': "OUT"}]
    assert cautare_tranzactii_dupa_data_si_suma("12/3/2022", "200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "14/12/2020",'suma': "400", 'tip': "IN"}]) == [{'data': "14/12/2020",'suma': "400", 'tip': "IN"}]
    
    try:
        cautare_tranzactii_dupa_data_si_suma("12/3/2019", "-200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "-1740", 'tip': "OUT"}])
        assert False
    except ValueError:
        assert True
    
    try:
        cautare_tranzactii_dupa_data_si_suma("12/3/2019", "1000d", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "-1740", 'tip': "OUT"}])
        assert False
    except ValueError:
        assert True

    try:
        cautare_tranzactii_dupa_data_si_suma("29/2/2022", "200", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "-1740", 'tip': "OUT"}])
        assert False
    except ValueError:
        assert True

test_cautare_tranzactii_dupa_data_si_suma()
test_cautare_tranzactii_mai_mari_decat_suma()

