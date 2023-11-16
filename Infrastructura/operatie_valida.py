def operatie_de_forma_A_B(operatie):
    #operatia: A.B cu A si B numere naturale
    for i in range(len(operatie)):
        if not (operatie[i] >= '0' and operatie[i] <= '9' or operatie[i] == '.'):
            raise ValueError("Operatia nu este valida")