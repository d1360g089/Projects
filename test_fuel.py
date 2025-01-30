import fuel_1
import pytest
from fuel_1 import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert(0/4) == 0
    assert convert(4/4) == 100
    assert convert(1/2) == 50
    assert convert(3/4) == 75
    assert convert(1/4) == 25

def test_errors():
    with pytest.raises(ZeroDivisionError):
        convert(1/0)
    with pytest.raises(ValueError):
        convert("5/a")
    with pytest.raises(ValueError):
        convert("cat")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    







if __name__ == "__main__":
    main()




