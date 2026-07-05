################################################################################
# SISTEMA DE GESTIÓN DE CURSOS ONLINE - EDUTECH
#
# cursos = [nombre, área, horas_totales, nivel, tutor, certificación_oficial]
# comercial = [valor_matricula, cupos_maximos]
################################################################################

cursos = {
    'C01': ['Python desde Cero', 'Tecnología', 40, 'Principiante', 'Marta Rivas', True],
    'C02': ['Finanzas Personales', 'Negocios', 20, 'Principiante', 'Pedro Soto', False],
    'C03': ['UI/UX Avanzado', 'Diseño', 60, 'Avanzado', 'Lucía López', True],
    'C04': ['Análisis de Datos', 'Tecnología', 50, 'Intermedio', 'Marta Rivas', True]
}

comercial = {
    'C01': [52000, 30],
    'C02': [70000, 25],
    'C03': [62000, 28],
    'C04': [152000, 20]
}


################################################################################
# VALIDACIONES
# Cada función de validación retorna solamente True o False.
################################################################################

def validar_codigo(codigo):
    codigo = codigo.strip()

    # Se usa el formato mostrado en el ejercicio: C01, C02, etc.
    if len(codigo) == 3 and codigo[0].upper() == 'C' and codigo[1:].isdigit():
        return True
    return False


def validar_nombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    return False


def validar_area(area):
    if area.strip().lower() in ('tecnología', 'negocios', 'diseño'):
        return True
    return False


def validar_horas(horas):
    try:
        horas_convertidas = int(horas)

        if horas_convertidas > 0:
            return True
        return False

    except ValueError:
        return False


def validar_nivel(nivel):
    if nivel.strip().lower() in ('principiante', 'intermedio', 'avanzado'):
        return True
    return False


def validar_tutor(tutor):
    if len(tutor.strip()) > 0:
        return True
    return False


def validar_certificacion(certificacion):
    if certificacion.strip().lower() in ('s', 'n'):
        return True
    return False


def validar_precio(precio):
    try:
        precio_convertido = int(precio)

        if precio_convertido > 0:
            return True
        return False

    except ValueError:
        return False


def validar_cupos(cupos):
    try:
        cupos_convertidos = int(cupos)

        # El enunciado permite que los cupos sean iguales a cero.
        if cupos_convertidos >= 0:
            return True
        return False

    except ValueError:
        return False


################################################################################
# FUNCIONES DEL SISTEMA
################################################################################

def cupos_por_area(area):
    total_cupos = 0

    for codigo, datos_curso in cursos.items():
        area_curso = datos_curso[1]

        if area_curso.lower() == area.strip().lower():
            total_cupos += comercial[codigo][1]

    print(f"Total de cupos disponibles para el área {area}: {total_cupos}")


def buscar_cursos_avanzado(precio_max, nivel):
    lista_cursos = []

    for codigo, datos_comerciales in comercial.items():
        precio = datos_comerciales[0]
        cupos = datos_comerciales[1]
        nivel_curso = cursos[codigo][3]

        if precio <= precio_max and cupos > 0:
            if nivel_curso.lower() == nivel.strip().lower():
                nombre_curso = cursos[codigo][0]
                lista_cursos.append(nombre_curso + "--" + codigo)

    if len(lista_cursos) == 0:
        print("No hay cursos disponibles para esos criterios.")
    else:
        lista_cursos.sort()
        print(f"Cursos disponibles: {lista_cursos}")


def actualizar_matricula(codigo, nuevo_precio):
    codigo = codigo.strip().upper()

    if codigo in comercial:
        comercial[codigo][0] = nuevo_precio
        return True
    return False


def agregar_curso(codigo, nombre, area, horas, nivel, tutor,
                  certificacion, precio, cupos):

    codigo = codigo.strip().upper()

    # Un código repetido no puede volver a registrarse.
    if codigo in cursos:
        return False

    if certificacion.strip().lower() == 's':
        certificacion_oficial = True
    else:
        certificacion_oficial = False

    cursos[codigo] = [
        nombre.strip(),
        area.strip().capitalize(),
        int(horas),
        nivel.strip().capitalize(),
        tutor.strip(),
        certificacion_oficial
    ]

    comercial[codigo] = [
        int(precio),
        int(cupos)
    ]

    return True


def eliminar_curso(codigo):
    codigo = codigo.strip().upper()

    if codigo in cursos:
        del cursos[codigo]
        del comercial[codigo]
        return True
    return False


def horas_por_tutor(nombre_tutor):
    total_horas = 0

    for codigo, datos_curso in cursos.items():
        tutor_curso = datos_curso[4]

        if tutor_curso.lower() == nombre_tutor.lower():
            total_horas += datos_curso[2]
    if total_horas==0:
        print("Tutor no encontrado")
    else:
        print(f"Total de horas dictadas por {nombre_tutor}: {total_horas}")


