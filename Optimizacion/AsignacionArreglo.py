class AsignacionArreglo:
    def __init__(self, tmp, fila, columna, codigo, tipo):
        self.temporal = tmp
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo
    
    def getTemporal(self):
        return self.temporal

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getC3D(self):
        return self.codigo
    
    def getTipo(self):
        return self.tipo

    def getCodigoAnterior(self):
        return self.codigo