class LlamadaFuncion:
    def __init__(self, id, fila, columna, codigo, tipo):
        self.id = id
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo
    
    def getId(self):
        return self.id

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getTipo(self):
        return self.tipo

    def getC3D(self):
        return self.codigo