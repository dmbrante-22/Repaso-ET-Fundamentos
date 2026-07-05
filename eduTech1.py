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
#############################################################
#VALIDACIONES
def validar_codigo(codigo):
    codigo=codigo.strip()

    if len(codigo)==3 and codigo[0].upper()=='C' and codigo[1:].isdigit():
        return True
    return False

def validar_nombre(nombre):
    if len(nombre.strip())>0:
        return True
    return False

def validar_area(area):
    if area.strip().lower() in ('tecnología', 'negocios', 'diseño'):
        return True
    return False

def validar_horas(horas):
    try:
        h=int(horas)
        if h>0:
            return True
        return False
    except ValueError:
        return False

def validar_nivel(nivel):
    if nivel.strip().lower() in ('principiante', 'intermedio' 'avanzado'):
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

def validar_valor(valor_matricula):
    try:
        v=int(valor_matricula)
        if v>0:
            return True
        return False
    except ValueError:
        return False

def validar_cupos(cupos_maximos):
    try:
        c=int(cupos_maximos)
        if c>=0:
            return True
        return False
    except ValueError:
        return False

#############################################################
#FUNCIONES DEL SISTEMA
def cupos_por_area(area):
    total_cupos=0
    for clave,valor in cursos.items():
        if valor[1].lower()==area.strip().lower():
            total_cupos+=comercial[clave][1]
    print(f"El total de cupos del área {area} es de {total_cupos}")

def buscar_cursos_avanzado(precio_max,nivel):
    lista_cursos=[]
    for clave,valor in comercial.items():
        precio=valor[0]
        cupos_maximos=valor[1]
        nivel_curso=cursos[clave][3]
        if precio<=precio_max and cupos_maximos>0:
            if nivel_curso.lower()==nivel.lower().strip():
                nombre_curso=cursos[clave][0]
                lista_cursos.append(nombre_curso + "--" + clave)
    if len(lista_cursos)==0:
        print("No hay cursos disponibles para esos criterios.")
    else:
        lista_cursos.sort()
        print(f"Cursos disponibles con el {precio_max} como presupuesto y en el nivel {nivel}: {lista_cursos}")

def actualizar_matricula(codigo,nuevo_precio):
    codigo=codigo.upper().strip()
    if codigo in comercial:
        comercial[codigo][0]=nuevo_precio
        return True
    return False

def agregar_curso(codigo,nombre,area,horas,nivel,tutor,
                  certificacion,valor_matricula,cupos_maximos):
    codigo=codigo.upper().strip()
    if codigo in cursos:
        return False
    
    if certificacion.lower().strip()=='s':
        certificacion_oficial=True
    else:
        certificacion_oficial=False
    
    cursos[codigo]=[
        nombre.strip(),
        area.strip().capitalize(),
        int(horas),
        nivel.strip().capitalize(),
        tutor.strip(),
        certificacion_oficial
    ]

    comercial[codigo]=[
        int(valor_matricula),
        int(cupos_maximos)
    ]

    return True

def eliminar_curso(codigo):
    codigo=codigo.upper().strip()
    if codigo in cursos:
        del cursos[codigo]
        del comercial[codigo]
        return True
    return False

def horas_por_tutor(tutor):
    total=0
    for clave,valor in cursos.items():
        if valor[4].lower()==tutor.lower():
            total+=valor[2]
    if total==0:
        print("Tutor no encontrado")
    else:
        print(f"El total de horas que dicta el tutor {tutor.lower()} es de {total}")

#############################################################
#MENÚ
def mostrar_menu():
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
    
