#########################################################################################
# Gimnasio / Centro Deportivo

actividades = {
    'A01': ['Yoga Dinámico', 'Bienestar', 60, 'Principiante', 'Ana Gómez', False],
    'A02': ['Crossfit Pro', 'Fuerza', 50, 'Avanzado', 'Carlos Plaza', True],
    'A03': ['Pilates Reformer', 'Bienestar', 45, 'Intermedio', 'Elena Marín', False],
    'A04': ['Spinning HIIT', 'Cardio', 45, 'Intermedio', 'Luis Fuentes', False],
    'A05': ['Zumba Fitness', 'Cardio', 60, 'Principiante', 'Luis Fuentes', False],
}

comercial_actividades = {
    'A01': [80000, 30],
    'A02': [70000, 20],
    'A03': [50000, 10],
    'A04': [43000, 10],
    'A05': [30000, 30],
}

def menu():
    print("\nMenu Principal")
    print("1. Cantidad de cupos por nivel")
    print("2. Filtrar actividades por valor mensual")
    print("3. Actualizar precio de actividad")
    print("4. Agregar actividad")
    print("5. Eliminar actividades")
    print("6. Salir")

def seleccione():
    try:
        op = int(input("Seleccione una opción: "))
        return op
    except:
        return 0

def cantidadCuporPorNivel(nivel):
    cant = 0

    for clave, valor in actividades.items():
        if valor[3].lower() == nivel.lower():
            cant += comercial_actividades[clave][1]

    if cant == 0:
        print("No existen actividades con este nivel")
    else:
        print(f"Existen {cant} cupos para actividades de nivel {nivel}")

def filtrarActividadPorValorMensualidad(minimo, maximo):
    lista = []

    for clave, valor in comercial_actividades.items():
        if valor[0] >= minimo and valor[0] <= maximo and valor[1] > 0:
            nombre = actividades[clave][0]
            categoria = actividades[clave][1]
            lista.append(nombre + " - " + categoria + " - $" + str(valor[0]))

    if len(lista) == 0:
        print("No existen actividades entre esos valores")
    else:
        lista.sort()
        for actividad in lista:
            print(actividad)

def actualizarPrecioPorCodigo(codigo, nuevoPrecio):
    if codigo in actividades:
        comercial_actividades[codigo][0] = nuevoPrecio
        return True
    return False

def eliminarPrecioPorCodigo(codigo):
    if codigo in actividades:
        del actividades[codigo]
        del comercial_actividades[codigo]
        return True
    return False

def agregarActividad(codigo, nombre, categoria, duracion, nivel, instructor, equipamiento, valor, cupos):
    if codigo in actividades:
        return False

    actividades[codigo] = [nombre, categoria, duracion, nivel, instructor, equipamiento]
    comercial_actividades[codigo] = [valor, cupos]

    return True

while True:
    menu()
    opcion = seleccione()

    match opcion:

        case 1:
            while True:
                nivel = input("Ingrese el nivel: ").strip()

                if len(nivel) > 0:
                    cantidadCuporPorNivel(nivel)
                else:
                    print("El nivel no puede estar vacío")
                resp = input("Desea repetir el proceso? (s/n): ").lower()
                if resp == "n":
                    break

        case 2:
            while True:
                try:
                    minimo = int(input("Ingrese valor mínimo: "))
                    maximo = int(input("Ingrese valor máximo: "))

                    if minimo < maximo and minimo > 0:
                        filtrarActividadPorValorMensualidad(minimo, maximo)
                    else:
                        print("El mínimo debe ser menor al máximo y mayor a cero")

                except:
                    print("Ingrese valores numéricos")

                resp = input("Desea repetir el proceso? (s/n): ").lower()
                if resp == "n":
                    break

        case 3:
            while True:
                try:
                    codigo = input("Ingrese código a modificar: ").strip().upper()
                    nuevoPrecio = int(input("Ingrese nuevo precio: "))

                    if nuevoPrecio > 0:
                        resp = actualizarPrecioPorCodigo(codigo, nuevoPrecio)

                        if resp == True:
                            print("Precio actualizado")
                        else:
                            print("Precio no actualizado, código no existe")
                    else:
                        print("El nuevo precio debe ser mayor a cero")

                except:
                    print("El precio debe ser numérico")

                resp = input("Desea continuar? (s/n): ").lower()
                if resp == "n":
                    break

        case 4:
            while True:
                try:
                    codigo = input("Ingrese código de la actividad: ").strip().upper()

                    if codigo in actividades:
                        print("El código ya existe")
                    else:
                        nombre = input("Ingrese nombre de la actividad: ").strip()
                        categoria = input("Ingrese categoría: ").strip()
                        duracion = int(input("Ingrese duración en minutos: "))
                        nivel = input("Ingrese nivel: ").strip()
                        instructor = input("Ingrese instructor: ").strip()

                        respuesta = input("¿Requiere equipamiento propio? (s/n): ").lower()

                        if respuesta == "s":
                            equipamiento = True
                        else:
                            equipamiento = False

                        valor = int(input("Ingrese valor mensualidad: "))
                        cupos = int(input("Ingrese cupos máximos: "))

                        if len(codigo) > 0 and len(nombre) > 0 and len(categoria) > 0 and len(nivel) > 0 and len(instructor) > 0:
                            if duracion > 0 and valor > 0 and cupos > 0:
                                resp = agregarActividad(codigo, nombre, categoria, duracion, nivel, instructor, equipamiento, valor, cupos)

                                if resp == True:
                                    print("Actividad agregada correctamente")
                                else:
                                    print("No se pudo agregar la actividad")
                            else:
                                print("Duración, valor y cupos deben ser mayores a cero")
                        else:
                            print("Los textos no pueden estar vacíos")

                except:
                    print("Error: duración, valor y cupos deben ser numéricos")

                resp = input("Desea continuar? (s/n): ").lower()
                if resp == "n":
                    break

        case 5:
            while True:
                codigo = input("Ingrese código a eliminar: ").strip().upper()

                resp = eliminarPrecioPorCodigo(codigo)

                if resp == True:
                    print("Eliminado")
                else:
                    print("No eliminado, código no existe")

                resp = input("Desea continuar? (s/n): ").lower()
                if resp == "n":
                    break

        case 6:
            print("Adiós...")
            break

        case _:
            print("Opción no válida")
