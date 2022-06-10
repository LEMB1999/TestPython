from answer import *

#verify the cases when number is multiple by five
def test_MultiplesOfFive():
    cases = [5,10,20,25,35,40,50]
    for case in cases:
        assert checkNumber(case) == "buzz"

#verify the cases when number is multiple by three
def test_MultiplesOfThree():
    cases = [3,6,9,12,18,21,24,27]
    for case in cases:
        assert checkNumber(case) == "fizz"

#verify the cases when number si multiple by both five and three
def test_BothMultiples():
    cases = [15,30,45]
    for case in cases:
        assert checkNumber(case) == "fizz buzz"

#verify if the user input a not number case
def test_NotNumber():
    assert checkNumber("s") == "s is not a number"


