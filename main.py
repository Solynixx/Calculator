"""
Main Calculator Program
------------------------
This file serves as the entry point for running the calculator 
defined in `calculator.py`.

Available Features:
1. Basic operations (Addition, Subtraction, Multiplication, Division)
2. View calculation history
3. Clear history
4. Save history to a file
5. Auto-save history when exiting the program
"""

from calculator import Calculator
from datetime import datetime

# Main program loop, keeps running until the user chooses to exit
while True:
    # Display the calculator menu
    Calculator.menu()
    # Get user input for menu option 
    option = Calculator.prompt()

    # Exit option
    if  option == 8 :
        Calculator.auto_save_on_exit()
        print("Thanks for using my Calculator !")
        break

    # Show history
    elif option == 5 :
        Calculator.show_history()
        continue

    # Clear history
    elif option == 6 :
        Calculator.clear_history()
        print()
        continue

    # Save history to file
    elif option == 7 :
        Calculator.save_history()
        print("Your history has been saved")
        print()
        continue

    # Invalid input (not a number)
    elif option is None :
        continue

    # Invalid numeric option (not between 1 and 8)
    elif option < 1 or option > 7 :
        print("Invalid Choice! Please enter a number between 1 and 8. ") 
        print()
        continue

    # Create a Calculator object for performing operations
    number = Calculator()
    x, y = number.get_number()

    # Perform the chosen operation
    result,op = number.calculator(option)

    # If result is None (e.g., division by zero), skip and continue loop
    if result is None :
        continue

    # Format and display result
    output = Calculator.format_result(x,y,result,op)
    print(f"{output}\n")

    # Save the result into history with timestamp
    specific_date = datetime.now().strftime("[%Y-%m-%d] [%I:%M %p]")
    Calculator.history.append((specific_date, output))