from calculator_normal import *
from calculator_scientific import *
from datetime import datetime

# ===============================
# 🧾 HISTORY STORAGE
# ===============================
history_normal = []
history_scientific = []

# ===============================
# 🧾 HISTORY MANAGEMENT FUNCTIONS
# ===============================
def show_history(history_list, title):
    print(f"\n===== {title} =====")
    if not history_list:
        print("No history available.\n")
    else:
        for order, entry in enumerate(history_list, start=1):
            print(f"{order}. {entry.strip()}")
    print()

def save_history(history_list, filename):
    if not history_list:
        print("No history to save.\n")
        return
    with open(filename, "w", encoding="utf-8") as file:
        for entry in history_list:
            file.write(entry)
    print(f"History saved successfully to '{filename}'\n")

def clear_history(history_list):
    history_list.clear()
    print("History cleared successfully!\n")

# ===============================
# 🧮 MAIN PROGRAM ENTRY POINT
# ===============================
while True:
    print("====== Welcome to the Calculator Program ======")
    print("Select calculator mode")
    print("1. Normal (Basic Operation)")
    print("2. Scientific (Advanced Operation)")
    print("3. Save history")
    print("4. Show history Calculator normal")
    print("5. Show history Calculator scientific")
    print("6. Clear History")
    print("7. Exit ")
    print("="*48)

    # Handle invalid menu input (non-integer)
    try:
        start_choice = int(input("Enter Number (1-7) = "))
    except ValueError:
        print("Please Enter in number")
        continue

    # =====================================
    # 🧾 NORMAL CALCULATOR MODE
    # =====================================
    if start_choice == 1:
        while True:
            Calculator.menu_normal()  # Display normal calculator menu

            choice_normal = Calculator.normal_prompt()  # Prompt the user for an operation choice

            if choice_normal == 5:  # Option 5 allows returning to the main menu
                print("Returning to main menu...\n")
                break

            cal_normal = Calculator()  # Create a new calculator instance

            num_normal = cal_normal.get_number_normal()  # Collect user input for numbers

            result, op = cal_normal.calculator_normal(choice_normal, num_normal)  # Perform the operation

            # If an invalid operation occurred (e.g., divide by zero), skip iteration
            if result is None:
                continue

            # Format and display the calculation result
            result_normal = cal_normal.format_result(num_normal, result, op, None)
            print(result_normal)

            # ✅ Save to history automatically
            history_normal.append(result_normal)

            continue  # Allow user to perform more operations before returning

    # =====================================
    # 🧮 SCIENTIFIC CALCULATOR MODE (COMING SOON)
    # =====================================
    elif start_choice == 2:
        # calculator_scientific.menu_scientific()
        # coming soon for calculator scientific
        pass

    # =====================================
    # 💾 SAVE HISTORY TO FILES
    # =====================================
    elif start_choice == 3:
        save_history(history_normal, "history_normal.txt")
        save_history(history_scientific, "history_scientific.txt")

    # =====================================
    # 📜 SHOW NORMAL CALCULATOR HISTORY
    # =====================================
    elif start_choice == 4:
        show_history(history_normal, "HISTORY - Normal Calculator")

    # =====================================
    # 📜 SHOW SCIENTIFIC CALCULATOR HISTORY
    # =====================================
    elif start_choice == 5:
        show_history(history_scientific, "HISTORY - Scientific Calculator")

    # =====================================
    # 🧹 CLEAR HISTORY
    # =====================================
    elif start_choice == 6:
        print("1. Clear normal calculator history")
        print("2. Clear scientific calculator history")
        print("3. Clear both")
        clear_choice = input("Enter choice: ")

        if clear_choice == "1":
            clear_history(history_normal)
        elif clear_choice == "2":
            clear_history(history_scientific)
        elif clear_choice == "3":
            clear_history(history_normal)
            clear_history(history_scientific)
        else:
            print("Invalid option.\n")

    # =====================================
    # 🚪 EXIT PROGRAM
    # =====================================
    elif start_choice == 7:
        print("THANK YOU FOR USING MY PROGRAM")
        break

    # =====================================
    # ⚠️ INVALID MENU CHOICE
    # =====================================
    else:
        print("This feature is not implemented yet or invalid.\n")
        continue