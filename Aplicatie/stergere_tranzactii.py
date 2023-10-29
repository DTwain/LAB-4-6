from Intrastructura import *
def filtrare_tranzactii_dupa_data(data, tranzactii: list) -> {bool, list}:
    # returneaza o lista cu tranzactiile care nu au data == "data"
    new_list_of_tranzactions = []
    if corectitudine_data.data_valida(data):
        data = get_data.get_data_with_default_format(data) # data este de forma dd/mm/yyyy
        for pozitie in range(len(tranzactii)):
            if not tranzactii[pozitie]['data'] == data:
                new_list_of_tranzactions.append(tranzactii[pozitie])
        return new_list_of_tranzactions
    else:
        return False

def filtrare_tranzactii_dupa_perioada(data_start, data_end, tranzactii: list) -> {bool, list}:
    # returneaza o lista cu tranzactiile care nu au data in intervalul [data_start, data_end]
    if corectitudine_data.data_valida(data_start) and corectitudine_data.data_valida(data_end):
        data_start = get_data.get_data_with_default_format(data_start)
        data_end = get_data.get_data_with_default_format(data_end)
        if not data_apartine_perioada.verify_data_is_in_range(data_start, data_start, data_end) :
            return False
        else:
            dimensiune = len(tranzactii)
            tranzactii_inafara_perioadei = []
            for poz in range(dimensiune):
                if not data_apartine_perioada.verify_data_is_in_range(data_start, tranzactii[poz]["data"], data_end):
                    tranzactii_inafara_perioadei.append(tranzactii[poz])
            return tranzactii_inafara_perioadei
    else:
        return False
    

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


def test_delete_tranzaction():
    rez = filtrare_tranzactii_dupa_data("21/2/2022", [{'data': "12/3/2019", 'suma':"123", 'tip':"IN"}, {'data': "21/2/2022", 'suma':"323", 'tip':"OUT"}, {'data': "21/2/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"12/3/2019", 'suma':"123", 'tip':"IN"}]

    rez = filtrare_tranzactii_dupa_data("1/6/2017", [{'data':"12/3/2019", 'suma':"1000", 'tip':"IN"}, {'data':"1/6/2017", 'suma':"200", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"12/3/2019", 'suma':"1000", 'tip':"IN"}, {'data':"21/2/2022", 'suma':"100", 'tip':"IN"}]

    rez = filtrare_tranzactii_dupa_data("23/10/2023",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == []
    
    rez = filtrare_tranzactii_dupa_data("32/3/2020",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == False

test_delete_tranzaction()

def test_filtrare_tranzactii_dupa_perioada():
    rez = filtrare_tranzactii_dupa_perioada("12/3/2019", "1/9/2019", [{'data':"11/3/2019", 'suma':"200", 'tip':"IN"}, {'data':"27/7/2019", 'suma':"323", 'tip':"OUT"}, {'data':"12/9/2019", 'suma':"100", 'tip':"IN"}])
    assert rez == [{'data':"11/3/2019", 'suma':"200", 'tip':"IN"}, {'data':"12/9/2019", 'suma':"100", 'tip':"IN"}]

    rez = filtrare_tranzactii_dupa_perioada("1/6/2017", "21/2/2022", [{'data':"12/3/2019", 'suma':"1000", 'tip':"IN"}, {'data':"1/6/2017", 'suma':"200", 'tip':"OUT"}, {'data':"21/2/2022", 'suma':"100", 'tip':"IN"}])
    assert rez == []

    rez = filtrare_tranzactii_dupa_perioada("23/10/2023", "23/10/2023",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == []

    rez = filtrare_tranzactii_dupa_perioada("23/10/2023", "23/10/2022",[{'data':"23/10/2023", 'suma':"1740", 'tip':"OUT"}, {'data':"23/10/2023", 'suma':"900", 'tip':"IN"}, {'data':"23/10/2023", 'suma':"200", 'tip':"IN"}])
    assert rez == False

test_filtrare_tranzactii_dupa_perioada()

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