### Regular Expressions ###

import re #modulo de Expresiones Regulares (regular expressions)

my_string = "Esta es la lección número 7: Lección Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])



maarch = re.match("Esta es la lección", my_other_string)
if match is not None:
  print(match)
  start, end = match.span()
  print(my_other_string[start:end])

# print(re.match("Expresiones Regulares", my_string))

# Search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# Findall

findall = re.findall("lección", my_string, re.I)
print(findall)
# print(type(findall))

# Split

split = re.split(":", my_string) #split divide a partir del primer patrón encontrado
print(split)

# Sub
resub = re.sub("lección", "LECCIÓN", my_string, re.I)
print(resub)
resub = re.sub("Expresiones Regulares", "RegEx", my_string, re.I)
print(resub)

# Patterns / Patrones

pattern = r'[lL]ección'
print(re.findall(pattern, my_string))

pattern = r'[lL]ección|Expresiones'
print(re.findall(pattern, my_string))
print(re.match(pattern,my_string))

pattern = r'[0-9]'
print(re.findall(pattern,my_string))
print(re.match(pattern,my_string))
print(re.search(pattern,my_string))

pattern = r'\d'
print(re.findall(pattern,my_string))

pattern = r'\D'
print(re.findall(pattern,my_string))

pattern = r'[l].*'
print(re.findall(pattern,my_string))

email ="jonnadvwork@gmail.com"
pattern = r'^[a.zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
print(re.match(pattern,email))
print(re.search(pattern,email))
print(re.findall(pattern,email))

email ="jonnadvwork@jonnadvwork.com.ar"
print(re.findall(pattern,email))
