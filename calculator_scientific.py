from datetime import datetime
import math

class CalculatorScientific:
    def __init__(self):
        pass

    # ===============================
    # 📋 DISPLAY MENU
    # ===============================
    @staticmethod
    def menu_scientific():
        print("="*30)
        print("SCIENTIFIC CALCULATOR")
        print("-"*30)
        print("1. Square Root (√x)")
        print("2. Power (x^y)")
        print("3. Logarithm (log10)")
        print("4. Sine (sin)")
        print("5. Cosine (cos)")
        print("6. Tangent (tan)")
        print("7. Factorial")
        print("8. Back")
        print("-"*30)

    # ===============================
    # 🧭 PROMPT
    # ===============================
    @staticmethod
    def scientific_prompt():
        while True:
            try:
                choice = int(input("Enter Number (1-8): "))
                if 1 <= choice <= 8:
                    return choice
                else:
                    print("Please enter a number between 1 and 8.")
            except ValueError:
                print("Please input a valid number!")

    # ===============================
    # 🔢 INPUT HANDLER
    # ===============================
    def get_number_scientific(self, choice):
        try:
            if choice in [1, 3, 4, 5, 6, 7]:  # single input
                x = float(input("Enter a number: "))
                return [x]
            elif choice == 2:  # power (x, y)
                nums = input("Enter base and exponent separated by space: ").split()
                return [float(n) for n in nums[:2]]
        except ValueError:
            print("Invalid input, please enter numbers only.")
            return None

    # ===============================
    # ⚙️ OPERATION HANDLER
    # ===============================
    def calculator_scientific(self, choice, numbers):
        try:
            if choice == 1:
                return math.sqrt(numbers[0]), "√"
            elif choice == 2:
                return math.pow(numbers[0], numbers[1]), "^"
            elif choice == 3:
                return math.log10(numbers[0]), "log"
            elif choice == 4:
                return math.sin(math.radians(numbers[0])), "sin"
            elif choice == 5:
                return math.cos(math.radians(numbers[0])), "cos"
            elif choice == 6:
                return math.tan(math.radians(numbers[0])), "tan"
            elif choice == 7:
                return math.factorial(int(numbers[0])), "!"
            else:
                return None, None
        except ValueError:
            print("Invalid mathematical operation (e.g., negative root or log).")
            return None, None

    # ===============================
    # 🧾 RESULT FORMATTING
    # ===============================
    def format_result(self, numbers, result, op, order=None):
        specific_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if result is None:
            return ""

        # Format number tampil rapi
        formatted_number = []
        for n in numbers:
            if n.is_integer():
                formatted_number.append(str(int(n)))
            else:
                formatted_number.append(f"{n:.2f}")

        if isinstance(result, (int, float)) and result.is_integer():
            result_display = str(int(result))
        else:
            result_display = f"{result:.5f}"

        # Format hasil string
        if op in ["√", "sin", "cos", "tan", "log"]:
            operation_str = f"{op}({formatted_number[0]})"
        elif op == "^":
            operation_str = f"{formatted_number[0]}^{formatted_number[1]}"
        elif op == "!":
            operation_str = f"{formatted_number[0]}!"
        else:
            operation_str = " ".join(formatted_number)

        if order is not None:
            return f"|{specific_date}| {order}. {operation_str} = {result_display}\n"
        else:
            return f"|{specific_date}| {operation_str} = {result_display}\n"