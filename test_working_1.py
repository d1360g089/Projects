import pytest
from working_1 import convert, convert_to_military

def main():
    test_convert()
    test_errors()


def test_convert():
    assert convert("9:00 AM TO 5:00 PM") == "09:00 to 17:00"
    assert convert("6:00 AM TO 6:00 PM") == "06:00 to 18:00"



def test_convert_to_military():
    assert convert_to_military("12", "00", "AM") == "00:00"
    assert convert_to_military("01", "00", "PM") == "13:00"

def test_errors():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("9 to 5")




if __name__ == "main":
    main()

