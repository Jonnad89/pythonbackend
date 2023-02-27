### List Comprehension / comprimida ###

my_original_list = [0,1,2,3,4,5,6,7]
print(my_original_list)

my_range = range(8) #le puedo pasar el numero que quiera
print(list(my_range))

my_list = [i +1 for i in range(8)]
print(my_list)

my_list = [i * 2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)] #se multiplican por el valor de si mismos
print(my_list)

def sum_five(number):
  return number +5
my_list = [sum_five(i) for i in range(8)] # Retorna el valor sumado 5
print(my_list)


