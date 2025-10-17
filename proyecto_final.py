"""
Proyecto Final - Registro de alumnos y calculadora de calificaciones
Basado en las convenciones PEP8 y las prácticas del proyecto PISA.
Autor: Nicolás Muñoz Cruz A01714495
"""

import csv

# Listas globales
tareas = []
resultados = []
promedios = []
valores = []


def promedio_cali(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    Parámetros:
        calificaciones (list): lista con valores numéricos
    Devuelve:
        float: promedio de calificaciones
    """
    promedio_alumno = sum(calificaciones) / len(calificaciones)
    return promedio_alumno


# Solicita número de salones
num_salones = int(input("¿Cuántos salones quieres?: "))
print()
cont_alumnos = 0
salones = []

print(
    "Registro de alumno y calculadora de calificaciones.\n"
    "Si quieres terminar de programar en matrícula presiona 0.\n"
)

for i in range(num_salones):
    print()
    print(f"Salón {i + 1}")
    print()
    tareas = []
    valores = []
    salon = []

    cant_alumnos = int(input("¿Cuántos alumnos quieres en este salón?: "))
    cont_alumnos += 1
    cant_tareas = int(input(f"¿Cuántas tareas vas a calificar para salón {i + 1}?: "))

    # Registro de tareas y valores
    for t in range(cant_tareas):
        tarea = input(f"Ingresa nombre de la tarea {t + 1}: ")
        tareas.append(tarea)
        valor = float(input(f"Ingresa el valor de la tarea {t + 1}: "))
        valores.append(valor)

    if sum(valores) != 100:
        print("Los valores deben sumar 100")
        valores.clear()
        print()
        for t in range(cant_tareas):
            valor = int(input(f"Ingresa el valor de la tarea {t + 1}: "))
            valores.append(valor)
            print()
    else:
        print("Valores registrados\n")

    # Registro de alumnos y calificaciones
    for j in range(cant_alumnos):
        print()
        print(f"Alumno {j + 1}")
        print()
        matricula = float(input("Ingresa matrícula: "))
        nombre = input("Ingresa nombre: ")
        carrera = input("Ingresa carrera: ")
        print()

        alumno = {
            "matricula": matricula,
            "nombre": nombre,
            "carrera": carrera,
            "calificaciones": {},
            "valores": {},
            "promedio": {},
        }

        print(f"Calificaciones para {nombre}")

        for tarea in tareas:
            while True:
                calificacion = float(
                    input(f"Ingresa calificación para {tarea}, del 1 al 10: ")
                )
                if 0 <= calificacion <= 10:
                    alumno["calificaciones"][tarea] = calificacion
                    alumno["valores"][tarea] = valores[tareas.index(tarea)]
                    alumno["promedio"][tarea] = promedio_cali(
                        alumno["calificaciones"].values()
                    )
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
        salon.append(alumno)

    salones.append(
        {"tareas": tareas.copy(), "valores": valores.copy(), "alumnos": salon}
    )

print("Registro finalizado.\n")

# Mostrar resultados
print("========== RESULTADOS ==========\n")

for s, data in enumerate(salones):
    tareas = data["tareas"]
    valores = data["valores"]
    salon = data["alumnos"]

    print()
    if len(salon) == 0:
        print(f"Salón {s + 1} vacío\n")
        continue

    print(f"- Salón {s + 1}: {len(salon)} alumnos -\n")
    print("{:<12}{:<15}{:<15}".format("Matrícula", "Nombre", "Carrera"), end="")
    for tarea in tareas:
        print("{:<10}{:<10}".format(tarea, "Valor"), end="")
    print("{:<10}".format("Promedio"))
    print("-" * 90)

    for alumno in salon:
        print(
            "{:<12}{:<15}{:<15}".format(
                alumno["matricula"], alumno["nombre"], alumno["carrera"]
            ),
            end="",
        )
        promedios.clear()
        for tarea in tareas:
            cal = alumno["calificaciones"][tarea]
            val = alumno["valores"][tarea]
            prom = alumno["promedio"][tarea]
            print("{:<10.1f}{:<10.1f}".format(cal, val), end="")
        total = sum(promedios)
        print("{:<10.2f}".format(total))
        print()

# Corrección: variable 'alumnos' no existía; se genera a partir de salones
alumnos = []
for s, data in enumerate(salones):
    for alumno in data["alumnos"]:
        promedio_final = promedio_cali(alumno["calificaciones"].values())
        alumnos.append(
            {
                "matricula": alumno["matricula"],
                "nombre": alumno["nombre"],
                "carrera": alumno["carrera"],
                "salon": s + 1,
                "promedio": round(promedio_final, 2),
            }
        )

# Guardar archivo CSV
with open("alumnos.csv", "w", newline="", encoding="utf-8") as archivo:
    campos = ["matricula", "nombre", "carrera", "salon", "promedio"]
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    writer.writerows(alumnos)

print(
    "Archivo 'alumnos.csv' listo en la misma carpeta del código.\n"
    "Puedes abrirlo en Excel o Google Sheets."
)
