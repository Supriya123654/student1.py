# test_app.py
from app import calculate_grade, calculate_average

def test_grade_S():
    assert calculate_grade(95) == "S"

def test_grade_A():
    assert calculate_grade(85) == "A"

def test_grade_B():
    assert calculate_grade(70) == "B"

def test_grade_C():
    assert calculate_grade(55) == "C"

def test_grade_D():
    assert calculate_grade(45) == "D"

def test_grade_F():
    assert calculate_grade(30) == "F"

def test_average_calculation():
    marks = [80, 90, 100]
    assert calculate_average(marks) == 90