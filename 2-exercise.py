#Luis Emmanuel Mendez Barrios
#2022/06/08


def fibonacci(number):
    result = []
    if number == 0:
        result = [0]
    elif number == 1:
        result = [1]
    elif number >= 3:
        result = [0,1]
        for i in range( 0 , number - 2 ):
            result.append(result[i]+result[i+1])

    return result

print(fibonacci(10))
        
