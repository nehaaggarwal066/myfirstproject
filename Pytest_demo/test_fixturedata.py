import pytest
#when fixture return data we use it like this, by giving fixtur name as parameter

class Test_fixture:
    def test_editprofile(self,dataload):
        print(dataload)
        print(dataload[1])
        print(dataload[2])