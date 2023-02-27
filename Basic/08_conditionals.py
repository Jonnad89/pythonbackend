### Conditionals ###

my_condition = False

if my_condition:  # es lo mismo que if my_condition == True:
  print("Se ejecuta la condición del if")
  #Si es verdadero se ejecutan las dos, sino la de abajo

my_condition = 5 * 2 

if my_condition == 11:
  print("Se ejecuta la condición del segundo if")
#De esta manera (linea 12) comprueba si es 10, si no lo es no muestra el print de linea 12, si el valor es 10, se ejecuta el print, de lo contrario muestra el print linea 14

if my_condition >= 10:
  print("Se ejecuta la condición del tercer if") #Se ejecutan ambos, cuando se ejecuta una condición tiene que haber un true para que se ejecute
print("La ejecución continúa")

if my_condition > 10:
  print("Es mayor que 10")# Si esta condición no se cumple...
else:
  print("Es menor o igual que 10")# Entonces haz esto

my_condition = 5 * 3

if my_condition > 10 and my_condition < 20:
  print("Es mayor que 10 y menor que 20")  #Cumple la condición de 5 * 5 
else:
  print("Es menor o igual que 10 o mayor o igual que 20")

print("Es menor o igual que 10 o mayor o igual que 20")
  

# Print tabulado, si lo tabulamos considera que está dentro del else, pero cuando le quito la tabulación el sistema considera que está fuera del else
my_condition = 5 * 5
if my_condition > 10 and my_condition < 20: # Primero comprueba esto
  print("Es menor o igual que 10 y menor que 20.")
elif my_condition == 25: # Luego comprueba esto
  print("Es igual a 25")
else: # Por ultimo comprueba esto
  print("Es menor o igual que 10 o mayor o igual que 20 o distinto de 25...")
  
my_string = ""  

if not my_string: # Acá estoy negando que esté vacía, se cumple la condición
  print("Mi cadena de texto es vacía")

if my_string == "Mi cadena de textooooooo": # Este caso no se cumple
  print("Estas cadenas de texto coinciden")  