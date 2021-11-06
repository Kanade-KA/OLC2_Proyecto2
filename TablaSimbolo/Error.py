class Error():
    def __init__(self, tipo, descripcion, fila, columna):
        self.tipoError = tipo
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna

    def toString(self):
        return self.tipoError + " - " + self.descripcion + ", en fila " + str(self.fila) + " y columna " + str(self.columna) + ".\n"

    def getTipo(self):
        return self.tipoError

    def  getDescripcion(self):
        return self.descripcion

    def getFila(self):
        return str(self.fila)

    def getColumna(self):
        return str(self.columna)