from utils import pausar

# Lista global de alumnos
alumnos = []

def agregar_alumno():
    print("\n--- Agregar Alumno ---")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    grupo = input("Grupo: ")

    alumno = {
        "nombre": nombre,
        "edad": edad,
        "grupo": grupo
    }

    alumnos.append(alumno)
    print("\nAlumno agregado correctamente")
    pausar()

def listar_alumnos():
    print("\n--- Lista de Alumnos ---")

    if not alumnos:
        print("No hay alumnos registrados")
    else:
        for i, alumno in enumerate(alumnos, start=1):
            print(f"{i}. {alumno['nombre']} | Edad: {alumno['edad']} | Grupo: {alumno['grupo']}")

    pausar()

def editar_alumno():
    if not alumnos:
        print("\nNo hay alumnos para editar")
        pausar()
        return

    listar_alumnos()
    try:
        indice = int(input("Número de alumno a editar: ")) - 1

        if indice < 0 or indice >= len(alumnos):
            print("Índice fuera de rango")
        else:
            alumno = alumnos[indice]
            print("\nDeja vacío para mantener el valor actual")

            nombre = input(f"Nombre ({alumno['nombre']}): ")
            edad = input(f"Edad ({alumno['edad']}): ")
            grupo = input(f"Grupo ({alumno['grupo']}): ")

            if nombre:
                alumno['nombre'] = nombre
            if edad:
                alumno['edad'] = edad
            if grupo:
                alumno['grupo'] = grupo

            print("\nAlumno actualizado correctamente")
    except:
        print("\nEntrada inválida")

    pausar()

def eliminar_alumno():
    if not alumnos:
        print("\nNo hay alumnos para eliminar")
        pausar()
        return

    listar_alumnos()
    try:
        indice = int(input("Número de alumno a eliminar: ")) - 1

        if indice < 0 or indice >= len(alumnos):
            print("Índice fuera de rango")
        else:
            eliminado = alumnos.pop(indice)
            print(f"\nAlumno {eliminado['nombre']} eliminado correctamente")
    except:
        print("\nEntrada inválida")

    pausar()

