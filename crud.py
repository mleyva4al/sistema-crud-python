# crud.py
from data import alumnos
from utils import pausar

def agregar_alumno():
    nombre = input("Nombre del alumno: ")
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
    if len(alumnos) == 0:
        print("\nNo hay alumnos registrados")
    else:
        print("\nLISTA DE ALUMNOS")
        for i, a in enumerate(alumnos, start=1):
            print(f"{i}. {a['nombre']} - {a['edad']} años - Grupo {a['grupo']}")
    pausar()

def eliminar_alumno():
    listar_alumnos()
    try:
        opcion = int(input("Número de alumno a eliminar: "))
        alumnos.pop(opcion - 1)
        print("\nAlumno eliminado correctamente")
    except:
        print("\nOpción inválida")
    pausar()
