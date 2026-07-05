################################################################################
# SISTEMA DE GESTIÓN DE CURSOS ONLINE - EDUTECH
#
# cursos = [nombre, área, horas_totales, nivel, tutor, certificación_oficial]
# comercial = [valor_matricula, cupos_maximos]
################################################################################

cursos = {
    'C01': ['Python desde Cero', 'Tecnología', 40, 'Principiante', 'Marta Rivas', True],
    'C02': ['Finanzas Personales', 'Negocios', 20, 'Principiante', 'Pedro Soto', False],
    'C03': ['UI/UX Avanzado', 'Diseño', 60, 'Avanzado', 'Lucía López', True],
    'C04': ['Análisis de Datos', 'Tecnología', 50, 'Intermedio', 'Marta Rivas', True]
}

comercial = {
    'C01': [52000, 30],
    'C02': [70000, 25],
    'C03': [62000, 28],
    'C04': [152000, 20]
}
###################################################################
#VALIDACIONES                                                     #
###################################################################
def validar_codigo(codigo):
    codigo=codigo.upper().strip()

    if len(codigo)==3 and codigo[0]=='C' and codigo[1:].isdigit():
        return True
    return False

def validar_nombre(nombre):
    if len(nombre.strip())>0:
        return True
    return False

def validar_area(area):
    if area.lower().strip() in ('tecnología','negocios','diseño'):
        return True
    return False

def validar_horas(horas_totales):
    try:
        h=int(horas_totales)
        if h>0:
            return True
        return False
    except ValueError:
        return False

def validar_nivel(nivel):
    if nivel.lower().strip() in ('principiante','intermedio','avanzado'):
        return True
    return False

def validar_tutor(tutor):
    if len(tutor.strip())>0:
        return True
    return False

def validar_certificacion(certificacion):
    if certificacion.lower().strip() in ('s','n'):
        return True
    return False

def validar_valor_matricula(valor_matricula):
    try:
        v=int(valor_matricula)
        if v>0:
            return True
        return False
    except ValueError:
        return False

def validar_cupos_maximos(cupos_maximos):
    try:
        c=int(cupos_maximos)
        if c>=0:
            return True
        return False
    except ValueError:
        return False
    
###################################################################
#FUNCIONES DEL PROGRAMA                                           #
###################################################################
def total_cupos(area):
    total=0
    for clave,valor in cursos.items():
        if valor[1].lower()==area.lower().strip():
            total+=comercial[clave][1]
    if total==0:
        print("No se encontró curso en esa área")
    else:
        print(f"Existen {total} cupos disponibles en el área de {area.strip().lower()}")

def buscar_cursos_avanzado(precio_max,nivel):
    lista=[]
    for clave,valor in comercial.items():
        if cursos[clave][3].lower()==nivel.lower().strip():
            precio=valor[0]
            nombre_curso=cursos[clave][0]
            cupos_maximos=valor[1]
            if precio<=precio_max and cupos_maximos>0:
                lista.append(nombre_curso+'--'+clave)
    lista.sort()
    if len(lista)==0:
        print("No hay cursos disponibles para estos criterios.")
    else:
        print(f"Con el presupuesto de ${precio_max} y el nivel de {nivel} los cursos disponibles son: {lista}")

def actualizar_matricula(codigo,nuevo_valor):
    if codigo.strip().upper() in comercial:
        comercial[codigo][0]=nuevo_valor
        return True
    return False

def agregar_curso(codigo,nombre,area,horas_totales,nivel,tutor,
                  certificacion,valor_matricula,cupos_maximos):
    codigo.upper().strip()==codigo
    if codigo in cursos:
        return False
    
    if certificacion.lower().strip() == 's':
        certificacion_oficial=True
    else:
        certificacion_oficial=False
    
    cursos[codigo]=[
        nombre,
        area.strip().capitalize(),
        int(horas_totales),
        nivel.strip().capitalize(),
        tutor,
        certificacion_oficial
    ]

    comercial[codigo]=[
        int(valor_matricula),
        int(cupos_maximos)
    ]

    return True

def eliminar_curso(codigo):
    if codigo.upper().strip() in comercial:
        del comercial[codigo]
        del cursos[codigo]
        return True
    return False

def horas_por_tutor(tutor):
    total=0
    for clave,valor in cursos.items():
        if valor[4].lower()==tutor.lower().strip():
            total+=valor[2]
    if total==0:
        print("tutor no encontrado")
    else:
        print(f"Las horas totales acumuladas del profesor {tutor} son de {total} horas")

