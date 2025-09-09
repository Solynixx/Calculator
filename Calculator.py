while True :
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
            option = float(input("Enter Choice : "))
            return option
        except  ValueError :
            print("invalid input must be whole number or decimal !!")
        except ZeroDivisionError :
            print("cannot be divided by 0")
    
    def get_number():
            x = float(input("Enter first number  : "))
            y = float(input("Enter second number : "))
        
    def add(x,y):
        result = x + y
        op = "+"
        return result
    
    def subtract(x,y):
        result = x - y
        op = "-"
        return result
    
    def Multiply(x,y):
        result = x * y
        op = "x"
        return result

    def Divide(x,y):
        result = x / y
        op = "÷"
        return result
    
    def calculator(x,y,option):
        if option == 5 :
            print("Thanks for using my Calculator !")
            break
        elif option <= 4 :
            if option == 1 :
                return add(x,y)
            elif option == 2 :
                return subtract(x,y)
            elif option == 3 :
                return Multiply(x,y)
            elif option == 4 :
                return Divide(x,y)
        else :
            print("Your choice is invalid !!") 
            print("Please print valid number !! ") 
            print()
            print("-"*25)
    
    def calculator():
        