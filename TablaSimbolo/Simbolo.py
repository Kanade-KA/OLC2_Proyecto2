
class Simbolo:
    def __init__(self, entorno, identificador, valor, tipo, fila, columna ):
        self.id = identificador
        self.ent = entorno
        self.valor = valor  ## instancia de clase OBJETO
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        

    def getID(self):
        return self.id

    def setID(self, id):
        self.id = id

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo  

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor

    def getFila(self):
        return self.fila
    
    def getColumna(self):
        return self.columna