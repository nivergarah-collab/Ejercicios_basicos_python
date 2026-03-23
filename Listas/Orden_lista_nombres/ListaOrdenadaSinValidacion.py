""" 
   En este programa me se crea una lista de numeros variable que contenga nombres
        # La lista se detiene al ingresar un caracter vacio
        # No se pueden repetir nombres
        # Se pueden ingresar numeros
"""

x = []
y = "Bypass first while"

# Inicio programa 

while y.strip() != (""):
    
    y = input("Ingrese un nombre\n")
    while y in x: 
        y = input("Valor repetido, ingrese otro nombre\n")
    if y.strip() == "": 
        break
    x.append(y)

x.sort()
print(x)
