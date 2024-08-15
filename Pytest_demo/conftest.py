import pytest
#conftest is a default file_name we need to create and store all fixtures in it
# which we want should be available for all test files

#scope variable will tell when to apply this fixture, if scope is class it will be applied before and after class exection

@pytest.fixture(scope="class")
def setup():
  print("this will be executed before the test")
  yield
  print("This will be executed after the test")


#when fixtures return data
@pytest.fixture()
def dataload():
  print("user profile data is created")
  return ["Neha", "Aggarwal","Nehaaggarwal.automationQA"]

#parameterised fixtures
#@pytest.fixture(params=[("Neha","aggarwal"),("chrome","new"),("Firefox","Volt")])
#def parameterized()