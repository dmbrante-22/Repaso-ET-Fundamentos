#########################################################################################
# EXAMEN TRANSVERSAL - FUNDAMENTOS DE PROGRAMACION
# Gimnasio / Centro Deportivo
# Actividades = [nombre actividad, categoria, duracion min, nivel, instructor, requiere equipamiento propio]
# Comercial_Actividades = [valor mensualidad, cupos maximos por clase]
#########################################################################################

actividades = {
    'A01': ['Yoga Dinamico', 'Bienestar', 60, 'Principiante', 'Ana Gomez', False],
    'A02': ['Crossfit Pro', 'Fuerza', 50, 'Avanzado', 'Carlos Plaza', True],
    'A03': ['Pilates Reformer', 'Bienestar', 45, 'Intermedio', 'Elena Marin', False],
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

niveles_validos = ['Principiante', 'Intermedio', 'Avanzado']

#########################################################################################
# FUNCIONES DE VALIDACION Y LECTURA DE DATOS
#########################################################################################

def leer_entero(mensaje):
    # Lee un numero entero usando ValueError para controlar errores.
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print('Error: debe ingresar un numero entero.')


def leer_positivo(mensaje):
    # Lee un numero entero positivo, mayor que cero.
    while True:
        numero = leer_entero(mensaje)
        if numero > 0:
            return numero
        else:
            print('Error: el numero debe ser mayor que cero.')


def leer_texto(mensaje):
    # Lee un texto no vacio.
    while True:
        texto = input(mensaje).strip()
        if len(texto) > 0:
            return texto
        else:
            print('Error: el texto no puede estar vacio.')


def leer_texto_letras(mensaje):
    # Lee un texto que debe contener solo letras y espacios.
    while True:
        texto = input(mensaje).strip()
        valido = True

        if len(texto) == 0:
            valido = False
        else:
            for letra in texto:
                if letra.isalpha() == False and letra != ' ':
                    valido = False

        if valido == True:
            return texto.title()
        else:
            print('Error: debe ingresar solo letras y espacios.')


def leer_nivel():
    # Valida que el nivel ingresado sea uno de los permitidos.
    while True:
        nivel = input('Ingrese nivel (Principiante/Intermedio/Avanzado): ').strip().title()
        if nivel in niveles_validos:
            return nivel
        else:
            print('Error: nivel no valido.')


def leer_sn(mensaje):
    # Valida respuestas S/N.
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta == 's' or respuesta == 'n':
            return respuesta
        else:
            print('Error: debe responder solo S o N.')


def validar_codigo(codigo):
    # Valida formato de codigo: A01, A02, A06, A15, etc.
    if len(codigo) == 3:
        if codigo[0].upper() == 'A' and codigo[1:].isdigit():
            return True
    return False


def leer_codigo(mensaje):
    # Lee y valida el formato del codigo.
    while True:
        codigo = input(mensaje).strip().upper()
        if validar_codigo(codigo) == True:
            return codigo
        else:
            print('Error: el codigo debe tener formato A01, A02, A06, etc.')

#########################################################################################
# FUNCIONES PRINCIPALES DEL PROGRAMA
#########################################################################################

def menu():
    print('\n========== MENU PRINCIPAL ==========')
    print('1. Cantidad de cupos por nivel')
    print('2. Filtrar actividades por valor mensual')
    print('3. Actualizar precio de actividad')
    print('4. Agregar actividad')
    print('5. Eliminar actividad')
    print('6. Buscar actividad por codigo')
    print('7. Mostrar todas las actividades')
    print('8. Salir')


def seleccionar_opcion():
    # Lee la opcion del menu.
    return leer_entero('Seleccione una opcion: ')


def buscar_actividad_por_codigo(codigo):
    # Busca si una actividad existe segun su codigo.
    if codigo in actividades:
        return True
    return False


def mostrar_tabla_encabezado():
    print('-' * 105)
    print(f"{'CODIGO':<8}{'NOMBRE':<22}{'CATEGORIA':<15}{'DURACION':<12}{'NIVEL':<15}{'INSTRUCTOR':<18}{'VALOR':<10}{'CUPOS':<8}")
    print('-' * 105)


def mostrar_actividad(codigo):
    # Muestra una actividad en formato de tabla.
    datos = actividades[codigo]
    comercial = comercial_actividades[codigo]

    print(f"{codigo:<8}{datos[0]:<22}{datos[1]:<15}{datos[2]:<12}{datos[3]:<15}{datos[4]:<18}{comercial[0]:<10}{comercial[1]:<8}")


def mostrar_todas_las_actividades():
    if len(actividades) == 0:
        print('No hay actividades registradas.')
    else:
        mostrar_tabla_encabezado()
        for codigo in actividades:
            mostrar_actividad(codigo)
        print('-' * 105)


def cantidad_cupos_por_nivel(nivel):
    # Suma los cupos de todas las actividades que tienen el nivel indicado.
    cant = 0

    for codigo, datos in actividades.items():
        if datos[3] == nivel:
            cant = cant + comercial_actividades[codigo][1]

    if cant == 0:
        print('No existen actividades con este nivel.')
    else:
        print(f'Existen {cant} cupos para actividades de nivel {nivel}.')


def filtrar_actividades_por_valor(minimo, maximo):
    # Filtra actividades entre un valor minimo y maximo.
    encontrados = 0

    for codigo, comercial in comercial_actividades.items():
        valor = comercial[0]
        cupos = comercial[1]

        if valor >= minimo and valor <= maximo and cupos > 0:
            if encontrados == 0:
                mostrar_tabla_encabezado()
            mostrar_actividad(codigo)
            encontrados = encontrados + 1

    if encontrados == 0:
        print('No existen actividades entre esos valores.')
    else:
        print('-' * 105)


def actualizar_precio_por_codigo(codigo, nuevo_precio):
    # Actualiza el valor mensual de una actividad existente.
    if buscar_actividad_por_codigo(codigo) == True:
        comercial_actividades[codigo][0] = nuevo_precio
        return True
    return False


def agregar_actividad(codigo, nombre, categoria, duracion, nivel, instructor, equipamiento, valor, cupos):
    # Agrega una nueva actividad a ambos diccionarios.
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
# FUNCIONES DE CADA OPCION DEL MENU
#########################################################################################

def opcion_cupos_por_nivel():
    while True:
        nivel = leer_nivel()
        cantidad_cupos_por_nivel(nivel)

        repetir = leer_sn('Desea repetir el proceso? (s/n): ')
        if repetir == 'n':
            break


def opcion_filtrar_por_valor():
    while True:
        minimo = leer_positivo('Ingrese valor minimo: ')
        maximo = leer_positivo('Ingrese valor maximo: ')

        if minimo < maximo:
            filtrar_actividades_por_valor(minimo, maximo)
        else:
            print('Error: el minimo debe ser menor que el maximo.')

        repetir = leer_sn('Desea repetir el proceso? (s/n): ')
        if repetir == 'n':
            break


def opcion_actualizar_precio():
    while True:
        codigo = leer_codigo('Ingrese codigo a modificar: ')
        nuevo_precio = leer_positivo('Ingrese nuevo precio: ')

        respuesta = actualizar_precio_por_codigo(codigo, nuevo_precio)

        if respuesta == True:
            print('Precio actualizado correctamente.')
        else:
            print('Precio no actualizado. El codigo no existe.')

        repetir = leer_sn('Desea continuar? (s/n): ')
        if repetir == 'n':
            break


def opcion_agregar_actividad():
    while True:
        codigo = leer_codigo('Ingrese codigo de la nueva actividad: ')

        if buscar_actividad_por_codigo(codigo) == True:
            print('Error: el codigo ya existe.')
        else:
            nombre = leer_texto('Ingrese nombre de la actividad: ')
            categoria = leer_texto_letras('Ingrese categoria: ')
            duracion = leer_positivo('Ingrese duracion en minutos: ')
            nivel = leer_nivel()
            instructor = leer_texto_letras('Ingrese instructor: ')
            respuesta_equipamiento = leer_sn('Requiere equipamiento propio? (s/n): ')

            if respuesta_equipamiento == 's':
                equipamiento = True
            else:
                equipamiento = False

            valor = leer_positivo('Ingrese valor mensualidad: ')
            cupos = leer_positivo('Ingrese cupos maximos: ')

            respuesta = agregar_actividad(codigo, nombre, categoria, duracion, nivel, instructor, equipamiento, valor, cupos)

            if respuesta == True:
                print('Actividad agregada correctamente.')
            else:
                print('No se pudo agregar la actividad.')

        repetir = leer_sn('Desea continuar? (s/n): ')
        if repetir == 'n':
            break


def opcion_eliminar_actividad():
    while True:
        codigo = leer_codigo('Ingrese codigo a eliminar: ')

        if buscar_actividad_por_codigo(codigo) == True:
            mostrar_tabla_encabezado()
            mostrar_actividad(codigo)
            print('-' * 105)
            confirmar = leer_sn('Esta seguro que desea eliminar esta actividad? (s/n): ')

            if confirmar == 's':
                respuesta = eliminar_actividad_por_codigo(codigo)
                if respuesta == True:
                    print('Actividad eliminada correctamente.')
                else:
                    print('No se pudo eliminar la actividad.')
            else:
                print('Eliminacion cancelada.')
        else:
            print('No existe una actividad con ese codigo.')

        repetir = leer_sn('Desea continuar? (s/n): ')
        if repetir == 'n':
            break


def opcion_buscar_actividad():
    while True:
        codigo = leer_codigo('Ingrese codigo a buscar: ')

        if buscar_actividad_por_codigo(codigo) == True:
            mostrar_tabla_encabezado()
            mostrar_actividad(codigo)
            print('-' * 105)
        else:
            print('No existe una actividad con ese codigo.')

        repetir = leer_sn('Desea continuar? (s/n): ')
        if repetir == 'n':
            break

#########################################################################################
# PROGRAMA PRINCIPAL
#########################################################################################

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
            opcion_buscar_actividad()

        case 7:
            mostrar_todas_las_actividades()

        case 8:
            print('Adios...')
            break

        case _:
            print('Opcion no valida.')
