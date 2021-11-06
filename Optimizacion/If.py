class If:
    def __init__(self, opi, opd, operador, goto, fila, columna, codigo, tipo):
        self.opi = opi
        self.opd = opd
        self.operador = operador
        self.goto = goto
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo

    def getOperador1(self):
        return self.opi

    def getOperador2(self):
        return self.opd

    def getOperador(self):
        return self.operador

    def getGoto(self):
        return self.goto

    def getTipo(self):
        return self.tipo

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getC3D(self):
        return self.codigo