
# ==========================================================
# GUÍA EXAMEN TRANSVERSAL - FUNDAMENTOS DE PROGRAMACIÓN
# Duoc UC - Versión de estudio
#
# Este archivo muestra una forma ordenada de resolver
# un examen transversal usando:
# - Funciones
# - Diccionarios
# - Validaciones reutilizables
# - try/except
# - CRUD
# ==========================================================

actividades = {
    'A01': ['Yoga Dinámico', 'Bienestar', 60, 'Principiante', 'Ana Gómez', False],
    'A02': ['Crossfit Pro', 'Fuerza', 50, 'Avanzado', 'Carlos Plaza', True],
    'A03': ['Pilates Reformer', 'Bienestar', 45, 'Intermedio', 'Elena Marín', False],
}

comercial = {
    'A01':[80000,30],
    'A02':[70000,20],
    'A03':[50000,10]
}

# ---------------- VALIDACIONES ----------------

def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: debe ingresar un número.")

def leer_positivo(mensaje):
    while True:
        numero = leer_entero(mensaje)
        if numero > 0:
            return numero
        print("Debe ser mayor que cero.")

def leer_si_no(mensaje):
    while True:
        r = input(mensaje).strip().upper()
        if r in ("S","N"):
            return r == "S"
        print("Ingrese solamente S o N.")

def leer_nivel():
    niveles=["Principiante","Intermedio","Avanzado"]
    while True:
        n=input("Nivel: ").capitalize()
        if n in niveles:
            return n
        print("Nivel inválido.")

def leer_codigo_nuevo():
    while True:
        codigo=input("Código: ").strip().upper()
        if codigo.startswith("A") and len(codigo)==3:
            if codigo not in actividades:
                return codigo
            print("Ese código ya existe.")
        else:
            print("Formato esperado: A01")

def leer_codigo_existente():
    while True:
        codigo=input("Código: ").strip().upper()
        if codigo in actividades:
            return codigo
        print("Código inexistente.")

# ---------------- FUNCIONES ----------------

def mostrar():
    print("\n=== ACTIVIDADES ===")
    for c,d in actividades.items():
        print(f"{c} -> {d} | Precio:{comercial[c][0]} Cupos:{comercial[c][1]}")

def agregar():
    codigo=leer_codigo_nuevo()
    nombre=input("Nombre: ").title()
    categoria=input("Categoría: ").title()
    duracion=leer_positivo("Duración: ")
    nivel=leer_nivel()
    instructor=input("Instructor: ").title()
    requiere=leer_si_no("¿Requiere equipamiento? (S/N): ")
    precio=leer_positivo("Precio mensual: ")
    cupos=leer_positivo("Cupos: ")

    actividades[codigo]=[nombre,categoria,duracion,nivel,instructor,requiere]
    comercial[codigo]=[precio,cupos]
    print("Actividad agregada.")

def actualizar_precio():
    codigo=leer_codigo_existente()
    precio=leer_positivo("Nuevo precio: ")
    comercial[codigo][0]=precio
    print("Precio actualizado.")

def eliminar():
    codigo=leer_codigo_existente()
    del actividades[codigo]
    del comercial[codigo]
    print("Actividad eliminada.")

def cupos_por_nivel():
    nivel=leer_nivel()
    total=0
    for codigo,datos in actividades.items():
        if datos[3]==nivel:
            total+=comercial[codigo][1]
    print("Total cupos:",total)

def filtrar_precio():
    minimo=leer_positivo("Precio mínimo: ")
    maximo=leer_positivo("Precio máximo: ")
    while minimo>maximo:
        print("El mínimo no puede ser mayor al máximo.")
        minimo=leer_positivo("Precio mínimo: ")
        maximo=leer_positivo("Precio máximo: ")
    for codigo,datos in comercial.items():
        if minimo<=datos[0]<=maximo:
            print(codigo, actividades[codigo][0], datos[0])

def menu():
    print("""
1. Cupos por nivel
2. Filtrar por precio
3. Actualizar precio
4. Agregar actividad
5. Eliminar actividad
6. Mostrar actividades
7. Salir
""")

while True:
    menu()
    op=leer_entero("Opción: ")

    match op:
        case 1:
            cupos_por_nivel()
        case 2:
            filtrar_precio()
        case 3:
            actualizar_precio()
        case 4:
            agregar()
        case 5:
            eliminar()
        case 6:
            mostrar()
        case 7:
            print("Hasta luego.")
            break
        case _:
            print("Opción inválida.")

# ---------------- RESUMEN PARA EL EXAMEN ----------------
#
# ¿Dónde validar?
# ✔ Puedes validar directamente dentro de cada función.
# ✔ Mejor práctica: crear funciones reutilizables como:
#   - leer_entero()
#   - leer_positivo()
#   - leer_codigo_existente()
#   - leer_codigo_nuevo()
#   - leer_nivel()
#   - leer_si_no()
#
# Git que debes conocer:
# git init
# git status
# git add .
# git commit -m "Primer commit"
# git push
#
# Consejo:
# Evita usar int(input()) directamente. Siempre usa try/except.
