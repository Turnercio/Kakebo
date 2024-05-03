from datetime import date

class Ingreso:
    def __init__(self, concepto, fecha, cantidad):

        self.concepto = concepto
        self.fecha = fecha
        self.cantidad = cantidad
        self.__validar_tipos()
        self.validar_inputs()


    def __validar_tipos(self):
        if not isinstance(self.concepto, str):
            raise TypeError("Concepto debe ser cadena de texto")
        if not isinstance(self.fecha, date):
            raise TypeError("Fecha tiene que tener el formato correcto: AAAA-MM-DD")
        if not (isinstance(self.cantidad, float) or isinstance(self.cantidad, int)):
            raise TypeError("Cantidad tiene que ser un numero")


    def validar_inputs(self):
        if self.cantidad == 0:
            raise ValueError("La cantidad no puede ser 0")
        if self.concepto == "" or len(self.concepto) < 5:
            raise ValueError("El concepto no puede estar vacio")   
        if self.fecha > date.today():
            raise ValueError("La fecha no puede ser posterior al dia de hoy")       
   


