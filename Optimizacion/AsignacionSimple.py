class AsignacionSimple:
    def __init__(self, tmp, opi, fila, columna, codigo, tipo):
        self.temporal = tmp
        self.opi = opi
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo

    def getTemporal(self):
        return self.temporal

    def getOperador1(self):
        return self.opi

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getCodigoAnterior(self):
        return self.codigo
        
    def getC3D(self):
        return self.codigo

    def getTipo(self):
        return self.tipo
