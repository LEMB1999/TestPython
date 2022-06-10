from answer import *

#verify if user pass not a number to the function
def test_NotNumber():
    assert fibonacci("s") == "s is not a number"

#verify if the user pass a number greater to 0
def test_NegativeNumber():
    assert fibonacci(-1) == "the number must be greater than 0"

#verify the serial fibonacci with diferents cases
def test_Serial():
    cases = [
        {"input":1 , "result" : [0]},
        {"input":2 , "result" : [0,1]},
        {"input":3 , "result" : [0,1,1]},
        {"input":4 , "result" : [0,1,1,2]},
        {"input":5 , "result" : [0,1,1,2,3]},
    ]
    
    for case in cases:
        assert fibonacci(case["input"]) == case["result"]

