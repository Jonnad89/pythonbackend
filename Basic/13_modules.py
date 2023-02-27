### Modules ###

#Un módulo es como el concepto de librerías, al final no deja de ser esa librería donde tenemos ese código en específico
#No me dejará importar módulos que comiencen con números

import my_module #acá puedo importar todo lo que haya en el módulo

from my_module import sumValues #puedo importar más utilizando comas
#esto es para ir en concreto a una función
# sumValues es el nombre que le di en el fichero "modules" y se importa acá

sumValues(5, 3, 1) 
#si lo importo en concreto, solo utilizo la función
my_module.printValue("Hola Python!") #así utilizo la función cuando llamo todo lo que haya en el módulo


#El módulo se trata de que haga operaciones muy concretas

# módulos creados por el sistema, o sea... fuera de nuestros ficheros

import math

print(math.pi) #nos da el acceso al valor de la variable pi

print(math.pow(2,8)) #256 esto es potencia, es 2 elevado a 8

from math import pi as PI_VALUE#importar algo en especifico con un nombre que yo le quiera dar "pi as..." seria "importar pi como..."

print(PI_VALUE)