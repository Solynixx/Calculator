class Calculator:
    def __init__(self):
        self.x = 0
        self.y = 0

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

    def get_number(self):
        self.x = float(input("Enter first number  : "))
        self.y = float(input("Enter second number : "))
        return self.x, self.y
    
    def add(self):
        result = self.x + self.y 
        op = "+"
        return result, op 
                
    def subtract(self):
        result = self.x - self.y
        op = "-"
        return result , op

    def multiply(self):
        result = self.x * self.y
        op = "x"
        return result , op

    def divide(self):
        try:
            result = self.x / self.y
        except ZeroDivisionError :
            print("cannot be divided by 0")
            print()
            return None, None
        op = "÷"
        return result, op
            
    def calculator(self,choice):
        if 1 <= choice <= 4 :
            if choice == 1 :
                return self.add()
            elif choice == 2 :
                return self.subtract()
            elif choice == 3 :
                return self.multiply()
            elif choice == 4 :
                return self.divide()
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
    Calculator.menu() 
    option = Calculator.prompt()
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
    number = Calculator()
    x, y = number.get_number()
    result,op = number.calculator(option)
    if result is None :
        continue
    Calculator.print_result(x,y,result,op)
