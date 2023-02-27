### Dictionaries ###
# un diccionario es un tipo de estructura donde podemos almacenar datos de tipo clave valor
my_dict = dict()

my_other_dict = {}

print(type(my_dict)) #<class 'dict'>
print(type(my_other_dict)) #<class 'dict'>

my_other_dict = {"Nombre":"Jonatan", "Apellido":"Di Vincenzo", "Edad":33, 1:"Python"}
my_dict = {
  "Nombre":"Jonatan", 
  "Apellido":"Di Vincenzo", 
  "Edad":33, 
  "Lenguajes":{"Python", "Swift","Kotlin"}, #un set dentro de un diccionario
  1:1.71
}

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Jonna" #Asi se acutaliza una clave en el dict
print(my_dict["Nombre"])
print(my_dict[1])
my_dict["Calle"] = "mi calle" #Agregando un nuevo valor al dict
print(my_dict)

del my_dict["Calle"] #Así elimino un elemento en especifico en un dict
print(my_dict)

print("Nombre" in my_dict) #Así compruebo si está, evalua la clave

print(my_dict.items()) #Listado de cada uno de los items
print(my_dict.keys()) #Un listado de las keys
print(my_dict.values())# Retorna todos los valores

my_new_dict = my_other_dict.fromkeys(("Nombre",1, "Piso"))#Crea un dict nuevo pero sin valores
print(my_new_dict)# {'Nombre': None, 1: None}

my_new_dict["Nombre"] = "Jonatan" #Así le agrego un nuevo valor al dict vacío
print(my_new_dict)

my_list = ["Nombre",1, "Piso"]

my_new_dict = dict.fromkeys((my_list)) #funciona con o sin parentesis
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict) #Me deja el diccionario vacío, o sea crea un nuevo diccionario donde me deja reaprovechar todas las claves
print(my_new_dict)

my_new_dict= dict.fromkeys(my_dict, ("Di Vincenzo", "Jonatan"))#le meti esto a todos los elementos
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict,"Jonatan")
print(my_new_dict)

my_values = my_new_dict.values()
print(type(my_values)) #<class 'dict_values'>

print(list(my_new_dict)) #Lo transformo a una lista, y me devuelve las claves []
print(tuple(my_new_dict)) #Lo paso a tupla ()
print(set(my_new_dict)) #Lo paso a set {}



