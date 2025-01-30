

def main():
    plate = input("Plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s: str) -> bool:
    if 2 <= len(s) <= 6:
        return True
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    if not s.isalnum():
        return False
    

    num_started = False
    for i,char in enumerate(s):
        if char.isdigit():
            if not num_started:
                if char == 0:
                    return False
                num_started = True
            else:
                continue 

        elif char.isalpha():
            if num_started:
                return False
        else:
            return False
            
    return True





if __name__ == "__main__":
    main()