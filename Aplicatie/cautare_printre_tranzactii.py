from Infrastructura import *
from Aplicatie.getter_setter_creaza_tranz import *
def filtrare_tranzactii_mai_mari_decat_suma(suma, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile mai mari decat suma data
    preconditii: suma - float nenul
                 tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca suma nu este valida
    """
    if corectitudine_suma.suma_valida(suma) or suma == "0":
        tranzactii_mai_mari_decat_suma = []
        for tranzactie in tranzactii:
            if float(get_suma(tranzactie)) > float(suma):
                tranzactii_mai_mari_decat_suma = set_tranzactii(tranzactii_mai_mari_decat_suma, tranzactie)
        return tranzactii_mai_mari_decat_suma
    else:
        return False

def filtrare_tranzactii_dupa_data_si_suma(data, suma, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile mai mari decat "suma", dar efectuate in inainte de "data"
    preconditii: suma - float nenul
                 data - string de forma dd/mm/yyyy
                 tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "suma" / "data" nu sunt valide
    """
    if corectitudine_suma.suma_valida(suma) or suma == "0":
        if corectitudine_data.data_valida(data):
            data = data_default.get_data_with_default_format(data)
            tranzactii_mai_mari_decat_suma_mai_mici_decat_data = []
            for tranzactie in tranzactii:
                if float(get_suma(tranzactie)) > float(suma) and data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(get_data(tranzactie), data):
                    tranzactii_mai_mari_decat_suma_mai_mici_decat_data = set_tranzactii(tranzactii_mai_mari_decat_suma_mai_mici_decat_data, tranzactie)
            return tranzactii_mai_mari_decat_suma_mai_mici_decat_data
    return False

def filtrare_tranzactii_dupa_tip(tip_ales:str, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile care au tipul "tip"
    preconditii : tip_ales - string egal cu "IN" sau "OUT"
                  tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "tip_ales" nu este valid
    """
    if tip_ales.upper() == "IN" or tip_ales.upper() == "OUT":
        tranzactii_cu_tipul_dorit = []
        dimensiune = len(tranzactii)
        for tranzactie in tranzactii:
            if get_tip(tranzactie) == tip_ales.upper():
                tranzactii_cu_tipul_dorit = set_tranzactii(tranzactii_cu_tipul_dorit, tranzactie)
        return tranzactii_cu_tipul_dorit
    return False



def test_filtrare_tranzactii_mai_mari_decat_suma():
    assert filtrare_tranzactii_mai_mari_decat_suma("100", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"50", 'tip':"IN"}]) == [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}]
    assert filtrare_tranzactii_mai_mari_decat_suma("1000", [{'data':"23/10/2023", 'suma':"1740.15", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}]) == [{'data':"23/10/2023", 'suma':"1740.15", 'tip':"IN"}]
    assert filtrare_tranzactii_mai_mari_decat_suma("10000", [{'data':"23/10/2023", 'suma':"1740", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}]) == []
    assert filtrare_tranzactii_mai_mari_decat_suma("-100", [{'data':"23/10/2023", 'suma':"1740.55", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}]) == False
    assert filtrare_tranzactii_mai_mari_decat_suma("120.0d", [{'data':"23/10/2023", 'suma':"500.48", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}]) == False
    assert filtrare_tranzactii_mai_mari_decat_suma("0", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}]) == [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}]

test_filtrare_tranzactii_mai_mari_decat_suma()

def test_filtrare_tranzactii_dupa_data_si_suma():
    assert filtrare_tranzactii_dupa_data_si_suma("23/10/2023", "100", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"22/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"50", 'tip':"IN"}]) == [{'data':"22/10/2023", 'suma':"900", 'tip':"IN"}]
    assert filtrare_tranzactii_dupa_data_si_suma("23/10/2023", "1000", [{'data':"14/9/2022", 'suma':"1740.15", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"200", 'tip':"IN"}]) == [{'data':"14/9/2022", 'suma':"1740.15", 'tip':"IN"}]
    assert filtrare_tranzactii_dupa_data_si_suma("23/10/2023", "10000", [{'data':"23/10/2023", 'suma':"1740", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"200", 'tip':"IN"}]) == []
    assert filtrare_tranzactii_dupa_data_si_suma("23/10/2023", "-100", [{'data':"23/10/2023", 'suma':"1740.55", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"200", 'tip':"IN"}]) == False
    assert filtrare_tranzactii_dupa_data_si_suma("23/10/2023", "120.0d", [{'data':"23/10/2023", 'suma':"500.48", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"200", 'tip':"IN"}]) == False
    assert filtrare_tranzactii_dupa_data_si_suma("29/2/2022", "1500", [{"data": "28/1/2022", "suma": "2000", "tip": "IN"}, {"data": "17/8/2021", "suma": "1100", "tip": "OUT"}]) == False

test_filtrare_tranzactii_dupa_data_si_suma()

def test_filtrare_tranzactii_dupa_tip():
    assert filtrare_tranzactii_dupa_tip("IN", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"22/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"50", 'tip':"IN"}]) == [{'data':"22/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"50", 'tip':"IN"}]
    assert filtrare_tranzactii_dupa_tip("iN", [{'data':"21/2/2022", 'suma':"760.13", 'tip':"IN"}, {'data':"28/5/2023", 'suma':"860", 'tip':"OUT"}, {'data':"12/6/2023", 'suma':"50", 'tip':"IN"}]) == [{'data':"21/2/2022", 'suma':"760.13", 'tip':"IN"}, {'data':"12/6/2023", 'suma':"50", 'tip':"IN"}]
    assert filtrare_tranzactii_dupa_tip("OUT", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"22/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"50", 'tip':"IN"}]) == [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}]
    assert filtrare_tranzactii_dupa_tip("OUT", [{'data':"22/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"50", 'tip':"IN"}]) == []
    assert filtrare_tranzactii_dupa_tip('oUtt', [{'data':"15/7/2022", 'suma':"532", 'tip':"IN"}, {'data':"5/2/2022", 'suma':"700", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"50", 'tip':"IN"}]) == False

test_filtrare_tranzactii_dupa_tip()
