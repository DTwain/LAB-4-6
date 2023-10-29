from Intrastructura import *
def filtrare_tranzactii_dupa_tip(tip: str, tranzactii: list) -> {bool, list}:
    # returneaza o lista cu tranzactiile care nu au tip == "tip"
    if tip.upper() == "IN" or tip.upper() == "OUT":
        tranzactii_cu_tipul_dorit = []
        dimensiune = len(tranzactii)
        for pozitie in range(dimensiune):
            if not tranzactii[pozitie]["tip"] == tip.upper():
                tranzactii_cu_tipul_dorit.append(tranzactii[pozitie])
        return tranzactii_cu_tipul_dorit
    else:
        return False

def filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat(suma, tip, tranzactii: list) -> {bool, list}:
    #5.2 Elimină toate tranzacțiile mai mici decât o sumă dată care au tipul specificat
    if corectitudine_suma.suma_valida(suma):
        if tip.upper() == "IN" or tip.upper() == "OUT":
            new_list_of_tranzaction = []
            for tranzactie in tranzactii:
                if not (float(tranzactie["suma"]) < float(suma) and tranzactie["tip"] == tip.upper()):
                    new_list_of_tranzaction.append(tranzactie)
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

def test_filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat():
    assert filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat("500.24", "iN", [{'data':"12/3/2019", 'suma':"400", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}, {'data':"14/7/2022", 'suma':"100", 'tip':"IN"}]) == [{'data':"21/2/2022", 'suma':"323.42", 'tip':"OUT"}] 
    assert filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat("140.69", "OuT",[{'data':"8/10/2003", 'suma':"650", 'tip':"OUT"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"89.10", 'tip':"OUT"}]) == [{'data':"8/10/2003", 'suma':"650", 'tip':"OUT"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"OUT"}]
    assert filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat("2000","IN",[{'data':"23/10/2023", 'suma':"1900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"21/10/2023", 'suma':"200", 'tip':"IN"}]) == []
    assert filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat("2300.3c", "iN", [{'data':"8/10/2003", 'suma':"650", 'tip':"OUT"}, {'data':"23/9/2004", 'suma':"400.50", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"89.10", 'tip':"OUT"}]) == False
    assert filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat("3000.35", "Outt",[{'data':"29/2/2000", 'suma':"1400", 'tip':"IN"}, {'data':"13/5/2007", 'suma':"1200", 'tip':"OUT"}, {'data':"30/4/2000", 'suma':"700", 'tip':"IN"}]) == False

test_filtrare_tranzactii_cu_suma_mai_mica_decat_x_si_cu_tipul_specificat()

