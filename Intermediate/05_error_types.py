### Error Types ###

#1- SyntaxError
"""Forma incorrecta"""
#print "¡Hola comunidad!"
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
"""Forma correcta"""
print("¡Hola comunidad!")

#2- NameError
"""Forma incorrecta"""
#print(language) NameError: name 'language' is not defined
"""Forma correcta"""
language = "Spanish"
print(language)

#3- IndexError

my_list = ["Python","Swift", "Kotlin", "Dart", "JavaScript"]

"""Forma incorrecta"""
#print(my_list[5]) IndexError: list index out of range

"""Forma Correcta"""
print(my_list[0]) #Python
print(my_list[4]) #JavaScript
print(my_list[-1]) #JavaScript

#4- ModuleNotFoundError
"""Forma Incorrecta"""
#import maths ModuleNotFoundError: No module named 'maths'
"""Forma Correcta"""
import math

#5- AttributeError
"""Forma Incorrecta"""
# print(math.PI) AttributeError: module 'math' has no attribute 'PI'. Did you mean: 'pi'?
"""Forma Correcta"""
print(math.pi)

#6- KeyError

my_dict = {"Nombre":"Jonatan", "Apellido":"Di Vincenzo", "Edad":33, 1:"Python"}
"""Forma Incorrecta"""
#print(my_dict["Apelido"])KeyError: 'Apelido'

"""Forma Correcta"""
print(my_dict["Edad"])

#7- TypeError

"""Forma Incorrecta"""
# print(my_list["Nombre"]) TypeError: list indices must be integers or slices, not str
# print(my_list["0"])
"""Forma Correcta"""
print(my_list[0])
#print(my_list[False]) aunque esto da 0, es una mala práctica

#8- ImportError
"""Forma Incorrecta"""
# from math import PI ImportError: cannot import name 'PI' from 'math' (unknown location)
"""Forma Correcta"""
from math import pi
print(pi)

#9- ValueError
"""Forma Incorrecta"""
# my_int = int("10 años") ValueError: invalid literal for int() with base 10: '10 años'
"""Forma Correcta"""
my_int = int("10")
print(type(my_int))
print(my_int)

#10- ZeroDivisionError
"""Forma Incorrecta"""
# print(4/0) ZeroDivisionError: division by zero
"""Forma Correcta"""
print(4/2)