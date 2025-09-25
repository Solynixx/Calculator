from datetime import datetime
class Calculator:
    """
    A simple Calculator class that supports basic arithmetic operations
    and tracks calculation history.

    Features:
    - Add, Subtract, Multiply, Divide
    - Show, Clear, Save history
    - Auto-save history on exit
    """
    history = []

    def __init__(self):
        """
        Initialize Calculator object with default values (x=0, y=0).
        """
        self.x = 0
        self.y = 0

    @staticmethod
    def menu():
        """
        Display the calculator menu options to the user.
        """
        print("-"*25)
        print("CALCULATOR")
        print("-"*25)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show history")
        print("6. Clear history")
        print("7. Save history")
        print("8. Exit")
        print("-"*25)  

    @staticmethod
    def prompt():
        """
        Prompt the user to enter a menu choice.

        Returns:
            int or None: user's choice (1-8), or None if invalid input.
        """
        try :
            choice = int(input("Enter Choice : "))
            return choice
        except  ValueError :
            print("Your choice is invalid !! ")
            print("Please input in numbers !!")
            print()
            return None

    def get_number(self):
        """
        Ask the user to input two numbers.

        Returns:
            tuple: (x, y) as floats
        """
        while True :
            try : 
                self.x = float(input("Enter first number  : "))
                break
            except ValueError :
                print("Invalid! Please input number only")
                print()
                continue
        while True :
            try : 
                self.y = float(input("Enter second number : "))
                break
            except ValueError :
                print("Invalid! Please input number only")
                print()
                continue
        return self.x, self.y
    
    def add(self):
        """
        Add two numbers.

        Returns:
            tuple: (result, '+')
        """
        result = self.x + self.y 
        op = "+"
        return result, op 
                
    def subtract(self):
        """
        Subtract y from x.

        Returns:
            tuple: (result, '-')
        """
        result = self.x - self.y
        op = "-"
        return result , op

    def multiply(self):
        """
        Multiply two numbers.

        Returns:
            tuple: (result, 'x')
        """
        result = self.x * self.y
        op = "x"
        return result , op

    def divide(self):
        """
        Divide x by y with zero division handling.

        Returns:
            tuple: (result, '÷') or (None, None) if division by zero
        """
        try:
            result = self.x / self.y
        except ZeroDivisionError :
            print("cannot be divided by 0")
            print()
            return None, None
        op = "÷"
        return result, op
    
    @staticmethod
    def show_history():
        """
        Display the list of previous calculations with timestamps.
        """
        if  len(Calculator.history) == 0 :
            print("No have history yet")
            print()
        else :
            for number, (specific_date, output) in enumerate(Calculator.history, start= 1) :
                print(f"{specific_date} {number}. {output}")
            print()

    @staticmethod
    def clear_history():
        """
        Clear all saved calculation history.
        """
        Calculator.history.clear()
        print("History cleared !")

    @staticmethod
    def auto_save_on_exit():
        """
        Automatically save history to a file if history exists.
        Called when the program exits.
        """
        if len(Calculator.history) > 0 :
            Calculator.save_history()
            print("History auto-saved")

    @staticmethod
    def save_history(filename = "save_history_calculator.txt"):
        """
        Save history to a text file.

        Args:
            filename (str): The name of the file where history is saved.
        """
        with open(filename,"w",encoding="utf-8") as file :
            for number, (specific_date, output) in enumerate (Calculator.history, start = 1 ):
                file.write(f"{specific_date} {number}. {output}"+"\n")

    def calculator(self,choice):
        """
        Perform calculation based on user's menu choice.

        Args:
            choice (int): menu option (1-4)

        Returns:
            tuple: (result, operator) or (None, None) if invalid choice
        """
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

    def format_result(x, y, result, op):
        """
        Format the calculation result with proper decimal precision.

        Args:
            x (float): first number
            y (float): second number
            result (float): calculation result
            op (str): operator symbol

        Returns:
            str: formatted result string
        """
        if op == "÷":
            if x.is_integer() and y.is_integer():
                return f"{x:.0f} {op} {y:.0f} = {result:.2f}"
            elif x.is_integer() and not y.is_integer():
                return f"{x:.0f} {op} {y:.2f} = {result:.2f}"
            elif y.is_integer() and not x.is_integer():
                return f"{x:.2f} {op} {y:.0f} = {result:.2f}"
            else:
                return f"{x:.2f} {op} {y:.2f} = {result:.2f}"
        else:
            if x.is_integer() and y.is_integer():
                return f"{x:.0f} {op} {y:.0f} = {result:.0f}"
            elif x.is_integer() and not y.is_integer():
                return f"{x:.0f} {op} {y:.2f} = {result:.2f}"
            elif y.is_integer() and not x.is_integer():
                return f"{x:.2f} {op} {y:.0f} = {result:.2f}"
            else:
                return f"{x:.2f} {op} {y:.2f} = {result:.2f}"
