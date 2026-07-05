cursos={
    "C01":['Python','Tecnologia',40,'Principiante','Matias Rivas',True],
    "C02":['Finanzas','Negocios',20,'Principiante','Pedro Soto',False],
    "C03":['UI Avanzado','Diseño',60,'Avanzado','Lucia Lopez',True],
    "C04":['Analisis de Datos','Tecnologia',50,'Intermedi','Marta Rivasd',True],
}

comercial={
    "C01":[52000,30],
    "C02":[70000,25],
    "C03":[62000,28],
    "C04":[152000,20],
}
###############################################################################
# validaciones
def validaCodigo(codigo):
    if len(codigo.strip())>0:
        return True
    return False
def validaNombre(nombre):
    if len(nombre.strip())>0:
        return True
    return False
def validaArea(area):
    if area in ('Tecnologia','Negocios','Diseño'):
        return True
    return False
def validaHoras(horas):
    try:
        h = int(horas)
        if h>0:
            return True
        return False
    except:
        return False

def validaNivel(nivel):
    if nivel in ('Principiante','Intermedio','Avanzado'):
        return True
    return False

def validaTutor(tutor):
    if len(tutor.strip())>0:
        return True
    return False

def validaCertificacion(certi):
    if certi.lower() in ('s','n'):
        return True
    return False

def validaMatricula(matri):
    try:
        m=int(matri)
        if m>0:
            return True
        return False
    except:
        return False

def validaCupos(cupos):
    try:
        c=int(cupos)
        if c>=0:
            return True
        return False
    except:
        return False
###############################################################################
# Funciones
def total_cupos_disponibles_area(area):
    cantidad = 0
    for clave,valor in cursos.items():
        if valor[1].lower()==area.lower():
           cantidad += comercial[clave][1]
    if cantidad==0:
        print("no existen cupos para esa area")
    else:
        print(f"existen {cantidad} de cupos para el area de {area}")

def buscar_curso_presupuesto_nivel(minimo,maximo,nivel):
    lista=[]
    for clave,valor in comercial.items():
        if valor[0]>=minimo and valor[0]<=maximo and valor[1]>0:
             if cursos[clave][3].lower()==nivel.lower():
                 nombre= cursos[clave][0]
                 lista.append([nombre+"-"+clave])
    if len(lista)==0:
        print("no existen cursos por ese presupuesto y nivel")             
    else:
        lista.sort()
        print(lista)

def modificar_valor_matricula(codigo,nuevo_valor):
    if codigo in cursos:
        comercial[codigo][0]=nuevo_valor
        return True
    return False

def eliminar_curso(codigo,nuevo_valor):
    if codigo in cursos:
        del cursos[codigo]
        del comercial[codigo]
        return True
    return False

def agregar(codigo,nombre,area,horas,nivel,tutor,certi,matr,cupos):
    if codigo in cursos:
        return False
    if certi=='n':
        certificacion=False
    else:
        certificacion=True
    cursos[codigo]=[nombre,area,int(horas),nivel,tutor,certificacion]
    comercial[codigo]=[int(matr),int(cupos)]
    return True
        
###############################################################################
# Menu
def menu():
    print("==EduTech==")
    print("1. Total cupos disponibles por area")
    print("2. Buscar curso por presupuesto y nivel")
    print("3. Modificar valor de matricula")
    print("4. Registrar nuevo curso en catalogo")
    print("5. Dar de baja curso")
    print("6. Reporte de horas por tutor")
    print("7. Salir")

def seleccione():
    try:
        op=int(input("Seleccione:"))
        return op
    except:
        return 0

while True:
    menu()
    opcion = seleccione()
    match opcion:
        case 1:
            while True:
                area = input("ingrese el area:")
                total_cupos_disponibles_area(area)
                resp = input("Desea repetir el proceso?(s/n):").lower()
                if resp=='n':
                    break
        case 2:
            while True:
                try:
                    minimo=int(input("ingrese el minimo:"))        
                    maximo=int(input("ingrese el maximo:"))
                    nivel=input("ingrese el nivel:")
                    if minimo<maximo and minimo>0:
                        buscar_curso_presupuesto_nivel(minimo,maximo,nivel)
                    else:
                        print("el minimo debe ser menor al maximo")
                except:
                    print("ingrese numeros enteros")
                resp=input("Desea repetir el proceso?(s/n):").lower()
                if resp=='n':
                    break
        case 3:
            while True:
                try:
                    codigo=input("ingrese codigo del curso:")
                    nuevo_precio=int(input("ingrese nuevo precio:"))
                    resp = modificar_valor_matricula(codigo,nuevo_precio)
                    if resp == True:
                        print("modifico el valor")
                    else:
                        print("no modifico el valor")
                except:
                    print("ingrese solo numeros como valor")
                resp=input("Desea repetir el proceso?(s/n):").lower()
                if resp=='n':
                    break
        
        case 7:
            print("adios")
            break