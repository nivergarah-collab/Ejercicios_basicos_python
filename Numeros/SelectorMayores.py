""" 
   Este programa determina los valores mas altos de una serie de numeros.
    Primero el usuario elige la cantidad de elementos de la lista
    Luego ingresa los valores
    Por ultimo muestra los mas altos de los ingresados. 
"""
lista = []
count = 0




# Inicio programa # 

print("Bienvenido a nuestro selecto de mayores.")
x = int(input("Elija la cantidad de datos a analizar\n"))

if x > 0 :
 while count < x: 
    y = int(input("ingrese numero\n"))
    while y in lista:
       y = int(input("Numero repetido\nIngrese otro\n"))  
    lista.append(y) 
    count += 1

 lista.sort()
 lista.reverse()

 print(f"Mayor numero: {lista[0]}")
 if x > 1: 
  print(f"Segundo mayor: {lista[1]}")
else: 
 print("Valor no apto para evalucion\n Vuelva en otra ocación")
