class BloqueImport:
    def __init__(self, fila, columna, codigo, tipo):
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo

    def getTipo(self):
        return self.tipo

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getC3D(self):
        return self.codigo