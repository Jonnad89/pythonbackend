### Lists ###
#Como definir listas
#Forma 1
my_list = list()
#Forma 2
my_other_list = []

print(len(my_list)) # 0

my_list = [33,70,2,52]
print(my_list) # [33,70,2,52]
print(len(my_list)) # 4

my_other_list = [33, 1.71, "Jonatan", "Di Vincenzo"]
print(my_other_list) # [33, 1.71, "Jonatan", "Di Vincenzo"]
print(len(my_other_list)) # 4
print(type(my_other_list)) # <class 'list'>

my_new_list = my_list[::-1] # Hago que se imprima al reves
print(my_new_list[::-1])

print(my_other_list[0]) # 33, muestra el primer elemento de la lista
print(my_other_list[1]) # 1.71 muestra el segundo elemento de la lista
print(my_other_list[2]) # Muestra mi nombre que es el tercer elemento de la lista
print(my_other_list[3]) # Muestra mi apellido que es el cuarto elemento de la lista
print(my_other_list.count("Jonatan")) # 1. Me cuenta las veces que aparece un valor
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

#Así puedo desestructurar una lista
age, height, name, surnmae = my_other_list
print(name)#Imprime mi nombre que esta definido en my_other_list, siempre siguiendo un orden

# Sumando / Concatenando
print(my_list + my_other_list)

# print(([1, 2, 3, 4]))#Así también se puede ejecutar una lista

my_other_list.append("LoganTech") #Agrega el appened al final
print(my_other_list) 

my_other_list.insert(1,"Naranja") #Hago un inserto en la posición que le indiqué
print(my_other_list)


my_other_list.remove("Naranja")# Ahora puedo eliminar lo que agregué, si hay dos elementos repetidos, elimina el primero que aparece
print(my_other_list)

my_list.pop() # Elimina el último elemento de la lista, también le puedo pasar parametros, por ejemplo pop(2)
print(my_list)
print(my_list.pop())# Acá me muestra el valor que eliminará

#del my_list[2] # del elimina por indice, en este caso eliminará el elemento con indice 2
#print(my_list)

my_new_list = my_list.copy()

my_list.clear() #Limpio todos los elementos de la lista, queda vacía
print(my_list)
print(my_new_list)


my_new_list.reverse()#me da el reverse, pero tengo que ejecutarlo así, no en el print
print(my_new_list)

my_new_list.sort()#ordena, también puede llevar parámetros
print(my_new_list)

print(my_new_list[1:2]) #[70]


#Le cambio el tipo de dato, en este caso es debilmente tipado
my_list = "Hola Python" #Si lo encierro en [] o pongo list() lo convierto en una lista
print(my_list)
print(type(my_list))# <class 'str'>

