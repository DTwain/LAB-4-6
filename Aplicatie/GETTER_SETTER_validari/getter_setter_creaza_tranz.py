from Infrastructura.data_default import get_data_with_default_format
def get_data(tranzactie: dict) -> str:
    """
        preconditii:
            functia primeste o lista de disctionare si doreste sa returneze elementul din lista
            de pe pozitia tranzactii[index_tranzactie]["data"]
        postconditii:
            returneaza tranzactii[index_tranzactie]["data"]
    """
    return tranzactie["data"]

def get_suma(tranzactie: dict) -> str:
    """
        preconditii:
            functia primeste o lista de disctionare si doreste sa returneze elementul din lista
            de pe pozitia tranzactii[index_tranzactie]["suma"]
        postconditii:
            returneaza tranzactii[index_tranzactie]["suma"]
    """
    return tranzactie["suma"]

def get_tip(tranzactie: dict) -> str:
    """
        preconditii:
            functia primeste o lista de disctionare si doreste sa returneze elementul din lista
            de pe pozitia tranzactii[index_tranzactie]["tip"]
        postconditii:
            returneaza tranzactii[index_tranzactie]["tip"]
    """
    return tranzactie["tip"]

def set_tranzactii_de_index(tranzactii: list , index_tranzactie: int, tranzactie_noua: dict):
    """
        preconditii:
            functia primeste o lista de disctionare si doreste sa modifice elementul din lista
            de pe pozitia tranzactii[index_tranzactie] cu tranzactie_noua
        postconditii:
            modifica lista de tranzactii prin adaugarea unei noi tranzactii pe pozitia 
            index_tranzactie.
    """
    tranzactii[index_tranzactie] = tranzactie_noua

def set_tranzactii(tranzactii: list, tranzactie_noua: dict):
    """
        preconditii:
            functia primeste o lista de disctionare si doreste sa modifice elementul din lista
            de pe pozitia tranzactii[index_tranzactie] cu tranzactie_noua
        postconditii:
            modifica lista de tranzactii prin adaugarea unei noi tranzactii la final
    """
    tranzactii.append(tranzactie_noua)

def creaza_tranzactie(data, suma, tip):
    """
        preconditii:
            functia primeste data, suma si tipul unei tranzactii
        postconditii:
            returneaza o tranzactie de forma {'data': data, 'suma': suma, 'tip': tip}
    """
    return {'data': get_data_with_default_format(data) , 'suma': suma, 'tip': tip.upper()}

def test_get_data():
    assert get_data({'data': "12/3/2019",'suma': "123", 'tip': "OUT"}) == "12/3/2019"
    assert get_data({'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}) == "26/12/2022"
    assert get_data({'data': "29/2/2022",'suma': "1740", 'tip': "IN"}) == "29/2/2022"
    assert get_data({'data': "14/4/2022",'suma': "2000", 'tip': "OUT"}) == "14/4/2022"
    assert get_data({'data': "1/6/2017",'suma': "200", 'tip': "IN"}) == "1/6/2017"

def test_get_suma():
    assert get_suma({'data': "12/3/2019",'suma': "123", 'tip': "OUT"}) == "123"
    assert get_suma({'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}) == "1740"
    assert get_suma({'data': "29/2/2022",'suma': "1740", 'tip': "IN"}) == "1740"
    assert get_suma({'data': "14/4/2022",'suma': "2000", 'tip': "OUT"}) == "2000"
    assert get_suma({'data': "1/6/2017",'suma': "200", 'tip': "IN"}) == "200"

def test_get_tip():
    assert get_tip({'data': "12/3/2019",'suma': "123", 'tip': "OUT"}) == "OUT"
    assert get_tip({'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}) == "OUT"
    assert get_tip({'data': "29/2/2022",'suma': "1740", 'tip': "IN"}) == "IN"
    assert get_tip({'data': "14/4/2022",'suma': "2000", 'tip': "OUT"}) == "OUT"
    assert get_tip({'data': "1/6/2017",'suma': "200", 'tip': "IN"}) == "IN"

def test_set_tranzactii_de_index():
    tranzactii = [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]
    set_tranzactii_de_index(tranzactii, 0, {'data': "12/3/2019",'suma': "123", 'tip': "IN"})
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]

    tranzactii = [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    set_tranzactii_de_index(tranzactii, 1, {'data': "12/3/2019",'suma': "123", 'tip': "IN"})
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]
    
    tranzactii = [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}, {'data': "14/4/2022",'suma': "2000", 'tip': "OUT"}]
    set_tranzactii_de_index(tranzactii, 2, {'data': "12/3/2019",'suma': "123", 'tip': "IN"})
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}, {'data': "12/3/2019",'suma': "123", 'tip': "IN"}]

def test_set_tranzactii():
    tranzactii = []
    set_tranzactii(tranzactii, {'data': "12/3/2019",'suma': "123", 'tip': "OUT"})
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]

    tranzactii = [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]
    set_tranzactii(tranzactii, {'data': "12/3/2019",'suma': "123", 'tip': "IN"})
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]
    
    tranzactii = [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    set_tranzactii(tranzactii, {'data': "12/3/2019",'suma': "123", 'tip': "IN"})
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}, {'data': "12/3/2019",'suma': "123", 'tip': "IN"}]

def run_teste():
    test_get_data()
    test_get_suma()
    test_get_tip()
    test_set_tranzactii_de_index()
    test_set_tranzactii()

run_teste()