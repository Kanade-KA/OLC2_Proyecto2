class AsignacionOperacion:
    def __init__(self, tmp, opi, opd, operador, fila, columna, codigo, tipo):
        self.temporal = tmp
        self.opi = opi
        self.opd = opd
        self.operador = operador
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo
    
    def getTemporal(self):
        return self.temporal

    def getOperador1(self):
        return self.opi

    def getOperador2(self):
        return self.opd

    def getOperador(self):
        return self.operador

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
