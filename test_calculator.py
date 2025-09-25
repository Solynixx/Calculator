from calculator import Calculator

def test_add():
    calc = Calculator()
    calc.x, calc.y = 2, 3
    result, op = calc.add()
    assert result == 5
    assert op == "+"

def test_subtract():
    calc = Calculator()
    calc.x, calc.y = 10, 4
    result, op = calc.subtract()
    assert result == 6
    assert op == "-"

def test_multiply():
    calc = Calculator()
    calc.x, calc.y = 6, 7
    result, op = calc.multiply()
    assert result == 42
    assert op == "x"

def test_divide():
    calc = Calculator()
    calc.x, calc.y = 8, 2
    result, op = calc.divide()
    assert result == 4
    assert op == "÷"

def test_divide_by_zero():
    calc = Calculator()
    calc.x, calc.y = 5, 0
    result, op = calc.divide()
    assert result is None
    assert op is None

def test_format_result_integer_division():
    output = Calculator.format_result(8, 2, 4, "÷")
    assert output == "8 ÷ 2 = 4.00"

def test_format_result_integer_addition():
    output = Calculator.format_result(3, 5, 8, "+")
    assert output == "3 + 5 = 8"

def test_format_result_float_multiplication():
    output = Calculator.format_result(2.5, 4, 10, "x")
    assert output == "2.50 x 4 = 10.00"

def test_history_append_and_show():
    Calculator.history.clear() 
    Calculator.history.append(("[2025-09-25] [10:00 AM]", "2 + 3 = 5"))
    assert len(Calculator.history) == 1
    assert Calculator.history[0][1] == "2 + 3 = 5"

def test_clear_history():
    Calculator.history.append(("[2025-09-25] [10:05 AM]", "4 x 2 = 8"))
    Calculator.clear_history()
    assert len(Calculator.history) == 0

import os

def test_save_history(tmp_path):
    Calculator.history.clear()
    Calculator.history.append(("[2025-09-25] [10:10 AM]", "6 - 1 = 5"))
    
    test_file = tmp_path / "test_history.txt"
    Calculator.save_history(filename=test_file)
    
    assert test_file.exists()
    content = test_file.read_text(encoding="utf-8")
    assert "6 - 1 = 5" in content
