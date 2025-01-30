import pytest
import num
from num import validate

def main():
    test_validate()


def test_validate():
    assert validate("255.0.1.40") == True
    assert validate("256.3.4.56") == False
    assert validate("cat") == False
    assert validate("") == False
    assert validate("256.700.700.2500") == False

if __name__ == "__main__":
    main()





