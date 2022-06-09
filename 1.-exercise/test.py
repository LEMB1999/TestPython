from answer import *

def checkMultiplesOfFive():
    cases = [5,10,20,25,35,40,50]
    for case in cases:
        assert checkNumber(case) == "buzz"

def checkMultiplesOfThree():
    cases = [3,6,9,12,18,21,24,27]
    for case in cases:
        assert checkNumber(case) == "fizz"

def checkBothMultiples():
    cases = [15,30,45]
    for case in cases:
        assert checkNumber(case) == "fizz buzz"

def checkNotNumber():
    assert checkNumber("s") == "s is not a number"

def test_answer():
    checkMultiplesOfFive()
    checkMultiplesOfThree()
    checkBothMultiples()
    checkNotNumber()
