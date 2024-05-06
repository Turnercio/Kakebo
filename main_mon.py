"""
1. Pedir si es ingreso o gasto o salir
2. Si es ingreso
    2.1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es gastos
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoria
3.5 Si es salir salimos a 7
4. Instancir el movimiento (ingreso o gasto)
5. Almacenar el movimiento en una lista
6. volver a 1

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final
"""
from kakebo import *; categoria_gastos
from datetime import date

lista_movimientos = []

def validarFecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False
def es_float_positivo(valor):
    try:
        valor = float(valor)
        if valor >0:
            return True
    except ValueError:
        return False
def es_entero(cadena):
    try:
        int(cadena)
        return True
    except ValueError:
        return False
def es_categoria_valida(cadena):
    if es_entero(cadena):
        entero = int(cadena)
        return es_entero(cadena) and int(cadena) in[categoria.value for categoria in categoria_gastos]
    else:
        return False

continuar = True
while continuar == True:
    tipo = input("Ingreso, Gasto o Salir (I/G/S): ").lower()

    while tipo not in ('i', 'g', 's'):
        print("Teclea I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    if tipo == 'i':
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha (YYYY-MM-DD): ") 
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat (fecha)

        cantidad = input("Cantidad: ")
        while not es_float_positivo(cantidad):
            print("introduce un número positivo")
            cantidad = input("Cantidad: ")
        cantidad = float(cantidad)

        lista_movimientos.append(Ingreso(concepto, fecha, cantidad))

    elif tipo == "g":
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe tener al menos 5 caracteres")
            concepto = input("Concepto: ")
        
        fecha = input("Fecha (YYYY-MM-DD): ") 
        while not validarFecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat (fecha)   

        cantidad = input("Cantidad: ")
        while not es_float_positivo(cantidad):
            print("introduce un número positivo")
            cantidad = input("Cantidad: ")
        cantidad = float(cantidad)

        print ("Lista de categoria de gastos: ")
        for categoria in categoria_gastos:
            print(f"{categoria.value} - {categoria.name}")
        cat = input("Elige una de las categorias a continuación: ")
        while not es_categoria_valida(cat):
            print("La categoria no es correcta: ")
            print ("Lista de categoria de gastos: ")
            for categoria in categoria_gastos:
                print(f"{categoria.value} - {categoria.name}")
            cat = input("Elige una de las categorias a continuación: ")
        cat= categoria_gastos(int(cat))

        lista_movimientos.append(  Gasto(concepto, fecha, cantidad, cat))

    elif tipo == "s":
        continuar = False

print (lista_movimientos)