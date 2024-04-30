from datetime import date

class Ingreso:
    def __init__(self, concepto, fecha, cantidad):

        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad
        self.__validar_tipos()


    def __validar_tipos(self):
        if not isinstance(self.concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")
        if not isinstance(self.fecha, date):
            raise TypeError("Fecha tiene que tener el formato correcto: AAAA-MM-DD")
        if not (isinstance(self.cantidad, float) or isinstance(self.cantidad, int)):
            raise TypeError("Cantidad tiene que ser un numero")


