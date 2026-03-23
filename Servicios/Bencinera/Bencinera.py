""" 
   Este programa simula funcionamiento basico de una bencinera.
    Permite ingresar la carga actual del vehiculo
    Evalua tal cantidad
    Permite cargar
    Reevalua la cantidad
    permite recargar
    Por ultimo muestra una salida con el calculo de cargas y el valor final
"""

def validacion(validado): 
 validado = int(input(""))
 while validado < 0:
   validado =  int(input("El numero no puede ser negativo\n"))
 return validado
def nivel_actual(nivel):
 if nivel < 10:
    print(f"Su nivel es bajo. Tiene: {nivel} Litros\n")
 elif 10 <= nivel < 20:
    print(f"Su nivel es medio. Tiene: {nivel} Litros\n")
 else:
    print(f"Su nivel es alto. Tiene: {nivel} Litros\n")

precio = 100
suma_cargas = []
Total = 0
actual = 0
carga = 0

# Inicio programa # 

print("=====================================")
print("   Bienvenido a nuestra bencinera")
print(f"   Valor: ${precio} x Litro")
print("=====================================")


d = 0
print("¿Cuanto combustible tiene?")
actual = validacion(actual)


while d == 0: 
 nivel_actual(actual)

 print("¿Cuanto desea cargar?")
 carga = validacion(carga)

 actual = actual + carga
 suma_cargas.append(carga)

 print(f"\nSu nivel actual de carga es {actual}")
 print("¿Desea una nueva carga?")

 d = int(input("1= Si \t 2=No\n")) - 1
 while d != 0 and d != 1 :
  d = int(input("Ingrese una opción\n")) -1

for i in suma_cargas:
   Total = Total + i
v = Total * precio

# Salida # 

print("\n=====================================")
print(f"   Cargo {Total}L")
print(f"   Su estanque tiene {actual}L")
print(f"   TOTAL: {Total}L * ${precio} = {v}")
print("   Gracias por su compra")
print("=====================================")



 