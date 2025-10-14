import math
from datetime import datetime

class CalculatorScientific:
    """
    Scientific Calculator class for advanced mathematical operations
    such as sin, cos, tan, sqrt, pow, log, log10, and factorial.
    """

    def __init__(self):
        pass

    # ===============================
    # 📋 DISPLAY MENU
    # ===============================
    @staticmethod
    def menu_scientific():
        print("=" * 35)
        print("SCIENTIFIC CALCULATOR")
        print("-" * 35)
        print("1. sin(x)")
        print("2. cos(x)")
        print("3. tan(x)")
        print("4. sqrt(x)")
        print("5. pow(x, y)")
        print("6. log(x)")
        print("7. log10(x)")
        print("8. factorial(x)")
        print("9. Back")
        print("-" * 35)

    # ===============================
    # 🧭 USER PROMPT HANDLING
    # ===============================
    @staticmethod
    def scientific_prompt():
        while True:
            try:
                choice = int(input("Enter Number (1-9) = "))
                if 1 <= choice <= 9:
                    return choice
                else:
                    print("Please enter a number between 1 and 9")
            except ValueError:
                print("Please input a number!")
                print()

    # ===============================
    # 🔢 USER NUMBER INPUT
    # ===============================
    def get_number_scientific(self, choice):
        """
        Ask user for number(s) depending on the selected operation.
        """
        while True:
            try:
                if choice == 5:  # pow(x, y)
                    nums = input("Input two numbers (x y): ").split()
                    if len(nums) != 2:
                        print("Please input exactly 2 numbers.")
                        continue
                    return [float(nums[0]), float(nums[1])]

                else:
                    num = float(input("Input a number: "))
                    return [num]

            except ValueError:
                print("Please input a valid number!")
                print()

    # ===============================
    # ⚙️ CALCULATION HANDLER
    # ===============================
    def calculator_scientific(self, choice, *numbers):
        try:
            if choice == 1:
                return math.sin(numbers[0]), "sin"
            elif choice == 2:
                return math.cos(numbers[0]), "cos"
            elif choice == 3:
                return math.tan(numbers[0]), "tan"
            elif choice == 4:
                if numbers[0] < 0:
                    print("Cannot take square root of a negative number.")
                    return None, None
                return math.sqrt(numbers[0]), "√"
            elif choice == 5:
                return math.pow(numbers[0], numbers[1]), "^"
            elif choice == 6:
                if numbers[0] <= 0:
                    print("Logarithm domain error (x must be > 0).")
                    return None, None
                return math.log(numbers[0]), "ln"
            elif choice == 7:
                if numbers[0] <= 0:
                    print("Logarithm domain error (x must be > 0).")
                    return None, None
                return math.log10(numbers[0]), "log10"
            elif choice == 8:
                if numbers[0] < 0 or not numbers[0].is_integer():
                    print("Factorial is only defined for non-negative integers.")
                    return None, None
                return math.factorial(int(numbers[0])), "!"
            else:
                return None, None
        except Exception as e:
            print(f"Error: {e}")
            return None, None

    # ===============================
    # 🧾 RESULT FORMATTING
    # ===============================
    def format_result(self, numbers, result, op, order=None):
        """
        Format the calculation result with timestamp and operation details.
        Integers are displayed without decimal points.
        """
        specific_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if result is None:
            return ""

        # Convert input numbers (display without decimals if integer)
        formatted_number = []
        for n in numbers:
            if n.is_integer():
                formatted_number.append(str(int(n)))
            else:
                formatted_number.append(f"{n:.2f}")

        # Format result
        if isinstance(result, float) and result.is_integer():
            result_display = str(int(result))
        elif isinstance(result, float):
            result_display = f"{result:.5f}"  # more precision for scientific ops
        else:
            result_display = str(result)

        # Operation display
        if op in ["sin", "cos", "tan", "√", "ln", "log10", "!"]:
            operation_display = f"{op}({', '.join(formatted_number)})"
        elif op == "^":
            operation_display = f"{formatted_number[0]} ^ {formatted_number[1]}"
        else:
            operation_display = f"{op.join(formatted_number)}"

        # Return formatted string
        if order is not None:
            return f"|{specific_date}| {order}. {operation_display} = {result_display}\n"
        else:
            return f"|{specific_date}| {operation_display} = {result_display}\n"