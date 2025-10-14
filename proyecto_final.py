
tareas = []
resultados = []
promedios= []
valores= []

def promedio_cali(calificaciones):
  promedio_alumno=sum(calificaciones) / len(calificaciones)
  return promedio_alumno

num_salones=int(input("¿Cuántos salones quieres?: "))
print()
cont_alumnos=0
salones=[]
print("Registro de alumno y calculadora de calificaciones, si quieres terminar de programar en matricula presione 0")

for i in range(num_salones):
  print()
  print(f"Salon {i+1}")
  print()
  tareas=[]
  valores=[]
  salon=[]
  cant_alumnos=int(input("¿Cuántos alumnos quieres en este salón?: "))
  cont_alumnos+=1
  cant_tareas=int(input(f"Cuantas tareas vas a calificar para salon {i+1}: "))
  for t in range(cant_tareas):
    tarea=input(f"Ingresa nombre de la tarea {t+1}: ")
    tareas.append(tarea)
    valor=float(input(f"Ingresa el valor de la tarea {t+1}: "))
    valores.append(valor)
  if sum(valores)!=100:
    print("Los valores deben sumar 100")
    valores.clear()
    print()
    for t in range(cant_tareas):
      valor=int(input(f"Ingresa el valor de la tarea {t+1}: "))
      valores.append(valor)
      print()
  else:
    print("Valores regitrados")
    print()

  for j in range(cant_alumnos):
    print()
    print(f"Alumno {j+1}")
    print()
    matricula = float(input("Ingresa matrícula: "))
    nombre = input("Ingresa nombre: ")
    carrera = input("Ingresa carrera: ")
    print()
    alumno = {"matricula": matricula, "nombre": nombre, "carrera": carrera, "calificaciones": {}, "valores": {}}
    print(f"calificaciones para {nombre}")
    for tarea in tareas:
      while True:
        calificacion = float(input(f"Ingresa calificación para {tarea}, del 1 al 10: "))
        if 0 <= calificacion <= 10:
          alumno["calificaciones"][tarea] = calificacion
          alumno["valores"][tarea] = valores[tareas.index(tarea)]
          alumno["promedio"][tarea] = promedio_cali(alumno["calificaciones"])
          break
        else:
          print("La calificación debe estar entre 0 y 10.")
    salon.append(alumno)
  salones.append({"tareas": tareas.copy(), "valores": valores.copy(),"alumnos": salon})

print("Registro finalizado.")
print()

print("Resultados")
for s, data in enumerate(salones):
  tareas = data["tareas"]
  valores = data["valores"]
  salon = data["alumnos"]
  print()
  if len(salon)==0:
    print(f"Salon {s+1} vacío")
    print()
    continue
  print(f"-Salon {s+1}: {len(salon)} alumnos-")
  print()
  print("{:<12}{:<15}{:<15}".format("Matrícula", "Nombre", "Carrera"), end="")
  for tarea in tareas:
    print("{:<10}{:<10}".format(tarea, "Valor"), end="")
  print("{:<10}".format("Promedio"))
  print("-" * 90)
  for alumno in salon:
    print("{:<12}{:<15}{:<15}".format(alumno["matricula"], alumno["nombre"], alumno["carrera"]), end="")
    promedios.clear()
    for tarea in tareas:
      cal = alumno["calificaciones"][tarea]
      val = alumno["valores"][tarea]
      prom= alumno["promedio"][tarea]
      print("{:<10.1f}{:<10.1f}".format(cal, val), end="")
    total = sum(promedios)
    print("{:<10.2f}".format(total))
    print()