################################################################################
# MENÚ
################################################################################

def mostrar_menu():
    print('''
========== GESTIÓN EDUTECH ==========
1. Total cupos disponibles por área
2. Buscar cursos por presupuesto y nivel
3. Modificar valor de matrícula
4. Registrar nuevo curso en catálogo
5. Dar de baja un curso
6. Reporte de horas por tutor
7. Salir
=====================================
''')


def seleccionar_opcion():
    try:
        opcion = int(input("Seleccione una opción (1-7): "))

        if opcion >= 1 and opcion <= 7:
            return opcion
        return 0

    except ValueError:
        return 0


################################################################################
# PROGRAMA PRINCIPAL
################################################################################

while True:
    mostrar_menu()
    opcion = seleccionar_opcion()

    match opcion:

        case 1:
            area = input("Ingrese un área (Tecnología, Negocios o Diseño): ")

            if validar_area(area) == True:
                cupos_por_area(area)
            else:
                print("El área ingresada no es válida.")

        case 2:
            try:
                precio_max = int(input("Ingrese el presupuesto máximo: "))

                if precio_max > 0:
                    nivel = input("Ingrese el nivel (Principiante, Intermedio o Avanzado): ")

                    if validar_nivel(nivel) == True:
                        buscar_cursos_avanzado(precio_max, nivel)
                    else:
                        print("El nivel ingresado no es válido.")
                else:
                    print("El presupuesto debe ser un número entero mayor que cero.")

            except ValueError:
                print("El presupuesto debe ser un número entero.")

        case 3:
            while True:
                codigo = input("Ingrese el código del curso: ")

                try:
                    nuevo_precio = int(input("Ingrese el nuevo valor de matrícula: "))

                    if nuevo_precio > 0:
                        if actualizar_matricula(codigo, nuevo_precio) == True:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El nuevo precio debe ser mayor que cero.")

                except ValueError:
                    print("El nuevo precio debe ser un número entero.")

                respuesta = input("¿Desea repetir el proceso? (s/n): ").lower()

                if respuesta in ('n', 'no'):
                    break

        case 4:
            codigo = input("Ingrese el código del curso: ").upper()

            if validar_codigo(codigo) == False:
                print("El código debe tener el formato C01.")
                continue

            nombre = input("Ingrese el nombre del curso: ")

            if validar_nombre(nombre) == False:
                print("El nombre no puede estar vacío.")
                continue

            area = input("Ingrese el área (Tecnología, Negocios o Diseño): ")

            if validar_area(area) == False:
                print("El área ingresada no es válida.")
                continue

            horas = input("Ingrese las horas totales del curso: ")

            if validar_horas(horas) == False:
                print("Las horas deben ser un número entero mayor que cero.")
                continue

            nivel = input(
                "Ingrese el nivel (Principiante, Intermedio o Avanzado): "
            )

            if validar_nivel(nivel) == False:
                print("El nivel ingresado no es válido.")
                continue

            tutor = input("Ingrese el nombre del tutor: ")

            if validar_tutor(tutor) == False:
                print("El nombre del tutor no puede estar vacío.")
                continue

            certificacion = input(
                "¿El curso entrega certificación oficial? (s/n): "
            )

            if validar_certificacion(certificacion) == False:
                print("Debe ingresar solamente s o n.")
                continue

            precio = input("Ingrese el valor de la matrícula: ")

            if validar_precio(precio) == False:
                print("El precio debe ser un número entero mayor que cero.")
                continue

            cupos = input("Ingrese la cantidad de cupos máximos: ")

            if validar_cupos(cupos) == False:
                print("Los cupos deben ser un número entero mayor o igual a cero.")
                continue

            resultado = agregar_curso(
                codigo,
                nombre,
                area,
                horas,
                nivel,
                tutor,
                certificacion,
                precio,
                cupos
            )

            if resultado == True:
                print("Curso registrado")
                print(cursos)
                print(comercial)
            else:
                print("El código ya existe. El curso no fue registrado.")

        case 5:
            codigo = input("Ingrese el código del curso que desea eliminar: ")

            if eliminar_curso(codigo) == True:
                print("Curso eliminado")
            else:
                print("El código no existe")

        case 6:
            nombre_tutor = input("Ingrese el nombre del tutor: ")

            if validar_tutor(nombre_tutor) == True:
                horas_por_tutor(nombre_tutor)
            else:
                print("El nombre del tutor no puede estar vacío.")

        case 7:
            print("Programa finalizado.")
            break

        case _:
            print("Debe seleccionar una opción válida")
