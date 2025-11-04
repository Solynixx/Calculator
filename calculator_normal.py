from datetime import datetime
class Calculator:

    def __init__(self):
        pass

    # ===============================
    # 📋 DISPLAY MENU
    # ===============================

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

        result = sum(numbers) 
        op = " + "
        return result, op 

    def subtract(self,*numbers):
        result = numbers[0]
        for num in numbers[1:] :
            result -= num
        op = " - "
        return result , op
    

    def multiply(self,*numbers):
        result = numbers[0]
        for num in numbers [1:]:
            result *= num
        op = " x "
        return result , op

    def divide(self, *numbers):
        try:
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
            op = " ÷ "
            return result, op
        except ZeroDivisionError:
            print("cannot be divided by 0")
            print()
            return None, None
        

    # ===============================
    # 🧭 USER PROMPT HANDLING
    # ===============================

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

    def calculator_normal(self, choice, numbers):
        if 1 <= choice <= 4 and numbers is not None:
            if choice == 1:
                return self.add(*numbers)
            elif choice == 2:
                return self.subtract(*numbers)
            elif choice == 3:
                return self.multiply(*numbers)
            elif choice == 4:
                return self.divide(*numbers)
        else:
            return None, None

    # ===============================
    # 🧾 RESULT FORMATTING
    # =============================== 
    def format_result(self, numbers,result, op, order=None):

        specific_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if result is None:
            return ""

        # Convert all numbers: show integers without decimals, 
        # and round floats to 2 digits if needed
        formatted_number = []
        for format in numbers :
            if format.is_integer():
                formatted_number.append(str(int(format))) # Convert to int and then string
            else :
                formatted_number.append(f"{format:.2f}") # Round float to 2 decimal places
                
        # Format the result the same way
        if result.is_integer():
            result_display = str(int(result))
        else :
            result_display = f"{result:.2f}"
        
        # Join all formatted numbers with the operation symbol (e.g., "3 + 2")
        format_result_operation = op.join(formatted_number)

        # Return formatted string with optional order number
        if order is not None:
            return f"|{specific_date}| {order}. {format_result_operation} = {result_display}\n"
        else:
            return f"|{specific_date}| {format_result_operation} = {result_display}\n"