import re

name = input("Name: ")

matches = re.search(r"^.+, .+$", name)


