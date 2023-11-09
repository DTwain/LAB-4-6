from Infrastructura import *
from Aplicatie.getter_setter_creaza_tranz import set_tranzactii_de_index, set_tranzactii, creaza_tranzactie
def add_tranzaction(data, suma, tip, tranzactii: list) -> {list, bool} :
    if corectitudine_data.data_valida(data) :
        if corectitudine_suma.suma_valida(suma) :
            if tip.upper() == "IN" or tip.upper() == "OUT":
                tranzactie_noua = creaza_tranzactie(data, suma, tip)
                tranzactii = set_tranzactii(tranzactii, tranzactie_noua)
                return tranzactii
    return False

def update_tranzaction(data, suma, tip, nr_tranzactie, tranzactii : list ) -> {list, bool}:
    if corectitudine_data.data_valida(data) :
        if corectitudine_suma.suma_valida(suma) :
            if tip.upper() == "IN" or tip.upper() == "OUT":
                if nr_tranzactie >= 0 or nr_tranzactie < len(tranzactii):
                    tranzactie_noua = creaza_tranzactie(data, suma, tip)
                    tranzactii = set_tranzactii_de_index(tranzactii, nr_tranzactie, tranzactie_noua)
                    return tranzactii
    return False 

def test_add_tranzaction():
    assert add_tranzaction("12/3/2019", "123", "IN", []) == [{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]
    assert add_tranzaction("12/3/2019", "123.12", "OUT", []) == [{'data': "12/3/2019",'suma': "123.12", 'tip': "OUT"}]
    assert add_tranzaction("12/3/2019", "-123.3", "IN", []) == False
    assert add_tranzaction("26/12/2022", "-1740", "IN", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == False
    assert add_tranzaction("26/12/2022", "1740", "OUT", [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]

def test_update_tranzaction():
    assert update_tranzaction("12/3/2019", "123", "IN", 0, [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == [{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]
    assert update_tranzaction("12/3/2019", "123.12", "OUT", 0, [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == [{'data': "12/3/2019",'suma': "123.12", 'tip': "OUT"}]
    assert update_tranzaction("12/3/2019", "-123.3", "IN", 0, [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == False
    assert update_tranzaction("29/2/2022", "1740", "IN", 0, [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == False
    assert update_tranzaction("26/12/2022", "1740", "OUT", 0, [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == [{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]

test_add_tranzaction()
test_update_tranzaction()