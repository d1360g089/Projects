import re
import sys


def main():
    ip_address = input("IPv4 Address: ")
    print(validate(ip_address))


def validate(ip):
    ip_regex = r"\b((25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9]{1,2})\b"

    if re.search(ip_regex, ip):
        return True
    else: 
        return False
    

if __name__ == "__main__":
    main()





