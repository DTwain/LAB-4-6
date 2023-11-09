from Infrastructura import data_default
from Aplicatie.getter_setter_creaza_tranz import creaza_tranzactie, set_tranzactii, get_data, get_suma, get_tip
def tranzactii_prelucrate(tranzactii : list) -> list:
    tranzactii_prelucrate = []
    for tranzactie in tranzactii:
        tranzactie_noua = creaza_tranzactie(data_default.get_data_with_default_format(get_data(tranzactie)), get_suma(tranzactie), get_tip(tranzactie))
        tranzactii_prelucrate = set_tranzactii(tranzactii_prelucrate, tranzactie_noua)
    return tranzactii_prelucrate

def tranzactie_anterioara_in_functie_de_ultima_operatie(tranzactii_anterioare : list, operatie_anterioara: float):
    if tranzactii_anterioare == []:
        return []
    if operatie_anterioara in [1.1, 1.2, 2.1, 2.2, 2.3, 5.1, 5.2] and len(tranzactii_anterioare) >= 2:
        return tranzactii_anterioare[-2]
    return tranzactii_anterioare[-1]

def tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata(tranzactii_anterioare: list, operatie_anterioara: float):
    if tranzactii_anterioare == []:
        return []
    if operatie_anterioara in [1.1, 1.2, 2.1, 2.2, 2.3, 5.1, 5.2] and len(tranzactii_anterioare) >= 2:
        return tranzactii_anterioare[0:-2]
    return tranzactii_anterioare[0:-1]

def test_tranzactii_prelucrate():
    assert tranzactii_prelucrate([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]
    assert tranzactii_prelucrate([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    assert tranzactii_prelucrate([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "12/3/2019",'suma': "123", 'tip': "IN"}]

def test_tranzactie_anterioara_in_functie_de_ultima_operatie():
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([], 1.1) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 1.1) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 1.2) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 2.1) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 2.2) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 2.3) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 5.1) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 5.2) == []
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}], 1.1) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]
    assert tranzactie_anterioara_in_functie_de_ultima_operatie([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}], 1.2) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]

def test_tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata():
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([], 1.1) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 1.1) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 1.2) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 2.1) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 2.2) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 2.3) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 5.1) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], 5.2) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}], 1.1) == []
    assert tranzactii_anterioare_in_functie_de_ultima_operatie_efectuata([{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}, {'data': "14/4/2022",'suma': "2000", 'tip': "OUT"}], 1.2) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]