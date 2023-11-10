from Infrastructura import data_apartine_perioada
from Aplicatie.getter_setter_creaza_tranz import get_data
def sortare_crescatoare_lista(tranzactii: list):
    for i in range(len(tranzactii)-1):
        for j in range(i+1, len(tranzactii)):
            if not data_apartine_perioada.verificare_data_1_mai_mica_decat_data_2(get_data(tranzactii[i]), get_data(tranzactii[j])):
                aux = tranzactii[i]
                tranzactii[i] = tranzactii[j]
                tranzactii[j] = aux
            