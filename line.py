import math

pendiente=float(input("Ingrese el coeficiente A: "))
ordenada=float(input("Ingrese el coeficiente B: "))

x1=float(input("Ingrese el coeficiente X1: "))
x2=float(input("Ingrese el coeficiente X2: "))

print(f"El coeficiente A de su ecuación de la recta es: {pendiente}")
print(f"El coeficiente B de su ecuación de la recta es: {ordenada}")
print(f"El coeficiente X1 de su ecuación de la recta es: {x1}")
print(f"El coeficiente X2 de su ecuación de la recta es: {x2}\n")

print(f"Para la siguiente ecuación:\n \tY = {pendiente}X + {ordenada}\n")

y1=float((pendiente*x1) + ordenada)
y2=float((pendiente*x2) + ordenada)

print(f"Dados los siguientes puntos:\n \tP1 ({x1}, {y1}) \n \tP2 ({x2}, {y2})\n")

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"La distancia entre ellos es: {distancia}")