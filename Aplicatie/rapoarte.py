from Intrastructura import *

def suma_tranzactiilor_de_un_anumit_tip(tip, tranzactii: list) -> {int, bool}:
    # returneaza suma tranzactiilor de tipul "tip"
    if tip.upper() == "IN" or tip.upper() == "OUT":
        suma = 0
        dimensiune = len(tranzactii)
        for pozitie in range(dimensiune):
            if tranzactii[pozitie]["tip"] == tip.upper():
                suma += float(tranzactii[pozitie]["suma"])
        return suma
    else:
        return False

def soldul_contului_la_o_data_specificata(data, tranzactii: list) -> {bool, list}:
    if corectitudine_data.data_valida(data):
        tranzactii = sortare_lista_crescator.sortare_crescatoare_lista(tranzactii)
        sold = 0
        data = get_data.get_data_with_default_format(data)
        for poz in range(len(tranzactii)):
            if data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(tranzactii[poz]["data"], data) or tranzactii[poz]["data"] == data:
                if tranzactii[poz]["tip"] == "IN":
                    sold += float(tranzactii[poz]["suma"])
                else:
                    sold -= float(tranzactii[poz]["suma"])
            else:
                break
        return sold
    return False

def tranzactiile_IN_or_OUT_ordonate_dupa_suma(tip, tranzactii: list) -> {bool, list}:
    if tip.upper() == "IN" or tip.upper() == "OUT":
        new_list_of_tranzaction = []
        for elem in tranzactii:
            if elem["tip"] == tip.upper():
                new_list_of_tranzaction.append(elem)
        new_list_of_tranzaction = sortare_lista_crescator.sortare_crescatoare_lista(new_list_of_tranzaction)
        return new_list_of_tranzaction
    else:
        return False
def test_suma_tranzactiilor_de_un_anumit_tip():
    epsilon = 0.0000001
    assert abs(suma_tranzactiilor_de_un_anumit_tip("IN", [{'data':"23/10/2023", 'suma':"1740.32", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"OUT"}]) - 2640.32) < epsilon
    assert abs(suma_tranzactiilor_de_un_anumit_tip("OUT", [{'data':"15/5/2020", 'suma':"50.64", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"240.53", 'tip':"OUT"}]) -240.53) < epsilon
    assert abs(suma_tranzactiilor_de_un_anumit_tip("IN", [{'data':"23/10/2023", 'suma':"43.3222", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"950.23", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"OUT"}]) - 993.5522) < epsilon
    assert abs(suma_tranzactiilor_de_un_anumit_tip("OUT", [{'data':"23/10/2023", 'suma':"1740", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"324", 'tip':"IN"}]) - 0) < epsilon
    assert suma_tranzactiilor_de_un_anumit_tip("INn", [{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"200", 'tip':"OUT"}]) == False

test_suma_tranzactiilor_de_un_anumit_tip()

def test_sold_cont_pana_intr_o_data():
    epsilon = 0.0000001
    assert abs(soldul_contului_la_o_data_specificata("14/3/2023", [{'data':"14/5/2022", 'suma':"323.92", 'tip':"IN"}, {'data':"23/4/2023", 'suma':"700", 'tip':"IN"}, {'data':"28/2/2022", 'suma':"200", 'tip':"IN"} ]) - 523.92) < epsilon
    assert abs(soldul_contului_la_o_data_specificata("21/7/2022", [{'data':"20/7/2022", 'suma':"323.92", 'tip':"OUT"}, {'data':"19/4/2021", 'suma':"700", 'tip':"IN"}, {'data':"28/2/2022", 'suma':"800", 'tip':"OUT"} ]) + 423.92) < epsilon
    assert abs(soldul_contului_la_o_data_specificata("14/3/2023", [{'data':"15/3/2023", 'suma':"323.92", 'tip':"IN"}, {'data':"19/8/2023", 'suma':"700", 'tip':"IN"}, {'data':"28/10/2023", 'suma':"200", 'tip':"IN"} ]) - 0) < epsilon
    assert soldul_contului_la_o_data_specificata("29/2/2022",[{'data':"20/7/2022", 'suma':"323.92", 'tip':"OUT"}, {'data':"19/4/2021", 'suma':"700", 'tip':"IN"}, {'data':"28/2/2022", 'suma':"800", 'tip':"OUT"}]) == False

test_sold_cont_pana_intr_o_data()
