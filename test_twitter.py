import pytest 
import twitter
from twitter import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("cat") == "ct"
    assert shorten("twitter") == "twttr"
    assert shorten("Harvard") == "Hrvrd"






if __name__ == "__main__":
    main()