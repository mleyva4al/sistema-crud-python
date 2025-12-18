# main.py
from crud import *

def menu():
    print("\n===== SISTEMA DE ALUMNOS =====")
    print("1. Agregar alumno")
    print("2. Listar alumnos")
    print("3. Eliminar alumno")
    print("4. Salir")

while True:
    menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        agregar_alumno()
    elif opcion == "2":
        listar_alumnos()
    elif opcion == "3":
        eliminar_alumno()
    elif opcion == "4":
        print("\nSaliendo del sistema...")
        break
    else:
        print("\nOpción no válida")
