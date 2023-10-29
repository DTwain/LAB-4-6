def suma_valida(suma):
    """
    functie care verifica daca suma introdusa este valida
    preconditii: suma - float nenul
    postconditii: -
    """
    for i in range(len(suma)):
        if suma[i] != '.':
            if suma[i] < '0' or suma[i] > '9':
                return False
    if float(suma) <= 0:
        return False
    return True

def test_suma_valida():
    assert suma_valida("123") == True 
    assert suma_valida("123.123") == True 
    assert suma_valida("890.4d") == False 
    assert suma_valida("0") == False 
    assert suma_valida("-123") == False 
    assert suma_valida("-123.123") == False 
    assert suma_valida("-424d") == False

test_suma_valida()
