from Abstract import Objeto
from TablaSimbolo import Tipo


class Error():
    def __init__(self, tipo, descripcion, fila, columna):
        self.tipoError = tipo
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna

    def toString(self):
        return self.tipoError + " - " + self.descripcion + ", en fila " + str(self.fila) + " y columna " + str(self.columna) + ".\n"
        