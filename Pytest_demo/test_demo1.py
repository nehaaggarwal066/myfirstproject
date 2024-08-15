#any pytest file shoould start or end with test keyword
#any code in file should go in function olny and function name should start with test
#any code should be wrapped in method only
#fucntion name should be unique otherwise it pytest will override
# we can run our test from cmd prompt with custom marks only: py.test -m mark_name -v -s
#pytest.mark.xfail- used to skip the reporting for this test(neither fail,pass or skip)
#pytest.mark.skip-- skip the test from execution
import pytest


#we can runthe same from cmd prompt->navigate to this path pytest_demo and run comd:
#py.test
#py.test -v              with verbose
#py.test -v -s           showing the report in output
#py.test -K               showing the method name
#py.test -m mark_name  eg.py.test -m smoke  will run all test with smoke mark
# we can create custom marks like pytest.mark.any_name
@pytest.mark.smoke
def test_firstprogram():
  print("Hello")

#we have predefined marks also, eg.skip-used to skip the test case
@pytest.mark.xfail
def test_second_function():
  print("Bye")

@pytest.mark.skip
def test_third_function():
  print("HIIIIIIIII")

test_firstprogram()