""" 
   Este programa simula funcionamiento basico de una Cafeteria.
    Permite elegir producto y cantidad
    Crea una boleta incremental
    Permite seguir comprando o cancelar
    Calcula el total de la compra realizada y presenta salida formato boleta.
"""




import Utils

y = 0  # Bucle maestro app
iva = 0.19
Producto = 0
menu = Utils.menu
boleta = []
# x = eleccion producto
# c = eleccion cantidad
# R y R_iva = valores segun cantidad
# F = confirmacion producto
# G = confirmacion nueva operacion


## Inicio programa ## 

print("==========================================================================")
print("++++++++++       Bienvenido a Cafeteria Buenos Granos        +++++++++++++")
print("==========================================================================")

while y == 0:
 print("Nuestro menú:")
 count = 0
 for i in menu:
     count += 1
     print(count,". ", i)

 print("¿Que deseea?")
 x = int(input(""))
 x = Utils.validacionUniversal(x,lambda x: x not in range(1,6))

 Utils.eleccion_producto(x, menu, boleta)

 c = int(input("¿cuantos desea?\n"))
 c = Utils.validacionUniversal("texto", c, lambda x: x<1)

 R = c * menu[x-1]["precio"]
 R_iva = R * (1 + iva)


 print(f"Usted esta comprando {c} {menu[x-1]["nombre"]}{Utils.plural(c)} ")
 print(f"Valor: {R_iva}\n")

 F = int(input("¿Desea confirmar?\n 1=Si\t 2=No\n"))
 F = Utils.validacionUniversal(F,lambda x: x not in range(1,3))


 if F == 2:
  print("Operacion cancelada\n")
  boleta.pop(Producto)
 

 else:
  boleta[Producto].update({"cantidad": c})
  boleta[Producto].update({"Total": R})
  Producto += 1
  

 G = int(input("¿Desea otra compra?\n 1=Si\t 2=No\n"))
 G = Utils.validacionUniversal(F,lambda x: x not in range(1,3))


 if G == 2: 
  y = 1
 else:
  y = 0
  
## Salida programa ##  

if Producto == 0:
 print("===========================================================")
 print("   Compra cancelada. Lo esperamos en una nueva ocacion")
 print("============================================================")
else: 
 print("===========================================================")
 


 for item in boleta:
  terminacion = Utils.plural(int(item["cantidad"]))
  print(f" {item["cantidad"]} {item["nombre"]}{terminacion}\t\t${item["Total"]}")

 suma_totales = 0
 for s in boleta: 
   suma_totales = suma_totales + int(s["Total"])
 print("\n___________________________________________________________")
 print(f"   Total                    ${suma_totales}")
 print(f"   IVA                      ${suma_totales*iva}")
 print("___________________________________________________________")
 print(f"   Final                    ${(suma_totales*iva) + suma_totales}")
 print("   Muchas gracias por su compra")
 print("===========================================================")

