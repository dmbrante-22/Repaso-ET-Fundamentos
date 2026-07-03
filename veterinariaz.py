# Clínica Veterinaria
# Servicios = [nombre servicio, categoría, duración min, nivel urgencia, especialista, requiere ayuno previo]
servicios = {
    'S01': ['Consulta General', 'Medicina', 30, 'Baja', 'Dra. Inés Ruiz', False],
    'S02': ['Cirugía Mayor', 'Cirugia', 120, 'Alta', 'Dr. Hugo Silva', True],
    'S03': ['Limpieza Dental', 'Estetica', 60, 'Media', 'Dra. Inés Ruiz', True],
    'S04': ['Radiografía Digital', 'Diagnostico', 40, 'Media', 'Dr. Hugo Silva', False],
    'S05': ['Vacunación Anual', 'Prevencion', 15, 'Baja', 'Dra. Inés Ruiz', False]
}


# Comercial_Servicios = [valor servicio, cupos diarios disponibles]
comercial_servicios = {
    'S01': [140000, 5],
    'S02': [85000, 8],
    'S03': [100000, 10],
    'S04': [130000, 14],
    'S05': [96000, 8]
}


def menu():
    print("== CLINICA VETERINARIA ==")
    print("1. Contar cupos por categoria")
    print("2. Listado de servicios por rango de precios")
    print("3. Actualizar precio de servicio")
    print("4. Ingresar nuevo servicio")
    print("5. Eliminar servicio")
    print("6. Salir")
def seleccione():
    try:
        op=int(input("Seleccione:"))
        return op
    except:
        return 0
def cuposPorCategoria(cate):
    cant=0
    for clave,valor in servicios.items():
        if valor[1].lower()==cate.lower():
            cant+=comercial_servicios[clave][1]
    if cant==0:
        print("No existe esa categoria")
    else:
        print(f"Existe {cant} cupos para {cate}")
def listadoPorPrecio(minimo,maximo):
    lista=[]
    for clave,valor in comercial_servicios.items():
        if valor[0]>=minimo and valor[0]<= maximo and valor[1]>0:
            nombre=servicios[clave][0]
            cate=servicios[clave][1]
            lista.append([nombre+" -- "+cate])
    if len(lista)==0:
        print("No hay servicios con esos precios")
    else:
        lista.sort()
        print(lista)
def actualizarPrecio(codigo,n_precio):
    if codigo in servicios:
        comercial_servicios[codigo][0]=n_precio
        return True
    return False
def EliminarServicio(codigo):
    if codigo in servicios:
        del servicios[codigo]
        del comercial_servicios[codigo]
        return True
    return False
def agregar_servicio(codigo,nombre,cate,durac,nivel,espe,ayuno,precio,cupos):
    if not codigo in servicios:
        return False
    if ayuno=='s':
        ayuno_previo=True
    else:
        ayuno_previo=False
    servicios[codigo]=[nombre,cate,int(durac),nivel,espe,ayuno_previo]
    comercial_servicios[codigo]=[int(precio),int(cupos)]
    return True
def validarCodigo(cod):
    if len(cod)>=3:
        return True
    return False
def validaServicio(ser):
    if len(ser.strip())>=2:
        return True
    return False
def validaCategoria(cate):
    if len(cate.strip())>=2:
        return True
    return False
def validaDuracion(dura):
    try:
        d=int(dura)
        if d>=10 and d<=90:
            return True
        return False
    except:
        return True
def validaNivel(nivel):
    if nivel in ('Baja','Alta','Media'):
        return True
    return True
def validaEspecialista(espe):
    if len(espe.strip())>=2:
        return True
    return False
def validaAyuno(ayuno):
    if ayuno in ('s','n'):
        return True
    return False
def validaPrecio(pre):
    try:
        p=int(pre)
        if p>=500 and p<=500000:
            return True
        return False
    except:
        return False
def validaCupos(cupos):
    try:
        c=int(cupos)
        if c>0:
            return True
        return False
    except:
        return False
while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            while True:
                cate=input("Ingrese la categoria:")
                cuposPorCategoria(cate)
                resp=input("Desea repetir el proceso (s/n):").lower()
                if resp in ('n','no'):
                    break
        case 2:
            while True:
                try:
                    minimo=int(input("Ingrese valor minimo:"))
                    maximo=int(input("Ingrese valor maximo:"))
                    if minimo>0 and minimo<maximo:
                        listadoPorPrecio(minimo,maximo)
                    else:
                        print("minimo no puede ser menor a cero o mayor a maximo")
                except:
                    print("Ingrese solo valor númerico")
                resp=input("Desea repetir el proceso (s/n):").lower()
                if resp in ('n','no'):
                    break    
        case 3:
            while True:
                try:
                    codigo=input("Ingrese codigo a buscar:").strip().upper()
                    n_precio=int(input("Ingrese nuevo precio:"))
                    if n_precio>0:
                        resp=actualizarPrecio(codigo,n_precio)
                        if resp==True:
                            print("Actualizado...")
                        else:
                            print("No actualizado...")
                    else:
                        print("Nuevo precio debe ser positivo")
                except:
                    print("El precio debe ser numerico")
                resp=input("Desea repetir el proceso (s/n):").lower()
                if resp in ('n','no'):
                    break
        case 4:
            while True:
                codigo=input("Ingrese codigo de su servicio:").upper()
                if validarCodigo(codigo)==False:
                    print("El codigo debe tener minimo 3 caracteres")
                    continue
                servicio=input("Ingrese nombre del servicio:")
                if validaServicio(servicio)==False:
                    print("El nombre debe tener minimo 2 caracteres")
                    continue
                cate=input("Ingrese la categoria:")
                if validaCategoria(cate)==False:
                    print("La categoria debe tener minimo 2 caracteres")
                    continue
                durac=input("Ingrese la duracion (10-90 minutos)")
                if validaDuracion(durac)==False:
                    print("Duracion debe ser un numero entre 10 y 90")
                    continue
                nivel=input("Ingrese nivel (alta,baja,media)")
                if validaNivel(nivel)==False:
                    print("Solo los tres niveles que se mostraron")
                    continue
                espe=input("Ingrese especialista:")
                if validaEspecialista(espe)==False:
                    print("No puede estar vacio")
                    continue
                ayuno=input("¿Necesita ayuno previo (s/n):")
                if validaAyuno(ayuno)==False:
                    print("Responde solo 's' o 'n'")
                    continue
                precio=input("Ingrese precio:")
                if validaPrecio(precio)==False:
                    print("Debe ser un numero entre 500 a 500000")
                    continue
                cupos=input("Ingrese los cupos:")
                if validaCupos(cupos)==False:
                    print("Debe ser un numero numerico mayor a cero")
                    continue
                resp=agregar_servicio(codigo,servicio,cate,durac,nivel,espe,ayuno,precio,cupos)
                if resp==False:
                    print("Agregado...")
                else:
                    print("No agregado...")
                resp=input("Desea repetir el proceso (s/n):").lower()
                if resp in ('n','no'):
                    break
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
        case 6:
            print("Adios...")
            break