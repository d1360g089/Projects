


def is_valid(s: str) -> bool:
    # Check length of the plate
    if len(s) < 2 or len(s) > 6:
        return False
    
    # Check the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # Initialize a flag for checking numbers
    number_started = False

    for i, char in enumerate(s):
        if char.isdigit():
            if not number_started:
                # Numbers cannot start with '0'
                if char == '0':
                    return False
                number_started = True
            else:
                continue  # Once numbers start, they can continue
        elif char.isalpha():
            if number_started:
                # Numbers cannot be followed by letters
                return False
        else:
            # No punctuation marks allowed
            return False

    return True

def main():
    plate = input("Enter a vanity plate: ").strip().upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()

