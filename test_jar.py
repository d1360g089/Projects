import pytest 
import jar
from jar import Jar 

def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(5) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(3)
    assert jar.size == 3
    with pytest.raises(ValueError, match="Exceeded capacity"):
        jar.deposit(13)
    with pytest.raises(ValueError, match="Can't deposit a negative amount"):
        jar.deposit(-4)



def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2
    with pytest.raises(ValueError, match="Can't subtract more than size"):
        jar.deposit(5)  #It is counting the size as 7 so if u put for example 6 it wont raise the valueError 
        jar.withdraw(8) #but if u put something like 8 it will because the size is 7 and 7 < 8 and u can't subtract 8 cookies from a 7 cookie jar
    with pytest.raises(ValueError, match="Not enough cookies to remove"):
        jar.withdraw(7)
        jar.deposit(0)
        jar.withdraw(1)
        





if __name__ == "__main__":
    main()
