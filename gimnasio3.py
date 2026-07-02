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
#######################################################
#FUNCIONES
def cantidad_cupos_nivel(nivel):
    cantidad=0
    for clave,valor in actividades.items():
        if valor [3].lower() == nivel.lower():
            cantidad+=comercial_actividades[clave][1]
    if cantidad==0:
        print("No hay cupos para este nivel")
    else:
        print(f"Tienes {cantidad} de cupos para el nivel {nivel}")

def listar_por_categoria(cate):
    lista=[]
    for clave,valor in actividades.items():
        if valor[1].lower()==cate.lower():
            nombre = valor[0]
            nivel=valor[3]
            precio=comercial_actividades[clave][0]
            lista.append([nombre+"-"+nivel+"-"+str(precio)])
    if len(lista)==0:
        print("No existen actividades con esa categoría")
    else:
        lista.sort()
        print(lista)

def actualizar_precio(codigo,nuevo_precio):
    if codigo in actividades:
        comercial_actividades[codigo][0]=nuevo_precio
        return True
    return False

def eliminar_actividad(codigo):
    if codigo in actividades:
        del comercial_actividades[codigo]
        del actividades[codigo]
        return True
    return False

#######################################################
def menu():
    print('''
    \n========== MENU PRINCIPAL ==========
    1. Cantidad de cupos por nivel
    2. Listar actividades por categoria
    3. Actualizar precio de mensualidad
    4. Agregar actividad
    5. Eliminar actividad
    6. Salir
        ''')

def seleccione():
    try:
        op=int(input("Seleccione: "))
        return op
    except:
        return 0

while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            while True:
                nivel=input("Ingrese el nivel a buscar: ")
                cantidad_cupos_nivel(nivel)
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 2:
            while True:
                cate=input("Ingrese la categoría: ")
                listar_por_categoria(cate)
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 3:
            while True:
                try:
                    codigo=input("Ingrese el código de la actividad a modificar el precio: ").upper().strip()
                    nuevo_precio=int(input("Ingrese el nuevo precio de la actividad"))
                    if nuevo_precio>0:
                        if actualizar_precio(codigo,nuevo_precio)==True:
                            print("Precio actualizado")
                        else:
                            print("Precio no actualizado")
                    else:
                        print("El nuevo precio debe ser mayor a 0")
                except:
                    print("El precio debe ser numerico")
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 5:
            while True:
                codigo=input("Ingrese el código de la actividad a eliminar: ").upper().strip()
                if eliminar_actividad(codigo)==True:
                    print("Actividad eliminada")
                else:
                    print("Actividad no eliminada")
                resp=input("¿Desea continuar? (s/n): ").lower()
                if resp in ('n','no'):
                    break
        case 6:
            print("Salir - Dana")
            break

