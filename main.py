from crud import (
    agregar_alumno,
    listar_alumnos,
    editar_alumno,
    eliminar_alumno
)

def menu():
    print("\n===== SISTEMA CRUD DE ALUMNOS =====")
    print("1. Agregar alumno")
    print("2. Listar alumnos")
    print("3. Editar alumno")
    print("4. Eliminar alumno")
    print("5. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_alumno()
        elif opcion == "2":
            listar_alumnos()
        elif opcion == "3":
            editar_alumno()
        elif opcion == "4":
            eliminar_alumno()
        elif opcion == "5":
            print("\nSaliendo del sistema...")
            break
        else:
            print("\nOpción inválida")

if __name__ == "__main__":
    main()

