from Infrastructura import data_default
from Aplicatie.getter_setter_creaza_tranz import creaza_tranzactie, set_tranzactii, get_data, get_suma, get_tip
from Afis_verifica.output_verify_opp import output
def tranzactii_prelucrate(tranzactii : list) -> list:
    tranzactii_prelucrate = []
    for tranzactie in tranzactii:
        tranzactie_noua = creaza_tranzactie(data_default.get_data_with_default_format(get_data(tranzactie)), get_suma(tranzactie), get_tip(tranzactie))
        set_tranzactii(tranzactii_prelucrate, tranzactie_noua)
    return tranzactii_prelucrate

def tranzactie_anterioara(tranzactii: list, tranzactii_precedente: list):
    if len(tranzactii_precedente) == 0: 
        raise ValueError("NU SE POATE DA UNDO")
    tranzactii_precedente.pop()
    if len(tranzactii_precedente) == 0:
        tranzactii.clear()
    else:
        tranzactii.clear()
        tranzactii.extend(tranzactii_precedente[-1])
 
def test_tranzactii_prelucrate():
    tranzactii = []
    set_tranzactii(tranzactii, creaza_tranzactie("12/3/2019", "123", "OUT"))
    set_tranzactii(tranzactii, creaza_tranzactie("26/12/2022", "1740", "OUT"))
    set_tranzactii(tranzactii, creaza_tranzactie("1/8/2023", "900", "IN"))
    assert tranzactii_prelucrate(tranzactii) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "1/8/2023",'suma': "900", 'tip': "IN"}]
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "1/8/2023",'suma': "900", 'tip': "IN"}]

    tranzactii = []
    assert tranzactii_prelucrate(tranzactii) == []
    assert tranzactii == []

    tranzactii = []
    set_tranzactii(tranzactii, creaza_tranzactie("12/3/2019", "123", "OUT"))
    assert tranzactii_prelucrate(tranzactii) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]

    tranzactii = []
    set_tranzactii(tranzactii, creaza_tranzactie("12/3/2019", "123", "OUT"))
    set_tranzactii(tranzactii, creaza_tranzactie("26/12/2022", "1740", "OUT"))
    assert tranzactii_prelucrate(tranzactii) == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]


def test_tranzactii_anterioara():
    tranzactii = []
    tranzactii_precedente = []
    set_tranzactii(tranzactii, creaza_tranzactie("12/3/2019", "123", "OUT"))
    copie_tranzactii = tranzactii_prelucrate(tranzactii)
    set_tranzactii(tranzactii_precedente, copie_tranzactii )

    set_tranzactii(tranzactii, creaza_tranzactie("26/12/2022", "1740", "OUT"))
    copie_tranzactii = tranzactii_prelucrate(tranzactii)
    set_tranzactii(tranzactii_precedente, copie_tranzactii )

    set_tranzactii(tranzactii, creaza_tranzactie("1/8/2023", "900", "IN"))
    copie_tranzactii = tranzactii_prelucrate(tranzactii)
    set_tranzactii(tranzactii_precedente, copie_tranzactii )

    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "1/8/2023",'suma': "900", 'tip': "IN"}]
    assert tranzactii_precedente == [[{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}], [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"},{'data': "1/8/2023",'suma': "900", 'tip': "IN"}]]
    assert len(tranzactii) == 3
    assert len(tranzactii_precedente) == 3

    tranzactie_anterioara(tranzactii, tranzactii_precedente)
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}, {'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]
    assert tranzactii_precedente == [[{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}], [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"},{'data': "26/12/2022",'suma': "1740", 'tip': "OUT"}]]

    tranzactie_anterioara(tranzactii, tranzactii_precedente)
    assert tranzactii == [{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]
    assert tranzactii_precedente == [[{'data': "12/3/2019",'suma': "123", 'tip': "OUT"}]]

    tranzactie_anterioara(tranzactii, tranzactii_precedente)
    assert tranzactii == []
    assert tranzactii_precedente == []

    try:
        tranzactie_anterioara(tranzactii, tranzactii_precedente)
        assert False
    except ValueError:
        assert True

test_tranzactii_prelucrate()
test_tranzactii_anterioara()
    



    