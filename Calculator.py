a=float(input("Enter 1st number:"))
b=float(input("Enter 2st number:"))
def Calculator(a,b):
    print("Choose Operators")
    print("1 for addition")
    print("2 for subtraction")
    print("3 for multiplication")
    print("4 for division")
    choice=int(input("Enter choice 1 (or) 2 (or) 3 (or) 4 ->"))
    if(choice==1):
        return a+b
    elif(choice==2):
        return a-b
    elif(choice==3):
        return a*b
    elif(choice==4):
        if(b!=0):
            return a/b
        else:
            return "DivisionByZeroError"       
    else:
        return "Invalid choice"
print(Calculator(a,b))