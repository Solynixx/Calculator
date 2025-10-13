from calculator_normal import *
from calculator_scientific import *
from datetime import datetime


# ===============================
# 🧮 MAIN PROGRAM ENTRY POINT
# ===============================

while True:
    print("====== Welcome to the Calculator Program ======")
    print("Select calculator mode")
    print("1. Normal (Basic Operation)")
    print("2. Scientific (Advenced Operation)")
    print("3. Save history")
    print("4. Show history Calculator normal")
    print("5. Show history Calculator scientific")
    print("6. Clear History")
    print("7. Exit ")
    print("="*48)

    # Handle invalid menu input (non-integer)
    try :
        start_choice = int(input("Enter Number (1-7) = "))
    except ValueError:
        print("Please Enter in number")
        continue
    
    # =====================================
    # 🧾 NORMAL CALCULATOR MODE
    # =====================================
    if start_choice == 1 :
        while True :

            Calculator.menu_normal() # Display normal calculator menu

            choice_normal = Calculator.normal_prompt() # Prompt the user for an operation choice

            if choice_normal == 5 : # Option 5 allows returning to the main menu
                print("Returning to main menu...\n")
                break

            cal_normal = Calculator() # Create a new calculator instance

            num_normal = cal_normal.get_number_normal() # Collect user input for numbers

            result,op = cal_normal.calculator_normal(choice_normal,num_normal)# Perform the selected arithmetic operation

            # If an invalid operation occurred (e.g., divide by zero), skip iteration
            if result is None :
                continue

            # Format and display the calculation result
            result_normal = cal_normal.format_result(num_normal,result,op,None)
            print(result_normal)

            continue # Continue allowing user to perform more operations before returning

    elif start_choice == 2 :
        # calculator_scientific.menu_scientific()
        # coming soon for calculator scientific
        pass

    elif start_choice == 3 :
        # show_history()
        # coming soon for save history calculator normal
        pass
   
    elif start_choice == 4:
        # show_history()
        # coming soon for save history calculator scientific
        pass

    elif start_choice == 5 :
        # save history 
        # coming soon 
        pass
    
    elif start_choice ==  6:
        # clear history
        # coming soon
        pass

    elif start_choice == 7:
        print("THANK YOU FOR USING MY PROGRAM")
        break
