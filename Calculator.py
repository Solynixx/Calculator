def menu():
    print("-"*25)
    print("CALCULATOR")
    print("-"*25)
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-"*25)  

def prompt():
    try :
        choice = int(input("Enter Choice : "))
        return choice
    except  ValueError :
        print("Invalid choice! Please enter a number between 1 and 5.")
        print()
        return None

def get_number():
    x = float(input("Enter first number  : "))
    y = float(input("Enter second number : "))
    return x, y
            
def add(x,y):
    result = x + y
    op = "+"
    return result , op

def subtract(x,y):
    result = x - y
    op = "-"
    return result , op

def multiply(x,y):
    result = x * y
    op = "x"
    return result , op

def divide(x,y):
    try:
        result = x / y
    except ZeroDivisionError :
        print("cannot be divided by 0")
        print()
        return None, None
    op = "÷"
    return result, op
        
def calculator(x,y,choice):
    if 1 <= choice <= 4 :
        if choice == 1 :
            return add(x,y)
        elif choice == 2 :
            return subtract(x,y)
        elif choice == 3 :
            return multiply(x,y)
        elif choice == 4 :
            return divide(x,y)
    else :
        return None, None

def print_result(x, y, result, op):
    if op == "÷":
        if x.is_integer() and y.is_integer():
            print(f"{x:.0f} {op} {y:.0f} = {result:.2f}")
        elif x.is_integer() and not y.is_integer():
            print(f"{x:.0f} {op} {y:.2f} = {result:.2f}")
        elif y.is_integer() and not x.is_integer():
            print(f"{x:.2f} {op} {y:.0f} = {result:.2f}")
        else:
            print(f"{x:.2f} {op} {y:.2f} = {result:.2f}")
    else:
        if x.is_integer() and y.is_integer():
            print(f"{x:.0f} {op} {y:.0f} = {result:.0f}")
        elif x.is_integer() and not y.is_integer():
            print(f"{x:.0f} {op} {y:.2f} = {result:.2f}")
        elif y.is_integer() and not x.is_integer():
            print(f"{x:.2f} {op} {y:.0f} = {result:.2f}")
        else:
            print(f"{x:.2f} {op} {y:.2f} = {result:.2f}")
    print()

while True :
    menu()
    option =  prompt()
    if  option == 5 :
        print("Thanks for using my Calculator !")
        break
    elif option is None :
        continue
    elif option < 1 or option > 5 :
        print("Your choice is invalid !!") 
        print("Please print valid number !! ") 
        print()
        continue    
    x, y = get_number()
    result,op = calculator(x,y,option)
    if result is None :
        continue
    print_result(x,y,result,op)
