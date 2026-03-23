""" 
   Este programa elige un numero al azar y luego permite al usuario adivinar en un numero limitado de intentos.
   Ademas debe dar pistas al usuario para lograr encontrar el numero y mostrar los intentos restantes
"""

import random
count = 0 
maximos_intentos = 10
x = random.randrange(1, 101)
# print(x)


# Inicio programa #

print("Ingrese un numero del 1 al 100")
while count != maximos_intentos:
 y = int(input(""))
 while y not in range(1, 101): 
  y = int(input("Opcion ingresada no es valida\n Intente otra vez\n"))
 if y < x: 
  count += 1
  print(f"Demasiado bajo.\nTe quedan {maximos_intentos - count} intentos\n")
 elif y > x: 
  count += 1
  print(f"Demasiado alto.\nTe quedan {maximos_intentos - count} intentos\n")
 else: 
  break
 

# Salida # 
 
if count != maximos_intentos:
  print("===============================================")
  print("          Felicidades, haz adivinado")
  print("===============================================")
else: 
 print("===============================================")
 print("                 Juego terminado")
 print("           Mas suerte para la proxima")
 print("===============================================")