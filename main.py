"""
1. Pedir si es ingreso o gasto o salir
2. Si es ingreso
    2,1 Pedir concepto
    2.2 Pedir fecha
    2.3 Pedir cantidad
3. Si es gasto
    3.1 Pedir concepto
    3.2 Pedir fecha
    3.3 Pedir cantidad
    3.4 Pedir categoria
3.5 si es salir, salimos a 7
4. Instanciar el movimiento
5. Almacenar el movimiento en una lista
6. Volver a 1

7. Procesar la lista de movimientos para obtener total de ingresos, gastos y saldo final
"""
from kakebo import *; categoria_gastos
from datetime import date
from enum import Enum

lista_ingreso = []
lista_gastos = []

def validar_fecha(fecha):
    try:
        return date.fromisoformat(fecha) <= date.today()
    except ValueError:
        return False


while True:
    tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    while tipo not in ("i", "g", "s"):
        print("Teclea I, G o S")
        tipo = input("Ingreso, Gasto o Salir (I/G/S)").lower()

    if tipo == "i":
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe de ser mayor a 5 caracteres")
            concepto = input("Concepto: ")
        print (concepto)   
        
        fecha = input("Fecha (YYYY-MM-DD): ")
        while not validar_fecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha)

        cantidad = float(input("Introduzca la cantidad del ingreso: "))
        while cantidad == 0:
            print("La cantidad no puede ser 0, introduce una cantidad valida: ")
            cantidad = float(input("Introduzca la cantidad del ingreso: "))
        cantidad = "{:.2f}".format(cantidad)
    
        lista_ingreso.append(Ingreso(concepto, fecha, cantidad))

    if tipo == "g":
        concepto = input("Concepto: ")
        while len(concepto) < 5:
            print("El concepto debe de ser mayor a 5 caracteres")
            concepto = input("Concepto: ")
        print (concepto)   
        
        fecha = input("Fecha (YYYY-MM-DD): ")
        while not validar_fecha(fecha):
            print("Introduzca una fecha valida (YYYY-MM-DD) y no futura")
            fecha = input("Fecha (YYYY-MM-DD): ")
        fecha = date.fromisoformat(fecha)

        cantidad = float(input("Introduzca la cantidad del ingreso: "))
        while cantidad == 0:
            print("La cantidad no puede ser 0, introduce una cantidad valida: ")
            cantidad = float(input("Introduzca la cantidad del ingreso: "))

        categoria = input("Introduce una categoria (Necesidad = 1, Cultura = 2, Ocio Vicio = 3, Extras = 4)")
        while categoria not in ("1", "2", "3", "4"):
            print("introduce una categoria correcta: ")
            categoria = input("Introduce una categoria (Necesidad = 1, Cultura = 2, Ocio Vicio = 3, Extras = 4)")
        categoria = categoria_gastos(int(categoria))


        lista_gastos.append(Gasto(concepto, fecha, cantidad, categoria))  
    
    
    else:

        total_ingresos = 0
        total_gastos = 0
        balance = 0

        for ingreso in lista_ingreso:
            total_ingresos = total_ingresos + ingreso.cantidad
        print (f"El total de los ingresos asciende a {total_ingresos}")

        for gasto in lista_gastos:
            total_gastos = total_gastos + gasto.cantidad
        print (f"El total de los gastos asciende a {total_gastos}")

        balance = (total_ingresos - total_gastos)
        print (f"El balance total asciende a {balance}")
