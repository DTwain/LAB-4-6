def verify_data_is_in_range(data_left, data_test, data_right) -> bool: 
    # verifica daca data este in perioada data
    data_left = data_left.split("/")
    data_right = data_right.split("/") # 12/2/2020 -> ["12", "2", "2020"]
    data_test = data_test.split("/")
    data_left = [int(data_left[0]), int(data_left[1]), int(data_left[2])]
    data_right = [int(data_right[0]), int(data_right[1]), int(data_right[2])]
    data_test = [int(data_test[0]), int(data_test[1]), int(data_test[2])]
    #   data_left[0] = ziua, 
    #   data_left[1] = luna, 
    #   data_left[2] = anul, 
    if data_left[2] < data_test[2] and data_test[2] < data_right[2]: 
        return True
    elif data_left[2] == data_test[2] and data_test[2] < data_right[2]:
        if data_left[1] < data_test[1]:
            return True
        elif data_left[1] == data_test[1]:
            if data_left[0] <= data_test[0]:
                return True
    elif data_left[2] < data_test[2] and data_test[2] == data_right[2]:
        if data_test[1] < data_right[1]:
            return True
        elif data_test[1] == data_right[1]:
            if data_test[0] <= data_right[0]:
                return True
    elif data_left[2] == data_test[2] and data_test[2] == data_right[2]:
        if data_left[1] < data_test[1] and data_test[1] < data_right[1]:
            return True
        elif data_left[1] == data_test[1] and data_test[1] < data_right[1]:
            if data_left[0] <= data_test[0]:
                return True
        elif data_left[1] < data_test[1] and data_test[1] == data_right[1]:
            if data_test[0] <= data_right[0]:
                return True
        elif data_left[1] == data_test[1] and data_test[1] == data_right[1]:
            if data_left[0] <= data_test[0] and data_test[0] <= data_right[0]:
                return True
    return False  
def test_cu_assert_data_apartine_interval():
    assert verify_data_is_in_range("13/3/2022", "13/3/2021", "1/1/2023") == False
    assert verify_data_is_in_range("13/3/2022", "29/3/2022", "31/12/2022") == True
    assert verify_data_is_in_range("17/9/2021", "18/8/2021", "30/9/2021") == False
    assert verify_data_is_in_range("1/2/2019", "18/8/2022", "21/11/2023") == True

test_cu_assert_data_apartine_interval()



def verificare_data_1_mai_mica_decat_data_2(data_1: str, data_2: str) -> bool:
    """
    preconditii: data_1, data_2 - string-uri de forma dd/mm/yyyy
    postconditii: True daca data_1 < data_2, False altfel
    """
    data_1 = data_1.split("/")
    data_2 = data_2.split("/")
    data_1 = [int(data_1[0]), int(data_1[1]), int(data_1[2])]
    data_2 = [int(data_2[0]), int(data_2[1]), int(data_2[2])]
    #   data_1[0] = ziua,
    #   data_1[1] = luna,
    #   data_1[2] = anul,
    if data_1[2] < data_2[2]:
        return True
    elif data_1[2] == data_2[2]:
        if data_1[1] < data_2[1]:
            return True
        elif data_1[1] == data_2[1]:
            if data_1[0] < data_2[0]:
                return True
    return False
    
def test_verificare_daca_o_data_mai_mica_decat_alta_data():
    assert verificare_data_1_mai_mica_decat_data_2("12/3/2020", "12/3/2021") == True
    assert verificare_data_1_mai_mica_decat_data_2("12/3/2020", "12/3/2020") == False
    assert verificare_data_1_mai_mica_decat_data_2("24/11/2022", "23/11/2022") == False
    assert verificare_data_1_mai_mica_decat_data_2("24/11/2022", "24/12/2022") == True

test_verificare_daca_o_data_mai_mica_decat_alta_data()
