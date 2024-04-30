from datetime import date

class Ingreso:
    def __init__(self, concepto, fecha, cantidad):
        if not isinstance(concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")
        if not isinstance(fecha, date):
            raise TypeError("Fecha tiene que tener el formato correcto: AAAA-MM-DD")
        if not (isinstance(cantidad, float) or isinstance(cantidad, int)):
            raise TypeError("Cantidad tiene que ser un numero")


        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad




