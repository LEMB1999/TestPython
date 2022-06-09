#Luis Emmanuel Mendez Barrios
#2022/06/08


def fibonacci(number):

    if not isinstance(number,int):
        return "{0} is not a number".format(number)

    if number <= 0:
        return "the number must be greater than 0"

    result = []
    if number == 1:
        result = [0]
    elif number == 2:
        result = [0,1]
    elif number >= 3:
        result = [0,1]
        for i in range( 0 , number - 2 ):
            result.append(result[i]+result[i+1])

    return result

#fibonacci(10)
        
