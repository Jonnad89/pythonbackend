### File Handling ###
import os
""" .txt file """

txt_file = open("Intermediate/my_file.txt", "w+") #Leer y Escribir

txt_file.write("Mi nombre es Jonatan\nMi apellido es Di Vincenzo\nTengo 33 años\nMi lenguaje favorito es Python")
#print(txt_file.read())
#print(txt_file.read(10)) leer 10 caracteres del fichero
#print(txt_file.readline()) imprime "mi nombre es jonatan"
#print(txt_file.readline()) imprime "mi apellido es Di Vincenzo"
# print(txt_file.readlines()) Imprime todo en un arreglo
for line in txt_file.readlines():
  print(line) #Lee todas las lineas y las junta en un listado

txt_file.write("\nAunque también me gusta React")
print(txt_file.readline())

txt_file.close()

with open("Intermediate/my_file.txt","a") as my_other_file:
  my_other_file.write("\nY CSS")
"""Borrar el fichero"""
#os.remove("Intermediate/my_file.txt")

# .json file
import json 

json.dump
#crea un json
json_file = open("Intermediate/my_file.json", "w+")

json_test = {
  "name":"Jonatan", 
  "surname":"Di Vincenzo", 
  "age":33, 
  "languages":["Python", "React", "NodeJs"],
  "website":"https://instagram.com/jonnadv"}

# Así se escribe un json

json.dump(json_test, json_file, indent = 2)

json_file.close() # Si no lo cierro no lo puedo leer

with open("Intermediate/my_file.json") as my_other_file:
  for line in my_other_file.readlines():
    print(line)

json_dict = json.load(open("Intermediate/my_file.json"))

print(json_dict)
print(type(json_dict))
print(json_dict["name"])

# .csv file

import csv

csv_file = open("Intermediate/my_file.csv","w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["name", "surname","age","language", "website" ])
csv_writer.writerow(["Jonatan", "Di Vincenzo",33,"Python", "https://instagram.com/jonnadv" ])
csv_writer.writerow(["Liliana", "Nenna",70,"Python", "https://instagram.com/jonnadv" ])

csv_file.close()

with open("Intermediate/my_file.csv") as my_other_file:
  for line in my_other_file.readlines():
    print(line)
# .xlsx file

#import xlrd #debe instalarse el módulo

# .xml file

import xml

