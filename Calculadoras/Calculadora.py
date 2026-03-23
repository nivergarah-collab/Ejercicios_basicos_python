"""
     Calculadora basica con operaciones limitadas y 2 entradas de numeros. 
"""

# Inicio programa #

x = int(input("Tipo de operación:\n 1 = suma,\n 2 = resta,\n 3 = multiplicación,\n 4 = división,\n 5 = potencia\n"))
while x not in range(1, 6):
    x = int(input("Elija una opcion valida\n"))



num1 = int(input("Ingrese el primer numero\n"))
num2 = int(input("Ingrese el segundo numero\n"))

if x == 1:
 r = num1 + num2
 print(f"El resultado es {num1} + {num2} = {r}")
elif x == 2:
 r = num1 - num2
 print(f"El resultado es {num1} - {num2} = {r}")
elif x == 3:
 r = num1 * num2
 print(f"El resultado es {num1} * {num2} = {r}")
elif x == 4:
 if num2 == 0:
  print(f"El resultado es {num1} / {num2} = error")
 else:
  r = num1 / num2
  print(f"El resultado es {num1} / {num2} = {r}")
elif x == 5:
 r = num1 ** num2
 print(f"El resultado es {num1} ^ {num2} = {r}")  