def eleccion_producto(eleccion, menu, boleta): 
 if eleccion == 1:
  boleta.append(menu[0])
 elif eleccion == 2:
  boleta.append(menu[1])
 elif eleccion == 3:
  boleta.append(menu[2])
 elif eleccion == 4:
  boleta.append(menu[3])
 elif eleccion == 5:
  boleta.append(menu[4])

menu = [
    {"nombre": "Medialuna", "precio": 10.0},
    {"nombre": "Dona", "precio": 100.0},
    {"nombre": "Berlin", "precio": 1000.0},
    {"nombre": "Café", "precio": 10000.0},
    {"nombre": "Té", "precio": 1000000.0}
]

def plural(cantidad):
 salida = ""
 if cantidad != 1:
  salida = "s"
 return salida 

def validacionUniversal(variable, Flambda):
 while Flambda(variable):
  variable = int(input("Ingrese una opcion Valida\n"))
 return variable
