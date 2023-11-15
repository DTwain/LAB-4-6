from Infrastructura.corectitudine_suma import suma_valida_tranzactie, suma_valida
from Infrastructura.corectitudine_data import data_valida
from Infrastructura.data_apartine_perioada import verificare_data_1_mai_mica_decat_data_2
def validare_suma_tranzactie(suma):
    if not suma_valida_tranzactie(suma):  
        raise ValueError("Suma invalida!")

def validare_data(data):
    if not data_valida(data):
        raise ValueError("Data invalida!")
    
def validare_tip(tip):
    if not (tip.upper() == "IN" or tip.upper() == "OUT"):
        raise ValueError("Tip invalid!")

def validare_suma(suma):
    if not suma_valida(suma):
        raise ValueError("Suma invalida!")
    
def validare_data_start_mai_mica_decat_data_end(data_start, data_end):
    if not (verificare_data_1_mai_mica_decat_data_2(data_start, data_end) or data_start == data_end ):
        raise ValueError("data_start > data_end!")

def validare_lungime_lista(tranzactii_precedente: list):
    if len(tranzactii_precedente) == 0: 
        raise ValueError("NU SE POATE DA UNDO!!")
    
def test_validare_suma_tranzactie():
    try:
        validare_suma_tranzactie("100")
        assert True
    except:
        assert False

    try:
        validare_suma_tranzactie("100.2")
        assert True
    except:
        assert False

    try:
        validare_suma_tranzactie("100.02")
        assert True
    except:
        assert False

    try:
        validare_suma_tranzactie("0.01")
        assert True
    except:
        assert False

    try:
        validare_suma_tranzactie("-100")
        assert False
    except:
        assert True
    
    try:
        validare_suma_tranzactie("100d")
        assert False
    except:
        assert True

    try:
        validare_suma_tranzactie("0.0")
        assert False
    except:
        assert True

def test_validare_data():
    try:
        validare_data("12/3/2019")
        assert True
    except:
        assert False

    try:
        validare_data("29/2/2020")
        assert True
    except:
        assert False

    try:
        validare_data("29/2/2021")
        assert False
    except:
        assert True

    try:
        validare_data("12/13/2019")
        assert False
    except:
        assert True

    try:
        validare_data("12/3/2019d")
        assert False
    except:
        assert True

    try:
        validare_data("12/3/2019/")
        assert False
    except:
        assert True
    
    try:
        validare_data("12/3/2019/12")
        assert False
    except:
        assert True

def test_validare_tip():
    try:
        validare_tip("IN")
        assert True
    except:
        assert False

    try:
        validare_tip("OUT")
        assert True
    except:
        assert False

    try:
        validare_tip("in")
        assert False
    except:
        assert True

    try:
        validare_tip("out")
        assert False
    except:
        assert True

    try:
        validare_tip("INOUT")
        assert False
    except:
        assert True

    try:
        validare_tip("INOUT")
        assert False
    except:
        assert True

def test_validare_suma_cautare():
    try:
        validare_suma("100")
        assert True
    except:
        assert False

    try:
        validare_suma("100.2")
        assert True
    except:
        assert False

    try:
        validare_suma("100.02")
        assert True
    except:
        assert False

    try:
        validare_suma("0.01")
        assert True
    except:
        assert False

    try:
        validare_suma("-100")
        assert True
    except:
        assert False
    
    try:
        validare_suma("100d")
        assert False
    except:
        assert True

    try:
        validare_suma("0.0")
        assert True
    except:
        assert False

    try:
        validare_suma("suma")
        assert False
    except:
        assert True

def test_validare_data_start_mai_mica_decat_data_end():
    try:
        validare_data_start_mai_mica_decat_data_end("12/3/2019", "12/3/2019")
        assert True
    except:
        assert False

    try:
        validare_data_start_mai_mica_decat_data_end("11/3/2019", "12/3/2019")
        assert True
    except:
        assert False

    try:
        validare_data_start_mai_mica_decat_data_end("12/3/2019", "12/3/2020")
        assert True
    except:
        assert False

    try:
        validare_data_start_mai_mica_decat_data_end("12/3/2019", "12/3/2018")
        assert False
    except:
        assert True

    try:
        validare_data_start_mai_mica_decat_data_end("12/3/2019", "12/1/2019")
        assert False
    except:
        assert True

    try:
        validare_data_start_mai_mica_decat_data_end("1/1/2019", "29/12/2014")
        assert False
    except:
        assert True

def test_validare_lungime_lista():
    try:
        validare_lungime_lista([])
        assert False
    except:
        assert True

    try:
        validare_lungime_lista([1,2,3])
        assert True
    except:
        assert False
    
    try:
        validare_lungime_lista([1])
        assert True
    except:
        assert False

def run_teste():
    test_validare_suma_tranzactie()
    test_validare_data()
    test_validare_tip()
    test_validare_suma_cautare()
    test_validare_data_start_mai_mica_decat_data_end()
    test_validare_lungime_lista()

run_teste()
    
