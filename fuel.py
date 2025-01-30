from fractions import Fraction 

while True:
    try: 
        fraction = Fraction(input("Fraction: "))
        if fraction == 4/4:
            print("F")
        if fraction in [0/4, 0/1, 0]:
            print("E")
        if fraction < 1:
            percentage = float(fraction) * 100
            print(f"{percentage}%")
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except NameError:
        pass
