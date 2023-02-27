#Variables
#se declaran en minusculas y se separan por guiones bajos
#Python utiliza la convensión de Snake case
my_string_variable ="My String variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = True
print(my_bool_variable)
#concatenación de variables en un print
print(my_string_variable,my_int_to_str_variable , my_bool_variable)
print("Este es el valor de:", my_bool_variable) #puedo concatenar así

print(type(print(print(my_string_variable,my_int_to_str_variable , my_bool_variable))))#nonetype

#Algunas funciones del sistema

print(len(my_string_variable)) #len mide la longitud 

#Variables en una sola linea

name, surname, alias, age = "Jonatan", "Di Vincenzo", "Jonna", 33
print("mi nombre es: ", name, "Me dicen:", alias,"Tengo:", age,"este es mi apellido", surname) #no es muy buena practica aunque se pueda hacer, pero es un foco de errores

"""
name = input('¿Cúal es tu nombre? ')
age = input('Cuántos años tienes? ')

print(name)
print(age)"""

#Cambiamos su tipo
name = 33
age = "Jonatan"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = 32
print(type(address))