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
    
    def setOperador(self, operador):
        self.operador = operador

    def getGoto(self):
        return self.goto
        
    def setGoto(self, goto):
        self.goto = goto

    def getCodigoAnterior(self):
        return self.codigo
    
    def getTipo(self):
        return self.tipo

    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getC3D(self):
        return "if "+str(self.getOperador1())+" "+str(self.getOperador())+" "+str(self.getOperador2())+" { goto "+self.getGoto()+"; }"