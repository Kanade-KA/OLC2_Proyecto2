class Goto:
    def __init__(self, etiqueta, fila, columna, codigo, tipo):
        self.etiqueta = etiqueta
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo
    
    def getEtiqueta(self):
        return self.etiqueta

    def setEtiqueta(self, etiqueta):
        self.etiqueta = etiqueta
        
    def getFila(self):
        return self.fila

    def getColumna(self):
        return self.columna

    def getCodigoAnterior(self):
        return self.codigo

    def getC3D(self):
        return "goto "+self.etiqueta+";"

    def getTipo(self):
        return self.tipo
