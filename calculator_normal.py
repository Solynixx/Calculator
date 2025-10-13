from datetime import datetime
import math
class Calculator:
    """
    A basic calculator class that supports fundamental arithmetic operations
    (addition, subtraction, multiplication, and division).
    It also handles user input, formatting, and validation.
    """

    """Initialize the Calculator instance."""
    def __init__(self):
        pass

    # ===============================
    # 📋 DISPLAY MENU
    # ===============================
    """
    Display the calculator's main operation menu for the user.
    """
    @staticmethod
    def menu_normal():
        
        print("="*25)
        print("CALCULATOR")
        print("-"*25)
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back")
        print("-"*25)  

    # ===============================
    # ➕ BASIC OPERATIONS
    # ===============================
    def add(self,*numbers):
        """
        Perform addition on all provided numbers.
        Args:
            *numbers (float): A list of numbers to add.
        Returns:
            tuple: (result, operator)
        """
        result = sum(numbers) 
        op = " + "
        return result, op 
                
        """
        Perform subtraction on all provided numbers.
        The operation is performed sequentially from left to right.
        """
    def subtract(self,*numbers):
        result = numbers[0]
        for num in numbers[1:] :
            result -= num
        op = " - "
        return result , op
    
        """
        Perform multiplication on all provided numbers.
        The operation is performed sequentially from left to right.
        """
    def multiply(self,*numbers):
        result = numbers[0]
        for num in numbers [1:]:
            result *= num
        op = " x "
        return result , op

        """
        Perform division on all provided numbers.
        Handles division by zero with exception control.
        """
    def divide(self,*numbers):
        try:
            result = numbers[0]
            for num in numbers [1:] :
                result /= num
        except ZeroDivisionError :
            print("cannot be divided by 0")
            print()
            return None, None
        op = " ÷ "
        return result, op

    # ===============================
    # 🧭 USER PROMPT HANDLING
    # ===============================
    """
        Ask the user to choose an operation from the calculator menu.

        Returns:
            int: The user's menu choice (1-5).
    """
    @staticmethod
    def normal_prompt():
        while True:
            try :
                choice = int(input("Enter Number (1-5) = "))
                if 1 <= choice <= 5:
                    return choice
                else :
                    print("Please enter a number between 1 and 5")
            except ValueError:
                print("Please input a number!")
                print()
   
    
    # ===============================
    # 🔢 USER NUMBER INPUT
    # ===============================
    """
        Collect numerical input from the user for performing operations.
        Supports multiple values separated by spaces.
    """
    def get_number_normal(self):
        while True:
            try :
                nums = input("Input numbers (you can use spaces) : ").split()
                if not nums :
                    print("Please input at least one number.")
                    continue
                numbers = []
                for num in nums :
                    numbers.append(float(num))
                return numbers  
            except ValueError:
                print("Please input a number!")
                print()
        
    
    # ===============================
    # ⚙️ CALCULATION HANDLER
    # ===============================
    """
        Execute the chosen arithmetic operation based on user input.

        Args:
            choice (int): The operation selected from the menu.
            numbers (list): The list of numbers to operate on.

        Returns:
            tuple: (result, operator) if valid, otherwise (None, None).
    """
    def calculator_normal(self,choice, numbers):
        while True :
            if 1 <= choice <= 4 and numbers is not None :
                if choice == 1 :
                    return self.add(*numbers)
                elif choice == 2 :
                    return self.subtract(*numbers)
                elif choice == 3 :
                    return self.multiply(*numbers)
                elif choice == 4 :
                    result, op = self.divide(*numbers)
                    if result is None :
                        print("Please re-enter valid numbers (cannot divide by 0).")
                        continue
                    return result,op
            else :
                return None, None

    # ===============================
    # 🧾 RESULT FORMATTING
    # ===============================
    """
        Format the calculation output with a timestamp for display or saving.

        Args:
            numbers (list): The list of numbers used in the operation.
            result (float): The result of the operation.
            op (str): The operation symbol used.
            order (int, optional): Optional index/order for history display.

        Returns:
            str: A formatted string showing the timestamp, operation, and result.
    """
    def format_result(self, numbers,result, op, order=None):
        specific_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        format_result_operation = op.join(map(str, numbers))
        if order is not None:
            return f"|{specific_date}| {order}. {format_result_operation} = {result}\n"
        else:
            return f"|{specific_date}| {format_result_operation} = {result}\n"
