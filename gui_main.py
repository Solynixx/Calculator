import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from calculator_normal import Calculator
from calculator_scientific import CalculatorScientific


class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Edbert's Calculator 🧮")
        self.root.geometry("500x600")
        self.root.configure(bg="#f5f5f5")

        # ========== Instances ==========
        self.normal_calculator = Calculator()
        self.scientific_calculator = CalculatorScientific()
        self.history_normal = []
        self.history_scientific = []

        # ========== Tabs ==========
        self.notebook = ttk.Notebook(self.root)
        self.frame_normal = ttk.Frame(self.notebook)
        self.frame_scientific = ttk.Frame(self.notebook)

        self.notebook.add(self.frame_normal, text="Normal")
        self.notebook.add(self.frame_scientific, text="Scientific")
        self.notebook.pack(expand=True, fill="both")

        # Setup UI for both tabs
        self.setup_normal_tab()
        self.setup_scientific_tab()

    # ===========================
    # NORMAL CALCULATOR TAB
    # ===========================
    def setup_normal_tab(self):
        title = tk.Label(self.frame_normal, text="Normal Calculator", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        # Entry
        self.entry_normal = tk.Entry(self.frame_normal, width=40, font=("Arial", 13))
        self.entry_normal.pack(pady=10)

        # Buttons Frame
        btn_frame = tk.Frame(self.frame_normal)
        btn_frame.pack(pady=10)

        buttons = [
            ("Add (+)", 1),
            ("Subtract (-)", 2),
            ("Multiply (×)", 3),
            ("Divide (÷)", 4)
        ]

        for i, (text, op) in enumerate(buttons):
            tk.Button(
                btn_frame, text=text, width=12, height=2, bg="#e0e0e0",
                command=lambda c=op: self.calculate_normal(c)
            ).grid(row=i // 2, column=i % 2, padx=5, pady=5)

        # Result
        self.result_label_normal = tk.Label(self.frame_normal, text="", font=("Arial", 12), fg="blue")
        self.result_label_normal.pack(pady=10)

        # History
        tk.Label(self.frame_normal, text="History:", font=("Arial", 12, "bold")).pack()
        self.text_history_normal = tk.Text(self.frame_normal, width=55, height=10, state="disabled", wrap="word")
        self.text_history_normal.pack(pady=5)

        # Clear Button
        tk.Button(
            self.frame_normal, text="Clear History", bg="#f0a0a0",
            command=lambda: self.clear_history(self.text_history_normal, "normal")
        ).pack(pady=5)

    def calculate_normal(self, choice):
        input_text = self.entry_normal.get().strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please input numbers first!")
            return
        try:
            numbers = [float(num) for num in input_text.split()]
            result, op = self.normal_calculator.calculator_normal(choice, numbers)
            if result is not None:
                formatted = self.normal_calculator.format_result(numbers, result, op)
                self.result_label_normal.config(text=formatted)
                self.add_history(formatted, "normal")
            else:
                self.result_label_normal.config(text="Error in calculation.")
        except ValueError:
            self.result_label_normal.config(text="Invalid input! Use spaces between numbers.")

    # ===========================
    # SCIENTIFIC CALCULATOR TAB
    # ===========================
    def setup_scientific_tab(self):
        title = tk.Label(self.frame_scientific, text="Scientific Calculator", font=("Arial", 16, "bold"))
        title.pack(pady=10)

        self.entry_sci = tk.Entry(self.frame_scientific, width=40, font=("Arial", 13))
        self.entry_sci.pack(pady=10)

        btn_frame = tk.Frame(self.frame_scientific)
        btn_frame.pack(pady=10)

        buttons = [
            ("sin", 1), ("cos", 2), ("tan", 3),
            ("sqrt", 4), ("pow", 5), ("log", 6),
            ("log10", 7), ("factorial", 8)
        ]

        for i, (text, op) in enumerate(buttons):
            tk.Button(
                btn_frame, text=text, width=10, height=2, bg="#e0e0e0",
                command=lambda c=op: self.calculate_sci(c)
            ).grid(row=i // 4, column=i % 4, padx=5, pady=5)

        # Result
        self.result_label_sci = tk.Label(self.frame_scientific, text="", font=("Arial", 12), fg="blue")
        self.result_label_sci.pack(pady=10)

        # History
        tk.Label(self.frame_scientific, text="History:", font=("Arial", 12, "bold")).pack()
        self.text_history_sci = tk.Text(self.frame_scientific, width=55, height=10, state="disabled", wrap="word")
        self.text_history_sci.pack(pady=5)

        # Clear Button
        tk.Button(
            self.frame_scientific, text="Clear History", bg="#f0a0a0",
            command=lambda: self.clear_history(self.text_history_sci, "scientific")
        ).pack(pady=5)

    def calculate_sci(self, choice):
        input_text = self.entry_sci.get().strip()
        if not input_text:
            messagebox.showwarning("Warning", "Please input number(s) first!")
            return
        try:
            if choice == 5:  # pow(x, y)
                nums = [float(x) for x in input_text.split()]
                if len(nums) != 2:
                    self.result_label_sci.config(text="Need exactly 2 numbers for pow(x, y).")
                    return
            else:
                nums = [float(input_text.split()[0])]

            result, op = self.scientific_calculator.calculator_scientific(choice, *nums)
            if result is not None:
                formatted = self.scientific_calculator.format_result(nums, result, op)
                self.result_label_sci.config(text=formatted)
                self.add_history(formatted, "scientific")
            else:
                self.result_label_sci.config(text="Math domain error.")
        except ValueError:
            self.result_label_sci.config(text="Invalid input!")

    # ===========================
    # HISTORY MANAGEMENT
    # ===========================
    def add_history(self, text, mode):
        if mode == "normal":
            self.history_normal.append(text)
            self.update_history_box(self.text_history_normal, self.history_normal)
        elif mode == "scientific":
            self.history_scientific.append(text)
            self.update_history_box(self.text_history_sci, self.history_scientific)

    def update_history_box(self, widget, history_list):
        widget.config(state="normal")
        widget.delete("1.0", tk.END)
        for item in history_list[-10:]:  # show last 10
            widget.insert(tk.END, item)
        widget.config(state="disabled")

    def clear_history(self, widget, mode):
        widget.config(state="normal")
        widget.delete("1.0", tk.END)
        widget.config(state="disabled")
        if mode == "normal":
            self.history_normal.clear()
        else:
            self.history_scientific.clear()
        messagebox.showinfo("Success", "History cleared successfully!")

# ===========================
# MAIN EXECUTION
# ===========================
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
