### OPERADORES ARITMETICOS###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)# Establece una división y te devuelve lo que resta
print(10 // 3)# Flor división, nos da un número entero
print(2 ** 3) # 8 exponente
print(2 ** 3 + 3 - 7 / 1 // 4)#ejecuta todo
print("Hola " * 2)
print("Hola " * (2 ** 3))


print("Hola " + "Python" + " .Qué tal?")# El signo más sirve para concatenar, con el signo menos no
#print("hola" + 8) #No se deben mezclar entre tipos diferentes porque da error
print("Hola " + str(5))#Así lo puedo concatenar

### Operadores Comparativos ###

print(3 > 4)#false
print(3 < 4)#true
print(3 >= 4)#false
print(3 <= 4)#true
print(3 == 4)#false
print(3 != 4) #true
print(3 > 4 == 2)#false 
print(3 > 4 > 2)#false

#Comprobando ordenación alfabetica
print("Hola" > "Python") #false
print("Hola" < "Python")#true
print("Hola" >= "Python")#false
print("Hola" <= "Python")#true
print("Hola" == "Python")#false
print("Hola" != "Python")#true

#Para comparar la longitud se utiliza len
print(len("aaaa") >= len("aaaa"))#true
print(len("aaaa") < len("aaaa"))#false
print(len("aaaa") >= len("aaa"))#true

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")#false
print(3 > 4 or "Hola" > "Python")#false
print(3 < 4 and "Hola" < "Python")#true
print(3 < 4 or "Hola" < "Python")#true
print(3 < 4 or ("Hola" > "Python" and 4 == 4))#true
print(not (3 > 4)) #true estoy negando toda la condición(le estoy diciendo que 3 no es mayor que 4)
print(not (3==3))#false, yo mismo se lo estoy negando


