from Infrastructura import *
from Aplicatie.getter_setter_creaza_tranz import *
def stergere_tranzactii_dupa_data(data, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile care NU au data == "data"
    preconditii :   data - string de forma dd/mm/yyyy
                    tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "data" nu este valida
    """
    if corectitudine_data.data_valida(data):
        data = data_default.get_data_with_default_format(data) # data este de forma dd/mm/yyyy
        for tranzactie in tranzactii[:]: # [:] - copie a listei https://gist.github.com/alexlouden/9f1ab4354d1c68ae4c1c94126ac51a20
            if get_data(tranzactie) == data:
                tranzactii.remove(tranzactie)
        return tranzactii
    else:
        return False

def stergere_tranzactii_dupa_perioada(data_start, data_end, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile care NU au data intre "data_start" si "data_end"
    preconditii :   data_start - string de forma dd/mm/yyyy
                    data_end - string de forma dd/mm/yyyy
                    tranzactii - lista de dictionare
                    data_start <= data_end
    postconditii: lista de dictionare sau False daca "data_start" sau "data_end" nu sunt valide
    """
    if corectitudine_data.data_valida(data_start) and corectitudine_data.data_valida(data_end):
        data_start = data_default.get_data_with_default_format(data_start)
        data_end = data_default.get_data_with_default_format(data_end)
        if not data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(data_start, data_end) and not data_start == data_end:
            return False
        else:
            for tranzactie in tranzactii[:]:
                if data_apartine_perioada.verify_data_is_in_range(data_start, get_data(tranzactie), data_end):
                    tranzactii.remove(tranzactie)
        return tranzactii
    else:
        return False
    

def stergere_tranzactii_dupa_tip(tip: str, tranzactii: list) -> {bool, list}:
    """
    functie care returneaza tranzactiile care NU au tipul "tip"
    preconditii : tip_ales - string egal cu "IN" sau "OUT"
                  tranzactii - lista de dictionare
    postconditii: lista de dictionare sau False daca "tip_ales" nu este valid
    """
    if tip.upper() == "IN" or tip.upper() == "OUT":
        for tranzactie in tranzactii[:]:
            if get_tip(tranzactie) == tip.upper():
                tranzactii.remove(tranzactie)
        return tranzactii
    else:
        return False


def test_stergere_tranzactii_dupa_data():
    rez = stergere_tranzactii_dupa_data("21/2/2022", [{'data': "12/3/2019", 'suma':"123", 'tip':"IN"}, {'data': "21/2/2022", 'suma':"323", 'tip':"OUT"}, {'data': "21/2/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"12/3/2019", 'suma':"123", 'tip':"IN"}]

    rez = stergere_tranzactii_dupa_data("1/6/2017", [{'data':"12/3/2019", 'suma':"1000", 'tip':"IN"}, {'data':"1/6/2017", 'suma':"200", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"12/3/2019", 'suma':"1000", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"100", 'tip':"IN"}]

    rez = stergere_tranzactii_dupa_data("23/10/2023",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == []
    
    rez = stergere_tranzactii_dupa_data("32/3/2020",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == False

test_stergere_tranzactii_dupa_data()

def test_stergere_tranzactii_dupa_perioada():
    rez = stergere_tranzactii_dupa_perioada("12/3/2019", "1/9/2019", [{'data':"11/3/2019", 'suma':"200", 'tip':"IN"}, {'data':"27/7/2019", 'suma':"323", 'tip':"OUT"}, {'data':"12/9/2019", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"11/3/2019", 'suma':"200", 'tip':"IN"}, {'data':"12/9/2019", 'suma':"100", 'tip':"IN"}]

    rez = stergere_tranzactii_dupa_perioada("1/6/2017", "21/2/2022", [{'data':"12/3/2019", 'suma':"1000", 'tip':"IN"}, {'data':"1/6/2017", 'suma':"200", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == []

    rez = stergere_tranzactii_dupa_perioada("23/10/2023", "23/10/2023",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == []

    rez = stergere_tranzactii_dupa_perioada("23/10/2023", "23/10/2022",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == False

test_stergere_tranzactii_dupa_perioada()

def test_stergere_tranzactii_dupa_tip():
    rez = stergere_tranzactii_dupa_tip("IN", [{'data':"12/3/2019", 'suma':"400", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}, {'data':"14/7/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}]

    rez = stergere_tranzactii_dupa_tip("OUT", [{'data':"25/5/2020", 'suma':"1500", 'tip':"IN"}, {'data':"15/6/2021", 'suma':"400", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"120", 'tip':"IN"}])
    assert rez == [{'data':"25/5/2020", 'suma':"1500", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"120", 'tip':"IN"}]

    rez = stergere_tranzactii_dupa_tip("in", [{'data':"29/2/2000", 'suma':"1400", 'tip':"IN"}, {'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}, {'data':"30/4/2000", 'suma':"700", 'tip':"IN"}])
    assert rez == [{'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}]

    rez = stergere_tranzactii_dupa_tip("out", [{'data':"8/10/2003", 'suma':"650", 'tip':"OUT"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"1000", 'tip':"OUT"}])
    assert rez == []

test_stergere_tranzactii_dupa_tip()