#nombre, categoría, tiempo_estimado, mecanico_asignado, requiere_elevador
servicios = {
    'S101': ['Cambio de aceite', 'Mecánica', 45, 'Juan Pérez', True],
    'S102': ['Revisión de batería', 'Electricidad', 30, 'María Soto', False],
    'S103': ['Alineación', 'Mecánica', 60, 'Carlos Díaz', True],
    'S104': ['Reparación de abolladura', 'Desabolladura', 120, 'Pedro Rojas', False],
    'S105': ['Revisión de luces', 'Electricidad', 40, 'María Soto', False]
}

#costo_base, insumos_disponibles
inventario = {
    'S101': [45000, 10],
    'S102': [30000, 6],
    'S103': [55000, 0],
    'S104': [90000, 4],
    'S105': [25000, 8]
}

##########################################################################
#VALIDACIONES
##########################################################################
def validar_codigo(codigo):
    codigo=codigo.strip().upper()
    if len(codigo)>0:
        return True
    return False

def validar_nombre(nombre):
    nombre=nombre.strip()
    if len(nombre)>0:
        return True
    return False

def validar_categoria(categoria):
    categoria=categoria.strip().lower()
    if categoria in ('mecánica','electricidad','desabolladura'):
        return True
    return False

def validar_tiempo_estimado(tiempo_estimado):
    try:
        t=int(tiempo_estimado)
        if t>0:
            return True
        return False
    except ValueError:
        return False

def validar_mecanico_asginado(mecanico_asignado):
    mecanico_asignado=mecanico_asignado.strip()
    if len(mecanico_asignado)>0:
        return True
    return False

def validar_requiere_elevador(requiere_elevador):
    requiere_elevador=requiere_elevador.strip().lower()
    if requiere_elevador in ('n','s'):
        return True
    return False

def validar_costo_base(costo_base):
    try:
        c=int(costo_base)
        if c>0:
            return True
        return False
    except ValueError:
        return False

def validar_insumos_disponibles(insumos_disponibles):
    try:
        i=int(insumos_disponibles)
        if i >=0:
            return True
        return False
    except ValueError:
        return False
    
##########################################################################
#FUNCIONES
##########################################################################
def insumos_por_categoria(categoria):
    contar=0
    for clave,valor in servicios.items():
        cate=valor[1]
        if cate.lower()==categoria.strip().lower():
            contar+=inventario[clave][1]
   
    print(f"El total de insumos para la categoria de {categoria} es de {contar} unidades")

def buscar_por_costo(costo_max):
    lista=[]
    for clave,valor in inventario.items():
        NombreServicio=servicios[clave][0]
        costo=valor[0]
        insumos_disponibles=valor[1]
        if costo<=costo_max and insumos_disponibles>0:
            lista.append(NombreServicio+'--'+clave)
    if len(lista)==0:
        print("No hay servicios disponibles para ese presupuesto.")
    else:
        lista.sort()
        print(f"Según el presupuesto máximo de ${costo_max} los servicios disponibles son: {lista}")

def actualizar_costo(codigo,nuevo_costo):
    codigo=codigo.upper().strip()
    if codigo in inventario:
        inventario[codigo][0]=nuevo_costo
        return True
    return False

def agregar_servicio(codigo,nombre, categoría, tiempo_estimado, mecanico_asignado,
                     requiere_elevador,costo_base, insumos_disponibles):
    codigo=codigo.upper().strip()
    if codigo in servicios:
        return False
    
    if requiere_elevador.lower().strip()=='s':
        elevador=True
    else:
        elevador=False
    
    servicios[codigo]=[
        nombre.strip().capitalize(),
        categoría.strip().capitalize(),
        int(tiempo_estimado),
        mecanico_asignado.strip(),
        elevador
    ]

    inventario[codigo]=[
        int(costo_base),
        int(insumos_disponibles)
    ]

    return True

def dar_de_baja(codigo):
    codigo=codigo.upper().strip()
    if codigo in servicios:
        del servicios[codigo]
        del inventario[codigo]
        return True
    return False
    


