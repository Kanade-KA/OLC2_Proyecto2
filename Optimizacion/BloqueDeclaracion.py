class BloqueDeclaracion:
    def __init__(self, ids, fila, columna, codigo, tipo):
        self.ids = ids
        self.fila = fila
        self.columna = columna
        self.codigo = codigo
        self.tipo = tipo

    def getids(self):
        return self.ids

    def getcodigo(self):
        return self.codigo