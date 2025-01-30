
def main():
    x = int(input("what is x? "))
    print("x squared is", square(x))


def square(n):
    return n * n


def even_or_odd():
    num = int(input("What is your number? "))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")


name = input("What's your name? ")

match name:
     case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
     case "Draco":
        print("Slytherin")
     case _:
        print("who? ")

 
Students = {
    "Chris":"Grade:F",
    "Smokie": "Grade D"}

print(Students["Chris"]) 

