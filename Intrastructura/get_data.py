import re # regular expression
def get_data_with_default_format(data): # data = "12:12.2000" -> "12/12/2000"
    zi_luna_an = re.split(r'[:./]', data)
    data = zi_luna_an[0] + "/" + zi_luna_an[1] + "/" + zi_luna_an[2] 
    return data

def test_get_data_with_default_format():
    assert get_data_with_default_format("12:12:2000") == "12/12/2000"
    assert get_data_with_default_format("31:4.2020") == "31/4/2020"
    assert get_data_with_default_format("29:2/2020") == "29/2/2020"
    assert get_data_with_default_format("29.6:2019") == "29/6/2019"
    assert get_data_with_default_format("31.13.2019") == "31/13/2019"
    assert get_data_with_default_format("32.12/2007") == "32/12/2007"
    assert get_data_with_default_format("29/2:2000") == "29/2/2000"
    assert get_data_with_default_format("29/2.1400") == "29/2/1400"
    assert get_data_with_default_format("29/2/1400") == "29/2/1400"

test_get_data_with_default_format()