from Infrastructura.corectitudine_data import data_valida
from Infrastructura.corectitudine_suma import suma_valida_tranzactie
from Aplicatie.GETTER_SETTER_validari.getter_setter_creaza_tranz import get_data, get_suma, get_tip
def tranzactie_valida(tranzactie: dict):
    data = get_data(tranzactie)
    if not data_valida(data):
        raise ValueError("Data invalida!")
    suma = get_suma(tranzactie)
    if not suma_valida_tranzactie(suma):
        raise ValueError("Suma invalida!")
    tip = get_tip(tranzactie)
    if tip != "IN" and tip != "OUT":
        raise ValueError("Tip invalid!")

def tranzactie_valida_si_indice_tranzactie_valid(tranzactie: dict, nr_tranzactie, nr_tranzactii_totale):
    data = get_data(tranzactie)
    if not data_valida(data):
        raise ValueError("Data invalida!")
    suma = get_suma(tranzactie)
    if not suma_valida_tranzactie(suma):
        raise ValueError("Suma invalida!")
    tip = get_tip(tranzactie)
    if tip != "IN" and tip != "OUT":
        raise ValueError("Tip invalid!")
    if nr_tranzactie < 0 or nr_tranzactie >= nr_tranzactii_totale:
        raise ValueError("Numarul tranzactiei invalid!") 

def test_tranzactie_valida():
    tranzactie_valida({"data": "12/12/2012", "suma": "100", "tip": "IN"})
    tranzactie_valida({"data": "12/12/2012", "suma": "100", "tip": "OUT"})
    tranzactie_valida({"data": "11/1/2020", "suma": "400", "tip": "IN"})
    try:
        tranzactie_valida({"data": "22/13/2012", "suma": "100", "tip": "OUT"})
        assert False
    except ValueError:
        assert True
    
    try:
        tranzactie_valida({"data": "29/2/2022", "suma": "100.a", "tip": "IN"})
        assert False
    except ValueError:
        assert True

    try:
        tranzactie_valida({"data": "29/2/2022", "suma": "a", "tip": "OUT"})
        assert False
    except ValueError:
        assert True

test_tranzactie_valida()

def test_tranzactie_valida_si_indice_tranzactie_valid():
    tranzactie_valida_si_indice_tranzactie_valid({"data": "12/12/2012", "suma": "100", "tip": "IN"}, 0, 1)
    tranzactie_valida_si_indice_tranzactie_valid({"data": "12/12/2012", "suma": "100", "tip": "OUT"}, 0, 1)
    tranzactie_valida_si_indice_tranzactie_valid({"data": "11/1/2020", "suma": "400", "tip": "IN"}, 0, 1)
    try:
        tranzactie_valida_si_indice_tranzactie_valid({"data": "22/13/2012", "suma": "100", "tip": "OUT"}, 0, 1)
        assert False
    except ValueError:
        assert True
    
    try:
        tranzactie_valida_si_indice_tranzactie_valid({"data": "29/2/2022", "suma": "100.a", "tip": "IN"}, 0, 1)
        assert False
    except ValueError:
        assert True

    try:
        tranzactie_valida_si_indice_tranzactie_valid({"data": "29/2/2022", "suma": "a", "tip": "OUT"}, 0, 1)
        assert False
    except ValueError:
        assert True

    try:
        tranzactie_valida_si_indice_tranzactie_valid({"data": "29/2/2022", "suma": "100", "tip": "OUT"}, -1, 1)
        assert False
    except ValueError:
        assert True

test_tranzactie_valida_si_indice_tranzactie_valid()

    