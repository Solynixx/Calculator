---

# 🧮 Calculator (Python CLI)

A simple calculator program written in Python.
It supports basic arithmetic operations, saves calculation history, and allows users to manage history easily.

---

## ✨ Features

* ➕ Addition
* ➖ Subtraction
* ✖️ Multiplication
* ➗ Division (with zero-division handling)
* 📜 Show history (with timestamp)
* 🧹 Clear history
* 💾 Save history to `.txt` file
* ❌ Exit program safely

---

## 📂 Project Structure

```
calculator/
│── calculator.py   # Core Calculator class
│── main.py         # Run the program
│── save_history_calculator.txt   # History file (generated after saving)
│── README.md       # Project documentation
```

---

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/calculator.git
   ```
2. Move to the project folder:

   ```bash
   cd calculator
   ```
3. Run the program:

   ```bash
   python main.py
   ```

---

## 📝 Example Output

```
-------------------------
CALCULATOR
-------------------------
1. Add
2. Subtract
3. Multiply
4. Divide
5. Show history
6. Clear history
7. Save history
8. Exit
-------------------------
Enter Choice : 1
Enter first number  : 10
Enter second number : 5
10 + 5 = 15
```

**History Example:**

```
[2025-09-18] [10:30 AM] 1. 10 + 5 = 15
[2025-09-18] [10:32 AM] 2. 20 ÷ 4 = 5.00
```

---

## 📦 Future Improvements

* Add **scientific mode** (square root, power, percentage, etc).
* Add **auto-save history on exit**.
* Create a **GUI version** using Tkinter/PyQt.
* Add **unit testing** for better reliability.

---

