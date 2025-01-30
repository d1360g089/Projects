import re
import validators

def main():
    print(validate(input("Email: ")))


def validate(email):
    if validators.email(email):
        return f"{email} is valid"
    else:
        return f"{email} is not valid"
    
if __name__ == "__main__":
    main()


    