#############################################################
#PROGRAMA PRINCIPAL
while True:
    mostrar_menu()
    op=seleccione()
    match op:
        case 1:
            area=input("Ingrese el área (Tecnología, Negocios o Diseño): ")
            if validar_area(area)==True:
                cupos_por_area(area)
            else:
                print("El área registrada no es válida")
        case 2:
            try:
                precio_max=int(input("Ingrese un presupuesto máximo en pesos: $"))
                if precio_max>0:
                    nivel=input("Ingrese el nivel a buscar (Principiante, Intermedio, Avanzado): ")
                    if validar_nivel(nivel)==True:
                        buscar_cursos_avanzado(precio_max,nivel)
                    else:
                        print("El nivel ingresado no es válido")
                else:
                    print("El presupuesto debe ser un número entero mayor a 0")
            except ValueError:
                print("El presupuesto máximo debe ser un número entero")
        case 3:
            while True:
                codigo=input("Ingrese el código del curso para modificar valor de matricula: ")
                try:
                    nuevo_precio=int(input(f"Ingrese nuevo valor de la matricula del curso {codigo}: $"))
                    if nuevo_precio>0:
                        if actualizar_matricula(codigo,nuevo_precio)==True:
                            print("Precio actualizado")
                        else:
                            print("El código no existe")
                    else:
                        print("Debe ingresar un valor mayor a 0")
                except ValueError:
                    print("El valor debe ser un número entero")
                
                resp=input("¿Desea continuar? (s/n)").lower()
                if resp in ('n','no'):
                    break
        case 4:
            codigo=input("Ingrese el código del nuevo curso: ").upper()
            if validar_codigo==False:
                print("El código debe tener el formato: C01")
                continue

            nombre=input("Ingrese el nombre del curso: ")
            if validar_nombre(nombre)==False:
                print("El nombre no debe estar vacío ni contener solo espacios.")
                continue

            area=input("Ingrese el área de conocimiento (Tecnología, Negocios o Diseño): ")
            if validar_area==False:
                print("El area del conocimiento. Debe ser exactamente 'Tecnología', 'Negocios' o 'Diseño'.")
                continue
            
            horas=input("Ingrese la duración total del curso en horas: ")
            if validar_horas(horas)==False:
                print("Las horas deben ser un número entero mayor que cero.")
                continue
            
            nivel=input("Ingrese el nivel de dificultad (Principiante, Intermedio o Avanzado): ")
            if validar_nivel==False:
                print("El nivel de dificultad. Debe ser exactamente 'Principiante', 'Intermedio' o 'Avanzado'.")
                continue
            
            tutor=input("Ingrese el nombre del instructor a cargo: ")
            if validar_tutor==False:
                print("El nombre del instructor a cargo no debe estar vacío ni contener solo espacios.")
                continue
            
            certificacion=input("¿El curso entrega diploma firmado? (s/n): ").lower().strip()
            if validar_certificacion==False:
                print("Debe ingresar 's' o 'n' ")
                continue

            valor_matricula=input("Ingrese el costo del curso en pesos: $")
            if validar_valor(valor_matricula)==False:
                print("El valor debe ser un número entero mayor que cero.")
                continue

            cupos_maximos=input("Ingrese la cantidad de vacantes libres para nuevos estudiantes.")
            if validar_cupos(cupos_maximos)==False:
                print("El valor debe ser un número entero mayor o igual a cero.")
                continue

            resultado = agregar_curso(
                codigo,
                nombre,
                area,
                horas,
                nivel,
                tutor,
                certificacion,
                valor_matricula,
                cupos_maximos
            )
            
            if resultado==True:
                print("Curso registrado")
            else:
                print("El código ya existe, no se pudo registrar el curso")
        
        case 5:
            codigo=input("Ingrese el código del curso a eliminar: ").upper().strip()
            if eliminar_curso(codigo)==True:
                print("curso eliminado correctamente")
            else:
                print("El código no existe. curso no eliminado")
        
        case 6:
            tutor=input("Ingrese el nombre del tutor: ")
            if validar_tutor(tutor)==True:
                horas_por_tutor(tutor)
            else:
                print("El nombre del instructor a cargo no debe estar vacío ni contener solo espacios.")

        case 7:
            print("Salir - Dana")
            break
        case _:
            print("Opción inválida")