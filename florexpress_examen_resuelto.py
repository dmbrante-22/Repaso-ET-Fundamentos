#########################################################################################
# Floreria FlorExpress
# arreglos = [nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada]
arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

# bodega = [precio, unidades]
bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
}
#########################################################################################
# FUNCIONES DE VALIDACION

def validarCodigo(codigo):
    codigo = codigo.upper().strip()
    if len(codigo) > 0 and codigo not in arreglos and codigo not in bodega:
        return True
    return False


def validarNombre(nombre):
    if len(nombre.strip()) > 0:
        return True
    return False


def validarTipo(tipo):
    if len(tipo.strip()) > 0:
        return True
    return False


def validarColorPrincipal(color_principal):
    if len(color_principal.strip()) > 0:
        return True
    return False


def validarTamano(tamano):
    tamano = tamano.upper().strip()
    if tamano == 'S' or tamano == 'M' or tamano == 'L':
        return True
    return False


def validarIncluyeTarjeta(incluye_tarjeta):
    incluye_tarjeta = incluye_tarjeta.lower().strip()
    if incluye_tarjeta == 's' or incluye_tarjeta == 'n':
        return True
    return False


def validarTemporada(temporada):
    if len(temporada.strip()) > 0:
        return True
    return False


def validarPrecio(precio):
    try:
        precio = int(precio)
        if precio > 0:
            return True
        return False
    except:
        return False


def validarUnidades(unidades):
    try:
        unidades = int(unidades)
        if unidades >= 0:
            return True
        return False
    except:
        return False

#########################################################################################
# FUNCIONES DEL PROGRAMA

def unidades_tipo(tipo):
    total = 0
    for codigo, datos in arreglos.items():
        if datos[1].lower() == tipo.lower().strip():
            total += bodega[codigo][1]
    print(f"El total de unidades disponibles es: {total}")


def busqueda_precio(p_min, p_max):
    lista = []
    for codigo, datos in bodega.items():
        precio = datos[0]
        unidades = datos[1]
        if precio >= p_min and precio <= p_max and unidades != 0:
            nombre = arreglos[codigo][0]
            lista.append(nombre + "--" + codigo)

    if len(lista) == 0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista.sort()
        print(f"Los arreglos encontrados son: {lista}")


def actualizar_precio(codigo, nuevo_precio):
    codigo = codigo.upper().strip()
    if codigo in bodega:
        bodega[codigo][0] = nuevo_precio
        return True
    return False


def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades):
    codigo = codigo.upper().strip()

    if codigo in arreglos or codigo in bodega:
        return False

    arreglos[codigo] = [nombre.strip(), tipo.strip(), color_principal.strip(), tamano.upper().strip(), incluye_tarjeta, temporada.strip()]
    bodega[codigo] = [precio, unidades]
    return True


def eliminar_arreglo(codigo):
    codigo = codigo.upper().strip()
    if codigo in arreglos and codigo in bodega:
        del arreglos[codigo]
        del bodega[codigo]
        return True
    return False

#########################################################################################
# MENU

def menu():
    print('''
========== MENÚ PRINCIPAL ==========
1. Unidades por tipo de arreglo
2. Búsqueda de arreglos por rango de precio
3. Actualizar precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
=====================================
''')


def seleccione():
    try:
        op = int(input("Ingrese opción: "))
        return op
    except:
        return 0

#########################################################################################
# PROGRAMA PRINCIPAL

while True:
    menu()
    op = seleccione()

    match op:
        case 1:
            tipo = input("Ingrese tipo de arreglo a consultar: ")
            unidades_tipo(tipo)

        case 2:
            while True:
                try:
                    p_min = int(input("Ingrese precio mínimo: "))
                    p_max = int(input("Ingrese precio máximo: "))

                    if p_min >= 0 and p_max >= 0 and p_min <= p_max:
                        busqueda_precio(p_min, p_max)
                        break
                    else:
                        print("Los precios deben ser mayores o iguales a cero y el mínimo no puede ser mayor al máximo")
                except:
                    print("Debe ingresar valores enteros")

        case 3:
            while True:
                try:
                    codigo = input("Ingrese código del arreglo: ").upper().strip()
                    nuevo_precio = int(input("Ingrese nuevo precio: "))

                    if nuevo_precio > 0:
                        if actualizar_precio(codigo, nuevo_precio) == True:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("El nuevo precio debe ser mayor a cero")
                except:
                    print("Debe ingresar un precio entero")

                while True:
                    resp = input("¿Desea actualizar otro precio (s/n)?: ").lower().strip()
                    if resp == 's' or resp == 'n':
                        break
                    else:
                        print("Debe responder s o n")

                if resp == 'n':
                    break

        case 4:
            codigo = input("Ingrese código del arreglo: ").upper().strip()
            nombre = input("Ingrese nombre: ")
            tipo = input("Ingrese tipo: ")
            color_principal = input("Ingrese color principal: ")
            tamano = input("Ingrese tamaño (S/M/L): ").upper().strip()
            incluye_tarjeta = input("¿Incluye tarjeta? (s/n): ").lower().strip()
            temporada = input("Ingrese temporada: ")
            precio = input("Ingrese precio: ")
            unidades = input("Ingrese unidades: ")

            if len(codigo.strip()) == 0:
                print("El código no puede estar vacío")
            elif validarCodigo(codigo) == False:
                print("El código ya existe")
            elif validarNombre(nombre) == False:
                print("El nombre no puede estar vacío")
            elif validarTipo(tipo) == False:
                print("El tipo no puede estar vacío")
            elif validarColorPrincipal(color_principal) == False:
                print("El color principal no puede estar vacío")
            elif validarTamano(tamano) == False:
                print("El tamaño debe ser S, M o L")
            elif validarIncluyeTarjeta(incluye_tarjeta) == False:
                print("Debe ingresar s o n en incluye tarjeta")
            elif validarTemporada(temporada) == False:
                print("La temporada no puede estar vacía")
            elif validarPrecio(precio) == False:
                print("El precio debe ser un entero mayor que cero")
            elif validarUnidades(unidades) == False:
                print("Las unidades deben ser un entero mayor o igual a cero")
            else:
                precio = int(precio)
                unidades = int(unidades)

                if incluye_tarjeta == 's':
                    incluye_tarjeta = True
                else:
                    incluye_tarjeta = False

                if agregar_arreglo(codigo, nombre, tipo, color_principal, tamano, incluye_tarjeta, temporada, precio, unidades) == True:
                    print("Arreglo agregado")
                else:
                    print("El código ya existe")

        case 5:
            codigo = input("Ingrese código del arreglo a eliminar: ").upper().strip()
            if eliminar_arreglo(codigo) == True:
                print("Arreglo eliminado")
            else:
                print("El código no existe")

        case 6:
            print("Programa finalizado.")
            break

        case _:
            print("Debe seleccionar una opción válida")
