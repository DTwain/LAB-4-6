import re # pentru split , expresii regulate

def data_valida(data):
    """
    functie care verifica daca data introdusa este valida
    preconditii: zi - natural nenul 
                 luna - natural 1<=luna<=12
                 an - natural
    postconditii: -
    """
    '''
    r'[/:.]' reprezintă expresia regulată care descrie delimitatorii folosiți pentru 
    împărțire: '/', ':', și '.'. Aceste caractere sunt plasate într-o 
    clasă de caractere, astfel încât oricare dintre ei să poată fi un delimitator.
    '''
    for i in range(len(data)):
        if data[i] != '/' and data[i] != ':' and data[i] != '.':
            if data[i] < '0' or data[i] > '9':
                return False
        # am verificat daca data este de forma dd/mm/yyyy
        # vreau sa nu am alte caractere in afara de delimitatori si cifre
    
    zi_luna_an = re.split(r'[:./]', data) 
    zi_luna_an = [int(x) for x in zi_luna_an]

    if len(zi_luna_an) != 3:
        return False # daca nu am 3 elemente in lista inseamna ca nu am introdus data corect
    
    zi = zi_luna_an[0]
    luna = zi_luna_an[1]
    an = zi_luna_an[2]

    if luna <= 0 or luna > 12:
        return False
    if an <= 0:
        return False
    if zi <= 0 or zi > 31:
        return False
    
    #verific daca anul este bisect
    bisect = False
    if an % 4 == 0:
        bisect = True
    else:
        bisect = False
    if an % 100 == 0:
        bisect = False
    if an % 400 == 0:
        bisect = True
    if luna == 1 or luna == 3 or luna == 5 or luna == 7 or luna == 8 or luna == 10 or luna == 12:
        if zi > 31:
            return False
    if luna == 4 or luna == 6 or luna == 9 or luna == 11:
        if zi > 30:
            return False
    if luna == 2 and bisect == False:
        if zi > 28:
            return False
    if luna == 2 and bisect == True:
        if zi > 29:
            return False
    return True
        
def test_data_valida():
    assert data_valida("12/12/2000") == True
    assert data_valida("31/4/2020") == False
    assert data_valida("29/2/2020") == True
    assert data_valida("29/2/2019") == False
    assert data_valida("31/13/2019") == False
    assert data_valida("32/12/2007") == False
    assert data_valida("29/2/2000") == True
    assert data_valida("29/2/1900") == False

test_data_valida()