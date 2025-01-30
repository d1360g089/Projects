

amount = 50 
 
while True:
    print("Amount due: ", amount)
    insert = int(input("Insert coin: "))

    if insert not in [25, 10, 5]:
        print(insert)
    
    else: 
        amount = amount - insert 
        print("Amount due: ", amount)

    if amount == 0:
        print("Change owed: 0")
        break



     

    

    

