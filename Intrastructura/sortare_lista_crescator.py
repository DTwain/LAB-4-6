from Intrastructura import data_apartine_perioada
def sortare_crescatoare_lista(tranzactii: list) -> list:
    for i in range(len(tranzactii)-1):
        for j in range(i+1, len(tranzactii)):
            if not data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(tranzactii[i]['data'],tranzactii[j]['data']):
                aux = tranzactii[i]
                tranzactii[i] = tranzactii[j]
                tranzactii[j] = aux
    return  tranzactii
            