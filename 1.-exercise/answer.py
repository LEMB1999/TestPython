#Luis Emmanuel Mendez Barrios
#2022/06/08

#this function check if the number pass as param is multiple of 5 or 3 or both
def checkNumber(number):

    #validate that the number pass in function is a number
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

#this function displays a list of numbers depending on the value show a fizz , buzz , fizz buzz or a number
# start ->  the start number of the list
# end   ->  the end   number of the list
def displayNumbers(start,end):
    for number in range( start , end + 1 ):
       checkNumber(number)


#displayNumbers(1,100)