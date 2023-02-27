### Functions ###

#¿Qué son las funciones o para qué utilizamos las funciones?
#con las funciones báscicamente intentamos resolver dos problemas, en primer lugar intentamos encapsular una logica muy concreta, es decir una función va a intentar resolver un problema muy concreto que nosotros vamos a indicar y por otra parte gracias a las funciones lo que vamos a hacer es evitar errores porque todo el código que va a resolver un problema muy concreto va a estar en único lugar, entonces nosotros siempre que querramos resolver ese problema llamaremos a esa misma función con lo cual todo estará centralizado y no tendremos que empezar a duplicar código que era algo muy típico al principio 

#¿Cómo se definen las funciones?
#Todo lo que tengamos tabulado hacia la derecha dentro o después de la función va a pertenecer a esta función
def my_function ():
  print("Esto es una función")

my_function()  #llamado a la función, si no la llamo no imprime
#Si llamo a la función dentro de la función se va a generar un bucle infinito

def sum_two_values(first_value: int, second_value:int):  #pasando parámetros o argumentos, aunque le diga que es un tipo int, va a concatenar los strings, ejemplo lina 19, no es necesario especificar el int
    print(first_value + second_value)

sum_two_values(5,7) # Acá le estoy pasando los valores
sum_two_values(54754,71231) # Si le pongo un valor más tira error, porque le pase 2 valores 
sum_two_values("5", "7") # Los concatena, da 57, si intentara dividir, tiraria error, solo se pueden dividir los números
sum_two_values(1.4,5.2) # 6.6


#función con retorno
def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values_with_return(10, 5) #Está retorna 15
#my_result = sum_two_values(1.4,5.2) si uso esta retorna None
print(my_result)

#definí una función, le pasé 2 parámetros, retorne la suma de los 2 parámetros, guarde en una variable el resultado pasandole por parametros 10 y 5, luego imprimí esa variable (my_return) y me dió el resultado de la suma de los parámetros que le pasé al principio, pdría no haber almacenado el valor en una variable, daría el mismo resultado, pero por buenas prácticas lo almacene en la variable my_result

# def sum_two_values_with_return(first_value, second_value):
#     my_sum = first_value + second_value
#     return my_sum función en varias lineas
    
def print_name (name, surname):
    print(f"{name} {surname}") #La f dice que en esta cadena de texto vamos a tener un formateo, si quito la f imprimiria {name}{surname}

print_name(surname = "Di Vincenzo",name = "Jonatan")# les doy una vuelta a los parámetros, le digo cual es el surname y el name  


# Llamados parámetros por defecto
def print_name_with_default(name,surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jonatan","Di Vincenzo", "Jonna")# Con alias 
print_name_with_default("Jonatan","Di Vincenzo")# Sin alias, si no le paso el alias, imprimirá "Jonatan Di Vincenzo Sin alias" ya que por defecto tiene que tener un valor, pero si no lo llamo dentro de la llamada va a adjuntar lo que tenga como valor por defecto 

#Si quiero pasarle infinitos parámetros
def print_texts(*texts): # El asterisco permite que le pase los parámetros que yo quiera, es un número de parámetros dinámico
  # for text in texts:  puedo hacerle un for
  #   print(text)
  print(texts)
  #print(type(text)) #clase tupla
print_texts("Hola", "Python", "Jonatan")  


def print_upper_texts(*texts):
    print(type(texts)) # <class 'tuple'>
    for text in texts:
      print(text.upper())
      #print(type(text)) <class 'str'>
print_upper_texts("hola", "python", "Jonatan")  