###################################################################
#MENU                                                             #
###################################################################
def menu():
    print('''
    ========== GESTIÓN EDUTECH ==========
    1. Total cupos disponibles por área
    2. Buscar cursos por presupuesto y nivel
    3. Modificar valor de matrícula
    4. Registrar nuevo curso en catálogo
    5. Dar de baja un curso
    6. Reporte de horas por tutor
    7. Salir
    =====================================
          ''')

def seleccione():
    try:
        op=int(input("Seleccione una opción (1-7): "))
        if op>=1 and op<=7:
            return op
        return 0
    except ValueError:
        return 0

###################################################################
#PROGRAMA PRINCIPAL                                               #
###################################################################
while True:
    menu()
    op=seleccione()
    match op:
        case 1:
            area=input("Seleccione el área (Tecnología, Negocios o Diseño): ")
            if validar_area(area)==True:
                total_cupos(area)
            else:
                print("El área de conocimiento debe ser exactamente: Teconología, Negocios o Diseño.")

        case 2:
            try:
                precio_max=int(input("Ingrese un presupuesto máximo en pesos: $"))
                if precio_max>0:
                    nivel=input("Ingrese el nivel de dificultad (Principiante, Intermedio o Avanzado): ")
                    if validar_nivel(nivel)==True:
                        buscar_cursos_avanzado(precio_max,nivel)
                    else:
                        print("Debe ser exactamente 'Principiante', 'Intermedio' o 'Avanzado'")
            except:
                print("Debe ingresar un número entero.")

        case 3:
            while True:
                codigo=input("Ingrese el código del curso a modificar: ").upper()
                try:
                    nuevo_valor=int(input("Ingrese el nuevo valor: $"))
                    if nuevo_valor>0:
                        if actualizar_matricula(codigo,nuevo_valor)==True:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                except ValueError:
                    print("El valor debe ser un numero")
                respuesta=input("¿Desea continuar? (s/n): ").lower()
                if respuesta == 'n':
                    break
        
        case 4:
            codigo=input("Ingrese el código del nuevo curso: ").upper()
            if validar_codigo(codigo)==False:
                print("El codigo debe tener el formato: C01")
                continue

            nombre=input("Ingrese nombre del curso: ")
            if validar_nivel(nombre)==False:
                print("No debe estar vacío ni contener solo espacios.")
                continue

            area=input("Ingrese área de conocimiento (Tecnología, Negocios o Diseño): ")
            if validar_area(area)==False:
                print(" Debe ser exactamente 'Tecnología', 'Negocios' o 'Diseño'.")
                continue

            horas_totales=input("Ingrese Duración total del curso en horas: ")
            if validar_horas(horas_totales)==False:
                print("Número entero mayor que cero.")
                continue

            nivel=input("Ingrese el nivel de dificultad: ")
            if validar_nivel(nivel)==False:
                print("Debe ser exactamente 'Principiante', 'Intermedio' o 'Avanzado'")
                continue

            tutor=input("Ingrese nombre del instructor a cargo")
            if validar_tutor(tutor)==False:
                print("No debe estar vacío ni contener solo espacios.")
                continue

            certificacion=input("¿El curso entrega diploma firmado? (s/n): ")
            if validar_certificacion(certificacion)==False:
                print("Debe ingresar 's' o 'n'")
                continue

            valor_matricula=input("Ingrese el costo del curso en pesos: $")
            if validar_valor_matricula(valor_matricula)==False:
                print(" Número entero mayor que cero.")
                continue

            cupos_maximos=input("Ingrese cantidad de vacantes libres para estudiantes: ")
            if validar_cupos_maximos(cupos_maximos)==False:
                print("Número entero mayor o igual a cero.")
                continue

            resultado=agregar_curso(codigo,nombre,area,horas_totales,nivel,tutor,
                                    certificacion,valor_matricula,cupos_maximos)
            if resultado==True:
                print("Curso registrado")
            else:
                print("El código ya existe, el curso no se pudo registrar")
        
        case 5:
            codigo=input("Ingrese el código del curso a eliminar").upper()
            if eliminar_curso(codigo)==True:
                print("Curso eliminado correctamente")
            else:
                print("El código no corresponde a ningún curso registrado")
        
        case 6:
            tutor=input("Ingrese el nombre del tutor: ")
            if validar_tutor(tutor) ==True:
                horas_por_tutor(tutor)

        case 7:
            print("Salir - Dana")
            break

        case _:
            print("Opción inválida")