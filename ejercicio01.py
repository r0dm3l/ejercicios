"""
Ejercicio 1: Hacer un programa que pida al usuario 5 nombres.
Crear una lista con los 5 nombres.
Despues hacer que muestre una frase los nombres que empiezan con la letra A
"""

nombres = []
nombresA = []

for n in range(1, 6):
    nombre = input(f"Ingresa el nombre nro: {n} ")
    nombres.append(nombre)

for nombre in nombres:
    if nombre[0] == "A":
        nombresA.append(nombre)

print("Los nombres que empiezan con la letra A son: ", ", ". join(nombresA))

