from Infrastructura import *
from Aplicatie.getter_setter_creaza_tranz import *
from Aplicatie.add_and_mod_tranzactii import add_tranzaction

def stergere_tranzactii_dupa_data(data, tranzactii: list):
    if corectitudine_data.data_valida(data):
        data = data_default.get_data_with_default_format(data) # data este de forma dd/mm/yyyy
        for tranzactie in tranzactii[:]: # [:] - copie a listei https://gist.github.com/alexlouden/9f1ab4354d1c68ae4c1c94126ac51a20
            if get_data(tranzactie) == data:
                tranzactii.remove(tranzactie)
        return
    raise ValueError("Data invalida")

def stergere_tranzactii_dupa_perioada(data_start, data_end, tranzactii: list):
    if corectitudine_data.data_valida(data_start) and corectitudine_data.data_valida(data_end):
        data_start = data_default.get_data_with_default_format(data_start)
        data_end = data_default.get_data_with_default_format(data_end)
        if not data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(data_start, data_end) and not data_start == data_end:
            raise ValueError("data_start > data_end")
        else:
            for tranzactie in tranzactii[:]:
                if data_apartine_perioada.verify_data_is_in_range(data_start, get_data(tranzactie), data_end):
                    tranzactii.remove(tranzactie)
            return
    raise ValueError("Data invalida")
    

def stergere_tranzactii_dupa_tip(tip: str, tranzactii: list):
    if tip.upper() == "IN" or tip.upper() == "OUT":
        for tranzactie in tranzactii[:]:
            if get_tip(tranzactie) == tip.upper():
                tranzactii.remove(tranzactie)
        return 
    raise ValueError("TIPUL este invalid")

def test_stergere_tranzactii_dupa_data():
    tranzactii = []
    add_tranzaction("12/2/2002", "3000", "IN", tranzactii)
    add_tranzaction("18/6/2015", "1700", "OUT", tranzactii)
    add_tranzaction("12/2/2022", "1000", "OUT", tranzactii)
    add_tranzaction("12/2/2022", "250", "OUT", tranzactii)

    stergere_tranzactii_dupa_data("12/2/2022",tranzactii)
    assert len(tranzactii) == 2
    assert get_data(tranzactii[0]) == "12/2/2002"
    assert get_suma(tranzactii[0]) == "3000"
    assert get_tip(tranzactii[0]) == "IN"

    assert get_data(tranzactii[1]) == "18/6/2015"
    assert get_suma(tranzactii[1]) == "1700"
    assert get_tip(tranzactii[1]) == "OUT"

    try: 
        stergere_tranzactii_dupa_data("31/6/2020", tranzactii)
        assert False
    except:
        assert True
    
    stergere_tranzactii_dupa_data("18/6/2015",tranzactii)
    assert len(tranzactii) == 1
    assert get_data(tranzactii[0]) == "12/2/2002"
    assert get_suma(tranzactii[0]) == "3000"
    assert get_tip(tranzactii[0]) == "IN"

    stergere_tranzactii_dupa_data("12/2/2002",tranzactii)
    assert len(tranzactii) == 0

    
def test_stergere_tranzactii_dupa_perioada():
    tranzactii = []
    add_tranzaction("15/3/2022", "300", "IN", tranzactii)
    add_tranzaction("20/3/2022", "100", "OUT", tranzactii)
    add_tranzaction("30/3/2022", "500", "IN", tranzactii)
    add_tranzaction("12/4/2022", "200", "OUT", tranzactii)

    stergere_tranzactii_dupa_perioada("14/3/2022", "1/4/2022", tranzactii)
    assert len(tranzactii) == 1
    assert get_data(tranzactii[0]) == "12/4/2022"
    assert get_suma(tranzactii[0]) == "200"
    assert get_tip(tranzactii[0]) == "OUT"

    try:
        stergere_tranzactii_dupa_perioada("1/4/2022", "31/3/2022", tranzactii)
        assert False
    except:
        assert True

    stergere_tranzactii_dupa_perioada("1/4/2022", "31/4/2022", tranzactii)
    assert len(tranzactii) == 0

def test_stergere_tranzactii_dupa_tip():
    tranzactii = []
    add_tranzaction("15/3/2022", "300", "IN", tranzactii)
    add_tranzaction("20/3/2022", "100", "OUT", tranzactii)
    add_tranzaction("30/3/2022", "500", "IN", tranzactii)
    add_tranzaction("12/4/2022", "200", "OUT", tranzactii)

    stergere_tranzactii_dupa_tip("Out", tranzactii)
    assert len(tranzactii) == 2
    assert get_data(tranzactii[1]) == "30/3/2022"
    assert get_suma(tranzactii[1]) == "500"
    assert get_tip(tranzactii[1]) == "IN"

    stergere_tranzactii_dupa_tip("Out", tranzactii)
    assert len(tranzactii) == 2

    try: 
        stergere_tranzactii_dupa_tip("Tipp", tranzactii)
        assert False
    except:
        assert True

    stergere_tranzactii_dupa_tip("iN", tranzactii)
    assert len(tranzactii) == 0

