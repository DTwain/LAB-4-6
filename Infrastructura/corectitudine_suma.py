def suma_valida_tranzactie(suma):
    """
    functie care verifica daca suma introdusa este valida
    preconditii: suma - float nenul
    postconditii: -
    """
    contor = 0
    for i in range(len(suma)):
        if suma[i] != '.':
            if suma[i] < '0' or suma[i] > '9':
                return False
        else:
            contor += 1
    if contor > 1:
        return False
    if float(suma) <= 0:
        return False
    return True

def suma_valida(suma):
    """
    functie care verifica daca suma introdusa este valida
    preconditii: suma - float 
    postconditii: -
    """
    contor_minus = 0
    contor_punct = 0
    for i in range(len(suma)):
        if suma[i] != '.' and suma[i] != '-':
            if suma[i] < '0' or suma[i] > '9':
                return False
        elif suma[i] == '-':
            contor_minus += 1
            if i != 0:
                return False
        else:
            contor_punct += 1
    if contor_minus > 1 or contor_punct > 1:
        return False
    return True

def test_suma_valida_tranzactie():
    assert suma_valida_tranzactie("100")
    assert suma_valida_tranzactie("100.00")
    assert not suma_valida_tranzactie("0")
    assert not suma_valida_tranzactie("-100")
    assert not suma_valida_tranzactie("100.0.0")
    assert not suma_valida_tranzactie("100.0a")
    assert not suma_valida_tranzactie("100.0-")
    assert suma_valida_tranzactie(".012")

def test_suma_valida():
    assert suma_valida("100")
    assert suma_valida("100.00")
    assert suma_valida("0")
    assert not suma_valida("--100")
    assert not suma_valida("100.0.0")
    assert not suma_valida("-100.0a")
    assert not suma_valida("100.0-")
    assert suma_valida(".012")

test_suma_valida_tranzactie()
test_suma_valida()
