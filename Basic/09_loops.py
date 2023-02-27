### Loops-bucles-ciclos ###

#¿Qué es iterar? Es intentar repetir algo, un bucle basicamente nos siver para pasar por el mismo código varias veces.

# While

my_condition = 0

while my_condition < 10:
  print(my_condition) 
  my_condition += 2 # para que no haga bucle infinito lo incrementé en 2, llega hasta 8 y se detiene, como 10 no es menor que 10 se detiene en el 8
else: #Este else pertenece al while
  print("mi condición es mayor o igual que 10")  
print("la ejecución continua")
# Esta estructura es la normal, aunque el else es opcional

while my_condition < 20:
  my_condition +=1
  if my_condition == 15:
    print("Se detiene la ejecución")
    break #para detener la ejecución cuando la condición se cumple
  print(my_condition)
print("la ejecución continua") #Este se ejecuta porque está fuera del while

# For

#Sirve para iterar un listado de elementos

my_list = [35, 24, 62, 52, 30, 30, 17]
#el for se va a repetir tatas veces como elementos tanga, cada vez que le de una vuelta al for va a estar accediendo a esos elementos del listado
#El for esta atado a ver cuantos elementos nosotros le estamos indicando dentro de una posible iteración

#element NO es una palabra reservada  

for element in my_list:
  print(element)

my_tuple = (33, 1.71, "Jonatan", "Di Vincenzo", "Jonna")
for element in my_tuple:
  print(element)
my_set = {"Jonatan", "Di Vincenzo", 33}
for element in my_set:
  print(element)
my_dict = {"Nombre":"Jonatan", "Apellido":"Di Vincenzo", "Edad": 33, 1:"Piso"}
for element in my_dict: #si quiero los valores tengo que pasarle my_dict.values()
  print(element) #En los diccionarios imprime los claves, no los valores
  if element == "Edad":
    break #Encontró "Edad" y ahí se detuvo el bucle
  print("Encontré 'Edad' ahora me detengo")
else:
  print("el bucle for para mi diccionario ha finalizado")  
# elif no se puede utilizar con el for 
print("La ejecución continúa") 

for element in my_dict:
  print(element)
  if element == "Edad":
    continue #Encuentra "Edad", vuelve a ejecutar
  print("Se ejecuta")
else:
  print("El bucle for para diccionario ha finalizado")  

print("La ejecución continúa")   
#el continue vuelve al for sin ejecutar lo que está debajo

#Brais no aconseja usar mucho el termino continue