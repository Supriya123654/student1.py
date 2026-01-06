from student1 import calculate_grade

def test_grade_S():
    avg = 95
    assert calculate_grade(avg) == "S"

def test_grade_A():
    avg = 85
    assert calculate_grade(avg) == "A"

def test_grade_B():
    avg = 70
    assert calculate_grade(avg) == "B"

def test_grade_C():
    avg = 55
    assert calculate_grade(avg) == "C"

def test_grade_D():
    avg = 45
    assert calculate_grade(avg) == "D"

def test_grade_F():
    avg = 30
    assert calculate_grade(avg) == "F"


def test_average_calculation():
    marks = [85, 90, 88]
    average = sum(marks) / len(marks)
    assert round(average, 2) == 87.67