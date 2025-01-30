from fractions import Fraction 

# Main is where you write the main function of the program (the main idea).
def main():
    while True:
        try: 
            fraction = Fraction(input("Fraction: "))
            percentage = convert(fraction)
            result = gauge(percentage)
            print(result)

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except NameError:
            pass

def convert(input):
    percentage = float(input) * 100
    return percentage

def gauge(percentage):
    if percentage in [0/4, 0]:
        return "E"
    if percentage > 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()



