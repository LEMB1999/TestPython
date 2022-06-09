#Luis Emmanuel Mendez Barrios
#2022/06/08

from sqlalchemy import Integer


def checkNumber(number):

    if not isinstance(number,int):
        return "{0} is not a number".format(number)

    if(number % 3 == 0 and number % 5 == 0 ):
        return "fizz buzz"
    elif(number % 3 == 0 ):
        return "fizz"
    elif(number % 5 == 0):
        return "buzz"
    else:
        return number

def displayNumbers(start,end):
    for number in range( start , end + 1 ):
       checkNumber(number)


#displayNumbers(1,100)