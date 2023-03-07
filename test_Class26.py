# Pytest => its testing framework
# how to install => from terminal use command as => pip install pytest
import pytest


def addition(x, y):
    if x != None and y != None:
        return x + y
    else:
        return "Values should not be None"

def subtraction(x,y):
    if x != None and y != None:
        return x - y
    else:
        return "Values should not be None"

def addition1(x, y):
    return x + y


# Positive integers
# negative numbers
# positive negative combination
# float numbers
# strings
# None value

# The method name should start with test
@pytest.mark.smoke
@pytest.mark.addition
@pytest.mark.regression
def test_addition_valid():
    result = addition(10, 5)
    assert result == 15

@pytest.mark.addition
@pytest.mark.regression
def test_addition_negative():
    result = addition(-3, -5)
    assert result == -8

@pytest.mark.addition
@pytest.mark.regression
def test_addition_positive_negative():
    result = addition(10, -4)
    assert result == 6

@pytest.mark.addition
@pytest.mark.regression
def test_addition_float():
    result = addition(10.34, 12.44)
    assert result == 22.78

@pytest.mark.addition
@pytest.mark.regression
def test_addition_strings():
    result = addition("Hi", "Python")
    assert result == "HiPython"

@pytest.mark.addition
@pytest.mark.regression
def test_addition_none():
    result = addition(None, None)
    assert result == "Values should not be None"

@pytest.mark.addition
@pytest.mark.regression
def test_addition1_none_error():
    is_error = False
    try:
        result = addition1(None, None)
    except:
        is_error = True
    assert is_error == True

@pytest.mark.smoke
@pytest.mark.regression
def test_subtraction_valid():
    result = subtraction(10, 5)
    assert result == 5

@pytest.mark.regression
def test_subtraction_negative():
    result = subtraction(-3, -5)
    assert result == 2

@pytest.mark.regression
def test_subtraction_positive_negative():
    result = subtraction(10, -4)
    assert result == 14

@pytest.mark.regression
def test_subtraction_float():
    result = subtraction(10.34, 12.44)
    assert result == -2.0999999999999996

@pytest.mark.regression
def test_subtraction_strings():
    isexception = False
    try:
        result = subtraction("Hi", "Python")
    except:
        isexception = True
    assert isexception

@pytest.mark.regression
def test_subtraction_none():
    result = subtraction(None, None)
    assert result == "Values should not be None"




# how to run the test cases from terminal => pytest -v
# -v => will give complete test summary/information
# pytest -k => we can execute matching of testcase name ex: pytest -k test_addition_none -v
# smoke => Testing high level/basic  functionality of application /positive flow of application
# Regression => this is an in detail testing to cover all cases(i.e positive ,negative,boundary) , to make
# sure existing functionality is not broken with any enhancement or bug fixes

# addition =>test_addition_valid,test_addition_negative,test_addition_positive_negative,test_addition_float,
#test_addition_strings

# mark => grouping the test cases , you can provide any group name
# pytest -m smoke
# to execute test cases under particular file name we will use command with file name like => pytest .\test_Class26.py -v

# parametrize