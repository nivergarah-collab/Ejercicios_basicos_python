""" 
   En este programa me se crea una lista de numeros variable que contenga nombres
        # La lista se detiene al ingresar un caracter vacio
        # No se pueden repetir nombres
        # No se pueden ingresar numeros
"""

def validador(validado):
   try:
      validado = int(validado)
      if validado == 0:
         validado += 1
      while validado:
         validado = input("NO INGRESE NUMEROS\n")
         validado = int(validado)
         if validado == 0:
            validado += 1
   except ValueError:
      complete = validado
      return 1, complete
   

x = []
y = "Bypass first while"

# Inicio programa 

while y.strip() != (""):
    y = input("Ingrese un nombre\n")
    Resultado_validacion = 0
    while Resultado_validacion != 1:
       Resultado_validacion, y = validador(y)
    while y in x: 
        y = input("Valor repetido, ingrese otro nombre\n")
        Resultado_validacion = 0
        while Resultado_validacion != 1:
         Resultado_validacion, y = validador(y)
    if y.strip() == "": 
        break
    else: 
       x.append(y)



x.sort()
print(x)

