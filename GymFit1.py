#nombre,intensidad,duracion_min,instructor,es_online
clases = {
    'C101': ['Yoga Inicial', 'Baja', 60, 'Ana Torres', True],
    'C102': ['Crossfit', 'Alta', 45, 'Pedro Rojas', False],
    'C103': ['Spinning', 'Media', 50, 'Laura Díaz', False],
    'C104': ['Pilates', 'Baja', 55, 'Ana Torres', True],
    'C105': ['Entrenamiento Funcional', 'Alta', 40, 'Carlos Soto', False]
}

#precio_pase,cupos
gimnasio = {
    'C101': [8000, 15],
    'C102': [12000, 8],
    'C103': [10000, 0],
    'C104': [9000, 12],
    'C105': [11000, 5]
}
######################################################################
#VALIDACIONES
######################################################################
def validar_codigo(codigo):
    codigo=codigo.strip()
    if len(codigo)>0:
        return True
    return False

def validar_nombre(nombre):
    nombre=nombre.strip()
    if len(nombre)>0:
        return True
    return False

def validar_intensidad(intensidad):
    intensidad=intensidad.strip().lower()
    if intensidad in ('baja','media','alta'):
        return True
    return False

def validar_duracion_min(duracion_min):
    try:
        d=int(duracion_min)
        if d>0:
            return True
        return False
    except ValueError:
        return False

def validar_instructor(instructor):
    instructor=instructor.strip()
    if len(instructor)>0:
        return True
    return False

def validar_es_online(es_online):
    es_online=es_online.lower().strip()
    if es_online in ('s','n'):
        return True
    return False

def validar_precio_pase(precio_pase):
    try:
        p=int(precio_pase)
        if p>0:
            return True
        return False
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        c=int(cupos)
        if c>=0:
            return True
        return False
    except ValueError:
        return False

######################################################################
#FUNCIONES
######################################################################
def cupos_intensidad(intensidad):
    intensidad=intensidad.lower().strip()
    total=0
    for clave,valor in clases.items():
        if valor[1].lower()==intensidad:
            total+=gimnasio[clave][1]
    print(f"El total de cupos in la intensidad {intensidad} es de {total} cupos")

def buscar_por_presupuesto(precio_max):
    lista=[]
    for clave,valor in gimnasio.items():
        cupos=valor[1]
        precio=valor[0]
        NombreClase=clases[clave][0]
        if precio<=precio_max and cupos>0:
            lista.append(NombreClase+'--'+clave)
    if len(lista)==0:
        print("No hay clases disponibles bajo ese presupuesto")
    else:
        lista.sort()
        print(f"Con el presupuesto de {precio_max} las clases disponibles son: {lista}")

def actualizar_precio(codigo,nuevo_precio):
    codigo=codigo.upper().strip()
    if codigo in gimnasio:
        gimnasio[codigo][0]=nuevo_precio
        return True
    return False

def agregar_clase(codigo,nombre,intensidad,duracion_min,instructor,
                  es_online,precio_pase,cupos):
    codigo=codigo.upper().strip()
    es_online=es_online.lower().strip()

    if codigo in clases:
        return False
    
    if es_online=='s':
        online=True
    else:
        online=False
    
    clases[codigo]=[
        nombre.strip().capitalize(),
        intensidad.strip().capitalize(),
        int(duracion_min),
        instructor.strip().capitalize(),
        online
    ]
    
    gimnasio[codigo]=[
        int(precio_pase),
        int(cupos)
    ]
    return True

def eliminar_clase(codigo):
    codigo=codigo.upper().strip()
    if codigo in clases:
        del clases[codigo]
        del gimnasio[codigo]
        return True
    return False

######################################################################
#MENÚ
######################################################################
def menu():
    print('''
1. Total cupos por intensidad
2. Buscar clases por presupuesto máximo
3. Modificar precio de pase diario
4. Registrar nueva clase
5. Cancelar/eliminar clase
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

######################################################################
#PROGRAMA PRINCIPAL
######################################################################

while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            intensidad=input("Ingrese una intensidad (baja, media o alta): ")
            if validar_intensidad(intensidad)==True:
                cupos_intensidad(intensidad)
            else:
                print("La intensidad debe ser baja, media o alta.")

        case 2:
            try:
                precio_max=int(input("Ingrese presupuesto máximo: $"))
                if precio_max>0:
                    buscar_por_presupuesto(precio_max)
                else:
                    print("El presupuesto debe ser mayor a 0")
            except ValueError:
                print("Debe ingresar un número entero")
        
        case 3:
            while True:
                codigo=input("Ingrese el código de la clase: ").upper()
                if validar_codigo(codigo)==True:
                    try:
                        nuevo_precio=int(input("Ingrese el nuevo precio de la clase: "))
                        if nuevo_precio>0:
                            if actualizar_precio(codigo,nuevo_precio)==True:
                                print("Precio actualizado")
                            else:
                                print("El código de clase no existe")
                        else:
                            print("El precio debe ser mayor a 0")
                    except ValueError:
                        print("El precio debe ser un número entero")
                else:
                    print("El código no debe estar vacío ni ser sólo espacios")
                
                resp=input("¿Desea modificar otro precio? (s/n): ").lower()
                if resp == 'n':
                    break
        case 4:
            codigo=input("Ingrese código de la nueva clase a registrar: ").upper()
            if validar_codigo(codigo)==False:
                print("El código no debe estar vacío y contener sólo espacios en blanco")
                continue

            nombre=input("Ingrese nombre de la clase (ej: Yoga, Crossfit): ")
            if validar_nombre(nombre)==False:
                print("No debe estar vacío ni contener solo espacios.")
                continue

            intensidad=input("Ingrese nivel de intensidad (baja,media,alta): ").lower()
            if validar_intensidad(intensidad)==False:
                print("Debe ser exactamente 'baja', 'media' o 'alta'.")
                continue
            
            duracion_min=input("Ingrese la duración en minutos: ")
            if validar_duracion_min(duracion_min)==False:
                print("Debe ser un número entero mayor que cero.")
                continue
            
            instructor=input("Ingrese nombre del profesor: ")
            if validar_instructor(instructor)==False:
                print("No debe estar vacío ni contener solo espacios.")
                continue
            
            es_online=input("Indica si se transmite online (s/n): ").lower()
            if validar_es_online(es_online)==False:
                print("Debe ingresar 's' o 'n'.")
                continue

            precio_pase=input("Ingrese el precio de un pase diario en pesos: $")
            if validar_precio_pase(precio_pase)==False:
                print("Debe ser un número entero mayor que cero")
                continue

            cupos=input("Ingrese cantidad de cupos presenciales disponibles: ")
            if validar_cupos(cupos)==False:
                print("Debe ser un número entero mayor o igual a cero")
                continue

            resp=agregar_clase(codigo,nombre,intensidad,duracion_min,instructor,
                  es_online,precio_pase,cupos)
            
            if resp==False:
                print("El código ingresado ya existe.")
            else:
                print("Nueva clase agregada correctamente.")
        
        case 5:
            codigo=input("Ingrese el código de la clase a eliminar: ")
            if validar_codigo(codigo)==True:
                if eliminar_clase(codigo)==True:
                    print("Clase eliminada correctamente")
                else:
                    print("El código no corresponde a ninguna clase")
            else:
                print("El código no debe estar vacío y contener sólo espacios en blanco")

        case 6:
            print("Salir - Dana")
            break
        case _:
            print("Debe seleccionar una opción válida")