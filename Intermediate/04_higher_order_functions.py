### Higher order finctions ###
"""
Son las funciones que están en lo más alto de la jerarquía
"""

def sum_one(value):
  return value +1
def sum_five(value):
  return value + 5  

def sum_two_values_and_add_value(first_value, second_value, f_sum):
  return f_sum(first_value + second_value)
  """"
  f_sum pasa a ser una función dentro de una función, en este ejemplo hay funciones que son capaces de ejecutar otras funciones
  """

print(sum_two_values_and_add_value(5,2,sum_one))  
print(sum_two_values_and_add_value(5,2,sum_five)) 

### Closures ###

def sum_ten(original_value):
    def add(value): #closure "add"
      return value + 10 + original_value
    return add
add_closure = sum_ten(1) 
print(add_closure(5))

print((sum_ten(5))(1)) #igual, pero en una sola línea

### Built-in Higher order finctions / las que ya existen en python ###

numbers = [2, 5 ,10, 21, 3, 30]

# Map

def multiply_two(number):
  return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter 

def filter_greater_than_ten(number):
  if number > 10:
    return True
  return False  

print(list(filter(filter_greater_than_ten, numbers)))# imprime 21 y 30
print(list(filter(lambda number: number > 10, numbers)))# imprime 21 y 30
"""
El map recorre todos los valores y ejecuta una función sobre ellos, para modificar su valor.
El filter recorre todos los valores y ejecuta una función que retorna True o False para saber como filtrar los valores del iteredo
"""

# Reduce
"""
reduce lo que hace es operar con un valor más el acumulado
"""
from functools import reduce

def sum_two_values(first_value, second_value):
  print(first_value)
  print(second_value)
  return first_value + second_value

print(reduce(sum_two_values, numbers))
