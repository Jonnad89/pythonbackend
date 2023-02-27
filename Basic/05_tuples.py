### Tuples ###
#Como definir una tupla
#forma 1
my_tuple = tuple()
#forma 2
my_other_tuple = ()

my_tuple = ( 33, 1.71, "Jonatan", "Di Vincenzo" )
my_other_tuple = (35,60,30)
print(my_tuple)
print(type(my_tuple)) # <class 'touple'>

print(my_tuple[0]) # 33
print(my_tuple[-1]) # Di Vincenzo
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError


print(my_tuple.count("Di Vincenzo")) #Retorna 1
print(my_tuple.index("Jonatan")) #2 porque esta en la posición 3.. sería 0,1 y 2

# my_tuple[1] = 1.80 No me deja cambiarle los valores, las tuplas son inmutables, son como las constantes, podemos guardar datos en ellas y ya nos deja ese valor guardado e inicializado

my_sum_tuple = my_tuple + my_other_tuple
# Concatena
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #'Di Vincenzo', 35, 60... Busca entre el indice 3 y 6, es un slice
#Pasar una tupla a lista
my_tuple = list(my_tuple)
print(type(my_tuple)) #<class 'list'>

my_tuple[2] = "LoganTech"
my_tuple.insert(1,"Naranja")
print(my_tuple) #[33, 'Naranja', 1.71, 'LoganTech', 'Di Vincenzo']
#Volver a que sea una tupla, o sea, para poder modificar una tupla, hay que convertirla en lista y luego volverla a tupla, aunque no sería lo mejor, pero se puede hacer
print(tuple(my_tuple))
#Antes hay que reasignar a que vuelva a ser una tupla
my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple)) #<class 'tuple'>

#Acá elimino la tupla y si hago el print me sale que no está definida
del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined




