#########################################################################################
# Gimnasio / Centro Deportivo
# Actividades = [nombre actividad, categoría, duración min, nivel, instructor, requiere equipamiento propio]
actividades = {
    'A01': ['Yoga Dinámico', 'Bienestar', 60, 'Principiante', 'Ana Gómez', False],
    'A02': ['Crossfit Pro', 'Fuerza', 50, 'Avanzado', 'Carlos Plaza', True],
    'A03': ['Pilates Reformer', 'Bienestar', 45, 'Intermedio', 'Elena Marín', False],
    'A04': ['Spinning HIIT', 'Cardio', 45, 'Intermedio', 'Luis Fuentes', False],
    'A05': ['Zumba Fitness', 'Cardio', 60, 'Principiante', 'Luis Fuentes', False],
}

# Comercial_Actividades = [valor mensualidad, cupos máximos por clase]
comercial_actividades = {
    'A01': [80000, 30],
    'A02': [70000, 20],
    'A03': [50000, 10],
    'A04': [43000, 10],
    'A05': [30000, 30],
}

def menu():
    print("Menu Principal")
    print("1. Cantidad de cupos por nivel")
    print("2. Filtar actividades por valor mensual")
    print("3. Actualizar precio de actividad")
    print("4. Agregar actividad")
    print("5. Eliminar actividades")
    print("6. Salir")

def seleccione():
    try:
        op=int(input("Seleccion"))
        return op
    except:
        return 0
    
def cantidadCuporPorNivel(nivel):
    cant=0
    for clave,valor in actividades.items():
        if valor[3].lower()==nivel.lower():
            cant+=comercial_actividades[clave][1]
    if cant==0:
        print("No existen actividades con este nivel")
    else:
        print(f"Existen {cant} cupos para actividades de nivel {nivel}")

def filtrarActividadPorValorMensualidad(minimo,maximo):
    lista=[]
    for clave,valor in comercial_actividades.items():
        if valor[0]>=minimo and valor[0]<=maximo and valor[1]>0:
            nombre=actividades[clave][0]
            categoria=actividades[clave][1]
            lista.append([nombre+" - "+categoria+" - "+str(valor[0])])
    if len(lista)==0:
        print("No existen actividades entre esos valores")
    else:
        lista.sort()
        print(lista)

def actualizarPrecioPorCodigo(codigo, nuevoPrecio):
    if codigo in actividades:
        comercial_actividades[codigo][0]=nuevoPrecio
        return True
    return False

def eliminarPrecioPorCodigo(codigo):
    if codigo in actividades:
        del actividades[codigo]
        del comercial_actividades[codigo]
        return True
    return False

while True:
    menu()
    opcion=seleccione()
    match opcion:
        case 1:
            while True:
                nivel=input("Ingrese el nivel: ")
                cantidadCuporPorNivel(nivel)
                resp=input("Desea repetir el proceso? (s/n): ").lower()
                if resp=="n":
                    break
        case 2:
            while True:
                try:
                    minimo=int(input("Ingrese valor minimo: "))
                    maximo=int(input("Ingrese valor maximo: "))
                    if minimo<maximo and minimo>0:
                        filtrarActividadPorValorMensualidad(minimo,maximo)
                    else:
                        print("el minimo debe ser menor al maximo y mayor a cero")
                except:
                    print(" Ingrese valores numericos")
                resp=input("Desea repetir el proceso (s/n):").lower()
                if resp=="n":
                    break
        case 3:
            while True:
                try:
                    codigo=input("Ingrese codigo a modificar:").strip().upper()
                    nuevoprecio=int(input("Ingrese nuevo precio:"))
                    if nuevoprecio>0:
                        resp=actualizarPrecioPorCodigo(codigo,nuevoprecio)
                        if resp== True:
                            print("Precio actualizado")
                        else:
                            print("Precio no actualizado")
                    else:
                        print("El nuevo precio debe ser mayor a cero...")
                except:
                    print("El precio debe ser numerico")
                resp=input("Desea continuar (s/n) :").lower()
                if resp=="n":
                    break
        
        case 5:
            while True:
                codigo=input("Ingrese codigo a eliminar:").strip().upper()
                resp=eliminarPrecioPorCodigo(codigo)
                if resp== True:
                    print("eliminado")
                else:
                    print("no eliminado")
                resp=input("Desea continuar (s/n) :").lower()
                if resp=="n":
                    break
        case 6:
            print("Adios....")
            break
    
