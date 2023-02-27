### Strings ###

my_string = "My string"
my_otrher_string = 'My string'

print(len(my_string))
print(len(my_otrher_string))

print(my_string + " " + my_otrher_string)

my_new_line_string = "Este es un Sring\ncon salto de linea" #\n va pegado asi se alinea bien
print(my_new_line_string)

my_new_tab_string = "\tEste es un String con tabulacion"
print(my_new_tab_string)

my_scape_string = "\tEste es un String \n escapado"
print(my_scape_string)

# Fromateo

name, surname, age = "Jonatan", "Di Vincenzo", 33

#forma correcta y buena practica
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %d" %(name,surname,age))
#forma más rápida
print(f"Mi nombre es {name} {surname} y mi edad es {age}")

#forma incorrecta y no es buena práctica
print("Mi nombre es " + name + " " + surname + " y mi edad es " + str(age))

# Desempaquetado de caracteres
language = "python"
a,b,c,d,e,f = language
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)

# División

language_slice = language[1:3]
print(language_slice)# imprime "yt" agarra desde la primer letra hasta la 3era sin contar la tercera

language_slice = language[1:]
print(language_slice) #ython
language_slice = language[0:6:2]
print(language_slice) # Pto

# Reverse

reversed_language = language[::-1] #el final empieza siempre por -1
print(reversed_language) # nohtyP  me dió vuelta al texto

### Funciones ###

print(language.capitalize()) # Pone la primer letra en Mayuscula
print(language.upper())#Todo a mayusculas
print(language.lower())#todo a minusculas
print(language.count("t"))#Me cuenta cuantas letras t tiene
print(language.isnumeric())#false
print(language.upper().isupper())#comprueba si esta en mayusculas, devuelve True
print(language.split())# ['python']
print(language.encode())#b'python
print(language.startswith("py"))#True
print(language.startswith("Py"))#False
