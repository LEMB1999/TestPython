from answer import *

def checkCountWords():
    cases = [
        {"input":"Hola hola como estas", "case_sensitive":True , "result" : {"Hola":1,"hola":1 , "como":1, "estas":1}},
        {"input":"Hola hola como estas", "case_sensitive":False , "result" : {"hola":2,"como":1, "estas":1}},
        {"input":"como estas ? estas bien ?" , "case_sensitive":False  , "result" : {"como":1,"estas":2 , "?":2 , "bien":1 } },
        {"input":"esta frase no tiene palabras repetidas", "case_sensitive":False , "result" :{ "esta":1,"frase":1,"no":1,"tiene":1,"palabras":1,"repetidas":1 }},
        {"input":"okey como dijiste" , "case_sensitive":False , "result" : {"okey":1 ,"como":1 ,"dijiste":1}},
        {"input":"carros 90 carros 80",  "case_sensitive":False ,"result" : {"carros":2,"90":1 ,"80":1}},
    ]

    for case in cases:
        assert countWords(case["input"],case["case_sensitive"]) == case["result"]

def checkInvalidInput():
    assert countWords(1) == "the 1 is not a string"

def checkEmptyInput():
    assert countWords("") == {}

def test_answer():
    checkCountWords()
    checkInvalidInput()
    checkEmptyInput()

