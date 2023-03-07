import pytest


def addition(x, y):
    return x + y


# parametrize => executing the same test case with different input and expecting different output

@pytest.mark.parametrize("a,b,output", [(2, 3, 5), (6, 7, 13), (-1, 3, 2)])
def test_addtion_parametrize(a, b, output):
    result = addition(a, b)
    assert result == output


# skip
# xfail

@pytest.mark.skip
def test_addition_fail():
    result = addition("Hi", 3435)


@pytest.mark.xfail
def test_addition_fail1():
    result = addition("Hi", 3435)
    assert result == "Hi3435"


# Pytest
# filename => test_
# method => test
# defining test cases
# how to execute all test cases inside folder  => pytest -v
# -v => it gives complete summary
# how to execute particular test case => pytest -k testname -v
# how to execute particular file name => pytest filename -v
# smoke
# regression
# how to group test cases => pytest.mark
# how to parametrize => pytest.mark.parametrize
# how to skip particular test case => pytest.mark.skip
# xfail => this is not consider even if test case is failed

# fixture => its combination of setup and tear down , will segregate these by using yield
# setup => precondition => this will execute before executing test method
# teardown => this will execute after executing test method
def test_file_operation():
    file1 = open("practice.txt")
    result = file1.read()
    assert len(result) > 0
    file1.close()

def test_file1_operation():
    file1 = open("practice.txt")
    result = file1.readlines()
    assert len(result) > 0
    file1.close()

@pytest.fixture()
def sample_fixture():
    print("executing before test method")
    yield 23
    print("executing after test method - dispose")

@pytest.mark.usefixtures("sample_fixture")
def test_add_fixture(sample_fixture):
    input = sample_fixture
    result = addition(input,44)
    print("I am executing inside test method")
    assert result == 67




