#########################################################################################
# Gimnasio / Centro Deportivo
# Versión preparada según pauta de evaluación transversal FPY1101
# Contiene: variables, entrada/salida, operaciones, condicionales, ciclos,
# excepciones, listas/diccionarios, funciones e integración desde programa principal.
#########################################################################################

# Diccionario principal:
# clave = código de actividad
# valor = [nombre, categoría, duración, nivel, instructor, requiere equipamiento propio]
actividades = {
    'A01': ['Yoga Dinámico', 'Bienestar', 60, 'Principiante', 'Ana Gómez', False],
    'A02': ['Crossfit Pro', 'Fuerza', 50, 'Avanzado', 'Carlos Plaza', True],
    'A03': ['Pilates Reformer', 'Bienestar', 45, 'Intermedio', 'Elena Marín', False],
    'A04': ['Spinning HIIT', 'Cardio', 45, 'Intermedio', 'Luis Fuentes', False],
    'A05': ['Zumba Fitness', 'Cardio', 60, 'Principiante', 'Luis Fuentes', False],
}

# Diccionario comercial:
# clave = código de actividad
# valor = [valor mensualidad, cupos máximos]
comercial_actividades = {
    'A01': [80000, 30],
    'A02': [70000, 20],
    'A03': [50000, 10],
    'A04': [43000, 10],
    'A05': [30000, 30],
}

niveles_validos = ['Principiante', 'Intermedio', 'Avanzado']

#########################################################################################
# FUNCIONES DE VALIDACIÓN Y LECTURA
#########################################################################################

def leer_entero(mensaje):
    # Esta función valida que el usuario ingrese un número entero.
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print('Error: debe ingresar un número entero.')


def leer_positivo(mensaje):
    # Esta función valida que el número sea mayor que cero.
    while True:
        numero = leer_entero(mensaje)
        if numero > 0:
            return numero
        else:
            print('Error: el número debe ser mayor que cero.')


def leer_texto(mensaje):
    # Esta función valida que el texto no quede vacío.
    while True:
        texto = input(mensaje).strip()
        if len(texto) > 0:
            return texto
        else:
            print('Error: el texto no puede estar vacío.')


def leer_texto_solo_letras(mensaje):
    # Valida textos con letras y espacios. Permite tildes porque isalpha las reconoce.
    while True:
        texto = leer_texto(mensaje)
        valido = True

        for caracter in texto:
            if caracter != ' ' and caracter.isalpha() == False:
                valido = False

        if valido == True:
            return texto
        else:
            print('Error: debe ingresar solo letras y espacios.')


def leer_sn(mensaje):
    # Esta función valida respuestas de tipo S/N.
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == 's' or respuesta == 'n':
            return respuesta
        else:
            print('Error: debe responder con s o n.')


def leer_nivel():
    # Esta función valida que el nivel exista dentro de los niveles permitidos.
    while True:
        nivel = leer_texto('Ingrese nivel (Principiante/Intermedio/Avanzado): ').capitalize()

        if nivel in niveles_validos:
            return nivel
        else:
            print('Error: nivel no válido.')


def validar_formato_codigo(codigo):
    # El código debe tener formato A01, A02, A06, etc.
    if len(codigo) == 3:
        if codigo[0] == 'A' and codigo[1:].isdigit():
            return True
    return False


def leer_codigo(mensaje):
    # Lee y valida el formato del código.
    while True:
        codigo = input(mensaje).strip().upper()
        if validar_formato_codigo(codigo) == True:
            return codigo
        else:
            print('Error: el código debe tener formato A01, A02, A06, etc.')

#########################################################################################
# FUNCIONES DE BÚSQUEDA Y MOSTRAR DATOS
#########################################################################################

def buscar_actividad_por_codigo(codigo):
    # Retorna True si la actividad existe en ambos diccionarios.
    if codigo in actividades and codigo in comercial_actividades:
        return True
    return False


def mostrar_tabla_actividades():
    # Muestra las actividades en una tabla ordenada.
    print('\nLISTADO DE ACTIVIDADES')
    print('-' * 105)
    print(f"{'Código':<8}{'Nombre':<22}{'Categoría':<15}{'Duración':<10}{'Nivel':<15}{'Precio':<12}{'Cupos':<8}")
    print('-' * 105)

    for codigo, datos in actividades.items():
        nombre = datos[0]
        categoria = datos[1]
        duracion = datos[2]
        nivel = datos[3]
        precio = comercial_actividades[codigo][0]
        cupos = comercial_actividades[codigo][1]

        print(f"{codigo:<8}{nombre:<22}{categoria:<15}{duracion:<10}{nivel:<15}${precio:<11}{cupos:<8}")

    print('-' * 105)

#########################################################################################
# FUNCIONES DEL PROBLEMA
#########################################################################################

def cantidad_cupos_por_nivel(nivel):
    # Suma los cupos máximos de todas las actividades que correspondan al nivel ingresado.
    cantidad = 0

    for codigo, datos in actividades.items():
        if datos[3] == nivel:
            cantidad = cantidad + comercial_actividades[codigo][1]

    if cantidad == 0:
        print('No existen actividades con este nivel.')
    else:
        print(f'Existen {cantidad} cupos para actividades de nivel {nivel}.')


