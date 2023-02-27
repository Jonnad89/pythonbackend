### Challenges / Retos ###
"""
              El famoso "FIZZ BUZZ":
 Escribe un programa que muestre por consola (con un print) los 
 numeros de 1 a 100(ambos incluidos y con un salto de linea entre cada 
 impresión), sustituyendo los siguientes:
 - Multiplos de 3 por la palabra "fizz",
 - Multiplos de 5 por la palabra "buzz",
 - Multiplos de 3 y 5 a la vez con la palabra "fizzbuzz"
"""
def fizzbuzz():
  for index in range(1,101): 
    if index % 3 == 0 and index % 5 == 0:
      print("fizzbuzz")
    elif index % 3 == 0:
      print("fizz")  
    elif index % 5 == 0:
      print("buzz")    
    else:   
      print(index) 
fizzbuzz()

"""
                ¿Es un anagrama?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un anagrama consiste en formar una palabra reordenando TODAS las letras
  de otra palabra inicial.
- No hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagramas.  
"""

def is_anagram(word_one, word_two):
  if word_one.lower() == word_two.lower():
    return False
  return sorted(word_one.lower()) == sorted(word_two.lower())
  #sorted ordena todas las letras de las palabras
print(is_anagram("AmoR", "OrMa"))

"""
        La sucesión de Fibonacci
Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de número en la que el siguiente siempre es la suma de los dos anteriores.
0,1,1,2,3,5,8,13...
"""

def fibonacci():

  prev =  0
  next = 1

  for index in range(0, 50):
      print(prev)
      fib = prev + next
      prev = next 
      next = fib
      print(fib) 
fibonacci()

### ¿Es un número primo?###
"""
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100
"""

def is_prime():
  for number in range(1,101):

      if number >= 2:

        is_divisible = False

        for index in range(2,number):
          if number % index == 0:
            is_divisible = True
            break
        if not is_divisible:  
          print(number)
is_prime()  

"""
Invirtiendo cadenas
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse(text):
  text_len = len(text) 
  reversed_text = ""
  for index in range(0, text_len):
      reversed_text += text[text_len - index -1]
  return reversed_text

print(reverse("Hola mundo"))  