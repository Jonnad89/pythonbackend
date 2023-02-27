### Lambdas / funciones sin nombres ###

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2,4)) #6

multiply_values = lambda first_value, second_value: first_value * second_value -3
print(multiply_values(2,4)) #5

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value
print(sum_three_values(5)(2,4)) #11

"""
Utilicé una lambda de mi propia idea
multy_values = lambda first, second: first * second * 3  
print(multy_values(2,4))
"""
