from tkinter.filedialog import LoadFileDialog


rusia = """
Seleccione una Opcion
(1)-Area Cuadrado
(2)-Area Rectangular
(3)-Area Circulo
"""
# opcion = int(input(rusia))
opcion = input(rusia)

if opcion == "1":
    lado = int(input("Ingrese el valor del lado (cm): "))
    area_c = lado * lado
    print("El area del cuadrado es: ", area_c)











# Comentario de una linea

"""
Comentario Multiples lineas
Comentario Multiples lineas
Comentario Multiples lineas
Comentario Multiples lineas

Se puede almacenar en una VARIABLE
"""