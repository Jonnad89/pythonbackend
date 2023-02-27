### Sets ###

# Definición
my_set = set()
my_other_set = {}
print(type(my_set)) #<class 'set'>
print(type(my_other_set)) #<class 'dict'> inicialmente es un diccionario

my_other_set = {"Jonatan","Di Vincenzo", 33}
print(type(my_other_set)) # ahora es clase set

print(len(my_other_set)) # 3

#print(my_other_set[0]) TypeError: 'set' object is not subscriptable

my_other_set.add("Jonna")
print(my_other_set) # Agrega "Jonna", Un set no es una estructura ordenada

my_other_set.add("Jonna") #Un set no admite repetidos
print(my_other_set)
#Un set no deja acceder a los elementos ya que se agrupan desordenadamente y nunca estarán en esa posición

print("Jonatan" in my_other_set)#True, estoy preguntando si existe en my_other_set
print("Jona" in my_other_set)#False

my_other_set.remove("Jonatan")
print(my_other_set) # {'Di Vincenzo', 33, 'Jonna'}

my_other_set.clear()
print(len(my_other_set)) # Devuelve set(), lo limpia y me muestra la longitud que es 0

del my_other_set
#print(my_other_set)  NameError: name 'my_other_set' is not defined

#Hace esto no es lo mejor, es muy arriesgado porque el orden será siempre aleatorio
my_set = {"Jonatan","Di Vincenzo", 33}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"React","Python","CSS"}

my_new_set = my_set.union(my_other_set)
print(my_new_set) #{33, 'React', 'CSS', 'Di Vincenzo', 'Jonatan', 'Python'}
print(my_new_set.union(my_new_set)) # No se duplican porque un set no admite repetidos, mientras no le esté pasando algo diferente no se va a añadir
print(my_new_set.union(my_new_set).union({"C#", "C++"}))#Ahora que le estoy pasando nuevos argumentos si los agrega

print(my_new_set.difference(my_set)) # {'CSS', 'Python', 'React'}, no aparecen los demás porque fueron agregados directamente en el print y no en la variable

#print(my_new_set.issuperset("Jonatan")) False
#print(my_new_set.isdisjoint("Jonatan")) True
