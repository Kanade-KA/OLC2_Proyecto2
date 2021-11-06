class BloqueDeclaracion:
    def __init__(self, ids, fila, columna, codigo, tipo):
        self.ids = ids
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo

    def getids(self):
        return self.ids

    def getC3D(self):
        return self.codigo

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getTipo(self):
        return self.tipo