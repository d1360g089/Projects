import pytest
from um import count


def main():
    test_count()


def test_count():
    assert count("Hello, um, thanks, um, very much") == 2
    assert count("Hello world") == 0
    assert count("That was yummy!") == 0
    assert count("UM, Thanks, uM") == 2
    





if __name__ == "__main__":
    main()