##########################################################################
#MENÚ
##########################################################################
def menu():
    print('''
    1. Consultar insumos por categoría
    2. Filtrar servicios por costo máximo
    3. Actualizar costo de servicio
    4. Registrar nuevo servicio técnico
    5. Dar de baja un servicio
    6. Salir
          ''')

def seleccione():
    try:
        op=int(input("Seleccione una opción (1-6): "))
        if op>=1 and op<=6:
            return op
        return 0
    except ValueError:
        return 0

##########################################################################
#PROGRAMA PRINCIPAL
##########################################################################
while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            categoria=input("Ingrese una categoría (Mecánica,Electricidad, Desabolladura): ").lower()
            if validar_categoria(categoria)==True:
                insumos_por_categoria(categoria)
            else:
                print("Debe ser exactamente 'mecánica', 'electricidad' o 'desabolladura'.")
        
        case 2:
            try:
                costo_max=int(input("Ingrese un presupuesto máximo: $"))
                if costo_max>0:
                    buscar_por_costo(costo_max)
                else:
                    print("Debe ingresar un monto mayor a 0")
            except ValueError:
                print("Ingrese un número entero válido")
        
        case 3:
            while True:
                codigo=input("Ingrese el código a actualizar: ").upper()
                if validar_codigo(codigo)==True:
                    try:
                        nuevo_costo=int(input("Ingrese el nuevo valor monetario: $"))
                        if nuevo_costo>0:
                            if actualizar_costo(codigo,nuevo_costo)==True:
                                print("Valor Actualizado")
                            else:
                                print("El código no existe")
                        else:
                            print("El nuevo valor debe ser mayor a 0")
                    except ValueError:
                        print("El nuevo valor debe ser un número entero")

                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp == 'n':
                    break
        
        case 4:
            codigo=input("Ingrese el nuevo código: ").upper()
            if validar_codigo(codigo)==False:
                print("El código debe estar el formato 'S101'")
                continue

            nombre=input("Ingrese el tipo de mantenimiento (Ej: alineación o cambio de aceite)").lower()
            if validar_nombre(nombre)==False:
                print("No debe quedar vacío ni contener solo espacios.")
                continue

            categoria=input("Ingrese una categoría (Mecánica,Electricidad, Desabolladura): ").lower()
            if validar_categoria(categoria)==False:
                print("Debe ser exactamente 'mecánica', 'electricidad' o 'desabolladura'.")
                continue
            
            tiempo_estimado=input("Ingrese la duración de la tarea en minutos: ")
            if validar_tiempo_estimado(tiempo_estimado)==False:
                print("Debe ser un número entero mayor que cero.")
                continue
            
            mecanico_asignado=input("Ingrese el nombre del técnico a cargo: ")
            if validar_mecanico_asginado(mecanico_asignado)==False:
                print("No debe estar vacío ni contener solo espacios.")
                continue
            
            requiere_elevador=input("¿El auto debe subirse a una plataforma? (s/n): ").lower()
            if validar_requiere_elevador(requiere_elevador)==False:
                print("Debe ingresar 's' o 'n'")
                continue

            costo_base=input("Ingres el valor del servicio en pesos: $")
            if validar_costo_base(costo_base)==False:
                print("Debe ser un número entero mayor que cero")
                continue

            insumos_disponibles=input("Ingrese cantidad de kits de repuestos o insumos en bodega: ")
            if validar_insumos_disponibles(insumos_disponibles)==False:
                print("Debe ser un número entero mayor o igual a cero")
                continue

            resp=agregar_servicio(codigo, nombre, categoria, tiempo_estimado, mecanico_asignado,
                     requiere_elevador,costo_base, insumos_disponibles)
            
            if resp==False:
                print("El código ingresado ya se encuentra registrado.")
            else:
                print("Servicio registrado.")
        
        case 5:
            codigo=input("Ingrese el nuevo código: ").upper()
            if validar_codigo(codigo)==True:
                if dar_de_baja(codigo)==True:
                    print("Servicio eliminado correctamente")
                else:
                    print("El código ingresado no se encuentra registrado")

        case 6:
            print("Salir - Dana")
            break

        case _:
            print("Debe seleccionar una opción válida")