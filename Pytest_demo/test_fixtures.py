import pytest


# fixtures are like before and after in testNG
#we created conftest file and kept all the fixutures in that, so all pytest files can use that
# first interpreter check in local file if fixture present if not then it will check in conftest file


#we need to pass this fixtures as param in our test, then only it will be considered by the test
def test_add(setup):
    print("a+b")


#Ques---If we want add fixture on class level(for all the functions in one class) ,so in fixture defination we need to mention scope=Class
#if scope in fixture defination is not defined as class then this fixture will run before and after every method of a class
@pytest.mark.usefixtures("setup")
class Test:
    def test_minus(self):
      print("a-b")

    def test_mult(self):
      print("a*b")
