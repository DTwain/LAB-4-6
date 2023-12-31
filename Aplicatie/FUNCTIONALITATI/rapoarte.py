from Infrastructura import *
from Aplicatie.GETTER_SETTER_validari.getter_setter_creaza_tranz import get_data, get_suma, get_tip, set_tranzactii
from Aplicatie.GETTER_SETTER_validari.validari import validare_suma, validare_data, validare_tip  
def suma_tranzactiilor_de_un_anumit_tip(tip, tranzactii: list) -> float:
    # returneaza suma tranzactiilor de tipul "tip"
    validare_tip(tip)  
    suma = 0
    for tranzactie in tranzactii:
        if get_tip(tranzactie) == tip.upper():
            suma += float(get_suma(tranzactie))
    return suma

def soldul_contului_la_o_data_specificata(data, tranzactii: list) -> float:
    validare_data(data)
    sortare.sortare_crescatoare_lista(tranzactii)
    sold = 0
    data = data_default.get_data_with_default_format(data)
    for tranzactie in tranzactii:
        if data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(get_data(tranzactie), data) or get_data(tranzactie) == data:
            if get_tip(tranzactie) == "IN":
                sold += float(get_suma(tranzactie))
            else:
                sold -= float(get_suma(tranzactie))
    return sold

def tranzactiile_IN_or_OUT_ordonate_dupa_suma(tip, tranzactii: list) -> list:
    validare_tip(tip)
    new_list_of_tranzaction = []
    for tranzactie in tranzactii:
        if get_tip(tranzactie) == tip.upper():
            set_tranzactii(new_list_of_tranzaction, tranzactie)
    sortare.sortare_crescatoare_lista(new_list_of_tranzaction)
    return new_list_of_tranzaction
    
def test_suma_tranzactiilor_de_un_anumit_tip():
    epsilon = 0.0000001
    assert abs(suma_tranzactiilor_de_un_anumit_tip("IN", [{'data':"23/10/2023", 'suma':"1740.32", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"OUT"}]) - 2640.32) < epsilon
    assert abs(suma_tranzactiilor_de_un_anumit_tip("OUT", [{'data':"15/5/2020", 'suma':"50.64", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"240.53", 'tip':"OUT"}]) -240.53) < epsilon
    assert abs(suma_tranzactiilor_de_un_anumit_tip("IN", [{'data':"23/10/2023", 'suma':"43.3222", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"950.23", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"OUT"}]) - 993.5522) < epsilon
    assert abs(suma_tranzactiilor_de_un_anumit_tip("OUT", [{'data':"23/10/2023", 'suma':"1740", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"324", 'tip':"IN"}]) - 0) < epsilon
    try:
        assert suma_tranzactiilor_de_un_anumit_tip("INn", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"200", 'tip':"OUT"}])
        assert False
    except:
        assert True
    
def test_sold_cont_pana_intr_o_data():
    epsilon = 0.0000001
    assert abs(soldul_contului_la_o_data_specificata("14/3/2023", [{'data':"14/5/2022", 'suma':"323.92", 'tip':"IN"}, {'data':"23/4/2023", 'suma':"700", 'tip':"IN"}, {'data':"28/2/2022", 'suma':"200", 'tip':"IN"} ]) - 523.92) < epsilon
    assert abs(soldul_contului_la_o_data_specificata("21/7/2022", [{'data':"20/7/2022", 'suma':"323.92", 'tip':"OUT"}, {'data':"19/4/2021", 'suma':"700", 'tip':"IN"}, {'data':"28/2/2022", 'suma':"800", 'tip':"OUT"} ]) + 423.92) < epsilon
    assert abs(soldul_contului_la_o_data_specificata("14/3/2023", [{'data':"15/3/2023", 'suma':"323.92", 'tip':"IN"}, {'data':"19/8/2023", 'suma':"700", 'tip':"IN"}, {'data':"28/10/2023", 'suma':"200", 'tip':"IN"} ]) - 0) < epsilon
    try:
        soldul_contului_la_o_data_specificata("29/2/2022",[{'data':"20/7/2022", 'suma':"323.92", 'tip':"OUT"}, {'data':"19/4/2021", 'suma':"700", 'tip':"IN"}, {'data':"28/2/2022", 'suma':"800", 'tip':"OUT"}])
        assert False
    except:
        assert True

test_suma_tranzactiilor_de_un_anumit_tip()
test_sold_cont_pana_intr_o_data()
