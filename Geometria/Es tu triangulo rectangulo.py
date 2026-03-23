"""   
   Programa que desde los 3 lados de un rectangulo, determina si es rectangulo.
        Ademas calcula el area en cualquier caso
        En este caso, para variar soluciones, no usaremos listas ni sort
        Se asume que solo entraran enteros, por lo que no podra haber nunca un rectangulo e isosceles.
"""
import math

def validador(validado): 
 while validado < 1: 
  validado = int(input("longitud no valida, ingrese otra:\n"))
 return validado
def repartidor(x, y, z):

 """
 Cuidado, esta funcion devuelve en el orden especifico del return
 """
 if x > y: 
  hip = x
  cat1 = y
  if z > x: 
   hip = z
   cat2 = x
  else:
   cat2 = z 
 else: 
  hip = y
  cat1= x
  if z > y: 
   hip = z
   cat2 = y
  else: 
   cat2 = z
 return hip, cat1, cat2
def numero_coincidencias(a,b,c): 
 coincidencias = 0 
 if a == b:
  coincidencias += 1
  if c == b:
   coincidencias += 1
 else: 
  if a == c or b == c: 
   coincidencias +=1
 return coincidencias
def area_universal(a,b,c): 
 s = (a + b + c )/2
 area = math.sqrt((s * (s-a) * (s-b) * (s-c)))
 return area
def salida(nombre, area):
  print (f"\nTriangulo {nombre}\n")
  print(f"Area = {area}")
  print (f"Perimetro = {x+y+z}")

coincidencias = 0 


# Inicio programa

print("¿Quieres saber si es un triangulo rectangulo?")
x = int(input("Ingresa un lado\n")) 
x = validador(x)
y = int(input("Ingresa otro lado\n"))
y = validador(y)
z = int(input("Ingresa otro lado\n"))
z = validador(z)

hip, cat1, cat2 = repartidor(x, y, z)
coincidencias = numero_coincidencias(x,y, z)

if cat1**2 + cat2**2 == hip**2:
  area = area_universal(x,y,z)
  nombre = "Rectangulo"
  salida(nombre, area)
else: 
 print("\nSu triangulo No es rectangulo\n")
 if coincidencias == 0:
  area = area_universal(x,y,z)
  nombre = "escaleno"
  salida(nombre, area)

 elif coincidencias == 1: 
  area = area_universal(x,y,z)
  nombre = "isosceles"
  salida(nombre, area)
 else:
  area = area_universal(x,y,z)
  nombre = "equilatero"
  salida(nombre, area)