def filtrar_actividades_por_valor(minimo, maximo):
    # Guarda en una lista las actividades cuyo valor esté dentro del rango ingresado.
    lista = []

    for codigo, datos_comerciales in comercial_actividades.items():
        precio = datos_comerciales[0]
        cupos = datos_comerciales[1]

        if precio >= minimo and precio <= maximo and cupos > 0:
            nombre = actividades[codigo][0]
            categoria = actividades[codigo][1]
            nivel = actividades[codigo][3]
            lista.append([codigo, nombre, categoria, nivel, precio, cupos])

    if len(lista) == 0:
        print('No existen actividades entre esos valores.')
    else:
        lista.sort()
        print('\nACTIVIDADES ENCONTRADAS')
        print('-' * 85)
        print(f"{'Código':<8}{'Nombre':<22}{'Categoría':<15}{'Nivel':<15}{'Precio':<12}{'Cupos':<8}")
        print('-' * 85)

        for actividad in lista:
            print(f"{actividad[0]:<8}{actividad[1]:<22}{actividad[2]:<15}{actividad[3]:<15}${actividad[4]:<11}{actividad[5]:<8}")

        print('-' * 85)


def actualizar_precio_por_codigo(codigo, nuevo_precio):
    # Actualiza el precio de una actividad si el código existe.
    if buscar_actividad_por_codigo(codigo) == True:
        comercial_actividades[codigo][0] = nuevo_precio
        return True
    return False


def agregar_actividad(codigo, nombre, categoria, duracion, nivel, instructor, equipamiento, valor, cupos):
    # Agrega una nueva actividad en ambos diccionarios.
    if buscar_actividad_por_codigo(codigo) == True:
        return False

    actividades[codigo] = [nombre, categoria, duracion, nivel, instructor, equipamiento]
    comercial_actividades[codigo] = [valor, cupos]
    return True


def eliminar_actividad_por_codigo(codigo):
    # Elimina una actividad de ambos diccionarios.
    if buscar_actividad_por_codigo(codigo) == True:
        del actividades[codigo]
        del comercial_actividades[codigo]
        return True
    return False

#########################################################################################
# FUNCIONES PARA CADA OPCIÓN DEL MENÚ
#########################################################################################

def opcion_cupos_por_nivel():
    while True:
        nivel = leer_nivel()
        cantidad_cupos_por_nivel(nivel)

        respuesta = leer_sn('¿Desea repetir el proceso? (s/n): ')
        if respuesta == 'n':
            break


def opcion_filtrar_por_valor():
    while True:
        minimo = leer_positivo('Ingrese valor mínimo: ')
        maximo = leer_positivo('Ingrese valor máximo: ')

        if minimo < maximo:
            filtrar_actividades_por_valor(minimo, maximo)
        else:
            print('Error: el valor mínimo debe ser menor al valor máximo.')

        respuesta = leer_sn('¿Desea repetir el proceso? (s/n): ')
        if respuesta == 'n':
            break


def opcion_actualizar_precio():
    while True:
        codigo = leer_codigo('Ingrese código a modificar: ')
        nuevo_precio = leer_positivo('Ingrese nuevo precio: ')

        resultado = actualizar_precio_por_codigo(codigo, nuevo_precio)

        if resultado == True:
            print('Precio actualizado correctamente.')
        else:
            print('No se pudo actualizar. El código no existe.')

        respuesta = leer_sn('¿Desea continuar? (s/n): ')
        if respuesta == 'n':
            break


def opcion_agregar_actividad():
    while True:
        codigo = leer_codigo('Ingrese código de la nueva actividad: ')

        if buscar_actividad_por_codigo(codigo) == True:
            print('Error: el código ya existe.')
        else:
            nombre = leer_texto('Ingrese nombre de la actividad: ')
            categoria = leer_texto_solo_letras('Ingrese categoría: ')
            duracion = leer_positivo('Ingrese duración en minutos: ')
            nivel = leer_nivel()
            instructor = leer_texto_solo_letras('Ingrese nombre del instructor: ')

            respuesta_equipo = leer_sn('¿Requiere equipamiento propio? (s/n): ')
            if respuesta_equipo == 's':
                equipamiento = True
            else:
                equipamiento = False

            valor = leer_positivo('Ingrese valor mensualidad: ')
            cupos = leer_positivo('Ingrese cupos máximos: ')

            resultado = agregar_actividad(codigo, nombre, categoria, duracion, nivel, instructor, equipamiento, valor, cupos)

            if resultado == True:
                print('Actividad agregada correctamente.')
            else:
                print('No se pudo agregar la actividad.')

        respuesta = leer_sn('¿Desea continuar? (s/n): ')
        if respuesta == 'n':
            break


def opcion_eliminar_actividad():
    while True:
        codigo = leer_codigo('Ingrese código a eliminar: ')
        resultado = eliminar_actividad_por_codigo(codigo)

        if resultado == True:
            print('Actividad eliminada correctamente.')
        else:
            print('No se pudo eliminar. El código no existe.')

        respuesta = leer_sn('¿Desea continuar? (s/n): ')
        if respuesta == 'n':
            break

#########################################################################################
# MENÚ PRINCIPAL
#########################################################################################

def menu():
    print('\nMENÚ PRINCIPAL')
    print('1. Cantidad de cupos por nivel')
    print('2. Filtrar actividades por valor mensual')
    print('3. Actualizar precio de actividad')
    print('4. Agregar actividad')
    print('5. Eliminar actividad')
    print('6. Mostrar todas las actividades')
    print('7. Salir')


def seleccionar_opcion():
    try:
        opcion = int(input('Seleccione una opción: '))
        return opcion
    except ValueError:
        return 0


def programa_principal():
    # El programa principal integra todas las funciones mediante match/case.
    while True:
        menu()
        opcion = seleccionar_opcion()

        match opcion:
            case 1:
                opcion_cupos_por_nivel()
            case 2:
                opcion_filtrar_por_valor()
            case 3:
                opcion_actualizar_precio()
            case 4:
                opcion_agregar_actividad()
            case 5:
                opcion_eliminar_actividad()
            case 6:
                mostrar_tabla_actividades()
            case 7:
                print('Adiós...')
                break
            case _:
                print('Opción no válida.')


programa_principal()
