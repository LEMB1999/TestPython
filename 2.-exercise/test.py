from answer import *

def checkNotNumber():
    assert fibonacci("s") == "s is not a number"

def checkNegativeNumber():
    assert fibonacci(-1) == "the number must be greater than 0"

def checkSerial():
    cases = [
        {"input":1 , "result" : [0]},
        {"input":2 , "result" : [0,1]},
        {"input":3 , "result" : [0,1,1]},
        {"input":4 , "result" : [0,1,1,2]},
        {"input":5 , "result" : [0,1,1,2,3]},
    ]
    for case in cases:
        assert fibonacci(case["input"]) == case["result"]

def test_answer():
    checkSerial()
    checkNegativeNumber()
    checkNotNumber()