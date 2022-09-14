# Variable para saber nombre
nombre = str(input("ingrese  su nombre: "))

# Variable edad, Se puede transformar a entero poniendo doble parentesis y poniendo antes del input int
edad = int(input("Ingrese su edad: "))

# Variable para sumar edad
edad_futura= edad + 5

# Variable Saber peso
peso = float(input("ingrese su peso en KG: "))

# Variable para saber el estado
# estado = False
estado = bool(input("Ingrese su estado: "))

# Podemos ver el resultado de la variable imprimiendolo
print("Bienvenido", nombre)

# Se reinicia con f y se encierra nombre en llaves
# Se puede saber la edad igualmente poniendo otras variables para saber que resultado da y imprimir
print(f"Bienvenido {nombre}, Su edad es {edad} años, en 5 años su edad sera {edad_futura}, Su peso es {peso} kg, Su estado es {estado}")