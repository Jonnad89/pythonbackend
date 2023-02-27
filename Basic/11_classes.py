### Classes ###

# Igual que una función al final nos vale para realizar una tarea muy concreta, la clase para lo que nos vale es para dosar al final del principio y de fin un objeto, una clase al final nos sirve para decir "si nosotros tenemos una clase, todo lo que esta dentro de una clase tiene que responder a una cierta logica" si tengo la clase "persona", la clase "persona" tendra que tener logica relacionada con "persona" 

#¿Cómo definir una clase?
# Las clases se definen en mayúsculas, si son dos o más palabras se usa calmelcase
# Las clases pueden tener constructores
# Se puede llamar con o sin parentesis 
# pass Evita el error, deja ejecutar la función aunque no tenga contenido
class MyEmptyPerson: 
  pass 

print(MyEmptyPerson) 
print(MyEmptyPerson()) 

# __init__ también es algo reservado del sistema que nos sirve para crear lo que se llama un constructor de clase
# Siempre va a llamar a "self", es algo que es requerido
# La definición __init__(self) es un constructor de clase
# Para almacenar los valores, en este caso name y surname se hace de la siguiente manera: 
# self.name = name y self.surname = surname
# De esa manera cuando vaya a hacer el print me deja acceder al name y al surname en my_person permitiendome colocar un punto para acceder a los datos que le pase anteriormente (name y surname)
# El uso del self es algo obligatorio, si nosotros queremos crear que tenga un constructor, le tenemos que pasar self, self se refiere a él mismo, ¿que es él mismo? si nosotros estamos dentro de "Person". Se refiere a la instancia de Person, a la clase Person que acabamos de crear
# name y surname son las propiedades que estamos creando dentro de Person y son las propiedades que en el momento que nosotros las definimos con self y que le asignamos un valor pasan a existir y pasan a existir fuera 
class Person:
  def __init__(self, name, surname):
      self.name = name
      self.surname = surname

my_person  = Person("Jonatan", "Di Vincenzo")
print(my_person.name) #imprime "Jonatan"
print(f"{my_person.name} {my_person.surname}") # Imprime "Jonatan Di Vincenzo"

# esto es lo mismo que lo de arriba, solo que estoy definiendo los parametros por dentro 

# class Person:
#   def __init__(self):
#       self.name = "Jonatan"
#       self.surname = "Di Vincenzo"

# my_person  = Person()
# print(f"{my_person.name} {my_person.surname}")


# Otra manera pero con todo almacenado en una sola

# class Person:
#   def __init__(self,name,surname):
#      self.full_name = f"{name} {surname}"
# my_person = Person ("Jonatan", "Di Vincenzo")
# print(my_person.full_name)    
# 
class Person:
   def __init__(self,name,surname, alias ="Sin alias"):
      self.full_name = f"{name} {surname} ({alias})" #propiedad pública
      self.__name = name # para poner en privado uso "__" no modificable
      

   def get_name(self):
    return  self.__name


   def walk(self): #le paso self, para poder acceder a los parámetros
    print(f"{self.full_name} está caminando") 



my_person = Person ("Jonatan", "Di Vincenzo")
print(my_person.full_name)   
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Jonatan", "Di Vincenzo", "Jonna")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Jonna di vincenzo (el loco de los perros)"
print(my_other_person.full_name)

# Le puedo cambiar siempre el tipo de dato que estoy definiendo, entonces a partir de acá pasa a ser un int
my_other_person.full_name = 555
print(my_other_person.full_name)
