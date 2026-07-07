#nombre, tipo, color_principal, tamaño, incluye_tarjeta, temporada
arreglos = {
'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

#precio, unidades
bodega = {
'FLO1': [15990, 8],
'FLO2': [29990, 3],
'FLO3': [9990, 12],
'FLO4': [24990, 5],
'FLO5': [19990, 0],
'FLO6': [22990, 6],
}

#################################################################
#VALIDACIONES
#################################################################
def validar_codigo(codigo):
    codigo=codigo.upper().strip()
    if codigo in arreglos:
        return False
    else:
        if len(codigo)>0:
            return True
        return False

def validar_nombre(nombre):
    nombre=nombre.strip()
    if len(nombre)>0:
        return True
    return False

def validar_tipo(tipo):
    tipo=tipo.strip().lower()
    if len(tipo)>0 and tipo in ('ramo','caja','centro'):
        return True
    return False

def validar_color_principal(color_principal):
    color_principal=color_principal.strip().lower()
    if len(color_principal)>0:
        return True
    return False

def validar_tamano(tamano):
    tamano=tamano.strip().upper()
    if tamano in ('S','M','L'):
        return True
    return False

def validar_incluye_tarjeta(incluye_tarjeta):
    incluye_tarjeta=incluye_tarjeta.lower().strip()
    if incluye_tarjeta in ('s','n'):
        return True
    return False

def validar_temporada(temporada):
    temporada=temporada.strip()
    if len(temporada)>0:
        return True
    return False

def validar_precio(precio):
    try:
        p=int(precio)
        if p>0:
            return True
        return False
    except ValueError:
        return False

def validar_unidades(unidades):
    try:
        u=int(unidades)
        if u>=0:
            return True
        return False
    except ValueError:
        return False

#################################################################
#FUNCIONES
#################################################################
def unidades_por_tipo(tipo):
    unidades=0
    for clave,valor in arreglos.items():
        if valor[1].lower()==tipo.strip().lower():
            unidades+=bodega[clave][1]
    print(f"El total de unidades por tipo {tipo} de arreglo es de: {unidades}")

def busqueda_precio(p_min,p_max):
    lista=[]
    for clave,valor in bodega.items():
        precio=valor[0]
        if p_min<=precio<=p_max and valor[1]>0:
            nombre=arreglos[clave][0]
            lista.append(nombre+'--'+clave)
    if len(lista)==0:
        print("No hay arreglos en ese rango de precios.")
    else:
        lista.sort()
        print(f"Los arreglos encontrados son: {lista}")

def actualizar_precio(nuevo_precio,codigo):
    codigo=codigo.upper().strip()
    if nuevo_precio in bodega:
        bodega[codigo][0]=nuevo_precio
        return True
    return False

def agregar_arreglo(codigo, nombre, tipo, color_principal, tamano,
                    incluye_tarjeta, temporada, precio, unidades):
    if codigo.upper().strip() in arreglos:
        return False
    
    if incluye_tarjeta=='s':
        tarjeta=True
    else:
        tarjeta=False
    
    arreglos[codigo]={
        nombre.capitalize(),
        tipo.strip().lower(),
        color_principal.strip().lower(),
        tamano.strip().upper(),
        tarjeta,
        temporada.strip().lower()
    }

    bodega[codigo]={
        int(precio),
        int(unidades)
    }
    return True

def eliminar_arreglo(codigo):
    codigo=codigo.upper().strip()
    if codigo in arreglos:
        del arreglos[codigo]
        del bodega[codigo]
        return True
    return False

#################################################################
#MENÚ
#################################################################
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
        op=int(input("Seleccione una opción (1-6): "))
        if op>=1 and op<=6:
            return op
        return 0
    except ValueError:
        return 0

#################################################################
#PROGRAMA PRINCIPAL
#################################################################

while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            tipo=input("Ingrese el tipo de arreglo (Ramo, Caja o Centro): ").lower()
            if validar_tipo(tipo)==True:
                unidades_por_tipo(tipo)
            else:
                print("El tipo no puede estar vacío y debe ser 'ramo', 'caja' o 'centro'.")

        case 2:
            while True:
                try:
                    p_min=int(input("Ingrese el valor mínimo: $"))
                    p_max=int(input("Ingrese el valor máximo: $"))
                    if p_min>=0 and p_max>=0 and p_min<=p_max:
                        busqueda_precio(p_min,p_max)
                        break
                except ValueError:
                    print("Debe ingresar valores enteros")
        
        case 3:
            while True:
                codigo=input("Ingrese código del arreglo a actualizar: ").upper().strip()
                if validar_codigo(codigo)==True:
                    try:
                        nuevo_precio=int(input("Ingrese nuevo precio que desea asignar: $"))
                        if nuevo_precio>0:
                            if actualizar_precio(nuevo_precio,codigo)==True:
                                print("Precio actualizado")
                            else:
                                print("El código no existe")
                        else:
                            print("El nuevo precio debe ser un valor entero positivo")
                    except ValueError:
                        print("Debe ingresar valores enteros")
                else:
                    print("El código debe tener el formato: FL01")
                
                resp=input("¿Desea actualizar otro precio (s/n)?: ").lower()
                if resp in ('s','n'):
                    if resp=='n':
                        break
                else:
                    print("Debe ingresar sólo 's' o 'n'")
                
        case 4:
            codigo=input("Ingrese nuevo código: ").upper().strip()
            if validar_codigo(codigo)==False:
                print("El código no debe estar vacío ni sólo espacios en blanco y además no debe existir en diccionarios")
                continue

            nombre=input("Ingrese nuevo nombre del arreglo: ")
            if validar_nombre(nombre)==False:
                print("No debe estar vacío ni ser sólo espacios en blanco")
                continue

            tipo=input("Ingrese el tipo de arreglo: ")
            if validar_tipo(tipo)==False:
                print("No debe estar vacío ni ser sólo espacios en blanco")
                continue
            
            color_principal=input("Ingrese cual va a ser el color principal: ")
            if validar_color_principal(color_principal)==False:
                print("No debe estar vacío ni ser sólo espacios en blanco")
                continue
            
            tamano=input("Ingrese el tamaño del arreglo ('S','M'o'L'): ").upper()
            if validar_tamano(tamano)==False:
                print("Debe ser exactamente 'S', 'M' o 'L'")
                continue
            
            incluye_tarjeta=input("¿Incluye Tarjeta? (s/n)").lower()
            if validar_incluye_tarjeta(incluye_tarjeta)==False:
                print("Debe ingresar sólo 's' o 'n'")
                continue
            
            temporada=input("Ingrese la temporada: ")
            if validar_temporada(temporada)==False:
                print("No debe estar vacío ni ser sólo espacios en blanco")
                continue

            precio=input("Ingrese el precio: ")
            if validar_precio(precio)==False:
                print("Debe ingresar un número entero mayor que cero")
                continue
            
            unidades=input("Ingrese las unidades: ")
            if validar_unidades==False:
                print("Debe ingresar un número entero mayor o igual a cero")
                continue
            
            resp=agregar_arreglo(codigo, nombre, tipo, color_principal, tamano,
                    incluye_tarjeta, temporada, precio, unidades)
            
            if resp==True:
                print("Arreglo agregado")
            else:
                print("El código ingresado ya existe")

        case 5:
            codigo=input("Ingrese el código del arreglo a eliminar: ").upper()
            if validar_codigo(codigo)==True:
                if eliminar_arreglo==True:
                    print("Arreglo eliminado")
                else:
                    print("El código no existe")                

        case 6:
            print("Programa finalizado - Dana")
            break
        case _:
            print("Debe seleccionar una opción válida")