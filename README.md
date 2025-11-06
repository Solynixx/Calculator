# 🧮 Calculator GUI with Python

A simple desktop calculator application featuring a *tabbed interface* built using Python and Tkinter. This application provides a **"Normal"** mode for basic arithmetic and a **"Scientific"** mode for more complex calculations.

-----

## ✨ Key Features

  * **Tabbed Interface (Notebook):** Easily switch between "Normal" and "Scientific" modes.
  * **Normal Calculator:**
      * Supports: Addition (+), Subtraction (-), Multiplication (×), and Division (÷).
      * Can process multiple numbers at once (separated by spaces, e.g., `10 5 2`).
  * **Scientific Calculator:**
      * **Trigonometry:** `sin`, `cos`, `tan`
      * **Powers & Roots:** `sqrt` (square root), `pow` (power, e.g., `4 2` for $4^2$)
      * **Logarithms:** `log` (natural log), `log10` (base 10)
      * **Other:** `factorial` (\!)
  * **Calculation History:**
      * Each tab (Normal & Scientific) maintains its own separate history box.
      * Displays the last 10 calculations.
      * A **"Clear History"** button is available to clear the history for each mode.

-----

## 📸 Application Preview

The application features two tabs. The "Normal" tab handles basic operations, while the "Scientific" tab provides advanced mathematical functions.

-----

## 📂 Project Structure

The recommended file structure for this project:

```
tkinter-calculator/
│
├── main.py                   # The main Tkinter GUI script (the code you provided)
├── calculator_normal.py      # Contains the Calculator class for normal logic
├── calculator_scientific.py  # Contains the CalculatorScientific class for scientific logic
└── README.md                 # This file
```

-----

## 🚀 How to Run

1.  **Prerequisites:** Ensure you have **Python 3** installed. The `tkinter` module is typically included with standard Python installations.

2.  **Save the Files:** Make sure all three Python files (`main.py`, `calculator_normal.py`, `calculator_scientific.py`) are in the same directory.

3.  **Run the Application:** Open your terminal or command prompt, navigate to the project directory, and execute the following command:

    ```bash
    python main.py
    ```

-----

## 📦 Future Improvements

  * **History Persistence:** Save the calculation history to a `.txt` or `.json` file so it isn't lost when the app closes.
  * **Keyboard Support:** Add key bindings (e.g., pressing the `Enter` key to trigger calculation).
  * **Dynamic Entry:** Create a more traditional calculator display (showing buttons pressed) instead of manual text entry.
  * **Unit Testing:** Add test cases to validate the logic in `calculator_normal.py` and `calculator_scientific.py`.
