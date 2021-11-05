class BloqueMetodo:
    def __init__(self, id, instrucciones, fila, columna, codigo, tipo):
        self.id = id
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo

    def getid(self):
        return self.id

    def getInstrucciones(self):
        return self.instrucciones

    def getTipo(self):
        return self.tipo