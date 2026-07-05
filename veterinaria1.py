#########################################################################################
# Clínica Veterinaria
# Servicios = [nombre servicio, categoría, duración min, nivel urgencia, especialista, requiere ayuno previo]
servicios = {
    'S01': ['Consulta General', 'Medicina', 30, 'Baja', 'Dra. Inés Ruiz', False],
    'S02': ['Cirugía Mayor', 'Cirugía', 120, 'Alta', 'Dr. Hugo Silva', True],
    'S03': ['Limpieza Dental', 'Estética', 60, 'Media', 'Dra. Inés Ruiz', True],
    'S04': ['Radiografía Digital', 'Diagnóstico', 40, 'Media', 'Dr. Hugo Silva', False],
    'S05': ['Vacunación Anual', 'Prevención', 15, 'Baja', 'Dra. Inés Ruiz', False]
}

# Comercial_Servicios = [valor servicio, cupos diarios disponibles]
comercial_servicios = {
    'S01': [140000, 5],
    'S02': [85000, 8],
    'S03': [100000, 10],              
    'S04': [130000, 14],        #{"clave":[valor1,valor2]}
    'S05': [96000, 8]
}

#############################################################################
#VALIDACIONES
def validar_codigo(codigo):
    if len(codigo.strip())==3:
        return True
    return False

def validar_nombre(nombre):
    if len(nombre.strip())>=2:
        return True
    return False

def validar_categoria(categoria):
    if len(categoria.strip())>=5:
        return True
    return False

def validar_duracion(duracion):
    try:
        d=int(duracion)
        if d>=10 and d<=90:
            return True
        return False
    except:
        return False

def validar_nivel(nivel):
    if nivel.lower() in ('bajo','medio','alto'):
        return True
    return False

def validar_especialista(especialista):
    if len(especialista.strip())>=2:
        return True
    return False

def validar_ayuno(ayuno):
    if ayuno.lower() in ('s','n'):
        return True
    return False

def validar_precio(precio):
    try:
        p=int(precio)
        if p >=10000 and p<=180000:
            return True
        return False
    except:
        return False

def validar_cupos(cupos):
    try:
        c=int(cupos)
        if c>0:
            return True
        return False
    except:
        return False

def agregar_servicio(codigo,nombre,categoria,duracion,nivel,especialista,ayuno,precio,cupos):
    if codigo.upper() in servicios:
        return False #si es que ya existe, no se puede agregar
    if ayuno.lower() in ('s','si'):
        ayuno_previo=True
    else:
        ayuno_previo=False
    servicios[codigo]=[nombre,categoria,int(duracion),nivel,especialista,ayuno_previo]
    comercial_servicios[codigo]=[int(precio),int(cupos)]
    print(servicios)
    print(comercial_servicios)
    return True
#############################################################################
def sumar_por_nivel(nivel):
    suma=0
    for clave,valor in servicios.items():
        if valor[3].lower()==nivel.lower():
            suma+=comercial_servicios[clave][0]
        if suma==0:
            print("No existen servicios con ese nivel")
        else:
            print(f"La suma del valor por servicios del nivel {nivel} es {suma}")

def busqueda_precio(p_min,p_max):
    lista=[]
    for clave,valor in comercial_servicios.items():
        if valor[0]>=p_min and valor[0]<=p_max and valor[1]>0:
            nombre=servicios[clave][0]
            doctor=servicios[clave][4]
            lista.append([nombre+"-"+doctor])
    if len(lista)>0:
        lista.sort()
        print(lista)
    else:
        print("No existen servicios entre los valores")

def actualizar_precio (codigo,nuevo_precio):
    if codigo in comercial_servicios:
        comercial_servicios[codigo][0]=nuevo_precio
        return True
    return False

def EliminarServicio(codigo):
    if codigo in servicios:
        del servicios[codigo]
        del comercial_servicios[codigo]
        return True
    return False
    
#############################################################################
#MENÚ

def menu():
    print('''
    \n========== MENU PRINCIPAL Clínica Veterinaria ==========
    1. Suma de valores de servicios por nivel de urgencia
    2. Listar de servicios por rango de precios
    3. Actualizar precio de servicios
    4. Agregar Servicio
    5. Eliminar Servicio
    6. Visualizar los datos
    7. Salir
        ''')

def seleccione():
    try:
        op=int(input("Seleccione una opción (1-7): "))
        if op>=1 and op<=7:
            return op
        return 0
    except:
        return 0

while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            while True:
                nivel=input("Ingrese el nivel de urgencia: ")
                sumar_por_nivel(nivel)
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 2:
            while True:
                try:
                    p_min=int(input("Ingrese el precio mínimo: "))
                    p_max=int(input("Ingrese el precio máximo: "))
                    if p_min<p_max and p_min>0:
                        busqueda_precio(p_min,p_max)
                    else:
                        print("Imprima mínimo debe ser menor que el máximo.")
                except:
                    print("Debe ingresar solo valores numéricos y enteros")
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 3:
            while True:
                try:
                    codigo=input("Ingrese código del servicio a modificar")
                    nuevo_precio= int(input("Ingrese nuevo precio: "))
                    if nuevo_precio>0:
                        if actualizar_precio(codigo,nuevo_precio)== True:
                            print("Se actualizó el precio correctamente")
                        else:
                            print("El nuevo precio debe ser mayor a 0")
                except:
                    print("Debe ingresar solo valores numéricos y enteros")
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 4:
            codigo=input("Ingrese el código").upper()
            if validar_codigo(codigo)==False:
                print("Código incorrecto")
                continue
            
            nombre=input("Ingrese el nombre del servicio: ")
            if validar_nombre(nombre)==False:
                print("Nombre incorrecto")
                continue
            
            categoria=input("Ingrese categoría: ")
            if validar_categoria(categoria)==False:
                print("Categoría incorrecta")
                continue
            
            duracion=input("Ingrese duración: ")
            if validar_duracion(duracion)==False:
                print("Duración entre 10 y 90")
                continue
            
            nivel=input("Ingrese el nivel: ")
            if validar_nivel(nivel)==False:
                print("Nivel incorrecto")
                continue
            
            especialista=input("Ingrese Especialista: ")
            if validar_especialista(especialista)==False:
                print("El doctor no debe estar vacío")
                continue
            
            ayuno=input("Ingrese Ayuno: (s/n): ").lower()
            if validar_ayuno(ayuno)==False:
                print("Debe escribir s o n")
                continue
            
            precio=input("Ingrese precio: ")
            if validar_precio(precio)==False:
                print("El precio es incorrecto")
                continue
            
            cupos=input("Ingrese cupos: ")
            if validar_cupos(cupos)==False:
                print("Cupos incorrectos")
                continue
            
            if agregar_servicio(codigo,nombre,categoria,duracion,nivel,especialista,ayuno,precio,cupos)==True:
                print("Agregado correctamente")
            else:
                print("No se grabó")
        case 5:
            while True:
                codigo=input("Ingrese codigo:").upper
                if EliminarServicio(codigo)==False:
                    print("No existe servicio con ese codigo")
                else:
                    print("Eliminado...")
                resp=input("Desea repetir el proceso (s/n):").lower()
                if resp in ('n','no'):
                    break
        case 7:
            print("Salir - Dana")
            break
        case _:
            print("Opción inválida")