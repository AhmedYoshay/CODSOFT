#Simple Arithmetic Calculator

def Calculator():
    print("Select The Operation You Want To Perform: \n1) ADDITION ( + )\n2) SUBTRACTION ( - )\n3) MULTIPLICATION ( * )\n4) DIVISION ( / ) ")

    choice = input("Enter The Symbol For Your Choice: ")

    if choice=='+':
        print("Enter two numbers")

        x=float(input("Enter 1st Number: "))

        y=float(input("Enter 2nd Number: "))

        print(x," + ",y," = ",x+y) 

    elif choice=='-':
        print("Enter two numbers")

        x=float(input("Enter 1st Number: "))

        y=float(input("Enter 2nd Number: "))

        print(x," - ",y," = ",x-y) 

    elif choice=='*':
        print("Enter two numbers")

        x=float(input("Enter 1st Number: "))

        y=float(input("Enter 2nd Number: "))

        print(x," x ",y," = ",x*y) 

    elif choice=='/':
        print("Enter two numbers")

        x=float(input("Enter 1st Number: "))

        y=float(input("Enter 2nd Number: "))

        if y==0:
            print("Divisor can not be zero! Enter the number again:")
            y=float(input("Enter 2nd Number: "))
        print(x," / ",y," = ",x/y)   
    else:
        print("Invalid Choice!")
        
Calculator()
     


    