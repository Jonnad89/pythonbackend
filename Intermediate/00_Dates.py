### Dates ###
#importo el modulo datetime y traigo datetime para trabajar solo con eso
from datetime import datetime
#declaro la variable existente dentro del modulo traido anteriormente
now = datetime.now()

def print_date(date):
  print(date.year)
  print(date.month)
  print(date.day)
  print(date.hour)
  print(date.minute)
  print(date.second)
  print(date.timestamp())
print_date(now)

print(f"año: {now.year}") #muestra el año
print(f"mes: {now.month}") #muestra el mes
print(f"día: {now.day}") #muestra el dia
print(f"hora: {now.hour}") #muestra la hora
print(f"minuto: {now.minute}") #muestra los minutos
print(f"segundo: {now.second}") #muestra los segundos

timestamp = now.timestamp()

print(f"tiempo transcurrido desde 1970: {timestamp}") #representación única de un tiempo

year_2024 = datetime(2024, 1, 1)

print_date(year_2024)

from datetime import time

current_time = time(21,6,0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

from datetime import date

current_date = date.today() #muestra la fecha de hoy

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(2023,2,10)

print(current_date.year)
print(current_date.month)
print(current_date.day)

current_date = date(current_date.year +1, current_date.month +1,current_date.day)

print(current_date.month)
print(current_date.year)

diff = year_2024 - now #los días que restan del año
print(diff)

diff = year_2024.date() - current_date
print(diff)

print(year_2024.time())

from datetime import timedelta

start_timedelta = timedelta(200, 100,100,weeks = 10)
end_timedelta = timedelta(300, 100,100,weeks = 13)
print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
print(end_timedelta == start_timedelta)
print(end_timedelta != start_timedelta)