#Luis Emmanuel Mendez Barrios
#2022/06/08

def displayNumbers(start,end):
    for number in range( start , end + 1 ):
        if(number % 3 == 0 and number % 5 == 0 ):
            print("fizz buzz")
        elif(number % 3 == 0 ):
            print("fizz")
        elif(number % 5 == 0):
            print("buzz")
        else:
            print(number)

displayNumbers(1,100)
