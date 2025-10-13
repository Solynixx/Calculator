from datetime import datetime

import math
class calculator_scientific:
    def __init__(self):
        super().__init__(self)

    @staticmethod
    def menu_scientific():
        print("-"*25)
        print("CALCULATOR")
        print("-"*25)
        print("1. Unary")
        print("2. Binary")
        print("3. Back")
        print("-"*25)

    @staticmethod
    def menu_scientific_unary():
        print("-"*25)
        print("CALCULATOR")
        print("-"*25)
        print("1. Square (x²)")
        print("2. Square root (√x)")
        print("3. Factorial (n!)")
        print("4. sin(x)")
        print("5. log₁₀(x)")
        print("6. Show history")
        print("7. Clear history")
        print("8. Save history")
        print("9. Back ")
        print("-"*25)

    @staticmethod
    def prompt_scientific_unary():
        try :
            choice_scientific_unary = int(input("Enter Choice : "))
            return choice_scientific_unary
        except ValueError :
            print("Your choice is invalid !! ")
            print("Please input in numbers !!")
            print()
            return None
    
    def get_number_scientific_unary(self):
        while True:
            try :
                self.x = float(input("Enter number : "))
                break
            except ValueError:
                print("Invalid! Please input number only")
                print()
                continue
        return self.x
    
    def square(self):
        result = (self.x**2)
        return result