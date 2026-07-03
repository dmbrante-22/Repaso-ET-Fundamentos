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

def unidades_tipo(tipo):
    cantidad=0
    for codigo,valor in arreglos.items():
        if valor[1].lower()==tipo.lower().strip():
            cantidad+=bodega[codigo][1]
    if cantidad==0:
        print("No hay ese tipo de arreglo")
    print(f"La cantidad de arreglos {tipo} es de {cantidad}")

def busqueda_precio(p_min,p_max):
    lista=[]
    
    if p_max>=0 and p_min >=0 and p_min<=p_max:
    

##########################################################################################
#MENU PRINCIPAL
def menu():
    print('''
    ========== MENÚ PRINCIPAL ==========
    1. Unidades por tipo de arreglo
    2. Búsqueda de arreglos por rango de precio
    3. Actualizar precio de arreglo
    4. Agregar arreglo
    5. Eliminar arreglo
    6. Salir
    ====================================
          ''')

def seleccione():
    try:
        op=int(input("Seleccione una opción (1-6): "))
        if op>=1 and op<=6:
            return op
        return 0
    except:
        return 0

while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            tipo=input("Ingrese el tipo de arreglo: ")
            unidades_tipo(tipo)
        case 2:
            try:
                p_min=int(input(""))
                p_max=int(input(""))
                busqueda_precio(p_min,p_max)
            except:
                print("Debe ingresar valores enteros")
        case 6:
            break
        case _:
            print("Debe seleccionar una opción válida")