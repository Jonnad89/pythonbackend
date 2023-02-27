### Exception Handling (manejo de errores) ###

# try: {
# run this code
# }
# except: {
# execute this code when there is an exception
# }else: {
# no exceptions? run this code
# }finally: {
#  Always run this code
# }

#un if y un else nunca van a sustituir a un try/except
#Va a intentar ejecutar la primer linea, si falla, va a ir por el except y va a imprimir "Se ha producido un error", si comento la linea 18, va a ejecutar "6" y además va a decir "No se ha producido un error"
numberOne, numberTwo =5, 1

numberTwo = "1"
#try except
try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except:
  print("Se ha producido un error")  

#try except else finally

try:
  print(numberOne + numberTwo)
  print("No se ha producido un error")
except:
  #Se ejecuta si se produce una excepcion
  print("Se ha producido un error")  
else: 
  #Esto se ejecuta si no se produce una excepción
  print("La ejecución continúa correctamente")  
# en este caso, comente la linea 18, en este caso se ha impreso la linea 34  
finally:
  #Se ejecuta siempre, pase lo que pase
  print("La ejecución continúa")
 #Se ejecuta está linea, en este caso, teniendo la linea 18 activa, ejecutará 2 veces "se ha producido un error" y también "la ejecución continúa", porque el else no se ejecuta, el finally significa que ejecuta siempre, pase lo que pase
 # Siempre si hay un try, hay un except, de forma opcional tenemos el else y el finally


#captura de excepciones por tipo
try:
  print(numberOne + numberTwo)
  print("No se ha producido un error") 
  #Este bloque except se ejecuta SOLO si se produce TypeError, también le puedo pasar que solo capture errores de tipo valueError, por ej:
except ValueError:
  print("Se ha producido un ValueError")
except TypeError:
  print("Se ha producido un TypeError")
#Esto está por fuera del bloque de código, mostrará error
#print(numberOne + numberTwo) 


#Captura de la información de la excepción
try:
  print(numberOne + numberTwo)
  print("No se ha producido un error") 
except ValueError as error: #error es el nombre que le dí a la variable
  print(error) # No solo capturar el error, sino que hacer algo con el
except Exception as error:
  print(error)  #atrapa el error como tal, imprime "unsupported operand type(s) for +: 'int' and 'str'"

#Estás fueron las excepciones básicas, en otro módulo veré más avanzadas  