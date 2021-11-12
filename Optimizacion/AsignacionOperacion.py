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

    def setOperador1(self, opi):
        self.opi = opi

    def getOperador2(self):
        return self.opd

    def setOperador2(self, opd):
        self.opd = opd

    def getOperador(self):
        return self.operador

    def setOperador(self, op):
        self.operador = op

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getC3D(self):
        return self.temporal + " = "+str(self.opi)+self.operador+str(self.opd)+";"

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getCodigoAnterior(self):
        return self.codigo

    def getOperacion(self):
        return str(self.opi)+self.operador+str(self.opd)
