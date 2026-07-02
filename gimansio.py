
#########################################################################################
# Gimnasio / Centro Deportivo
# Actividades = [nombre actividad, categoría, duración min, nivel, instructor, requiere equipamiento propio]
actividades = {
    'A01': ['Yoga Dinámico', 'Bienestar', 60, 'Principiante', 'Ana Gómez', False],
    'A02': ['Crossfit Pro', 'Fuerza', 50, 'Avanzado', 'Carlos Plaza', True],
    'A03': ['Pilates Reformer', 'Bienestar', 45, 'Intermedio', 'Elena Marín', False],
    'A04': ['Spinning HIIT', 'Cardio', 45, 'Intermedio', 'Luis Fuentes', False],
    'A05': ['Zumba Fitness', 'Cardio', 60, 'Principiante', 'Luis Fuentes', False],
}

# Comercial_Actividades = [valor mensualidad, cupos máximos por clase]
comercial_actividades = {
    'A01': [80000, 30],
    'A02': [70000, 20],
    'A03': [50000, 10],
    'A04': [43000, 10],
    'A05': [30000, 30],
}

#Como puedo saber cuántos cupos en matrícula tengo por un nivel en especial Ej:principiante

def cupos_por_nivel(nivel):
    cantidad=0
    for clave,valor in actividades.items(): #El metodo .items separa el diccionario en un strig (la clave) y una lista (el valor)
        if valor[3].lower()==nivel.lower():
            cantidad+=comercial_actividades[clave][1]
    print(f"La cantidad de cupos del nivel {nivel} es {cantidad}")

nivel=input("Ingrese el nivel a buscar: ")
cupos_por_nivel(nivel)

#Contar los cursos por categoría
def cursos_por_categoria(categoria):
    cantidad=0
    for clave,valor in actividades.items():
        if valor[1].lower()==categoria.lower():
            cantidad+=1
    if cantidad==0:
        print("No cuentas con cursos de esta categoría")
    else:
        print(f"Cuentas con {cantidad} cursos de la categoria {categoria}")

categoria=input("Ingrese la categoría a contabilizar: ")
cursos_por_categoria(categoria)

#Sumar los valores mensuales por duración
def valores_por_duración(minutos):
    suma=0
    for clave,valor in actividades.items(): #El metodo .items separa el diccionario en un strig (la clave) y una lista (el valor)
        if valor[2]==minutos:
            suma+=comercial_actividades[clave][0]
    if suma==0:
        print("No encontró cursos con esos minutos")
    else:
        print(f"Valores por duración: {suma}")

minutos=int(input("Ingrese la cantidad de minutos de la actividad: "))
valores_por_duración(minutos)

#contar la cantidad de cursos por un rango de valores 10000 y 50000
def cantidad_por_rango(v1,v2):
    cant=0
    for clave,valor in comercial_actividades.items():
        if valor[0]>=v1 and valor[0]<=v2:
            cant+=1
    if cant==0:
        print(f"No encontró cursos entre {v1} y {v2}")
    else:
        print(f"Encontré {cant} cursos entre los valores {v1} y {v2}")
        
v1=int(input("Ingrese el valor mínimo del rango: "))
v2=int(input("Ingrese el valor máximo del rango: "))
cantidad_por_rango(v1,v2)

#Como crear una lista con todos los cursos que se encuentren entre un rango de valores
#Se necesita Nombre-Precio_Cupos
#Ordenados por nombre de curso

def listado_cursos_rango_valores(v1,v2):
    lista=[] #Acá va a ir guardando los nombres del curso entre los valores que piden
    for clave,valor in comercial_actividades.items():
        if valor[0]>=v1 and valor[0]<=v2:
            nombre_curso=actividades[clave][0]
            lista.append([nombre_curso+"-"+str(valor[0])])
    if len(lista)==0:
        print(f"No existen cursos entre {v1} y {v2}")
    else:
        lista.sort() #ordenar de menor a mayor
        print(lista)
v1=int(input("Ingrese el valor mínimo del rango: "))
v2=int(input("Ingrese el valor máximo del rango: "))
listado_cursos_rango_valores(v1,v2)