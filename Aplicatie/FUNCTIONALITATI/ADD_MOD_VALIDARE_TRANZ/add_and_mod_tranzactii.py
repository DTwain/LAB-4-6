from Infrastructura import *
from Aplicatie.GETTER_SETTER_validari.getter_setter_creaza_tranz import set_tranzactii_de_index, set_tranzactii, creaza_tranzactie, get_data, get_suma, get_tip
from Aplicatie.FUNCTIONALITATI.ADD_MOD_VALIDARE_TRANZ.validare_tranzactie import tranzactie_valida, tranzactie_valida_si_indice_tranzactie_valid

def add_tranzaction(data, suma, tip, tranzactii: list):
    tranzactie_noua = creaza_tranzactie(data, suma, tip)
    tranzactie_valida(tranzactie_noua)
    set_tranzactii(tranzactii, tranzactie_noua) # adauga tranzactia noua in lista de tranzactii

def update_tranzaction(data, suma, tip, nr_tranzactie, tranzactii : list ):
    tranzactie_noua = creaza_tranzactie(data, suma, tip)
    tranzactie_valida_si_indice_tranzactie_valid(tranzactie_noua, nr_tranzactie, len(tranzactii))
    set_tranzactii_de_index(tranzactii, nr_tranzactie, tranzactie_noua)

def test_add_tranzaction():
    tranzactii = []
    add_tranzaction("12/3/2019", "400", "IN", tranzactii)
    assert len(tranzactii) == 1
    assert get_data(tranzactii[0]) == "12/3/2019"
    assert get_suma(tranzactii[0]) == "400"
    assert get_tip(tranzactii[0]) == "IN"

    add_tranzaction("21/2/2022", "323.42", "OUT", tranzactii)
    assert len(tranzactii) == 2
    assert get_data(tranzactii[1]) == "21/2/2022"
    assert get_suma(tranzactii[1]) == "323.42"
    assert get_tip(tranzactii[1]) == "OUT"

    try:
        add_tranzaction("29/2/2022", "100", "IN", tranzactii)
        assert False
    except ValueError:
        assert True

    try:
        add_tranzaction("28/2/2022", "-100", "IN", tranzactii)
        assert False
    except ValueError:
        assert True

def test_update_tranzaction():
    tranzactii = []
    add_tranzaction("12/3/2019", "400", "IN", tranzactii)
    add_tranzaction("21/2/2022", "323.42", "OUT", tranzactii)
    update_tranzaction("12/3/2019", "400", "IN", 0, tranzactii)
    assert len(tranzactii) == 2
    assert get_data(tranzactii[0]) == "12/3/2019"
    assert get_suma(tranzactii[0]) == "400"
    assert get_tip(tranzactii[0]) == "IN"

    update_tranzaction("21/2/2022", "323.42", "OUT", 1, tranzactii)
    assert len(tranzactii) == 2
    assert get_data(tranzactii[1]) == "21/2/2022"
    assert get_suma(tranzactii[1]) == "323.42"
    assert get_tip(tranzactii[1]) == "OUT"

    try:
        update_tranzaction("29/2/2022", "100", "IN", 0, tranzactii)
        assert False
    except ValueError:
        assert True

    try:
        update_tranzaction("28/2/2022", "-100", "IN", 0, tranzactii)
        assert False
    except ValueError:
        assert True

    try:
        update_tranzaction("28/2/2022", "-100", "IN", -1, tranzactii)
        assert False
    except ValueError:
        assert True

    try:
        update_tranzaction("28/2/2022", "-100", "IN", 2, tranzactii)
        assert False
    except ValueError:
        assert True

test_add_tranzaction()
test_update_tranzaction()
