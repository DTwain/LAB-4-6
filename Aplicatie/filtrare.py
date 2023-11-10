from Infrastructura import *
from Aplicatie.getter_setter_creaza_tranz import *
def filtrare_tranzactii_dupa_tip(tip: str, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile care NU au tipul "tip"
    preconditii : tip_ales - string egal cu "IN" sau "OUT"
                  tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "tip_ales" nu este valid
    """
    if tip.upper() == "IN" or tip.upper() == "OUT":
        tranzactii_cu_tipul_dorit = []
        for tranzactie in tranzactii:
            if not get_tip(tranzactie) == tip.upper():
                set_tranzactii(tranzactii_cu_tipul_dorit, tranzactie)
        return tranzactii_cu_tipul_dorit
    else:
        return False

def filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit(suma, tip, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile care au tipul != "tip" si NU au suma mai mica decat "suma"
    preconditii: suma - float nenul
                 tip - string egal cu "IN" sau "OUT"
                 tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "suma" / "tip" nu sunt valide
    """
    if corectitudine_suma.suma_valida(suma):
        if tip.upper() == "IN" or tip.upper() == "OUT":
            new_list_of_tranzaction = []
            for tranzactie in tranzactii:
                if not (float(get_suma(tranzactie)) < float(suma) and get_tip(tranzactie) == tip.upper()):
                    set_tranzactii(new_list_of_tranzaction, tranzactie)
            return new_list_of_tranzaction
    return False


def test_filtrare_tranzactii_dupa_tip():
    rez = filtrare_tranzactii_dupa_tip("IN", [{'data':"12/3/2019", 'suma':"400", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}, {'data':"14/7/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}]

    rez = filtrare_tranzactii_dupa_tip("OUT", [{'data':"25/5/2020", 'suma':"1500", 'tip':"IN"}, {'data':"15/6/2021", 'suma':"400", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"120", 'tip':"IN"}])
    assert rez == [{'data':"25/5/2020", 'suma':"1500", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"120", 'tip':"IN"}]

    rez = filtrare_tranzactii_dupa_tip("in", [{'data':"29/2/2000", 'suma':"1400", 'tip':"IN"}, {'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}, {'data':"30/4/2000", 'suma':"700", 'tip':"IN"}])
    assert rez == [{'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}]

    rez = filtrare_tranzactii_dupa_tip("out", [{'data':"8/10/2003", 'suma':"650", 'tip':"OUT"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"1000", 'tip':"OUT"}])
    assert rez == []

test_filtrare_tranzactii_dupa_tip()

def test_filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit():
    rez = filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit("100", "IN", [{'data':"12/3/2019", 'suma':"400", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}, {'data':"14/7/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"12/3/2019", 'suma':"400", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}, {'data':"14/7/2022", 'suma':"100", 'tip':"IN"}]

    rez = filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit("200", "OUT", [{'data':"25/5/2020", 'suma':"1500", 'tip':"IN"}, {'data':"15/6/2021", 'suma':"400", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"120", 'tip':"OUT"}])
    assert rez == [{'data':"25/5/2020", 'suma':"1500", 'tip':"IN"}, {'data':"15/6/2021", 'suma':"400", 'tip':"OUT"}]

    rez = filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit("1000", "in", [{'data':"29/2/2000", 'suma':"1400", 'tip':"IN"}, {'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}, {'data':"30/4/2000", 'suma':"700", 'tip':"IN"}])
    assert rez == [{'data':"29/2/2000", 'suma':"1400", 'tip':"IN"}, {'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}]

    rez = filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit("1000", "out", [{'data':"8/10/2003", 'suma':"650", 'tip':"OUT"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"1000", 'tip':"OUT"}])
    assert rez == [{'data':"21/2/2022", 'suma':"1000", 'tip':"OUT"}]

    rez = filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit("1000", "in", [{'data':"8/10/2003", 'suma':"59.44", 'tip':"IN"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"999", 'tip':"IN"}])
    assert rez == []

test_filtrare_tranzactii_cu_suma_mai_mare_egal_cu_x_si_cu_tipul_specificat_diferit()
